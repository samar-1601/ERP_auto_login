import loginData as USER

from selenium import webdriver
import selenium # main selenium import
from selenium.webdriver.common.keys import Keys # import which helps us use keys like Enter, Escape
import time # to add delay, sleep featues

# to comabt the depreciation warning which I'd got before
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# for waiting part code
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s) # use a variable driver to access the webpage
# driver.maximize_window()  # To maximize the window which will open after the code is run 

# Open ERP
driver.get("https://erp.iitkgp.ac.in/SSOAdministration/login.htm?sessionToken=F6949C1656A2C6C65D0617A5A78FDEEA.worker3&requestedUrl=https://erp.iitkgp.ac.in/IIT_ERP3/showmenu.htm") 

# Wait for ERP to open
driver.implicitly_wait(1)

# Handle user_id
user_id_text = driver.find_element(By.ID, 'user_id')
# Clear the input box if something is already written
user_id_text.clear()
# Input the user_id
user_id_text.send_keys(USER.user_name)

# Handle user_password
password_text = driver.find_element(By.ID, 'password')     
# Clear the input box if something is already written
password_text.clear()
# Input the user_password
password_text.send_keys(USER.password)

# Wait untill the security question appears
security_question = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.ID, 'question'))
)

# print(f"security_question : {security_question}")
# print(f"security_question.text : {security_question.text}")

# Initializing security_answer
security_answer = ""

# Iterate throught the "question_list" dictionary to get the corresponding answer
for question, answer in USER.question_list.items():
    if question == security_question.text:
        security_answer = answer

# Handle the security_answer 
security_answer_text = driver.find_element(By.ID, 'answer') 
# Clear the input box if something is already written
security_answer_text.clear()
# input the security_answer
security_answer_text.send_keys(security_answer)

# Now we finally submit after filling all the details
submit_button = driver.find_element(By.ID, 'loginFormSubmitButton')
submit_button.click()

# added this line so the the script keeps running
temp = input()

