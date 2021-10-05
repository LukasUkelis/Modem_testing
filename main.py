import Modules.dataParser as dataParser
import Modules.connection as connection
import Modules.formatResultsFile as formatResultsFile
import Modules.device as device
class Testing:
  __device  = None
  __deviceData = None
  __dataFile = './DataAndResults/data.json'
  __connection = None
  __results = None
  def __init__(self):
    self.data = dataParser.Data(self.__dataFile)
    
  def __checkDevice(self,deviceName):
    self.__device = self.data.getDevice(deviceName)
    if not self.__device:
      print("{dev} does not exist".format(dev = deviceName))
      return False
    else:
      self.__deviceData = device.deviceData(self.__device)
      self.__results = formatResultsFile.formatData()
      self.__results.writeTitle(self.__deviceData.getDeviceInfo())
      return True

  def __connect(self):
     self.__connection = connection.Conecting(self.__deviceData.getConnectionInfo())
     return self.__connection.connect()


  def __writeResult(self, id , answer ):
    self.__results.writeCommand({'command':self.__deviceData.getRawCommand(id),'extras':self.__deviceData.getRawExtras(id),'answer':answer})


  def __testCommand(self,command,answer):
    try:
      comandReturn = self.__connection.writeCommand(command)
      if not comandReturn:
        return "ERROR"
      if(answer == comandReturn[:len(answer)].decode()):
        return "Works correctly"
      return "Does not work"
    except:
      return "ERROR"

  
  def __testAllCommands(self):
    id = 0
    while id < self.__deviceData.getCommandsCount():
      answer = self.__testCommand(self.__deviceData.getFormedCommand(id),self.__deviceData.getAnswer(id))
      self.__writeResult(id,answer)
      id = id +1


  def testingDevice(self,deviceName):
    if not self.__checkDevice(deviceName):
      pass
    else:
      if not self.__connect():
        print("No connection")
      self.__testAllCommands()
      self.__connection.disconnect()


def main():
  test = Testing()
  deviceName = input("Enter device name:\n")
  test.testingDevice(deviceName)

if __name__ == "__main__":
    main()