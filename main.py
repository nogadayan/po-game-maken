import random
from words import word_list

def get_word():
  word = random.choice(word_list)


def play(word):
  word_completion = "-" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 5






  def display_hangman(tries):
    stages = [  """
                    --------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / \\
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |      \\|/
                    |       |
                    |
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |      \\|
                    |       |
                    | 
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |       |
                    |       |
                    |
                    -
                """,
                """
                    --------
                    |       |
                    |       o
                    |
                    | 
                    |
                    -
                """,
                """
                    --------
                    |       |
                    |
                    |
                    |
                    |
                    -
    ]
    return stages[tries]