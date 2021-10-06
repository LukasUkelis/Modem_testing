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
    finalAnswer = ""
    answer = None
    try:
      answer = stdout.readlines()
    except:
      print("Reading error in -> sshConnection.py")
      return False
    i = 0
    finalAnswer = answer[0].strip("\n").strip("\r")
    for ans in answer:
      if i != 0:
        finalAnswer = finalAnswer +" "+ ans.strip("\n").strip("\r")
      i = i+1
    return finalAnswer
    


  def writeCommand(self,command):
    try:
      stdin, stdout, stderr =self.__ssh.exec_command(command)
    except:
      print("Writing error in -> sshConnection.py")
      return False
    answer = self.__readAnswer(stdout)
    if not answer:
      return False
    return answer
    
    
  def closeConnection(self):
    self.__ssh.close()