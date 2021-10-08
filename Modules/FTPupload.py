import ftplib

class upload:
  __ftp_host = "dropboc.com"
  __ftp_user = "lukasukelis@gmail.com"
  __fp_password = "Pskvx14VtGsZ0uPvu0"
  def __init__(self) -> None:
      pass
    
  def upladeTest(self,deviceInfo):
    
    fileName = './DataAndResults/{deviceName}-testing_results.csv'.format(deviceName= deviceInfo['deviceName'])
    try:
      ftp = ftplib.FTP(self.__ftp_host)
      ftp.login(user=self.__ftp_user,passwd=self.__fp_password)
    except:
      print("FTP connection error in -> FTPupload.py")
      return False
    ftp.storbinary('STOR '+fileName,open(fileName,'rb'))
    ftp.quit()
    return True