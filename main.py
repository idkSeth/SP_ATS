import os
from dotenv import load_dotenv
from re import fullmatch
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

user_id = os.getenv("user_id")
pw = os.getenv("pw")

ats_url = "https://myats.sp.edu.sg/"

if user_id == "" or pw == "":
    print("user_id or pw field in .env file is empty. Please input your login details.")
    exit()
elif not fullmatch("p[0-9]{7}", user_id):
    print("user_id field in .env file is invalid. Please check your login details.")
    exit()

ats_code = input("Enter ATS code: ")
# check if ats_code is 6 digits long
while not fullmatch("[0-9]{6}", ats_code):
    ats_code = input("Invalid ATS, please re-enter ATS code: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")

browser = webdriver.Chrome(options=chrome_options)
browser.get(ats_url)
if "502 Bad Gateway" in browser.page_source:
    print("Could not access ATS site, are you connected to SP network?")
    browser.quit()
    exit()
elem = browser.find_element(By.ID, "userid")
elem.send_keys(user_id)
elem = browser.find_element(By.ID, "pwd")
elem.send_keys(pw)
elem = browser.find_element(By.ID, "Submit")
elem.click()
elem = browser.find_element(By.ID, "A_ATS_ATCD_SBMT_A_ATS_ATTNDNCE_CD")
elem.send_keys(ats_code)
elem = browser.find_element(By.ID, "A_ATS_ATCD_SBMT_SUBMIT_BTN")
elem.click()
sleep(3)
browser.quit()
exit()