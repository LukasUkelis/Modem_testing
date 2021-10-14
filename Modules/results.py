import csv
import time
from datetime import datetime
class formatData:
  __fileName = None
  __deviceInfo = None
  __writer = None

  __fieldNames = ['Command','Extras','Expected answer','Received answer','Status']
  def __init__(self,deviceInfo):
      self.__deviceInfo = deviceInfo

  def openWriter(self):
    now = datetime.now()
    dt_string = now.strftime('%d-%m-%Y_%H-%M-%S')
    fileName = '{deviceName}-testing_{time}.csv'.format(deviceName =self.__deviceInfo['deviceName'],time=dt_string)
    self.__fileName = './Results/{filename}'.format(filename= fileName)
    self.__writer = open(self.__fileName,'w')
    return fileName
  
  def closeWriter(self):
    self.__writer.close()
    time.sleep(1)

  def writeTitle(self):
      self.__writer.write("\r\nDevice name: {name}\r\n".format(name=self.__deviceInfo['deviceName']))
      self.__writer.write("Connection type: {connection}\r\n".format(connection = self.__deviceInfo['connectionType']))
      self.__writer.write("Address: {address}\r\n\r\n".format(address=self.__deviceInfo['address']))
      rowWriter = csv.DictWriter(self.__writer,fieldnames=self.__fieldNames)
      rowWriter.writeheader()

  def writeCommand(self, commandInformation):
      rowWriter = csv.DictWriter(self.__writer,fieldnames=self.__fieldNames)
      rowWriter.writerow({'Expected answer':commandInformation['expAnswer'],'Received answer':commandInformation['recAnswer'],'Command':commandInformation['command'],'Extras':commandInformation['extras'],'Status':commandInformation['status']})

