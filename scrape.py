import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import service
from time
def scrape_website(website):
    print("Connecting to Scraping Browser...")
    
    chrome_driver_path=""
    options=webdriver.ChromeOptions()
    driver=webdriver.Chrome(service=Service(chrome_driver_path),options=options)

    try:
        driver.get(website)
        print("page loaded")
        html=driver.page_source
        time.sleep()




        return html
    
    finally:
        driver.quit()