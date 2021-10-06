
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
    return answer.strip("\n")
    
  def closeConnection(self):
    pass

# s = Connection({'address':"192.168.1.1",'port':"22",'username':"root",'password':"Admin123"})
# s.connect()
# print(s.writeCommand("gsmctl -p wwan0"))
# s.closeConnection()