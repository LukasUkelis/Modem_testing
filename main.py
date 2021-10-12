import Modules.testing as testing
from Modules.colors import bcolors
import argparse
def main():
  __writingToFTP= False
  __defaultPort = 22
  parser = argparse.ArgumentParser()
  parser.add_argument('--d','-device', help='Device name')
  parser.add_argument('--f','-ftp', help='Writing results to FTP. True/False')
  parser.add_argument('--a','-address', help='Device address.')
  parser.add_argument('--p','-port', help='Device port')

  args = parser.parse_args()
  # device name
  if (args.d == None):
    print(f"{bcolors.FAIL}Enter device name.\r\n{bcolors.WARNING}Arguments format: -d/-device device name{bcolors.ENDC}")
    return 0
  else:
    print(f"Testing device: {bcolors.WARNING}{args.d.upper()}{bcolors.ENDC}")
  # writing to ftp
  if (args.f != None and args.f != "True" and args.f != "False"):
    print(f"{bcolors.FAIL}Bad argument.\r\n{bcolors.WARNING}Arguments format: -f/-ftp True/False{bcolors.ENDC}")
    return 0
  else:
    if (args.f == None or args.f == "False"):
      print(f"Writing to ftp: {bcolors.WARNING}DISABLED{bcolors.ENDC}")
      pass
    if (args.f == "True"):
      print(f"Writing to ftp: {bcolors.WARNING}ENABLED{bcolors.ENDC}")
      __writingToFTP = True
  # device address
  if (args.a == None):
    print(f"{bcolors.FAIL}Enter device address.\r\n{bcolors.WARNING}Arguments format: -a/-address device address{bcolors.ENDC}")
    return 0
  else:
    print(f"Device address set to: {bcolors.WARNING}{args.a}{bcolors.ENDC}")
  if (args.p == None):
    print(f"Device port set to default: {bcolors.WARNING}22{bcolors.ENDC}")
  else:
    print(f"Device port set to: {bcolors.WARNING}{args.p}{bcolors.ENDC}")
  test = testing.Testing()
  test.testingDevice(args.d.upper(),__writingToFTP,args.a,__defaultPort)


if __name__ == "__main__":
    main()