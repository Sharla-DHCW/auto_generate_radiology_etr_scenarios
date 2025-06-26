from test_data import (TEST_USERNAME,
                       TEST_PASSWORD,
                       TEST_NHS_NUMBER,
                       TEST_EXAM,
                       TEST_CLINICAL_QUESTION_STANDARD,
                       SRC_NAME,
                       PATIENT_LOCATION, SPECIALITY)
import pytest # Imports pytest framework to enable writing and running automated tests
from time import sleep # Imports the sleep() function directly from the time module
from selenium.webdriver.common.by import By # Imports By class frm Selenium framework to locate elements on a webpage
from selenium.webdriver.common.keys import Keys #Imports key class to simulate keyboard presses like enter, tab for input automation
from reusable_Functions import login_wcp, logout_wcp, sign_off_form, search_patient, continue_session_bypass, \
    navigate_and_open_radiology_etr

class TestGenerateETR:

    # Create pytest marker called ETR (Can selectively run or group tests per marker)
    @pytest.mark.etr
    # Create parametrization decorator
    @pytest.mark.parametrize("username, password, tpnhs", [(TEST_USERNAME, TEST_PASSWORD, TEST_NHS_NUMBER)])

    def test_generate_rad_etr(self,driver,username,password,tpnhs):

        #Login Functionality
        #username and password defined in test_data.py
        login_wcp(self,driver,username,password)

        # Search Patient Functionality
        # tpnhs will search for test patient nhs number defined in test_data.py
        search_patient(self, driver, tpnhs)

        # Navigate to and open Radiology ETR
        navigate_and_open_radiology_etr(self, driver)

        #
        # Complete Maximum Data Form Functionality (Step into Iframe of form)
        #

        # Switch to Iframe drive
        driver.switch_to.frame(driver.find_element(By.ID, "createEdit"))

        # Check for multiple sessions pop up/Bypass
        continue_session_bypass(driver)

        

