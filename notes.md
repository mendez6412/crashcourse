# Introduction (5-10 minutes)
  - Shannon and Tommy
    - backgrounds
  - Students
    - background with programming

# Getting Ready (10 minutes)
  - Install Atom via https://atom.io/
  - Setting Up
    - command + space --> terminal
    - cd Desktop
    - mkdir number_game
    - cd number_game
    - touch guess.py
    - atom .

# Python Basics (15-20 minutes)
  - Python3 Shell
    - Types (String, Float, Int, Bool, Class Object)
      - Which types might we be using to build our number guessing game?
      - List/Array, Dict, (Tuple)
    - Variables (x = 1, x = 'a', etc)
      - What is a variable?
      - Why might variables be useful?
    - Operators (!=, <, >, ==, %)
      - and
    - Functions (def fancy(x))
      - return
      - print
      - example: if KEYWORD
      - When might it be better to return vs. print?
    - Loops (While, For)
    - Other Keywords (import, (lambda))
    - Explain dunder name == dunder main

# Creating the Game (40 minutes)
  - We will be making the game so that the human player has to guess the number the computer is thinking of.
  - We need a secret number
    - How could we have the computer choose the number?
    - import random
    - set secret number variable
      - Why do we need to set this as a variable? Why can't we just say we want a random number every time?
    - place in a function
    - What does putting this in a function help us with?
  - Testing
  - We need to get a guess
    - What type does input return?
      - How do we convert that? int()
    - set guess variable
    - Why should we set this to a variable?
    - place in a function
  - Check guess compared to secret number
  - Play the game

# Improving the Game
  - # of Guesses
    - Use while loop with incrementing variable
  - High or Low
    - Have the computer tell you if your guess was high or low
  - You hide a number from the computer
  - OOP

#Wrap Up and Reflection (10 minutes)
  - Which types did we end up using to make our game?
  - What are some ways you could improve your game?
  - What are some things you learned to do with Python through making this game?
  - What were the two reasons we used print()?
