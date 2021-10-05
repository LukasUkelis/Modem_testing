import json
class Data:
  __data = None
  def __init__(self, address):
    self.file = open(address)
    self.__data = json.load(self.file)
    self.file.close()

  def getDevice(self, deviceName):
    for device in self.__data['devices']:
      if(deviceName == device['device']):
        return device
    return False