from selenium import webdriver
from time import sleep
​
driver= webdriver.Chrome("/Users/ryo/chromedriver")
url="https://id.jobcan.jp/users/sign_in"
driver.get(url)
login_id=driver.find_element_by_xpath("//input[@id='user_email']")
login_pass=driver.find_element_by_xpath("//input[@id='user_password']")
​
userid="メールアドレス打つ"
userpass="パスワードはここ"
login_id.send_keys(userid)
login_pass.send_keys(userpass)
sleep(1)
​
login_pass.submit()
sleep(1)
​
attendance=driver.find_element_by_link_text("勤怠")
attendance.click()
sleep(3)
​
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_id('adit-button-push').click()
​
​
​
​
​
