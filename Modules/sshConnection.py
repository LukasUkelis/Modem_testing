import paramiko
import time
import Modules.colors as bcolors

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
    try:
      self.__ssh.connect(host,port=port,username=username,password=password)
    except:
      print(f"{bcolors.FAIL}Connection error in -> sshConnection.py")
      return False
    self.__shell = self.__ssh.invoke_shell()
    while not self.__shell.recv_ready():
      time.sleep(0.5)
    self.__shell.recv(9999)

    self.__shell.send("uci get system.@system[0].routername\n")
    while not self.__shell.recv_ready():
      time.sleep(0.5)
    deviceName = self.__shell.recv(9999)
    if not self.__checkIFdeviceNamecorrect(deviceName):
      return False
    else:
      self.__shell.send("/etc/init.d/gsmd stop\n")
      time.sleep(0.2)
      self.__shell.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\n")
      time.sleep(0.2)
      self.__shell.send("AT&F\n")
      time.sleep(0.2)
      while not self.__shell.recv_ready():
        time.sleep(0.5)
      self.__shell.recv(9999).decode("ascii")
      return True

  def __checkIFdeviceNamecorrect(self,data):
    dataList = data.decode()
    dataList = dataList.split("\r\n")
    if(dataList[1]==self.__connectionInfo['deviceName']):
      return True
    else:
      print(f"{bcolors.FAIL}Device name do not match")
      return False

  def __parsingDataToList(self, data):
    dataList = data.decode()
    return dataList.split("\n")
    
  def executeCommand(self,command):
    
    try:
      self.__shell.send(command['command']+"\n")
      time.sleep(1)
      if(len(command['extras']) != 0):
        for e in command['extras']:
          time.sleep(1)
          self.__shell.send(e)
          time.sleep(1)
      
      while not self.__shell.recv_ready():
        time.sleep(2)
      data = self.__shell.recv(9999)
      
      return self.__parsingDataToList(data)
      
    except:
      print(f"{bcolors.FAIL}Command writing error in -> sshConnection.py")
      return False    
    
  def closeConnection(self):
    self.__shell.send("\x03".encode("utf8"))
    time.sleep(0.5)
    self.__shell.send("/etc/init.d/gsmd start\n")
    time.sleep(0.5)
    self.__shell.close()
    self.__ssh.close()

