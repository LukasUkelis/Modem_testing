class Conecting:
  __connection = None

  def __init__(self,connectionInfo):
    self.__connectionInfo = connectionInfo

  def __loadModule(self, moduleType):
    module = None
    try:
      mod= __import__('Modules.{type}Connection'.format(type=moduleType))
      module= getattr(mod,'{type}Connection'.format(type=moduleType))
      return module
    except:
       print("Bad connection type error in -> connection.py")
       return False    

  def __loadMethod(self,module,methodName):
    try:
      method = getattr(module,methodName)
      return method
    except:
      print("Bad method error in -> connection.py")
      return False

  def connect(self):
    methodName = "Connection"
    module = self.__loadModule(self.__connectionInfo['connectionType'])
    if not module:
      return False
    method = self.__loadMethod(module,methodName)
    if not method:
      return False
    self.__connection = method(self.__connectionInfo)
    if not self.__connection.connect():
      return False

    return True

  def writeCommand(self,command):
    return self.__connection.executeCommand(command)

  def disconnect(self):
    self.__connection.closeConnection()