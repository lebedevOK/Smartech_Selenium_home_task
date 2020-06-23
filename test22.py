from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math


try: 
    #открываем яндекс
    link = "https://yandex.ru/"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим поле, пишем текст запроса
    input1 = browser.find_element_by_id("text")
    input1.send_keys("расчет расстояний между городами")

    #нажимаем на кнопку Найти
    button1 = browser.find_element_by_class_name("search2__button")
    button1.click()
    
    time.sleep(5)

    #нажимаем на ссылку
    browser.find_element_by_partial_link_text("avtodispetcher.ru").click()

    new_window = browser.window_handles[1]    
    browser.switch_to.window(new_window)    
    time.sleep(10)
    browser.execute_script("window.scrollTo(0, 450)")
            
    #находим поле Откуда, пишем текст 
    input1 = browser.find_element_by_name("from")
    input1.send_keys("Тула")

    #находим поле Куда, пишем текст 
    input2 = browser.find_element_by_name("to")
    input2.send_keys("Санкт-Петербург")

    #находим поле Расход топлива, пишем текст 
    browser.find_element_by_name("fc").clear()
    input3 = browser.find_element_by_name("fc")
    input3.send_keys("9")

    #находим поле Цена топлива, пишем текст 
    browser.find_element_by_name("fp").clear()
    input4 = browser.find_element_by_name("fp")
    input4.send_keys("46")

    #нажимаем на кнопку Рассчитать
    button2 = browser.find_element_by_xpath("//div[@class='submit_button']//input")
    button2.click()

    time.sleep(5)
    browser.execute_script("window.scrollTo(0, 450)")
    time.sleep(5)

    #проверяем результаты
    #находим элемент, содержащий текст
    totalDistance = browser.find_element_by_id("totalDistance")
    distance = totalDistance.text
    #print(distance)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "897" == distance, "Проверка расстояния не выполнена"

    pet_val = browser.find_element_by_tag_name("body")
    val_rr = pet_val.text
    find = "3726"
    #print(val_rr)
    #assert 
    if find in val_rr:
        print("Все хорошо")
 
    link1 = browser.find_element_by_class_name("anchor")   
    link1.click()
    time.sleep(3)

    input5 = browser.find_element_by_xpath("//input[@name='v']")
    input5.send_keys("Великий Новгород;")
    
    browser.maximize_window()
    #ждем 60 секунд
    time.sleep(60) 
    
    browser.execute_script("window.scrollTo(0, 250)")

    #share = browser.find_element_by_xpath("//div[@class='submit_button']//input")
    #webdriver.ActionChains(browser).move_to_element(share).click(share).perform()
    #button1 = browser.find_element_by_xpath("//div[@class='submit_button']//input")
    #button1.click()

    element = browser.find_element_by_xpath("//div[@class='submit_button']//input")
    element.send_keys(Keys.ENTER)

    time.sleep(20)
    browser.execute_script("window.scrollTo(0, 400)")
    
    #проверяем результаты
    #находим элемент, содержащий текст
    totalDistance = browser.find_element_by_id("totalDistance")
    distance = totalDistance.text
    #print(distance)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "966" == distance, "Проверка скорректированного расстояния не выполнена"

    pet_val = browser.find_element_by_tag_name("body")
    val_rr = pet_val.text
    find = "4002"
    #print(val_rr) 
    if find in val_rr:
        print("Все опять хорошо ;)")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    
    browser.quit()
    
