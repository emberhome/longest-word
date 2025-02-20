import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        import random
        import string
        self.grid = random.choices(string.ascii_uppercase, k=9)
        pass


    # def is_valid(self, word: str) -> bool:
    #     """Return True if and only if the word is valid, given the Game's grid"""

    #     word_letters = list(word)

    #     if len(word_letters) == 0:
    #         return False

    #     else:
    #             grid_copy = self.grid.copy()

    #             for l in word_letters:
    #                if l in grid_copy: grid_copy.remove(l)
    #                else:
    #                    return False
    #             return True


    def is_valid(self, word):
        word_letters = list(word)

        if len(word_letters) == 0:
            return False

        else:
            return self.__check_dictionary(word)


    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']



# game = Game()
# print(game.grid) # --> OQUWRBAZE

# word = 'BAROQUE'
# print(game.is_valid(word)) # --> True
