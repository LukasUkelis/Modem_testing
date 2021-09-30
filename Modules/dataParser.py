import json
class Data:
  ID = -1
  def __init__(self, address):
    self.file = open(address)
    self.data = json.load(self.file)

  def checkDevice(self, device):
    i =0
    for dev in self.data['devices']:
      if(device == dev['device']):
        self.ID = i
        return True
      i = i+1
    return False
    
  def returnConnection(self):
    dev = self.data['devices'][self.ID]
    if(dev['connection']=="serial"):
      return [dev['connection'],dev['address']]
    else:
      return [dev['connection'],dev['address'],dev['username'],dev['password']]
  
  def returnFormedCommand(self,id):
    try:
      return self.formCommand(id)
    except:
      return False

  def returnCommandCount(self):
    return len(self.data['devices'][self.ID]['commands'])

  def returnAnswer(self,id):
    try:
      return self.data['devices'][self.ID]['commands'][id]['answer']
    except:
      return False

  def formExtras(self,id):
    formed = ""
    for extra in self.data['devices'][self.ID]['commands'][id]['extras']:
      formed = formed+extra
    return formed

  def returnCommand(self,id):
    return self.data['devices'][self.ID]['commands'][id]['command']
    
  def returnExtras(self, id):
    formed = ""
    i = 0
    try:
      while i < len(self.data['devices'][self.ID]['commands'][id]['extras']):
        formed = self.data['devices'][self.ID]['commands'][id]['extras'][i]
        i=i+2
    except:
      pass
    return formed

  def returnDeviceInfo(self):
    return[self.data['devices'][self.ID]['device'],self.data['devices'][self.ID]['connection'],self.data['devices'][self.ID]['address']]

  def formCommand(self,id):
    if(len(self.data['devices'][self.ID]['commands'][id]['extras'])>0):
      extras = self.formExtras(id)
      return self.data['devices'][self.ID]['commands'][id]['command']+"\r\n"+extras
    else:
      return self.data['devices'][self.ID]['commands'][id]['command']+"\r\n"
