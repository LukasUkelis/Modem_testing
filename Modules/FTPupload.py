import ftplib
import dropbox

class upload:
  __ftp_host = "dropboc.com"
  __ftp_user = "lukasukelis@gmail.com"
  __fp_password = "Pskvx14VtGsZ0uPvu0"
  __accessToken = 'sl.A592n0MRLQSAx2rhRvoB5y7EEYzRBkWL5noERQ8MsAvzxK8rZ1z-hmjjG9-MjoUXBJfHy1C89-O3ZvSQ_yhl44k0pOGd-avnTuAxW6n90-hfy-X7d0nzaqpW2PE67McZ4wHHz3c'
  def __init__(self) -> None:
      pass

  def upladeTest(self,deviceInfo):
    
    filePath = './DataAndResults/{deviceName}-testing_results.csv'.format(deviceName= deviceInfo['deviceName'])
    fileTo = '/testas/{deviceName}-testing_results.csv'.format(deviceName= deviceInfo['deviceName'])
    dbx = dropbox.Dropbox(self.__accessToken)
    with open(filePath,'rb') as f:
      dbx.files_upload(f.read(),fileTo)
    
    # def upladeTest(self,deviceInfo):
    
    # fileName = './DataAndResults/{deviceName}-testing_results.csv'.format(deviceName= deviceInfo['deviceName'])
    # try:
    #   ftp = ftplib.FTP(self.__ftp_host)
    #   ftp.login(user=self.__ftp_user,passwd=self.__fp_password)
    # except:
    #   print("FTP connection error in -> FTPupload.py")
    #   return False
    # ftp.storbinary('STOR '+fileName,open(fileName,'rb'))
    # ftp.quit()
    # return True