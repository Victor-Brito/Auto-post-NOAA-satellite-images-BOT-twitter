from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pathlib
#path1 = pathlib.Path(__file__).parent.absolute()#Usa o diretório do arquivo que ta sendo rodado
'''
NOTE: Change the image directory on your computer

EXAMPLE:
path1 = r'C:\\Users\\gurib\\Desktop\\Bot de clima\\Imagens'
'''


name = "1Amazon.gif" 

csp = str(path1)
pathfile = csp + "/" + name
print(pathfile)


driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.twitter.com/login')

email_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
pasword_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
login_button_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div'

time.sleep(8)

email_element = driver.find_element_by_xpath(email_xpath)
passwod_element = driver.find_element_by_xpath(pasword_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)

email_element.click()
email_element.send_keys('@youruser')
passwod_element.click()
passwod_element.send_keys('yourpassword')

time.sleep(2)
login_button_element.click()
time.sleep(5)
tweet_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'

tweet_element = driver.find_element_by_xpath(tweet_xpath)
tweet_element.click()
tweet_element.send_keys('Imagens atualizadas a cada 5 minutos')
driver.find_element_by_xpath("//*[@data-testid='fileInput']").send_keys(pathfile)
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@data-testid,'tweetButtonInline')]").click()
time.sleep(3)

#foto_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[1]/div[1]/div'
#foto_element = driver.find_element_by_xpath(foto_xpath)
#foto_element.click()
