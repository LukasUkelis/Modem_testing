
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
    # self.__ssh.load_system_host_keys()
    self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    self.__ssh.connect(host,port=port,username=username,password=password)
    stdin, stdout, stderr = self.__ssh.exec_command("ls /dev")
    lines = stdout.readlines()
    print(lines)

  def __readAnswer(self):
    pass
  def writeCommand(self,command):
    pass
  def closeConnection(self):
    pass


s = Connection({'address':"192.168.1.1",'port':"22",'username':"root",'password':"Admin123"})
s.connect()