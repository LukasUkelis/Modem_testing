import csv
class formatData:
  fileName = 'results.csv'
  def __init__(self):
      pass
  def writeTitle(self, titleInformation):
    with open(self.fileName,'w') as f:
      f.write("\r\nDevice name: {name}\r\n".format(name=titleInformation[0]))
      f.write("Connection type: {connection}\r\n".format(connection = titleInformation[1]))
      f.write("Address: {address}\r\n\r\n".format(address=titleInformation[2]))
      fieldnames = ['Command','Extras','Status']
      writer = csv.DictWriter(f,fieldnames=fieldnames)
      writer.writeheader()
  def writeCommand(self, commandInformation):
    with open(self.fileName,'a') as f:
      fieldnames = ['Command','Extras','Status']
      writer = csv.DictWriter(f,fieldnames=fieldnames)
      writer.writerow({'Command':commandInformation[0],'Extras':commandInformation[1],'Status':commandInformation[2]})

