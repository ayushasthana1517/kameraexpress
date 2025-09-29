import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome()
# Actions = ActionChains(driver)


def test_navigate():
    driver.get("https://www.kamera-express.nl/")
    driver.maximize_window()
    driver.implicitly_wait(3)

def test_accept():
    accept = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[3]/div/button[3]")
    accept.click()

def test_products():
    product = driver.find_element(By.XPATH,"//div[@class='header']//li[1]//button[1]//*[name()='svg']//*[name()='path' and contains(@d,'M5 10L12 1')]")
    Actions = ActionChains(driver)
    Actions.move_to_element(product).perform()

def test_fotocamera():
    fotocamera = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/ul/li[1]/span')
    Actions = ActionChains(driver)
    Actions.move_to_element(fotocamera).perform()

def test_fotocam():
    fotocam=driver.find_element(By.XPATH,"//div[@class='nav-menu']//ul[1]//li[1]//a[1]")
    fotocam.click()
    driver.back()

def test_systemcamera():
    test_products()
    test_fotocamera()
    systemcam = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/div/div/ul[1]/li[2]/a')
    systemcam.click()
    driver.back()

def test_spgelrefcamera():
    test_products()
    test_fotocamera()
    spgelrefcam = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/div/div/ul[1]/li[3]/a')
    spgelrefcam.click()
    driver.back()

def test_compactcamera():
    test_products()
    test_fotocamera()
    compcam = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/div/div/ul[1]/li[4]/a')
    compcam.click()
    driver.back()

def test_bridgecamera():
    test_products()
    test_fotocamera()
    bridgecam = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/div/div/ul[1]/li[5]/a')
    bridgecam.click()
    driver.back()

def test_objective():
    test_products()
    obj = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/div/div/ul[1]/li[1]/a/strong')
    Actions = ActionChains(driver)
    Actions.move_to_element(obj).perform()

def test_primelenses():
    primelens = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/div/div/ul[1]/li[2]/a')
    primelens.click()
    driver.back()
    time.sleep(2)

# # def test_zoomlenses():
# #     test_products()
# #     test_objective()
# #     zoomlens=driver.find_element(By.XPATH,"//div[@class='megamenu-sublevel2-container producten']//a[normalize-space()='Zoomlenzen']")
# #     zoomlens.click()
# #     driver.back()
#
# # def test_groothlenses():
# #     test_products()
# #     test_objective()
# #     groothlens =driver.find_element(By.XPATH,'//div[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/div/div/ul[1]/li[4]/a')
# #     groothlens.click()
# #     driver.back()
# #
# # def test_tripods():
# #     test_products()
# #     tripod = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[3]/div[1]/div[3]/div/ul[1]/li[1]/a/strong')
# #     Actions = ActionChains(driver)
# #     Actions.move_to_element(tripod).perform()
# #
# # def test_tripo():
# #     test_products()
# #     test_tripods()
# #     tripo = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/div/div/ul[1]/li[2]/a/font/font')
# #     tripo.click()
# #     driver.back()
#
# # def test_tweedehands():
# #     test_products()
# #     tweedehands = driver.find_element(By.XPATH,'//div[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/ul/li[2]/button/svg/path')
# #     Actions = ActionChains(driver)
# #     Actions.move_to_element(tweedehands).perform()
# #
# #
# # def test_tweedecompcam():
# #     tweedecompcam = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/div/div[1]/ul[1]/li[2]/a')
# #     tweedecompcam.click()
# #     driver.back()
#
# def test_merken():
#     merken = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/ul/li[2]/button/svg/path')
#     Actions = ActionChains(driver)
#     Actions.move_to_element(merken).perform()
#
# def test_canon():
#     canon=driver.find_element(By.XPATH,"//div[@class='nav-menu']//li[@class='active']")
#     Actions = ActionChains(driver)
#     Actions.move_to_element(canon).perform()
#
# def test_canoncompcam():
#     test_merken()
#     test_canon()
#     canoncompcam = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/nav/div/div/div/div[1]/ul[1]/li[2]/a')
#     canoncompcam.click()
#     driver.back()



