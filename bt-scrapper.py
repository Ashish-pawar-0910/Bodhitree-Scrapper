from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import subprocess

# This is done to sync this file to the resources file in the assets folder
subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)

######################################################################################################
# Enter login credentials
email = ""
password = ""

"""
Sometimes, the given expected score for Bodhitree quizzes is different from the actual expected score. This is because
(Bodhitree is shit) the number of attempts/scores fluctuate or the content gets boom! So to balance those changes, a per subject fluctuation has to be maintained.
And this is what this balance dictionary is about!
The format is "Subject-Name" : [out video score fluctuation, in video score fluctuation]
For e.g., in the DM course of Div. A and B, the actual attainable out video score is 59, whereas the given max out video score is 60. This fluctuation is noted here.
"""

balance = {
    "Discrete Mathematics SE Comp A & B": [1, 0],
    "Object Oriented Programming using C++ , Division B and D": [0, 0],
    "Fundamental of Data Structures": [0, 7],
    "Computer Graphics Lab (Div - B)": [1, 0],
    "Humanity and Social Science": [0, 0],
    "Digital Electronics Lab ( SE COMP B Division)": [10, 3],
    "Data Structure Laboratory_SE_B": [0, 1],
    "DELD Theory SE COMP Div B-Dr. Ranjanikar": [0, 0],
    "Computer Graphics": [0, 0],
}

###############################################################################################

try:
    browser = webdriver.Chrome(executable_path="./assets/chromedriver_linux")
except:
    try:
        browser = webdriver.Chrome(executable_path="assets\\chromedriver_windows.exe")
    except:
        raise Exception("ERROR: Place the appropriate web driver in the assets folder")

print("The process usually takes 1-2 minutes! (Don't interfere)\n")


def login():
    browser.maximize_window()
    browser.get("https://pccoe.bodhi-tree.in/accounts/login/")

    # Entering Credentials
    browser.find_element_by_id("signinUsername").clear()
    browser.find_element_by_id("signinUsername").send_keys(email + Keys.RETURN)
    browser.find_element_by_id("signinPassword").clear()
    browser.find_element_by_id("signinPassword").send_keys(password + Keys.RETURN)


def main():
    login()
    # Student's name
    name = (
        WebDriverWait(browser, timeout=15)
        .until(lambda b: b.find_element_by_css_selector(".dropdown-toggle"))
        .text
    )

    # List of all the courses enrolled
    courses = browser.find_elements_by_css_selector(".mycourseTitle a")

    # Opening all courses in new tabs
    for course in courses:
        course.send_keys(Keys.CONTROL + Keys.RETURN)

    # Maintaining list of visited tabs
    visited = [browser.current_window_handle]

    title_printed = False
    for tab in browser.window_handles:
        if tab not in visited:
            browser.switch_to.window(tab)
            visited.append(tab)

            leaderboard = browser.find_element_by_css_selector(
                "#sideList-score-card"
            ).click()
            try:
                scores = [
                    score.text.split("\n")
                    for score in WebDriverWait(browser, timeout=20).until(
                        lambda b: b.find_elements_by_css_selector(".panel-title")
                    )
                ]
            except:
                raise Exception("ERROR: Connection Error!")

            course_title = browser.find_element_by_css_selector(".courseTitle").text

            imbalanced = False
            try:
                expected_out_video_score = (
                    int(
                        browser.find_element_by_xpath(
                            "//span[@data-reactid='.1.1.0.0.0.0.1.0.0.1']"
                        ).text
                    )
                    - balance[course_title][0]
                )
                expected_in_video_score = (
                    int(
                        browser.find_element_by_xpath(
                            "//span[@data-reactid='.1.1.0.0.0.0.1.0.1.1']"
                        ).text
                    )
                    - balance[course_title][1]
                )
            except:
                expected_out_video_score = int(
                    browser.find_element_by_xpath(
                        "//span[@data-reactid='.1.1.0.0.0.0.1.0.0.1']"
                    ).text
                )
                expected_in_video_score = int(
                    browser.find_element_by_xpath(
                        "//span[@data-reactid='.1.1.0.0.0.0.1.0.1.1']"
                    ).text
                )
                imbalanced = True

            for i in scores:
                if i[1] == name:
                    out_video_score = int(i[3])
                    in_video_score = int(i[5])
                    title_printed = False

                    if expected_out_video_score > out_video_score:
                        print("Course Name:", course_title)
                        print(
                            "Remaining out video score:",
                            expected_out_video_score - out_video_score,
                        )
                        title_printed = True

                    if expected_in_video_score > in_video_score:
                        if title_printed == False:
                            print("Course Name:", course_title)
                            title_printed = True
                        print(
                            "Remaining in video score:",
                            expected_in_video_score - in_video_score,
                        )

                    if title_printed:
                        print("")
                    break

    if imbalanced:
        print("If possible, update the resource.py file in the assets folder with your course!")
    if title_printed == False:
        print("Well Done! All quizzes completed.\n")


main()
