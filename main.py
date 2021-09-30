import Modules.dataParser as dataParser
import Modules.connection as connection
import Modules.formatResultsFile as formatResultsFile
class Testing:
  def __init__(self,data):
    self.data = dataParser.Data(data)
    
  def checkDevice(self,device):
    if not self.data.checkDevice(device):
      pass
    else:
      self.result = formatResultsFile.formatData()
      self.result.writeTitle(self.data.returnDeviceInfo())
    return self.data.checkDevice(device)

  def connect(self):
     self.con = connection.Conecting(self.data.returnConnection())
     self.con.connect()

  def writeResults(self, id , awnser ):
    self.result.writeCommand([self.data.returnCommand(id),self.data.returnExtras(id),awnser])

  def testCommand(self,command,awnser):
    try:
      comandReturn = self.con.writeCommand(command)
      if(awnser == comandReturn[:len(awnser)].decode()):
        return "Works correctly"
      return "Works incorrectly"
    except:
      return "ERROR"

  
  def testAllCommands(self):
    id = 0
    while id < self.data.returnCommandCount():
      a = self.testCommand(self.data.returnFormedCommand(id),self.data.returnAnswer(id))
      self.writeResults(id,a)
      id = id +1

  def testingDevice(self,deviceName):
    if not self.checkDevice(deviceName):
      print("Device not found")
      return False
    self.connect()
    self.testAllCommands()

def main():
    test = Testing('./DataAndResults/data.json')
    deviceName = input("Enter device name:\n")
    test.testingDevice(deviceName)

if __name__ == "__main__":
    main()