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
    summarize_points(submissions)
    summarize_groups(submissions)



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
    my_course = int(input("Pick a course id:"))
    while my_course not in course_ids:
        my_course = int(input("Pick a course id:"))
    return my_course


# 7) summarize_points


def summarize_points(submissions: []):
    total_possible = 0
    points_obtained = 0
    for submission in submissions:
        if submission["score"] is not None:
            points_possible = submission["assignment"]["points_possible"]
            group_weight = submission["assignment"]["group"]["group_weight"]
            total_possible = total_possible + (points_possible * group_weight)
            points_obtained = points_obtained + (submission["score"] * group_weight)
    print("Points possible so far: " + str(total_possible))
    print("Points obtained: " + str(points_obtained))
    print("Current grade: " + str(round((points_obtained / total_possible) * 100)))


# 8) summarize_groups
def summarize_groups(submissions:list):
    group_points={}
    group_score={}
    for submission in submissions:
        if submission["score"] is not None:
            group_name = submission["assignment"]["group"]["name"]
            if group_name not in group_score:
                group_points[group_name] = 0
                group_score[group_name] = 0
            group_score[group_name] = group_score[group_name] + submission["score"]
            group_points[group_name] = group_points[group_name] + submission["assignment"]["points_possible"]
    for name in group_score:
        score = group_score[name]
        points = group_points[name]
        print("*", name, round(100 * score/points))



# 9) plot_scores
import matplotlib.pyplot as plt

def plot_scores(grade:int,submissions:dict):
   pass


# 10) plot_grade_trends
#def plot_grade_trends():
  #  pass


# Keep any function tests inside this IF statement to ensure
# that your `test_my_solution.py` does not execute it.
if __name__ == "__main__":
    main('hermione')
    main('ron')
    main('harry')

    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')
