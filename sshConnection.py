import serial
class Connection:
  def __init__(self):
    pass
  def returnConnection(self,connectionInfo):
    pass

ser = serial.Serial('COM3', 38400, timeout=0,parity=serial.PARITY_EVEN, rtscts=1)
s= ser.read(100)
print(s)