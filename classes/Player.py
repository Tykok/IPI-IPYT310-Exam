import json

class Player:
    def __init__(self, id: int, first_name: str, last_name: str, elo_points: int, confrontation = None):
        self.id = id
        self.first_name = first_name 
        self.last_name = last_name 
        self.elo_points= elo_points
        self.confrontation = confrontation

    def set_confrontation(self, confront):
        self.confrontation = confront

    def __str__(self):
        return f"{self.first_name} {self.last_name} (\033[92m{self.elo_points}\033[0m)"
    
    def print_versus(self):
        print(f"{self} \033[1mVS\033[0m {self.confrontation}")

    @staticmethod
    def print_list(list_of_players: list):
        for item in list_of_players:
            print(item)