from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# A suite test for login in digikala.com

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

email = "saahaar_vahedi@yahoo.com"
password = "sahar1995"

# open browser and open digikala.com
driver.maximize_window()
driver.get('https://www.digikala.com')
sleep(5)
assert "دیجی‌کالا" in driver.title

# click on login button
driver.find_element(By.XPATH,'//*[contains(text(), "ورود | ثبت‌نام")]').click()
sleep(1)

# fill username data
username_page_check = driver.find_element(By.XPATH,'//*[contains(text(), "ورود | ثبت‌نام")]').text
assert username_page_check == "ورود | ثبت‌نام"
username = driver.find_element(By.NAME,"username")
username.send_keys(email)
sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div[2]/form/button/div[2]').click()
sleep(2)

# fill password data
pass_page_check = driver.find_element(By.XPATH,'//*[contains(text(), "رمز عبور را وارد کنید")]').text
assert pass_page_check == "رمز عبور را وارد کنید"
ramz = driver.find_element(By.NAME,"password")
ramz.send_keys(password)
sleep(2)
driver.find_element(By.XPATH,'//*[contains(text(), "تایید")]').click()
sleep(3)

# click on account button for validate login
driver.find_element(By.XPATH,'//div[contains(@class, "BaseLayoutMiniProfile_BaseLayoutMiniProfile__profileButton__wUvro")]').click()
sleep(2)
profile_name_check = driver.find_element(By.XPATH,'//*[contains(text(), "سحر واحدی")]').text
assert profile_name_check == "سحر واحدی"
sleep(5)