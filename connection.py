
import serial
class Conecting:
  ser = serial.Serial()
  def __init__(self, connectionInfo):
    self.connectionInfo = connectionInfo

  def loadModule(self, moduleType):
    module = None
    try:
      module = __import__('{type}Connection'.format(type=moduleType))
      return module
    except:
      return False

  def loadMethod(self,module,methodName):
    try:
      method = getattr(module,methodName)
      return method
    except:
      return False

  def connect(self):
    methodName = "Connection"
    module = self.loadModule(self.connectionInfo[0])
    if not module:
      return False
    method = self.loadMethod(module,methodName)
    if not method:
      return False
    fun = method()
    self.ser = fun.returnConnection(self.connectionInfo)
    return True
  def readAnswer(self):
    try:
      answer = self.ser.readlines()
      return answer[len(answer)-1]
    except:
      return False
  def writeCommand(self,command):
      self.ser.write(command.encode())
      return self.readAnswer()