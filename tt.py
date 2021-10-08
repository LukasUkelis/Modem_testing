import ftplib

FTP_host = "https://www.dropbox.com/home"
FTP_user = "dlpuser"
FTP_pass = "rNrKYTX9g7z3RgJRmxWuGHbeu"
ftp = ftplib.FTP('dropbox.com')
ftp.login(user=FTP_user,passwd = FTP_pass)
output =("/ftp/results/")
filename = 'test.png'
ftp.storbinary('STOR ' +filename, open(filename,'rb'))
ftp.dir()
ftp.quit()

