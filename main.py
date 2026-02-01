import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url)
yc_web = response.text
soup = BeautifulSoup(yc_web,"html.parser")

address=[]
link=[]
price=[]

hotel_name=soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
# print(hotel_name.text)
for i in hotel_name:
    price.append(i.text)

hotel_addr_And_link = soup.find_all(name="div",class_="StyledPropertyCardDataWrapper")
# hotel_addr = hotel_addr_And_link.find("address")
# print(hotel_addr.text.strip())
for i in hotel_addr_And_link:
    address.append(i.find("address").text.strip())
    link.append(i.find("a").get("href"))
    
# hotel_link = hotel_addr_And_link.find("a").get("href")
# print(hotel_link)

# print(address)
# print(link)
# print(price)

# fill the gogle form automatically
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(link)):
    # add fill in the link to your google form 
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScRRRYuBs3JaRMnodHb7HFaIpHrYd5Z9rKwqSjbIEaDMJAZMA/viewform?usp=sf_link')
    time.sleep(2)
    # use the xpath to select the short anser filled in google form
    addres = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    links = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prices = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    addres.send_keys(address[n])
    prices.send_keys(price[n])
    links.send_keys(link[n])
    submit_button.click()

driver.quit()


  




