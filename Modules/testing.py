import Modules.dataParser as dataParser
import Modules.connection as connection
import Modules.results as results
import Modules.device as device
import time
class Testing:
  __dataFile = './DataAndResults/data.json'
  __device  = None
  __deviceData = None
  __connection = None
  __results = None
  __goodCommands = 0
  __badCommands = 0
  __errorCommands = 0

  def __init__(self):
    self.data = dataParser.Data(self.__dataFile)
  
  def __checkDevice(self,deviceName):
    self.__device = self.data.getDevice(deviceName)
    if not self.__device:
      print("{dev} does not exist".format(dev = deviceName))
      return False
    else:
      self.__deviceData = device.deviceData(self.__device)
      self.__results = results.formatData(self.__deviceData.getDeviceInfo())
      self.__results.openWriter()
      self.__results.writeTitle()
      return True

  def __connect(self):
     self.__connection = connection.Conecting(self.__deviceData.getConnectionInfo())
     return self.__connection.connect()


  def __writeResult(self, id , answer ):
    self.__results.writeCommand({'command':self.__deviceData.getRawCommand(id),'extras':self.__deviceData.getRawExtras(id),'answer':answer})


  def __testCommand(self,command,answer):
    try:
      commandReturn = self.__connection.writeCommand(command)
    except:
      return "ERROR"
    if not commandReturn:
      return "ERROR"
    for co in commandReturn:
      if(co == answer):
        self.__goodCommands = self.__goodCommands +1
        return "Works correctly"
    self.__badCommands  = self.__badCommands +1
    return "Does not work"
    
  
  
  def __testAllCommands(self):
    id = 0
    print("Program have to test {number} commands".format(number = self.__deviceData.getCommandsCount()), flush=True)
    while id < self.__deviceData.getCommandsCount():
      answer = self.__testCommand(self.__deviceData.getFormedCommand(id),self.__deviceData.getAnswer(id))
      self.__writeResult(id,answer)
      print(f"\rWorking commands: {self.__goodCommands}   Not working commands:{self.__badCommands} Current command: {self.__deviceData.getFormedCommand(id)}         ", end='\r')
      id = id +1
    print(f"\r                                                                                                                           ", end='\r')
    print(f"\r\nWorking commands: {self.__goodCommands}")
    print(f"\rNot working commands:{self.__badCommands}")


  def testingDevice(self,deviceName):
    if not self.__checkDevice(deviceName):
      return False
    else:
      if not self.__connect():
        return False
      self.__testAllCommands()
      time.sleep(1)
      self.__connection.disconnect()