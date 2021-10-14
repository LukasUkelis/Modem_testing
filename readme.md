##### Required pip packages for the program: 
  +  Pyserial
  +  Paramiko
  +  ftplib

##### Arguments:

  +  -d/--device  ->> Sets device name.
  +  -f/--ftp     ->> Enables writing to ftp server. By default is set to disable.
  +  -a/--address ->> Sets device address.
  +  -p/--port    ->> Sets address port. By default is set to 22.
  +  -u/--username ->> Sets ftp server username. Mandatory if using writing to ftp.
  +  -ps/--password ->> Sets ftp server password. Mandatory if using writing to ftp.
  +  -af/--addressftp ->> Sets ftp server address. Mandatory if using writing to ftp.

##### Mandatory arguments:

  +  Device name.
  +  Device address.

##### Program launch examples:

  + /bin/python3 ./main.py -d rut950 -a 192.168.1.1
  + /bin/python3 ./main.py -d rut950 -a 192.168.1.1 -p 23 -f True -u username -ps password -af 192.168.10.58
  + /bin/python3 ./main.py -d trm250 -a /dev/ttyUSB2 -f True -u username -ps password -af 192.168.10.58