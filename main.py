import Modules.testing as testing
import Modules.colors as bcolors
import argparse
def main():
  arguments = Arguments()
  if arguments == 0:
    return 0
  else:
    test = testing.Testing()
    test.testingDevice(arguments)


def Arguments():
  __writingToFTP = False
  __defaultPort = 22
  __username= ""
  __password= ""
  __addressftp=""

  parser = argparse.ArgumentParser()
  parser.add_argument('-d','--device', help='Device name.')
  parser.add_argument('-f','--ftp', help='Writing results to FTP. True/False.')
  parser.add_argument('-a','--address', help='Device address.')
  parser.add_argument('-p','--port', help='Device port.')
  parser.add_argument('-u','--username', help='Ftp server username. Necessary if writing to ftp server.')
  parser.add_argument('-ps','--password', help='Ftp server password. Necessary if writing to ftp server.')
  parser.add_argument('-af','--addressftp', help='Ftp server address. Necessary if writing to ftp server.')

  args = parser.parse_args()
  # device name
  if (args.device == None):
    print(f"{bcolors.FAIL}Enter device name.\r\n{bcolors.WARNING}Arguments format: -d/-device device name{bcolors.ENDC}")
    return 0
  else:
    print(f"Testing device: {bcolors.WARNING}{args.device.upper()}{bcolors.ENDC}")


  # writing to ftp
  if (args.ftp != None and args.ftp != "True" and args.ftp != "False"):
    print(f"{bcolors.FAIL}Bad argument.\r\n{bcolors.WARNING}Arguments format: -f/-ftp True/False{bcolors.ENDC}")
    return 0
  else:
    if (args.ftp == None or args.ftp == "False"):
      print(f"Writing to ftp: {bcolors.WARNING}DISABLED{bcolors.ENDC}")
      pass
    if (args.ftp == "True"):
      print(f"Writing to ftp: {bcolors.WARNING}ENABLED{bcolors.ENDC}")
      __writingToFTP = True
      if(args.username == None or args.password == None or args.addressftp == None):
        print(f"{bcolors.FAIL}Enter necessary arguments for ftp writing: address, username, password. More info in --help")
        return 0
      else:
        
        __username = args.username
        __password = args.password
        __addressftp = args.addressftp
        print(f"  Writing to {bcolors.WARNING}{__addressftp}{bcolors.ENDC} ftp server")


  # device address
  if (args.address == None):
    print(f"{bcolors.FAIL}Enter device address.\r\n{bcolors.WARNING}Arguments format: -a/-address device address{bcolors.ENDC}")
    return 0
  else:
    print(f"Device address set to: {bcolors.WARNING}{args.address}{bcolors.ENDC}")

  # device port
  if (args.port == None):
    print(f"Device port set to default: {bcolors.WARNING}22{bcolors.ENDC}")
  else:
    print(f"Device port set to: {bcolors.WARNING}{args.port}{bcolors.ENDC}")
  return {'deviceName':args.device.upper(),'ftp':__writingToFTP,'port':__defaultPort,'address':args.address,'username':__username,'password':__password,'addressftp':__addressftp}

if __name__ == "__main__":
    main()