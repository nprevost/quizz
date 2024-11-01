# -*- coding: utf-8 -*-
"""Quizz.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EjpuTsmbqrnwe9Qzs-Flmkz29hxjqivO
"""

class Quizz():
  def __init__(self, nb_de_chances):
    self.nb_de_chances = nb_de_chances

    print("Voici notre quiz, tu as {} chances !".format(self.nb_de_chances))

  def question(self, questions):

    for key, question in questions.items():
      if self.nb_de_chances > 0:
        question1= input(question["Q"])
        while question1 != question["R"]:
          self.nb_de_chances -= 1
          print("Dommage ! Il te reste {} chances".format(self.nb_de_chances))
          if self.nb_de_chances == 0:
            print("Oh non ! Tu as perdu le jeu...")
            break
          question1 = input(question["Q"])

    if self.nb_de_chances > 0:
      print("Bravo ! Tu as gagné le quiz !")

quizz1 = Quizz(3)

questions = {"question1": {"Q": "Combien de fois la France a gagné la coupe du monde ? ", "R": "2"},
             "question2": {"Q": "Quand a été fondé Apple ? ", "R": "1976"},
             "question3": {"Q": "Qui a fondé SpaceX ? ", "R": "elon musk"}}

quizz1.question(questions)