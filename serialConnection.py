import serial
class Connection:
  def __init__(self):
    pass
  def returnConnection(self,connectionInfo):
    self.ser = serial.Serial()
    self.ser.port = connectionInfo[1]
    self.ser.timeout= 0.10
    self.ser.open()
    self.ser.write("AT&F\r\n".encode())
    self.ser.write("ATE1\r\n".encode())
    self.ser.readlines()
    return self.ser
