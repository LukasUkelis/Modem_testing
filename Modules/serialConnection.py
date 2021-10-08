import serial
class Connection:
  __connection = None
  __connectionInfo = None
  def __init__(self,connectionInfo):
    self.__connectionInfo = connectionInfo

  def connect(self):

    try:
      self.__connection = serial.Serial()
      self.__connection.port = self.__connectionInfo['address']
      self.__connection.timeout= 0.5
      self.__connection.open()
    except:
      print("Connection error in -> serialConnection.py")
      return False
    self.__connection.write("AT&F\r\n".encode())
    self.__connection.write("ATE1\r\n".encode())
    self.__connection.readlines()
    return True

  
  def executeCommand(self,command):
    try:
      command = command+"\r\n"
      self.__connection.write(command.encode())
    except:
      print("Command writing error in -> serialConnection.py")
      return False
    answer = self.__readAnswer()
    if not answer:
      print("Answer reading error in -> serialConnection.py")
      return False
    return answer

  def __readAnswer(self):
    answer = None
    try:
      answer = self.__connection.readlines()
    except:
      return False
    finalAnswer = []
    for ans in answer:
      finalAnswer.append(ans.decode().strip("\r\n"))
    return finalAnswer

  def closeConnection(self):
    try:
      self.__connection.close()
    except:
      print("Connection closing error in -> serialConnection.py")
      return False


