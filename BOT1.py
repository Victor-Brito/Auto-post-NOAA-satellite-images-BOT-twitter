from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pathlib


driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.star.nesdis.noaa.gov/GOES/sector_band.php?sat=G16&sector=nsa&band=GEOCOLOR&length=24')

time.sleep(30)
botao_down = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[4]/a")
botao_down.click()

time.sleep(10)

botao_download = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div/a")
botao_download.click()

time.sleep(10)

botao_fechar = driver.find_element_by_xpath("/html/body/div[4]/div/div/a")
botao_fechar.click()

time.sleep(5)
'''
NOTE: Change the image directory on your computer

EXAMPLE:
dir = 'C:/Users/gurib/Desktop/Bot de clima/Imagens'
'''
os.chdir(dir)
files=os.listdir(dir)
for i in range (len(files)):
    os.rename(files[i], str(i+1)+'Amazon.gif')
time.sleep(15)
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
tweet_element.send_keys('Loop de 4 horas - 24 imagens - atualizadas em 10 minutos ')
'''
NOTE: Change the image directory on your computer

EXAMPLE:
path1 = r'C:\\Users\\gurib\\Desktop\\Bot de clima\\Imagens'  
'''
    
name = "1Amazon.gif" 

csp = str(path1)
pathfile = csp + "/" + name
print(pathfile) 

driver.find_element_by_xpath("//*[@data-testid='fileInput']").send_keys(pathfile)
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@data-testid,'tweetButtonInline')]").click()
time.sleep(35)
'''
NOTE: Change the image directory on your computer

EXAMPLE:
os.unlink('C:\\Users\\gurib\\Desktop\\Bot de clima\\Imagens\\1Amazon.gif') #comando para deletar a imagem 
'''

time.sleep(30)#intervalo de tempo

def reiniciarBot():
  driver.get('https://www.star.nesdis.noaa.gov/GOES/sector_band.php?sat=G16&sector=nsa&band=GEOCOLOR&length=24')
  time.sleep(570)
  botao_down = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[4]/a")
  botao_down.click()

  time.sleep(10)

  botao_download = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div/a")
  botao_download.click()

  time.sleep(10)

  botao_fechar = driver.find_element_by_xpath("/html/body/div[4]/div/div/a")
  botao_fechar.click()

  time.sleep(5)
    '''
    NOTE: Change the image directory on your computer

    EXAMPLE:
  dir = 'C:/Users/gurib/Desktop/Bot de clima/Imagens'
  '''
  os.chdir(dir)
  files=os.listdir(dir)
  for i in range (len(files)):
    os.rename(files[i], str(i+1)+'Amazon.gif')
  time.sleep(15)
  driver.get('https://www.twitter.com/login')

  time.sleep(5)
  tweet_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'

  tweet_element = driver.find_element_by_xpath(tweet_xpath)
  tweet_element.click()
  tweet_element.send_keys('Loop de 4 horas - 24 imagens - atualizadas em 10 minutos ')
  '''
  NOTE: Change the image directory on your computer

    EXAMPLE:
  path1 = r'C:\\Users\\gurib\\Desktop\\Bot de clima\\Imagens'  
  '''
    
  name = "1Amazon.gif" 

  csp = str(path1)
  pathfile = csp + "/" + name
  print(pathfile) 

  driver.find_element_by_xpath("//*[@data-testid='fileInput']").send_keys(pathfile)
  time.sleep(3)
  driver.find_element_by_xpath("//*[contains(@data-testid,'tweetButtonInline')]").click()
  time.sleep(35)
  '''
  NOTE: Change the image directory on your computer

    EXAMPLE:
  os.unlink('C:\\Users\\gurib\\Desktop\\Bot de clima\\Imagens\\1Amazon.gif') #comando para deletar a imagem 
  '''
  time.sleep(20)
if __name__ == "__main__":
    for i in range(1,500):
        reiniciarBot()

