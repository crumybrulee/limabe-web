from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import json

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://kemensos.go.id/direktorat-jenderal-rehabilitasi-sosial")


produklist = []
i = 1

while i<=120:
    for produk in driver.find_elements_by_tag_name("article"):
        driver.execute_script("arguments[0].scrollIntoView();", produk) #auto scroll
        print(produk.text.split("\n"))
        for img in produk.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            # urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".jpg")
            i = i+1

            produklist.append(
                {
                    "Judul": produk.text.split("\n")[0],
                    "Link" : produk.find_element_by_tag_name('a').get_attribute('href'),
                    "Penulis": produk.text.split("\n")[2],
                    "Editor": produk.text.split("\n")[4],                    
                    "Publish" : produk.find_element_by_xpath("//*[@class='meta-post']//a").text,
                    "Image": img.get_attribute("src")                
                }
            )
    try:
        driver.find_element_by_class_name("pagination").find_element_by_link_text("»").click()
    except NoSuchElementException as e:
        break

hasil_scraping = open("hasilscraping.json", "w")
json.dump(produklist, hasil_scraping, indent=6)
hasil_scraping.close()

driver.quit
