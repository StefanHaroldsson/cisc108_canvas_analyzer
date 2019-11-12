"""
Project 4C
Canvas Analyzer
CISC108 Honors
Fall 2019

Access the Canvas Learning Management System and process learning analytics.

Edit this file to implement the project.
To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Stefan Haroldsson
"""
__version__ = 7

# 1) main
import canvas_requests


def main(user_id):
    user_info = canvas_requests.get_user(user_id)
    print_user_info(user_info)
    courses = canvas_requests.get_courses(user_id)
    filter_available_courses(courses)
    print_courses(courses)
    course_ids = get_course_ids(courses)
    choose_course(course_ids)
    submissions = canvas_requests.get_submissions
    summarize_points(submissions, points_possible, group_weight, score)
    summarize_groups()
    plot_scores()
    plot_grade_trends()


# 2) print_user_info
user_info = canvas_requests.get_user


def print_user_info(user_info: dict):
    print("Name: " + user_info['name'])
    print("Title: " + user_info['title'])
    print("Primary Email: " + user_info['primary_email'])
    print("Bio: " + user_info['bio'])


# 3) filter_available_courses

def filter_available_courses(courses: dict):
    available_courses = []
    for course in courses:
        if course["workflow_state"] == "available":
            available_courses.append(course)
    return available_courses


# 4) print_courses
def print_courses(courses):
    for course in courses:
        print(str(course["id"]) + " : " + course["name"])


# 5) get_course_ids
def get_course_ids(courses):
    course_ids = []
    for course in courses:
        course_ids.append(course["id"])
    return course_ids


# 6) choose_course
def choose_course(course_ids)->int:
    while int(input("What is your class ID?")) not in course_ids:
        user_id = int(input("What is your class ID?"))
    return user_id


# 7) summarize_points


def summarize_points(submissions: list, points_possible: int, group_weight: int, score: int):
   points_possible_so_far = submissions[points_possible] * submissions[group_weight]
   points_obtained = submissions[score] * submissions[group_weight]
   raw_grade = points_obtained / points_possible_so_far
   unrounded_grade = raw_grade * 100
   grade = round(unrounded_grade, 2)
   return grade


# 8) summarize_groups
#def summarize_groups():
 #   pass


# 9) plot_scores
import matplotlib.pyplot as plt


#def plot_scores():
  #  '''import datetime
   # a_string_date = submissions[date_due]
    #due_at = datetime.datetime.strptime(a_string_date, "%Y-%m-%dT%H:%M:%SZ")
  #  x = grade
  #  y = due_at
  #  fig = plt.figure()
   # ax = fig.add_subplot(111)
   # ax.plot(x, y, color='blue', linewidth=5)
   # plt.savefig('plotofscores.png')
   # plt.show()'''
 #   pass


# 10) plot_grade_trends
#def plot_grade_trends():
  #  pass


# Keep any function tests inside this IF statement to ensure
# that your `test_my_solution.py` does not execute it.
if __name__ == "__main__":
    main('hermione')
    # main('ron')
    # main('harry')

    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')
