Programa pritaikyta python3.


Programai reikalingi pip paketai: 
  1)  Pyserial.
  2)  Paramiko.
  3)  ftplib.

Programos argumentai ir jų paskirtis:

  1)  --d/-device  ->> Nustato testuojamo įrenginio pavadinimą.
  2)  --f/-ftp     ->> Įjungia rezultatų įrašymą į ftp serverį. Nepasirinkus šio parametro jis bus išjungtas.
  3)  --a/-address ->> Nustato adresą kuriuo bus tikrinamas įrenginys.
  4)  --p/-port    ->> Nustato portą kuriuo bus tikrinamas įrenginys. Nepasirinkus šio parametro jis bus nustatomas į 22.

Programai paleisti būtini šie argumentai:

  1)  Testuojamo įrenginio pavadinimas.
  2)  Adresas kuriuo bus testuojamas įtreginys.

Programos paleidimo pavyzdžiai:

  1) /bin/python3 ./main.py -d rut950 -a 192.168.1.1
  2) /bin/python3 ./main.py -d rut950 -a 192.168.1.1 -p 23 -f True
  3) /bin/python3 ./main.py -d trm250 -a /dev/ttyUSB2 -f True