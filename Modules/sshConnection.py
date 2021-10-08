import paramiko
import time

class Connection:
  __ssh = None
  __shell = None
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
    self.__shell = self.__ssh.invoke_shell()
    self.__shell.send("/etc/init.d/gsmd stop\n")
    time.sleep(0.2)
    self.__shell.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\n")
    time.sleep(0.2)
    self.__shell.send("AT&F\n")
    time.sleep(0.2)
    while not self.__shell.recv_ready():
      time.sleep(0.5)
    self.__shell.recv(9999).decode("ascii")

  def __parsingDataToList(self, data):
    dataList = data.decode()
    return dataList.split("\n")
    
  def executeCommand(self,command):
    try:
      self.__shell.send(command+"\n")
      time.sleep(1)
      while not self.__shell.recv_ready():
        time.sleep(2)
      data = self.__shell.recv(9999)
      return self.__parsingDataToList(data)
      
    except:
      print("Command writing error in -> sshConnection.py")
      return False    
    
  def closeConnection(self):
    self.__shell.send("\x03".encode("utf8"))
    time.sleep(0.5)
    self.__shell.send("/etc/init.d/gsmd start\n")
    time.sleep(0.5)
    self.__shell.close()
    self.__ssh.close()
