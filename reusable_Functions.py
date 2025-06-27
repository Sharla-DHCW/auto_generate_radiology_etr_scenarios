import time
from time import sleep
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By # Imports By class frm Selenium framework to locate elements on a webpage
from selenium.webdriver.support.wait import WebDriverWait # Imports WebDriverWait from selenium to allow you to wait for certain conditions/elements before proceeding
from selenium.webdriver.support import expected_conditions as ec # Imports the expected conditions module and renames it to ec to contain predefined conditions to use with WebDriverWait
from test_data import (SIGNOFF_NAME, SIGNOFF_ROLE, SIGNOFF_GMC, SIGNOFF_CONTACT_INFO)

#Function to log into WCP on PIT4
def login_wcp (self, driver,username,password):
    # Navigate to WCP PIT 4
    driver.get("https://pit4wcp.cymru.nhs.uk/Login.aspx")

    # Enter Username
    username_locator = driver.find_element(By.ID, "usernameLoginTextBox")
    username_locator.send_keys(username)

    # Enter Password
    password_locator = driver.find_element(By.ID, "passwordLoginTextBox")
    password_locator.send_keys(password)

    # Select environment dropdown
    envdropdown_locator = driver.find_element(By.XPATH, "/html/body/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr/td/div[3]/div[2]/form/fieldset/div[3]/button")
    envdropdown_locator.click()

    # Wait for options to drop down
    wait = WebDriverWait(driver, 5)
    wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/ul[1]/li[4]/a")))

    # Select HDD Main Test environment
    hdd_locator = driver.find_element(By.XPATH, "/html/body/ul[1]/li[4]/a")
    hdd_locator.click()

    # Select Login Button
    login_locator = driver.find_element(By.ID, "loginBtn")
    login_locator.click()

    # Wait for page to load
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.ID, "MyPatientsSearch")))

#Function to search for patient (nhs number to be defined in tpnhs)
def search_patient(self,driver,tpnhs):
    # Select Patient Search Button
    driver.find_element(By.ID, "MyPatientsSearch").click()

    # Wait for dropdown options
    wait = WebDriverWait(driver, 5)
    wait.until(ec.presence_of_element_located((By.ID, "Search")))

    # Select Search
    search_locator = driver.find_element(By.ID, "Search")
    search_locator.click()
    time.sleep(1)

    # Enter Test Patient NHS into PatientID search box
    patientid_locator = driver.find_element(By.ID, "searchByIdTextBox")
    patientid_locator.send_keys(tpnhs)

    # Select Search Button
    searchpat_locator = driver.find_element(By.ID, "searchButton")
    searchpat_locator.click()

#Function to search for female patient (nhs number to be defined in ftpnhs)
def search_female_patient(self,driver,ftpnhs):
    # Select Patient Search Button
    driver.find_element(By.ID, "MyPatientsSearch").click()

    # Wait for dropdown options
    wait = WebDriverWait(driver, 5)
    wait.until(ec.presence_of_element_located((By.ID, "Search")))

    # Select Search
    search_locator = driver.find_element(By.ID, "Search")
    search_locator.click()
    time.sleep(1)

    # Enter Test Patient NHS into PatientID search box
    patientid_locator = driver.find_element(By.ID, "searchByIdTextBox")
    patientid_locator.send_keys(ftpnhs)

    # Select Search Button
    searchpat_locator = driver.find_element(By.ID, "searchButton")
    searchpat_locator.click()

#Function to Navigate to the Radiology ETR form from the patient search
def navigate_and_open_radiology_etr(self, driver):
    # Wait for quick actions button to load
    wait = WebDriverWait(driver, 30)
    wait.until(ec.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr/td/div[3]/div[1]/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/img")))
    sleep(2)

    # Quick actions button
    quickactions_button_locator = driver.find_element(By.XPATH, "/html/body/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr/td/div[3]/div[1]/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/img")
    quickactions_button_locator.click()

    # Wait for dropdown to load
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.ID, "ui-id-7")))

    # Open patient test results
    results_page_locator = driver.find_element(By.ID, "ui-id-7")
    results_page_locator.click()

    # Check for multiple sessions pop up/Bypass
    continue_session_bypass(driver)

    # Wait for page to load
    wait = WebDriverWait(driver, 30)
    wait.until(ec.presence_of_element_located((By.ID, "newDocumentMenuContainer")))
    sleep(5)

    # Check for multiple sessions pop up/Bypass
    continue_session_bypass(driver)

    # Select Forms button
    forms_locator = driver.find_element(By.ID, "newDocumentMenuContainer")
    forms_locator.click()

    # Select Radiology Request
    radiology_form_locator = driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/table/tbody/tr/td/div[2]/div[2]/div/div[1]/div/ul/li[2]/div")
    radiology_form_locator.click()
    sleep(5)

    # Check for multiple sessions pop up/Bypass
    continue_session_bypass(driver)

    # Wait for Radiology Form to Load
    wait = WebDriverWait(driver, 60)
    wait.until(ec.presence_of_element_located((By.ID, "createEdit")))

    # Check for multiple sessions pop up/Bypass
    continue_session_bypass(driver)

#Function to check and bypass a multiple session pop up
def continue_session_bypass(driver):
    try:
        # Find pop up by css selector
        span = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/button[1]")
        # Press enter
        span.send_keys(Keys.ENTER)
    except (NoSuchElementException, ElementClickInterceptedException):
        time.sleep(1)

#Function to sign off the ETR and submit the form
def sign_off_form (self, driver, password):
     # Enter Sign off Name
     name_signoff = driver.find_element(By.ID, "RadiologySignOff_RequestorName")
     name_signoff.clear()
     name_signoff.send_keys(SIGNOFF_NAME)

     # Enter Role
     role_signoff = driver.find_element(By.ID, "RadiologySignOff_RequestorRole")
     role_signoff.clear()
     role_signoff.send_keys(SIGNOFF_ROLE)

     # Enter Professional Registration
     pro_reg_signoff = driver.find_element(By.ID, "RadiologySignOff_RequestorGmc")
     pro_reg_signoff.clear()
     pro_reg_signoff.send_keys(SIGNOFF_GMC)

     # Enter Contact Information
     contact_info = driver.find_element(By.ID, "RadiologySignOff_RequestorContactInformation")
     contact_info.clear()
     contact_info.send_keys(SIGNOFF_CONTACT_INFO)

     # Enter Password
     password_signoff = driver.find_element(By.ID, "password")
     password_signoff.send_keys(password)

     # Select Place Request
     place_request = driver.find_element(By.ID, "submitBtn")
     place_request.click()

     # Wait for form submission
     wait = WebDriverWait(driver, 5)
     wait.until(ec.presence_of_element_located((By.ID, "writebackSuccess")))
     select_ok = driver.find_element(By.XPATH, "/html/body/div/div/input")
     select_ok.click()

#Function to exit the form and log out of WCP PIT4
def logout_wcp (self, driver):
    # Step out of Iframe
    driver.switch_to.default_content()
    sleep(2)

    # Select logout
    log_out = driver.find_element(By.ID, "btnLogout")
    log_out.click()
    sleep(3)