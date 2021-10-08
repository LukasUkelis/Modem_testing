import Modules.testing as testing
import argparse
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--d','-device', help='Device name')
  args = parser.parse_args()
  if (args.d == None):
    print("Enter device name. --d/-device device name")
  else:
    print("Testing device: {devicename}".format(devicename = args.d.upper()))
    test = testing.Testing()
    test.testingDevice(args.d.upper())


if __name__ == "__main__":
    main()