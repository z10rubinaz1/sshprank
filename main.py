from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)



driver.get("https://www.feelingsurf.fr/login")

time.sleep(4)
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[1]/div/div/form/fieldset/div[1]/div/input').send_keys("z10rubinaz1")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/form/fieldset/div[2]/div/input').send_keys("mina38985")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[1]/div/div/form/fieldset/div[3]/button').click()
time.sleep(7)
driver.get("https://www.feelingsurf.fr/surfbar")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/div[1]/div/div/button').click()
time.sleep(600)
print(driver.title)
time.sleep(800)
print("Working")
time.sleep(710)
print("Seems like working..;)")
time.sleep(870)

print("Done :)")
driver.quit()
