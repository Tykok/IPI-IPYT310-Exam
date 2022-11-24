
import argparse
from utils.suisse import main as suisse
# from utils.bruteforce import main as bruteforce

def args():
  parser = argparse.ArgumentParser(description='Description of my script')
  parser.add_argument('--suisse', required=False, help='Run the suisse program', action="store_true")
  parser.add_argument('--bruteforce', required=False, help='Run the brute force program', action="store_true")

  return parser.parse_args()

if __name__ == "__main__":
  program = args()
  if(program.suisse == True):
    suisse()
  elif(program.bruteforce == True):
    print("brutforce")
