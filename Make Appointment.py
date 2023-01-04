
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@ class='text-vertical-center']"))).click()
driver.find_element(By.ID, "btn-make-appointment").click()
driver.implicitly_wait(5)

logIn_URL: str = "https://katalon-demo-cura.herokuapp.com/profile.php#login"

# URL verification
assert driver.current_url == logIn_URL
current_url = driver.current_url
if current_url == logIn_URL:
    print("Current URL is OK: ", driver.current_url)
else:
    print("Current URL is different than Expected URL", driver.current_url)

pageTitle = "CURA Healthcare Service"

current_title = driver.title

# Page Title verification
if current_title == pageTitle:
    print("Current Title is Correct: ", driver.title)
else:
    print("Current Title is different than Expected Title. Current Title is: ", driver.title)

wait.until(EC.visibility_of_element_located((By.ID, "login")))
# finds username text field
driver.find_element(By.ID, "txt-username").send_keys("John Doe")
driver.find_element(By.XPATH, "//input[@id='txt-password']").send_keys("ThisIsNotAPassword")
driver.find_element(By.ID, "btn-login").submit()

driver.implicitly_wait(5)
# Appointment URL verification
appt_URL = "https://katalon-demo-cura.herokuapp.com/#appointment"
assert driver.current_url == appt_URL
current_url = driver.current_url
if current_url == appt_URL:
    print("The URL is correct!", current_url)
else:
    print("Wrong URL!")

# Page Title verification
expectedPageTitle = "CURA Healthcare Service"
current_title = driver.title

if current_title == expectedPageTitle:
    print("Current Title is Correct: ", driver.title)
else:
    print("Current Title is different than Expected Title. Current Title is: ", driver.title)


elements = driver.find_elements(By.CSS_SELECTOR, "h2")

driver.find_element(By.ID, "btn-make-appointment").click()
driver.find_element(By.ID, "combo_facility").click()
dropdown = driver.find_element(By.ID, "combo_facility")
dropdown.find_element(By.XPATH, "//option[. = 'Seoul CURA Healthcare Center']").click()
driver.find_element(By.ID, "chk_hospotal_readmission").click()
driver.find_element(By.ID, "radio_program_medicaid").click()
driver.find_element(By.CSS_SELECTOR, ".glyphicon").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > .day:nth-child(2)").click()
driver.find_element(By.ID, "btn-book-appointment").click()
driver.find_element(By.CSS_SELECTOR, ".fa-bars").click()
driver.find_element(By.LINK_TEXT, "History").click()
elements = driver.find_elements(By.CSS_SELECTOR, "h2")
assert len(elements) > 0
elements = driver.find_elements(By.CSS_SELECTOR, ".row:nth-child(2)")
assert len(elements) > 0

#Appointment Confirmation verification

assert driver.find_element(By.CSS_SELECTOR, ".col-sm-offset-2:nth-child(1) .panel-heading").text == "23/01/2023"
elements = driver.find_elements(By.ID, "facility")
assert len(elements) > 0
elements = driver.find_elements(By.CSS_SELECTOR, ".col-sm-offset-2:nth-child(1) .col-sm-2:nth-child(4) > label")
assert len(elements) > 0
elements = driver.find_elements(By.CSS_SELECTOR, ".col-sm-offset-2:nth-child(1) .col-sm-2:nth-child(7) > label")
assert len(elements) > 0

