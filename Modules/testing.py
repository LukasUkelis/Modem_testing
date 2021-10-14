import Modules.dataParser as dataParser
import Modules.connection as connection
import Modules.results as results
import Modules.device as device
import Modules.upload as upload
import Modules.colors as bcolors



class Testing:
  __dataFile = './DataAndResults/data.json'
  __device  = None
  __deviceData = None
  __connection = None
  __results = None
  __resultsUpload= None
  __goodCommands = 0
  __badCommands = 0
  __devicePath = None

  def __init__(self):
    self.data = dataParser.Data(self.__dataFile)
  
  def __checkDevice(self,deviceName,address):
    self.__device = self.data.getDevice(deviceName)
    if not self.__device:
      print(f"{bcolors.FAIL}{deviceName} does not exist")
      return False
    else:
      self.__deviceData = device.deviceData(self.__device)
      self.__results = results.formatData(self.__deviceData.getDeviceInfo(address))
      self.__devicePath = self.__results.openWriter()
      self.__results.writeTitle()
      self.__resultsUpload = upload.upload()
      return True

  def __connect(self,address,port):
     self.__connection = connection.Conecting(self.__deviceData.getConnectionInfo(address,port))
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
        return "Passed"
    self.__badCommands  = self.__badCommands +1
    return "Failed"
    
  
  
  def __testAllCommands(self):
    id = 0
    print(f"Testing{bcolors.HEADER} {self.__deviceData.getCommandsCount()}{bcolors.ENDC} commands.")
    while id < self.__deviceData.getCommandsCount():
      answer = self.__testCommand(self.__deviceData.getFormedCommand(id),self.__deviceData.getAnswer(id))
      self.__writeResult(id,answer)
      print(f"\r{bcolors.OKGREEN}Passed commands: {self.__goodCommands}   {bcolors.FAIL}Failed commands: {self.__badCommands}   {bcolors.OKBLUE}Current command: {self.__deviceData.getFormedCommand(id)}         {bcolors.ENDC}", end='\r')
      id = id +1
    print(f"\r                                                                                                                           ", end='\r')
    print(f"\r\n{bcolors.OKGREEN}Passed commands:  {self.__goodCommands}{bcolors.ENDC}")
    print(f"\r{bcolors.FAIL}Failed commands:  {self.__badCommands}{bcolors.ENDC}")
    self.__results.closeWriter()


  def testingDevice(self,arguments):
    if not self.__checkDevice(arguments['deviceName'],arguments['address']):
      return False
    else:
      if not self.__connect(arguments['address'],arguments['port']):
        return False
      self.__testAllCommands()
      if arguments['ftp']:
        self.__resultsUpload.FTPuploadTest(self.__devicePath,{'username':arguments['username'],'password':arguments['password'],'address':arguments['addressftp']})
      self.__connection.disconnect()