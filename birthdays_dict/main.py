
import sys

from birthdays_dict import BirthdaysDict

def main() :
  print("Welcome to the birthday dictionary.")
  scientists = BirthdaysDict()
  scientists.get_switches()

if __name__ == '__main__':
  sys.exit(main())
