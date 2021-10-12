import ftplib

class upload:
  __ftp_host = "188.69.245.225"
  __ftp_user = "teltonika"
  __fp_password = "teltonika1212"
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
    
