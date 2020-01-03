from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Obtain and assign the web driver from the location of the file (chromedriver.exe)
driver = webdriver.Chrome("C:\\Users\\jbuen\\OneDrive\\Documents\\misc_git_repository\\misc\\chromedriver_win32\\chromedriver.exe")

# Get the Base Website: allegiantair.com
driver.get("https://www.allegiantair.com/")

# Wait until page boots up
wait = WebDriverWait(driver, 10) # Set Max Timeout Time for 10 Seconds
wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='ui-button-icon-primary ui-icon ui-icon-closethick']")))


# Click X on the Pop-Up
driver.find_element(By.XPATH,"//span[@class='ui-button-icon-primary ui-icon ui-icon-closethick']").click()


wait.until(EC.presence_of_element_located((By.NAME, "search_form[departure_city]")))


#   BOOK A TRIP PAGE
# City variables (to and from)
city_origin = "Las Vegas"
city_destination = "El Paso"

# Type in Origin City
driver.find_element_by_name("search_form[departure_city]").send_keys(city_origin)
time.sleep(2) # take some time to locate city before pressing Enter key
driver.find_element_by_name("search_form[departure_city]").send_keys(Keys.RETURN) # Press Enter Key

# Type in Destination City
driver.find_element_by_name("search_form[destination_city]").send_keys(city_destination)
time.sleep(2)   # take some time to locate city before pressing Enter key
driver.find_element_by_name("search_form[destination_city]").send_keys(Keys.RETURN) # Press Enter Key

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='allegiant_searchform']/div[2]/div[1]/div/div/div/button")))

# Select Departure Date
driver.find_element_by_name("search_form[departure_date]").click()
time.sleep(1)
# Traverse through 5 months until June
for x in range(5):
    driver.find_element_by_xpath("//span[@class='ui-icon ui-icon-circle-triangle-e']")
    time.sleep(1)
    driver.find_element_by_xpath("//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

time.sleep(1)

# Select June 25 for Departure Date
driver.find_element_by_id("ui-datepicker-0-5-25").click()
time.sleep(1)

# Select Return Date
driver.find_element_by_name("search_form[return_date]").click()
time.sleep(1)
# Select June 28 for Return Date
driver.find_element_by_id("ui-datepicker-0-5-28").click()
time.sleep(1)

# Click the Search Button to Advance
driver.find_element_by_id("submit-search").click()

time.sleep(2)



#   FLIGHTS PAGE
# Some variables for flight prices
dollar_sign = "$"
departing_price = 73.00
returning_price = 73.00

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='flights']/div[6]/div[3]/button")))
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='flights']/div[6]/div[3]/button").click()



#   BUNDLES PAGE
# Selected Allegiant Basic Bundle
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='package']/div[1]/div/button")))
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='package']/div[1]/div/button").click()



#   GETTING AROUND PAGE
# Selected the Fullsize 2/4 Door Vehicle fo r Rental
car_rental_price = 224.00    # Price of car rental chosen

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='vendors']/div[2]/table/tbody/tr[5]/td[2]/span/a")))
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='vendors']/div[2]/table/tbody/tr[5]/td[2]/span/a").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='pricing']/div/table/tbody[4]/tr/td")))
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='transport']/div[3]/div[3]/div/button")))
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='transport']/div[3]/div[3]/div/button").click()



#   TRAVELERS PAGE
# Add up all prices from flights + bundle + car rental
# Recall, the bundle chosen was the 'Allegiant Basic Bundle' which costs $0.00, no need to
# include in the equation..
expected_total_price = departing_price + returning_price + car_rental_price

# Convert total price to string
str_exp_total_price = str(expected_total_price)
str_exp_total_price = dollar_sign + str_exp_total_price + "0"  # Yields "$377.00"


wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='pricing']/div/table/tbody[4]/tr/td")))
actual_total = driver.find_element(By.XPATH, "//*[@id='pricing']/div/table/tbody[4]/tr/td")

# Verify and assert the expected total price to the actual total price shown on the page.
# If totals do not match -> AssertionError with the following msg
assert actual_total.text == str_exp_total_price, "Total prices DO NOT match."

# If totals do match -> display following msg on the console
if actual_total.text == str_exp_total_price:
    print("Total prices match.")

time.sleep(3)


# Stop the automation and close the window.
driver.quit()


