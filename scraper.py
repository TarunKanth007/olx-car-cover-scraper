import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def scrape_car_covers_from_olx():
    url = "https://www.olx.in/items/q-car-cover"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    print("Opening OLX search page...")

    driver.get(url)
    time.sleep(5) 

    print("Extracting listings...")
    listings = []

    items = driver.find_elements(By.CSS_SELECTOR, 'li[data-aut-id="itemBox"]')

    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, 'span[data-aut-id="itemTitle"]').text
            price = item.find_element(By.CSS_SELECTOR, 'span[data-aut-id="itemPrice"]').text
            location = item.find_element(By.CSS_SELECTOR, 'span[data-aut-id="item-location"]').text
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')

            listings.append({
                "title": title,
                "price": price,
                "location": location,
                "link": link
            })
        except Exception:
            continue

    driver.quit()
    print(f"Found {len(listings)} car cover listings.")

    with open("output.json", "w", encoding="utf-8") as output_file:
        json.dump(listings, output_file, indent=4, ensure_ascii=False)

    print("Listings saved to output.json")


if __name__ == "__main__":
    scrape_car_covers_from_olx()
