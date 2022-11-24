
import argparse
from utils.suisse import main as suisse
from utils.bruteforce import generate_pwd, possible_combination, time_for_bruteforce, average_of_time_bruteforce

def args():
  parser = argparse.ArgumentParser(description="Description of my script")
  parser.add_argument("--suisse", required=False, help="Run the suisse program", action="store_true")
  parser.add_argument("--bruteforce", choices=["passgen", "possibility", "time", "average"], required=False, help="Run the brute force program")
  parser.add_argument("--password", type=str, required=False, help="Give a password for the bruteforce program", default="[6Yhum")
  parser.add_argument("--length", type=int, required=False, help="Use this argument to give a length password to bruteforce progam (option passgen)", default=7)
  parser.add_argument("--test", type=int, required=False, help="Number of test for a password brute force", default=3)

  return parser.parse_args()

if __name__ == "__main__":
  program = args()
  if(program.suisse == True):
    suisse()
  elif(program.bruteforce == "passgen"):
    generate_pwd(program.length)
  elif(program.bruteforce == "possibility"):
    possible_combination(program.password)
  elif(program.bruteforce == "time"):
    time_for_bruteforce(program.password)
  elif(program.bruteforce == "average"):
    average_of_time_bruteforce(program.password, program.test)
