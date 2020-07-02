import random
from words import word_list

def get_word():
  word = random.choice(word_list)


def play(word):
  word_completion = "-" * len(word)