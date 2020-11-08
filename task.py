# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

import json


def load_from_file(filename):
  with open(filename, "r") as file:
    return json.load(file)


def save_to_file(data, filename):
  with open(filename, "w") as file:
    json.dump(data, file)


def add_school(data, name):
  data["schools"].append({"name": name, "sclasses": []})
  return data


def add_class(school, name):
  school["classes"].append({"name": name, "students": []})
  return school


def get_school_by_name(data, name):
  return list(filter(lambda school: school["name"] == name, data["schools"]))[0]


def get_sclass_by_name(school, name):
  return list(filter(lambda sclass: sclass["name"] == name, school["sclasses"]))[0]


if __name__ == "__main__":
  data = load_from_file("data.json")
  add_school(data, "TESTSCHOOL")
  school2 = get_school_by_name(data, "Liceum Ogólnokształcące im. Stanisława Staszica nr 1 w Krakowie")
  school2["sclasses"].append({"name": "TEST"})

  save_to_file(data, "test.json")