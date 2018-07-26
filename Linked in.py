from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def producing_links(driver, wait):

    driver.get('https://www.linkedin.com/')

    driver.find_element_by_xpath('//*[@id="login-email"]').send_keys('sunilkumarsdlp@gmail.com')
    driver.find_element_by_xpath('//*[@id="login-password"]').send_keys('sumonilka@link')
    driver.find_element_by_xpath('//*[@id="login-submit"]').click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@class,'feed-s-follows-module__view-all')]")))
    driver.find_element_by_xpath("//a[contains(@class,'feed-s-follows-module__view-all')]").click()

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@class,'feed-s-follow-recommendation-card__profile-link')]")))
        links = [item.get_attribute("href") for item in driver.find_elements_by_xpath("//a[contains(@class,'feed-s-follow-recommendation-card__profile-link')]")]
        if (len(links) == 200): 
            break


    for link in links:
        get_docs(driver, wait, link)

def get_docs(driver, wait, name_link):

    driver.get(name_link)
    try:
        for item in driver.find_elements_by_xpath("//div[contains(@class,'pv-top-card-section__information') or contains(@class,'org-top-card-module__details') or (@class='org-top-card-module__main-column')]"):
            name = item.find_element_by_xpath(".//h1[@title]|.//h1[contains(@class,'pv-top-card-section__name')]").text
            title = item.find_element_by_xpath(".//span[contains(@class,'company-industries')]|.//h2[contains(@class,'pv-top-card-section__headline')]").text
    except Exception as e:
        print(e)

    finally:
        try:
            print(name, title)
        except Exception as ex:
            print(ex)


if __name__ == '__main__':

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        producing_links(driver, wait)
    finally:
        driver.quit()