from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

expectedPageTitle = "CURA Healthcare Service"

current_title = driver.title

# Page Title verification
if current_title == expectedPageTitle:
    print("Current Title is Correct: ", driver.title)
else:
    print("Current Title is different than Expected Title. Current Title is: ", driver.title)

wait.until(EC.visibility_of_element_located((By.ID, "login")))
# finds username text field
driver.find_element(By.ID, "txt-username").send_keys("John Doe")
driver.find_element(By.XPATH, "//input[@id='txt-password']").send_keys("ThisIsNotAPassword")
driver.find_element(By.ID, "btn-login").submit()

#URL verification
expectedURL = "https://katalon-demo-cura.herokuapp.com/#appointment"
if driver.current_url == expectedURL:
    print("Test Passed")
else:
    print("Test failed!", driver.current_url )

makeAppointment = driver.find_element(By.ID, "appointment")
if makeAppointment:
    print("User is logged in")
else:
    print("user is not logged in")

driver.quit()




