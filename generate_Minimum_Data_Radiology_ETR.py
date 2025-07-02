import pytest # Imports pytest framework to enable writing and running automated tests
from time import sleep # Imports the sleep() function directly from the time module
from selenium.webdriver.common.by import By # Imports By class frm Selenium framework to locate elements on a webpage
from selenium.webdriver.common.keys import Keys #Imports key class to simulate keyboard presses like enter, tab for input automation
from reusable_Functions import login_wcp, search_patient, navigate_and_open_radiology_etr, sign_off_form, logout_wcp, \
    continue_session_bypass
from test_data import (TEST_USERNAME,
                       TEST_PASSWORD,
                       TEST_NHS_NUMBER,
                       TEST_EXAM,
                       SRC_NAME,
                       PATIENT_LOCATION, SPECIALITY, TEST_CLINICAL_QUESTION_MINIMUM)

class TestETR:

    @pytest.mark.etr
    # Create parametrization decorator
    @pytest.mark.parametrize("username, password, tpnhs", [(TEST_USERNAME, TEST_PASSWORD, TEST_NHS_NUMBER)])

    def test_generate_min_rad_etr (self, driver, username, password, tpnhs):

        # Login Functionality
        # username and password defined in @pytest.mark.parametrize
        login_wcp(self, driver, username, password)

        # Search Patient Functionality
        # tpnhs will search for test patient nhs number defined in @pytest.mark.parametrize
        search_patient(self, driver, tpnhs)

        # Navigate to and open Radiology ETR
        navigate_and_open_radiology_etr(self, driver)

        #
        # Complete Minimum Data Input Form Functionality (Switch Automation into Iframe of form)
        #

        # Switch to Iframe drive
        driver.switch_to.frame(driver.find_element(By.ID, "createEdit"))

        # Check for multiple sessions pop up/Bypass
        continue_session_bypass(driver)

        # Select Urgency - Routine
        select_urgency = driver.find_element(By.ID, "Urgency_04")
        select_urgency.click()

        # Select Patient Category - Fee paying NHS
        select_pat_cat = driver.find_element(By.ID, "AdministrativeCategory_II")
        select_pat_cat.click()

        # Select if patient has capacity to consent - Yes
        select_consent_capacity = driver.find_element(By.ID, "PatientRadiologyCapacityToConsent_Y")
        select_consent_capacity.click()

        # Send Request to Organisation - HDD RISP
        # Select Textbox
        send_org = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div/div/div[5]/div[1]/div/div/div[2]/div/div[1]/button")
        send_org.click()
        # Select HDD RISP
        hdd_risp = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div/div/div[5]/div[1]/div/div/div[2]/div/div[1]/div/ul/li[6]/a/span[1]")
        hdd_risp.click()

        # Select Patient Location - GGH Radiography Ward
        # Select Textbox
        pat_location = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[1]/button")
        pat_location.click()
        location_textbox = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[1]/div/div/input")
        location_textbox.click()
        # Location Name - Type GGH Radiography and hit enter
        location_textbox.send_keys(PATIENT_LOCATION)
        location_textbox.send_keys(Keys.ENTER)

        # Select Presentation - Walk around
        sel_pres = driver.find_element(By.ID, "PresentationToRadiologyDepartment_01")
        sel_pres.click()

        # Select Transport - Walking
        sel_transport = driver.find_element(By.ID, "Transport_01")
        sel_transport.click()

        # Select Speciality
        sel_speciality = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div/div/div[7]/div[1]/div/div/div[2]/div/div[1]/button/span[1]")
        sel_speciality.click()
        sel_textbox = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div/div/div[7]/div[1]/div/div/div[2]/div/div[1]/div/div/input")
        sel_textbox.click()
        # Speciality name - Type Radiology and hit enter
        sel_textbox.send_keys(SPECIALITY)
        sel_textbox.send_keys(Keys.ENTER)

        # Select Senior Responsible Clinician for this request
        sel_senior_rad = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div/div/div[7]/div[2]/div/div/div[2]/div/div[1]/button")
        sel_senior_rad.click()
        # Select Textbox
        choose_src = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div/div/div[7]/div[2]/div/div/div[2]/div/div[1]/div/div/input")
        choose_src.click()
        # Enter SRC Name - Type Sandford and hit enter
        choose_src.send_keys(SRC_NAME)
        choose_src.send_keys(Keys.ENTER)

        # Add Test Set - XR Skull
        # Select Textbox
        add_test_field = driver.find_element(By.ID, "examination-search")
        add_test_field.click()
        # Enter XR Skull - Arrow Down Key and hit Enter to select
        add_test_field.send_keys(TEST_EXAM)
        sleep(2)
        add_test_field.send_keys(Keys.ARROW_DOWN)
        add_test_field.send_keys(Keys.ENTER)

        # Add text into Clinical question to be answered by this request and relevant clinical details textbox
        clin_question = driver.find_element(By.ID, "ReasonForRequest")
        clin_question.send_keys(TEST_CLINICAL_QUESTION_MINIMUM)

        # Add Preferred Language - English
        pref_language = driver.find_element(By.ID, "PreferredLanguage")
        pref_language.click()
        select_english = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[3]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div[2]/div/select/option[2]")
        select_english.click()

        #Sign Off Form
        sign_off_form(self, driver,password)

        #Log Out Functionality
        logout_wcp(self,driver)