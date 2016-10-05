# File:    semester.py
# Started: by Dr. Gibson
# Author:  YOUR NAME GOES EHRE
# Date:    DATE GOES HERE
# Section: SECTION NUMBER GOES HERE
# E-mail:  EMAIL_GOES_HERE@umbc.edu 
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

    #### YOU NEED TO PUT A WHILE LOOP HERE
    
        # save the course and ask for another
        courseList.append(course)
        course = input("What course did you take? ('NONE' to stop): ")
    
    # create variables to help calculate the student's average


    # go through the course list; continue while the list is not empty
    
        # ask about their grade for each course and save it to the total

        # remove() the course from the list


    # calculate their average raw grade


    # print out their average raw grade


main()
