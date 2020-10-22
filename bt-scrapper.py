from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from assets import resource
import subprocess

# This is done to sync this file to the resources file in the assets folder
subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)

try:
    browser = webdriver.Chrome(executable_path="assets/chromedriver")
except:
    try:
        browser = webdriver.Chrome(executable_path="assets\\chromedriver_windows.exe")
    except:
        print("ERROR: Place the appropriate web driver in the assets folder")

print("The process usually takes 1-2 minutes! (Don't interfere)\n")

browser.maximize_window()
browser.get("https://pccoe.bodhi-tree.in/accounts/login/")

# Entering Credentials
browser.find_element_by_id("signinUsername").clear()
browser.find_element_by_id("signinUsername").send_keys(resource.email + Keys.RETURN)
browser.find_element_by_id("signinPassword").clear()
browser.find_element_by_id("signinPassword").send_keys(resource.password + Keys.RETURN)

# Student's name
name = (WebDriverWait(browser, timeout=15).until(lambda b: b.find_element_by_css_selector(".dropdown-toggle")).text)

# List of all the courses enrolled
courses = browser.find_elements_by_css_selector(".mycourseTitle a")

# Opening all courses in new tabs
for course in courses:
    course.send_keys(Keys.CONTROL + Keys.RETURN)

# Maintaining list of visited tabs
visited = [browser.current_window_handle]

for tab in browser.window_handles:
    if tab not in visited:
        browser.switch_to.window(tab)
        visited.append(tab)

        leaderboard = browser.find_element_by_css_selector("#sideList-score-card").click()
        try:
            scores = [
                score.text.split("\n")
                for score in WebDriverWait(browser, timeout=20).until(
                    lambda b: b.find_elements_by_css_selector(".panel-title")
                )
            ]
        except:
            print("ERROR: Connection Error!")

        course_title = browser.find_element_by_css_selector(".courseTitle").text
        expected_out_video_score = int(browser.find_element_by_xpath("//span[@data-reactid='.1.1.0.0.0.0.1.0.0.1']").text) - resource.balance[course_title][0]
        expected_in_video_score = int(browser.find_element_by_xpath("//span[@data-reactid='.1.1.0.0.0.0.1.0.1.1']").text)- resource.balance[course_title][1]

        for i in scores:
            if i[1] == name:
                out_video_score = int(i[3])
                in_video_score = int(i[5])
                title_printed = False

                if expected_out_video_score > out_video_score:
                    print("Course Name:", course_title)
                    print("Remaining out video score:",expected_out_video_score - int(i[3]))
                    title_printed = True

                if expected_in_video_score > in_video_score:
                    if title_printed == False:
                        print("Course Name:", course_title)
                        title_printed = True
                    print("Remaining in video score:", expected_in_video_score - int(i[5]))

                if title_printed:
                    print("")
                break
                
if title_printed == False:
    print("Well Done! All quizzes completed.\n")    