# File:    semester.py
# Started: by Dr. Gibson
# Author:  Uzoma Uwanamodo
# Date:    10/5/2016
# Section: 05
# E-mail:  uu3@umbc.edu
# Description:
#   This file contains python code that asks the user for their
#   courses, then goes through the list and asks them for their
#   raw grade for each course, removes the course from the list, 
#   and calculates and prints their average grade for the semester.

def main():

    # constant for the sentinel value, and an empty list to start
    COURSE_SENTINEL = "NONE"
    courseList = []
    

    # populate the course list
    course = input("What course did you take? ('NONE' to stop): ")

    while course != COURSE_SENTINEL:
    
        # save the course and ask for another
        courseList.append(course)
        course = input("What course did you take? ('NONE' to stop): ")
    
    # create variables to help calculate the student's average
    totalGrade = 0 # The raw sum of all of the grades
    i = 0
    # go through the course list; continue while the list is not empty
    
    while i < len(courseList):
        totalGrade += int(input("What raw grade did you get in %s? " % courseList[i]))     # ask about their grade for each course and save it to the total


        i+=1

    # print out their average raw grade
    print("In the %s courses you took, you received a %.2f as your average raw grade." % (i,totalGrade/i))

main()
