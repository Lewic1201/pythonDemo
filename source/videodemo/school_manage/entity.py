#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 18:21
# @Author  : Administrator
# @File    : entity.py
# @Software: PyCharm
# @context :
import pickle


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address

        self.teachers = {}
        self.students = {}
        self.courses = {}
        self.classes = {}


class Student:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.school = None
        self.classs = None

    def select_school(self, school):
        self.school = school

    def select_class(self, classs):
        self.classs = classs


class Course:
    def __init__(self, name, period, price, address=None):
        self.name = name
        self.period = period
        self.price = price
        self.address = address


class Teacher:
    def __init__(self, name, classs={}):
        self.name = name
        self.classs = classs

    def add_class(self, classs):
        self.classs[classs.class_name] = classs


class Classs:
    def __init__(self, name, teacher, course, students={}):
        self.name = name
        self.teacher = teacher
        self.course = course
        self.students = students

    def add_student(self, student):
        self.students[student.name] = student


class ManageView:
    def __init__(self, school):
        self.school = school

    def create_teacher(self, teacher_name):
        self.school.teachers[teacher_name] = Teacher(teacher_name)

    def create_course(self, course_name, period, price):
        self.courses[course_name] = Course(course_name, period, price, self.school.address)

    def create_class(self, class_name, teacher, course, students={}):
        new_class = Classs(class_name, teacher, course, students)
        self.school.classes[class_name] = new_class

    # def get_teacher(self):
    #     teachers = [name for name in self.teachers]
    #     return teachers


class TeacherView:
    def __init__(self, teacher):
