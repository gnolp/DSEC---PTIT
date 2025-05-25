from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import os
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)

import sys

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]

MSSV = USERNAME.upper()
BASE_URL = "https://dsec.ptit.edu.vn"
KEYS_DIR = os.path.join(os.getcwd(), "ans")



driver.get(BASE_URL + "/login")
time.sleep(1)
driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)


driver.get(BASE_URL + "/student/question")
time.sleep(2)
while True:
    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    print(f"🔍 Found {len(rows)} questions.")

    links = []
    for row in rows:
        link_elem = row.find_elements(By.TAG_NAME, "a")[0]
        question_url = link_elem.get_attribute("href")
        links.append(question_url)

    print(f"Đã lấy được {len(links)} link câu hỏi.")

    for question_url in links:
        question_code = question_url.rstrip("/").split("/")[-1]
        filename = f"{MSSV}.{question_code}.lab"
        filepath = os.path.join(KEYS_DIR, filename)

        if not os.path.isfile(filepath):
            print(f"❌ File not found: {filename}")
            continue

        driver.get(question_url)
        time.sleep(1)

        file_input = driver.find_element(By.ID, "fileInput")
        file_input.send_keys(filepath)

        submit_btn = driver.find_element(By.CSS_SELECTOR, "form button[type=submit]")
        submit_btn.click()
        print(f"✅ Submitted: {filename}")

        time.sleep(1)
    try:
        next_page_link = driver.find_element(By.CSS_SELECTOR, "ul.pagination li.page-item a.page-link[rel='next']").get_attribute("href")
    except:
        next_page_link = None
    if not next_page_link:
        print("✅ Xong rồi!")
        break

    driver.get(next_page_link)
    time.sleep(2)
driver.quit()