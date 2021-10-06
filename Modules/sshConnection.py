
import paramiko
class Connection:
  __ssh = None
  __connectionInfo = None
  def __init__(self,connectionInfo):
    self.__connectionInfo = connectionInfo
  def connect(self):
    host = self.__connectionInfo['address']
    port =self.__connectionInfo['port']
    username = self.__connectionInfo['username']
    password = self.__connectionInfo['password']
    self.__ssh = paramiko.SSHClient()
    self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    self.__ssh.connect(host,port=port,username=username,password=password)

  def __readAnswer(self,stdout):
    try:
      return stdout.readlines()
    except:
      print("Reading error in -> sshConnection.py")
      return False
  def writeCommand(self,command):
    try:
      stdin, stdout, stderr =self.__ssh.exec_command(command)
    except:
      print("Writing error in -> sshConnection.py")
      return False
    answer = self.__readAnswer(stdout)
    if not answer:
      return False
    answer =answer[len(answer)-1]
    return answer.strip("\n").strip("\r")
    
  def closeConnection(self):
    pass