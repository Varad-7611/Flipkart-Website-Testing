from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# setup driver
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.flipkart.com/")
time.sleep(2)

box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/header/div[1]/div[2]/form/div/div/input")
box.send_keys("samsung s25 ultra")
box.send_keys(Keys.ENTER)
time.sleep(3)

f = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div[1]/div/div[1]/div/section[3]/div[2]/div/div[4]/div/label/div[2]")
f.click()
time.sleep(7)

clear1 =  driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div/div[1]")
clear1.click()
time.sleep(4)

option = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[4]").click()
time.sleep(3)

page_height = driver.execute_script("return document.body.scrollHeight")

# Smooth scroll down
for i in range(0, page_height, 50):  # step = 50px
    driver.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(0.01)   # wait to make it smooth

time.sleep(2)

# Smooth scroll up
for i in range(page_height, 0, -50):
    driver.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(0.01)
time.sleep(3)

wait = WebDriverWait(driver, 10)
add = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]").click()
time.sleep(5)

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

add_to = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()
time.sleep(2)

pincode_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/button")
pincode_btn.click()
pincode_box = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div[2]/input")))
pincode_box.send_keys("400001")
pincode_box.send_keys(Keys.ENTER) 
time.sleep(2)

save = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div[3]/div[2]/div[1]").click()
time.sleep(2)

remove_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]")))
remove_cart.click()
time.sleep(2)


confirm_remove = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div[1]")))
confirm_remove.click()
time.sleep(5)

driver.quit()


