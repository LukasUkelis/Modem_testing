class deviceData:
  __device = None

  def __init__(self,device):
      self.__device=device
  
  # Data for commands testing
  def getCommandsCount(self):
    try:
      return len(self.__device['commands'])
    except:
      return False


  def formExtras(self,id):
      extrasList = []
      for extra in self.__device['commands'][id]['extras']:
        if(extra == 'z'):
          extrasList.append("\x1a")
        else:
          extrasList.append(extra)
      return extrasList


  def getFormedCommand(self,id):
    return {'command': self.__device['commands'][id]['command'],'extras':self.formExtras(id)}


  def getAnswer(self, id):
    try:
      return self.__device['commands'][id]['answer']
    except:
      return False


  # Data for results file
  def getRawCommand(self,id):
    return self.__device['commands'][id]['command']


  def getRawExtras(self,id):
    formed = ""
    i = 0
    try:
      while i < len(self.__device['commands'][id]['extras']):
        formed = formed + self.__device['commands'][id]['extras'][i] + "  "

        i=i+2
    except:
      return False
    return formed


  def getDeviceInfo(self,address):
    return {'deviceName':self.__device['device'],'connectionType':self.__device['connection'],'address':address}


  # Data for connection
  def getConnectionInfo(self,address,port):
    return {'connectionType':self.__device['connection'],'address':address,'deviceName':self.__device['device'],'port':port,'username':self.__device['username'],'password':self.__device['password']}