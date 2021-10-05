import serial
class Connection:
  __connection = None
  __connectionInfo = None
  def __init__(self,connectionInfo):
    self.__connectionInfo = connectionInfo

  def connect(self):
    self.__connection = serial.Serial()
    self.__connection.port = self.__connectionInfo['address']
    self.__connection.timeout= 0.1
    self.__connection.open()
    self.__connection.write("AT&F\r\n".encode())
    self.__connection.write("ATE1\r\n".encode())
    self.__connection.readlines()

  def __readAnswer(self):
    try:
      return self.__connection.readlines()
    except:
      return False
  def writeCommand(self,command):
    try:
      self.__connection.write(command.encode())
    except:
      print("Command writing error")
      return False
    answer = self.__readAnswer()
    if not answer:
      print("Answer reading error")
      return False
    return answer[len(answer)-1]

  def closeConnection(self):
    try:
      self.__connection.close()
    except:
      print("Connection closing error")
      return False
