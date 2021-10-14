import Modules.dataParser as dataParser
import Modules.connection as connection
import Modules.results as results
import Modules.device as device
import Modules.upload as upload
import Modules.colors as bcolors



class Testing:
  __dataFile = './data.json'
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


  def __writeResult(self, id , status, expAnswer,recAnswer ):
    self.__results.writeCommand({'command':self.__deviceData.getRawCommand(id),'extras':self.__deviceData.getRawExtras(id),'expAnswer':expAnswer,'recAnswer':recAnswer,'status':status})


  def __testCommand(self,command,answer,id):
    status = 'ERROR'
    recAnser = " "
    try:
      commandReturn = self .__connection.writeCommand(command)
    except:
      status = "ERROR"
    if not commandReturn:
      status = "ERROR"
    i = 0
    for co in commandReturn:
      if(i!=0):
        if(i==1):
          recAnser = recAnser +co[:20]
        else:
          recAnser = recAnser +"\r\n"+co[:20]
        if(co == answer):
          self.__goodCommands = self.__goodCommands +1
          status = "Passed"
          break
        else:
          status = "Failed"
      i = i+1
    if(status == "Failed"):
      self.__badCommands  = self.__badCommands +1
    self.__writeResult(id,status,answer,recAnser)
    return True
    
  
  
  def __testAllCommands(self):
    id = 0
    print(f"Testing{bcolors.HEADER} {self.__deviceData.getCommandsCount()}{bcolors.ENDC} commands.")
    while id < self.__deviceData.getCommandsCount():
      command = self.__deviceData.getFormedCommand(id)['command']
      self.__testCommand(self.__deviceData.getFormedCommand(id),self.__deviceData.getAnswer(id),id)
      print(f"\r{bcolors.OKGREEN}Passed commands: {self.__goodCommands}   {bcolors.FAIL}Failed commands: {self.__badCommands}   {bcolors.OKBLUE}Current command: {command}                                      {bcolors.ENDC}", end='\r')
      id = id +1
    print(f"\r                                                                                                ", end='\r')
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