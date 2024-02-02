from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Ww
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Python Selenium\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://demo.automationtesting.in/Register.html')
driver.maximize_window()

# User Registration
# All text fields
fname = driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys('Dana')
lName = driver.find_element(By.XPATH, "//input[@ng-model='LastName'] ").send_keys('Test')

add = driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']").send_keys('123 Street Bangalore KA')
eMail = driver.find_element(By.XPATH, "//input[@type='email']").send_keys('test@test.com')

phone = driver.find_element(By.XPATH, "//input[@ng-model='Phone']").send_keys('9886320044')

# try some checkboxes  - Gender Selection

maleSelect = driver.find_element(By.XPATH, "//input[@type='radio' and @value='Male']").click()

# Hobbies selection

driver.find_element(By.XPATH, "//input[@value='Hockey']").click()

# listCountry = driver.find_element(By.XPATH, "//div[@class='col-md-4 col-xs-4 col-sm-4']/multi-select[1]/div[2]/ul/li[2]/a").click()

skillsSelect = Select(driver.find_element(By.XPATH, "//select[@id='Skills']"))

skillsList = skillsSelect.options

for a in skillsList:
    print(a.text)

select = skillsSelect.select_by_index(2)

# scroll page

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# Select country & print all countires name

countrySelect = Select(driver.find_element(By.XPATH, "//select[@id='countries']"))

countryList = countrySelect.options

for x in countryList:
    print(x.text)

cntrySel = countrySelect.select_by_index(1)

# Select COuntry

DropdownCountry = driver.find_element(By.XPATH, "//span[@role='combobox']").click()

# searchCntry = driver.find_element(By.XPATH, "//body/span[1]/span[1]/span[1]/input[@type='search']").send_keys('India')

selectIndia = driver.find_element(By.XPATH, "//body/span[1]/span[1]/span[2]/ul/li[contains(text(), 'India')]").click()

# Ww(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "://body/span[1]/span[1]/span[2]/ul/li[contains(text(), 'India')]" ))).click()


# Date of Birth

yearSelect = Select(driver.find_element(By.XPATH, "//select[@id='yearbox']"))

# ListYear  = yearSelect.options

clickYear = yearSelect.select_by_value('1988')


monSelect = Select(driver.find_element(By.XPATH, "//select[@ng-model='monthbox']"))

clickMonth = monSelect.select_by_value('June')


daySelect = Select(driver.find_element(By.XPATH, "//select[@id='daybox']"))

clickDay = daySelect.select_by_value('8')


# Password enter

driver.find_element(By.XPATH, "//input[@id='firstpassword']").send_keys('Test123')

driver.find_element(By.ID, "secondpassword").send_keys('Test123')

driver.find_element(By.ID, "submitbtn").click()



print(driver.title)
time.sleep(3)
driver.quit