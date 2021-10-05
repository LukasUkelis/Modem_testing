import csv
class formatData:
  __fileName = './DataAndResults/Results.csv'
  def __init__(self):
      pass
  def writeTitle(self, titleInformation):
    with open(self.__fileName,'w') as f:
      f.write("\r\nDevice name: {name}\r\n".format(name=titleInformation['deviceName']))
      f.write("Connection type: {connection}\r\n".format(connection = titleInformation['connectionType']))
      f.write("Address: {address}\r\n\r\n".format(address=titleInformation['address']))
      fieldnames = ['Command','Extras','Status']
      writer = csv.DictWriter(f,fieldnames=fieldnames)
      writer.writeheader()
  def writeCommand(self, commandInformation):
    with open(self.__fileName,'a') as f:
      fieldnames = ['Command','Extras','Status']
      writer = csv.DictWriter(f,fieldnames=fieldnames)
      writer.writerow({'Command':commandInformation['command'],'Extras':commandInformation['extras'],'Status':commandInformation['answer']})

