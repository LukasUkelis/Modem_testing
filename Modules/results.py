import csv
class formatData:
  __fileName = None
  __deviceInfo = None
  __writer = None
  __fieldNames = ['Command','Extras','Status']
  def __init__(self,deviceInfo):
      self.__deviceInfo = deviceInfo

  def openWriter(self):
    self.__fileName = './DataAndResults/{deviceName}-testing_results.csv'.format(deviceName= self.__deviceInfo['deviceName'])
    self.__writer = open(self.__fileName,'w')
  
  def closeWriter(self):
    self.__writer.close()

  def writeTitle(self):
      self.__writer.write("\r\nDevice name: {name}\r\n".format(name=self.__deviceInfo['deviceName']))
      self.__writer.write("Connection type: {connection}\r\n".format(connection = self.__deviceInfo['connectionType']))
      self.__writer.write("Address: {address}\r\n\r\n".format(address=self.__deviceInfo['address']))
      rowWriter = csv.DictWriter(self.__writer,fieldnames=self.__fieldNames)
      rowWriter.writeheader()

  def writeCommand(self, commandInformation):
      rowWriter = csv.DictWriter(self.__writer,fieldnames=self.__fieldNames)
      rowWriter.writerow({'Command':commandInformation['command'],'Extras':commandInformation['extras'],'Status':commandInformation['answer']})

