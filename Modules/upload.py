import ftplib

class upload:
  __ftp_host = "192.168.10.58"
  __ftp_user = "studentas"
  __fp_password = "iotakademija"
  def __init__(self) -> None:
      pass 
  def FTPuploadTest(self,deviceName):
    fileName = deviceName
    filePath = './DataAndResults/{filename}'.format(filename= deviceName)
    try:
      ftp = ftplib.FTP(self.__ftp_host)
      ftp.login(user=self.__ftp_user,passwd=self.__fp_password)
    except:
      print("FTP connection error in -> FTPupload.py")
      return False
    file = open(filePath,mode='rb')
    ftp.storbinary('STOR '+fileName, file)
    ftp.quit()
    
