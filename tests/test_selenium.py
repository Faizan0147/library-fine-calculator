"""Selenium checks for the library fine calculator.

Start the app first (python app.py), then run: python tests/test_selenium.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "http://127.0.0.1:5000/"

CASES = [
    ("-1", "Invalid input"),
    ("0", "Fine: Rs 0"),
    ("3", "Fine: Rs 0"),
    ("4", "Fine: Rs 10"),
    ("20", "Fine: Rs 170"),
    ("21", "Invalid input"),
]


def main():
    driver = webdriver.Chrome()
    print(f"{'Input':<8}{'Expected':<18}{'Actual':<18}Result")
    failed = 0
    try:
        for value, expected in CASES:
            driver.get(URL)
            driver.find_element(By.ID, "days").send_keys(value)
            driver.find_element(By.ID, "submit").click()
            actual = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "result"))
            ).text
            status = "PASS" if actual == expected else "FAIL"
            failed += status == "FAIL"
            print(f"{value:<8}{expected:<18}{actual:<18}{status}")
    finally:
        driver.quit()
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
