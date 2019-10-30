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

#1) main
import canvas_requests
def main(user_id):
    user_info = canvas_requests.get_user
    print_user_info(user_info)
    all_courses=canvas_requests.get_courses
    filter_available_courses(all_courses,available_courses)
    print_courses(available_courses)
    get_course_ids(available_courses, course_ids)
    choose_course(course_ids)
    submissions = canvas_requests.get_submissions
    summarize_points(submissions, points_possible, group_weight, score)
    summarize_groups()
    plot_scores()
    plot_grade_trends()

# 2) print_user_info

user_info = canvas_requests.get_user
def print_user_info(user_info:dict):
    print(user_info)
# 3) filter_available_courses
all_courses = canvas_requests.get_courses
def filter_available_courses(all_courses:dict, available_courses:list):
    for course in all_courses:
        if "available" == course["course_availability"]:
            available_courses = available_courses.append["course"]
            return available_courses
        else:
            return None
# 4) print_courses
def print_courses(available_courses):
    for course in available_courses:
        print (course[id] + ":" + course)
# 5) get_course_ids
def get_course_ids(available_courses, course_ids=list):
    for course in available_courses:
        course_ids = course_ids.append[course[id]]
        return course_ids
# 6) choose_course
def choose_course(course_ids):
    initial_user_id = input("What is your class ID?")
    while user_id in course_ids == True:
        user_id: int = int(initial_user_id)
    return user_id
# 7) summarize_points
submissions = canvas_requests.get_submissions
def summarize_points(submissions:list, points_possible:int, group_weight:int, score:int):
    points_possible_so_far= submissions[points_possible] * submissions[group_weight]
    points_obtained = submissions[score]*submissions[group_weight]
    raw_grade = points_obtained / points_possible_so_far
    unrounded_grade = raw_grade*100
    grade = round(unrounded_grade,2)
    return grade
# 8) summarize_groups
def summarize_groups():

# 9) plot_scores
import matplotlib.pyplot as plt
def plot_scores():
    import datetime
    a_string_date = submissions[]
    due_at = datetime.datetime.strptime(a_string_date, "%Y-%m-%dT%H:%M:%SZ")
    x = grade
    y = due_at
# 10) plot_grade_trends
def plot_grade_trends():


# Keep any function tests inside this IF statement to ensure
# that your `test_my_solution.py` does not execute it.
if __name__ == "__main__":
    main('hermione')
    # main('ron')
    # main('harry')
    
    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')