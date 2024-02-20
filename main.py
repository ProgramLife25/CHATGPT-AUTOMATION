import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.get("https://chat.openai.com/c/83043961-3f72-4266-b094-a46f9d777c1f") #Getting the CHATGPT website

time.sleep(5)
print("Opened login page")
loginbutton = driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/button[1]') #Clicking on the login button
loginbutton.click()
time.sleep(5)
email = driver.find_element(By.XPATH,'//*[@id="username"]') #Entering username or email
email.send_keys("vivektyagi19829@gmail.com")
submit = driver.find_element(By.XPATH,'/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button')
submit.click()
time.sleep(4)
password = driver.find_element(By.XPATH,'//*[@id="password"]') #Entering Password
password.send_keys("hihello25hihello25")
submit2 = driver.find_element(By.XPATH,'/html/body/div[1]/main/section/div/div/div/form/div[2]/button')
submit2.click()
time.sleep(5)
while True:
    user_question = input("Enter your question: ") #Question here

    #OR
    #user_question = ""

    text_place = driver.find_element(By.XPATH,'//*[@id="prompt-textarea"]')
    text_place.send_keys(user_question)
    text_place.send_keys(Keys.RETURN)
    time.sleep(11)
    answer = driver.find_elements(By.XPATH,'//div[contains(@class, "markdown")]')
    print(answer[-1].text) #Getting the answer
    f = open("conversations.txt","a") #saving conversations in a basic text file
    f.write("user: " + user_question +"\n")
    f.write("chatgpt: " + answer[-1].text + "\n")