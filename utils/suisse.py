from defnition import JSON_PATH_SUISSE, JSON_PATH_SUISSE_OPPONENTS
import json
from classes.Player import Player


def main():
  """
  Main of the program Suisse, print all opponents and the two groups of players.
  At last, serialize the JSON.
  """
  list_of_players = load_json(JSON_PATH_SUISSE)
  groups = separate_group(list_of_players)
  print("\033[1mGroup S1\033[0m")
  Player.print_list(groups[0])
  print("\n\033[1mGroup S2\033[0m")
  Player.print_list(groups[1])
  print("\n")
  list_of_confrontation = confrontation(groups[0], groups[1])
  for item in list_of_confrontation:
    item.print_versus()
  save_json(JSON_PATH_SUISSE_OPPONENTS, list_of_confrontation)

def separate_group(players: list) -> tuple[Player]:
  """
  Sort the players array according to the elo_point and split it in 2 distinct list
  """
  players_sort = sorted(players, key=lambda x:x.elo_points, reverse=True)
  first_group = players_sort[0:len(players_sort)//2]
  second_group = players_sort[len(players_sort)//2:]
  return first_group, second_group

def confrontation(first_group, second_group) -> list[Player] :
  """
  Return a list of each players with his opponent
  """
  list_of_confrontation = []
  for item in first_group:
    index = first_group.index(item)
    item.set_confrontation(second_group[index])
    list_of_confrontation.append(item)
  return list_of_confrontation
    


def load_json(file_name: str) -> list[Player]:
  """
  Read the JSON file and return the JSON object.
  """
  file = open(file_name)
  data = json.load(file)
  list_of_player = []
  for item in data:
    list_of_player.append(Player(**item))
  return list_of_player

def save_json(file_name: str, data: list[Player]):
  """
  Serialize the data in a json file given in arguments.
  """
  with open(file_name, "w") as write_file:
    json.dump(data, write_file ,default=lambda o: o.__dict__, ensure_ascii=True, indent=4)