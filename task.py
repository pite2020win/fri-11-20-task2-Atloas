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

class SubjectGrades:
  def __init__(self, name):
    self.name = name
    self.grades = {}

  def add_grade(self, weight, grade):
    if weight in self.grades:
      self.grades[weight].append(grade)
    else:
      self.grades[weight] = [grade]

class Student:
  def __init__(self, name, surname, subjects):
    self.name = name
    self.surname = surname
    self.attendance = {}
    self.subjectGrades = {}
    for subject in subjects:
      self.subjectGrades[subject] = SubjectGrades(subject)

  def __str__(self):
    return "Student {name} {surname}".format(name=self.name, surname=self.surname)

class HClass:
  def __init__(self, year, letter, subjects):
    self.students = []
    self.year = year
    self.letter = letter
    self.name = "{year}{letter}".format(year=year, letter=letter)
    self.subjects = subjects

  def add_student(self, name, surname):
    self.students.append(Student(name, surname, self.subjects))
  
  def add_students(self, studentList):
    for student in studentList:
      self.add_student(student.get("name"), student.get("surname"))

  def __str__(self):
    to_print = "Class {name}\n".format(name=self.name)
    for student in self.students:
      to_print += "-{student}\n".format(student=student)
    return to_print

class School:
  def __init__(self, name):
    self.name = name
    self.hclasses = []

  def add_class(self, name):
    self.hclasses.append(HClass(name))

  def get_hclass_by_name(hclass_name):
    for hclass in hclasses:
      if hclass.name == hclass_name:
        return hclass

if __name__ == "__main__":
  c = HClass(1, "A", ["Maths", "Physics"])
  c.add_student("A", "B")
  c.add_student("C", "D")
  studentList = []
  student1 = {}
  student1["name"] = "E"
  student1["surname"] = "F"
  student2 = {}
  student2["name"] = "G"
  student2["surname"] = "H"
  studentList.append(student1)
  studentList.append(student2)
  c.add_students(studentList)
  print(str(c))