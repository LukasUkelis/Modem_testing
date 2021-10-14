import ftplib
import Modules.colors as bcolors
class upload:
  def __init__(self) -> None:
      pass 
  def FTPuploadTest(self,deviceName,arguments):
    ftp_host = arguments['address']
    ftp_user = arguments['username']
    ftp_password = arguments['password']
    fileName = deviceName
    filePath = './DataAndResults/{filename}'.format(filename= deviceName)
    try:
      ftp = ftplib.FTP(ftp_host)
      ftp.login(user=ftp_user,passwd=ftp_password)
    except:
      print(f"{bcolors.FAIL}FTP connection error in -> FTPupload.py{bcolors.ENDC}")
      return False
    try:
      file = open(filePath,mode='rb')
    except:
      print(f"{bcolors.FAIL}File open error in -> FTPupload.py{bcolors.ENDC}")
      return False
    try:
      ftp.storbinary('STOR '+fileName, file)
    except:
      print(f"{bcolors.FAIL}File upload error -> FTPupload.py{bcolors.ENDC}")
    ftp.quit()
    
