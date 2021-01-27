from selenium import webdriver
from sources import tokens
import csv

driver = webdriver.Chrome("driver/chromedriver.exe")



with open("data.csv","w",newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["token","aDAI","ONC","vUSD","BAL","BT","ONS"])

def scrape(token):
    driver.get(f"https://etherscan.io/address/{token}")
    driver.implicitly_wait(3)
    dropdown = driver.find_element_by_xpath("//*[@id='availableBalanceDropdown']")
    dropdown.click()
    driver.implicitly_wait(3)
    search = driver.find_element_by_xpath("//*[@id='availableBalanceClick']/div[1]/input")
    search.clear()
    search.send_keys("aDaI")
    aDAI = driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li/a/div[2]/span[1]").text
    print("aDAI: "+aDAI)
    search.clear()
    search.send_keys("ONC")
    ONC = driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li/a/div[2]/span[1]").text
    print("ONC: "+ONC)
    search.clear()
    search.send_keys("vUSD")
    vUSD = driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li/a/div[2]/span[1]").text
    print("vUSD: "+vUSD)
    search.clear()
    search.send_keys("BAL")
    BAL = driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li/a/div[2]/span[1]").text
    print("BAL: "+BAL)
    search.clear()
    search.send_keys("BT.")
    BT = driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li/a/div[2]/span[1]").text
    print("BT: "+BT)
    search.clear()
    search.send_keys("ONS")
    ONS = driver.find_element_by_xpath("//*[@id='mCSB_1_container']/ul/li/a/div[2]/span[1]").text
    print("ONS: "+ONS)
    with open("data.csv", "a", newline="")as file:
        writer = csv.writer(file)
        writer.writerow([token,aDAI,ONC,vUSD,BAL,BT,ONS])

for token in tokens:
    scrape(token)