from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Path for executable stored in driver object
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Goes to desired website
driver.get("https://www.office-angels.com/")

# To maxmimize the window and make finding elements easier
driver.maximize_window()

# Your details
desired_job = ''
desired_location = ''
first_name = ''
last_name = ''
phone_number = ''
email = ''
file = r''


# Waits for page to load and accepts cookie if it appears
try:
    cookie = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'onetrust-reject-all-handler'))
    )
    cookie.click()
except:
    print('COOKIE IS IN THE WAY')
else:
    print('COOKIE HAS BEEN DEALT WITH')

# Inputs job title
job_field = driver.find_element(By.NAME, 'txtkeyword')
job_field.send_keys(desired_job)

# Inputs location
location_field = driver.find_element(By.XPATH, '//*[starts-with(@id,"txtlocation")]')
location_field.send_keys(desired_location)

# Click 'find jobs' button
find_jobs = driver.find_element(By.XPATH, '//*[@id="header_0_headercontent_5_ctl13_hlksearchJobs"]')
find_jobs.click()

# Button is unresponsive sometimes, so a few more clicks just in case
try:
    find_jobs.click()
    find_jobs.click()
except:
    pass


# To find the radius slider
slider = driver.find_element(By.XPATH, '//*[@id="radiusSlider"]/div[2]/div/div/div')

# Moves the slider horizontally to the left, hence the minus sign. Keeps results within 10 miles
action = ActionChains(driver)
action.drag_and_drop_by_offset(slider, -385, 263)
action.perform()

#VERY IMPORTANT. OTHERWISE THERE WILL BE A STALE EXCEPTION THROWN
time.sleep(0.8)



#                                                   FUNC DEFINTIONS


def applyBot():
    jobs = driver.find_elements(By.XPATH, '//*[contains(@data-bind,"text: JobTitle")]')
    counter = 0
    while (counter < len(jobs)):
        # Get the refreshed elements after each loop to avoid stale exception
        jobs = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//*[contains(@data-bind,"text: JobTitle")]'))
            )
        # Scroll to element at current index
        driver.execute_script("arguments[0].scrollIntoView();", jobs[counter])
        time.sleep(0.4)
        jobs[counter].click()
        # Click on 'Apply now' button
        apply_button = driver.find_element(By.XPATH, '//*[@id="mainContent"]/article/div[2]/div[1]/div/div/div/a')
        apply_button.click()
        # Input first name
        first_name_field = driver.find_element(By.ID, 'firstNameOA')
        first_name_field.send_keys(first_name)
        # Input last name
        last_name_field = driver.find_element(By.ID, 'lastNameOA')
        last_name_field.send_keys(last_name)
        # Input phone number
        phone_number_field = driver.find_element(By.ID, 'phoneOA')
        phone_number_field.send_keys(phone_number)
        # Input e-mail
        email_field = driver.find_element(By.ID, 'emailOA')
        email_field.send_keys(email)
        # Scroll down to 'browse' button and send file path to upload CV
        browse = driver.find_element(By.ID, 'fileUploadOA')
        driver.execute_script("arguments[0].scrollIntoView();", browse)
        time.sleep(0.4)
        browse.send_keys(file)
        # Submit CV
        submit = driver.find_element(By.XPATH, '//*[@id="my_nav"]/div[2]/div[2]/div/div[2]/div[6]/a')
        submit.click()
        thanks_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//strong[text()="Thank you "]')))
        # Go back and repeat for the next job
        print(f'{counter} job down')
        counter += 1
        driver.back()
        driver.back()
        driver.back()
        time.sleep(0.7)






# Keeps the script running until it completes the final page, and breaks
page_count = 1

while True:
    applyBot()
    print(f'Page {page_count} is done')
    page_count += 1
    try:
        next_page = driver.find_element(By.LINK_TEXT, 'Next')
        time.sleep(1)
        next_page.click()
    except:
        print('end of final page')
    time.sleep(1.5)