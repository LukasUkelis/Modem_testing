
import paramiko
class Connection:
  __connection = None
  __connectionInfo = None
  def __init__(self,connectionInfo):
    self.__connectionInfo = connectionInfo
  def connect(self):
    host = self.__connectionInfo['address']
    port =self.__connectionInfo['port']
    username = self.__connectionInfo['username']
    password = self.__connectionInfo['password']
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,port,username,password)
    stdin, stdout, stderr = ssh.exec_command("ifconfig")
    lines = stdout.readlines()
    print(lines)

  def __readAnswer(self):
    pass
  def writeCommand(self,command):
    pass

  def closeConnection(self):
    pass

  
s = Connection()
s.returnConnection(["ss","192.168.1.1","root","Admin123"])