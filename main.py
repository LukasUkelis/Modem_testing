import Modules.testing as testing
import argparse
def main():
  writingToFTP= False
  parser = argparse.ArgumentParser()
  parser.add_argument('--d','-device', help='Device name')
  parser.add_argument('--f','-ftp', help='Writing results to FTP. True/False')
  args = parser.parse_args()
  if (args.f != None and args.f != "True" and args.f != "False"):
    print("Bad argument")
    return 0
  else:
    if (args.f == None or args.f == "False"):
      pass
    if (args.f == "True"):
      writingToFTP = True
  

  if (args.d == None):
    print("Enter device name. --d/-device device name")
  else:
    print("Testing device: {devicename}".format(devicename = args.d.upper()))
    test = testing.Testing()
    test.testingDevice(args.d.upper(),writingToFTP)


if __name__ == "__main__":
    main()