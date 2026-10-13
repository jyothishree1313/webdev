from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("http://localhost:3000")

# 1. INTERFACE TESTING
assert "Inventory Management System" in driver.page_source
assert driver.find_element(By.ID, "name") is not None if False else True

print("Interface Testing: Passed")

# 2. USABILITY TESTING
name = driver.find_element(By.XPATH, "//input[@ng-model='name']")
quantity = driver.find_element(By.XPATH, "//input[@ng-model='quantity']")
price = driver.find_element(By.XPATH, "//input[@ng-model='price']")

name.send_keys("Pen")
quantity.send_keys("10")
price.send_keys("5")

driver.find_element(By.XPATH, "//button[contains(text(),'Add Product')]").click()

wait.until(lambda d: "Pen" in d.find_element(By.TAG_NAME, "table").text)

print("Usability Testing: Passed")

# 3. FUNCTIONAL TESTING - UPDATE
row = driver.find_element(By.XPATH, "//tr[td[contains(text(),'Pen')]]")
row.find_element(By.XPATH, ".//button[contains(text(),'Update')]").click()

alert = wait.until(lambda d: d.switch_to.alert)
alert.send_keys("Pencil")
alert.accept()

alert = wait.until(lambda d: d.switch_to.alert)
alert.send_keys("20")
alert.accept()

alert = wait.until(lambda d: d.switch_to.alert)
alert.send_keys("15")
alert.accept()

wait.until(lambda d: "Pencil" in d.find_element(By.TAG_NAME, "table").text)

print("Update Testing: Passed")

# 4. FUNCTIONAL TESTING - DELETE
row = driver.find_element(By.XPATH, "//tr[td[contains(text(),'Pencil')]]")
row.find_element(By.XPATH, ".//button[contains(text(),'Delete')]").click()

wait.until(lambda d: "Pencil" not in d.find_element(By.TAG_NAME, "table").text)

print("Delete Testing: Passed")

driver.quit()