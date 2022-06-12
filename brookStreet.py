from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time



# Path for executable stored in driver object
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


# Goes to desired website. For this one, the job and location have already been selected before this screen. Saves time
driver.get("https://www.brookstreet.co.uk/jobs/greater-london/")

# To maxmimize the window and make finding elements easier
driver.maximize_window()


# Personal details
first_name = ''
last_name = ''
email = ''
phone_number = ''
# File path for CV. Raw string to ignore escape characters
file = r''



def applyBot():
    jobs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href,"/apply/") and text()="Apply Now"]'))
    )
    counter = 0
    while (counter < len(jobs)):
        # Get the refreshed elements after each loop to avoid stale exception
        try:
            jobs = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href,"/apply/") and text()="Apply Now"]'))
            )
        except:
            print('ERROR LOCATING JOBS')
        # Scroll to element at current index and click using JavaScript executor, since it's hidden by menu bar
        driver.execute_script("arguments[0].scrollIntoView();", jobs[counter])
        driver.execute_script("arguments[0].click();", jobs[counter])
        # Fill in the form with the following details
        try:
            first_name_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="user_user_profile_attributes_first_name"]'))
            )
            first_name_field.send_keys(first_name)
        except:
            print('ERROR IN FIRST NAME')
        try:
            last_name_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="user_user_profile_attributes_last_name"]'))
            )
            last_name_field.send_keys(last_name)
        except:
            print('ERROR IN LAST NAME')
        try:
            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'user_email'))
            )
            email_field.send_keys(email)
        except:
            print('ERROR IN EMAIL')
        try:
            phone_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="user_registration_answers_attributes_9057_answer"]'))
            )
            phone_field.send_keys(phone_number)
        except:
            print('ERROR IN PHONE NUMBER')
        try:
            dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="user_registration_answers_attributes_11197_answer"]'))
            )
            Select(dropdown).select_by_visible_text('London Holborn') # Hard coded closest branch; it won't change
        except:
            print('ERROR IN DROPDOWN')
        try:
            upload_cv = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="user_candidate_uploads_attributes__upload"]'))
            )
            upload_cv.send_keys(file)
        except:
            print('ERROR IN CV UPLOAD')            
        try:
            gdpr = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="consents_35"]'))
            )
            gdpr.click()
        except:
            print('ERROR IN GDPR CHECKBOX')
        # Submit CV
        try:
            apply_for_this_job = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="form-holder"]/div/div/div[1]/form/div[4]/input'))
            )
            apply_for_this_job.click()
        except:
            print('ERROR IN APPLY BUTTON')
        #time.sleep(5)
        try:
            weird_page = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//a[@id="return-btn"]'))
            )
        except:
            pass
        #time.sleep(5)
        print(f'{counter + 1} job done') if counter == 0 else print(f'{counter + 1} jobs done')
        # Increment counter to go to the next job
        counter += 1
        driver.back()
        driver.back()



page_count = 1


# Keeps the process going until it can't find any more pages
while True:
    applyBot()
    print(f'Page {page_count} is complete')
    page_count += 1
    try:
        next_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Next ›'))
        )
        next_page.click()
    except:
        print('END OF FINAL PAGE')
        break