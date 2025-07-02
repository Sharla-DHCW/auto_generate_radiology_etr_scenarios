from test_data import (TEST_USERNAME,
                       TEST_PASSWORD,
                       TEST_EXAM,
                       SRC_NAME,
                       PATIENT_LOCATION, SPECIALITY, TEST_CLINICAL_QUESTION_MAXIMUM, TEST_FEMALE_NHS_NUMBER,
                       REASON_FOR_RBD, INFECTION_CONTROL_ISSUES, OTHER_REL_DETAILS, RECENT_REL_RESULTS_NOT_LISTED)
import pytest # Imports pytest framework to enable writing and running automated tests
from time import sleep # Imports the sleep() function directly from the time module
from selenium.webdriver.common.by import By # Imports By class frm Selenium framework to locate elements on a webpage
from selenium.webdriver.common.keys import Keys #Imports key class to simulate keyboard presses like enter, tab for input automation
from reusable_Functions import login_wcp, logout_wcp, sign_off_form, continue_session_bypass, navigate_and_open_radiology_etr, search_female_patient
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestETR:

    # Create pytest marker called ETR (Can selectively run or group tests per marker)
    @pytest.mark.etr
    # Create parametrization decorator
    @pytest.mark.parametrize("username, password, ftpnhs", [(TEST_USERNAME, TEST_PASSWORD, TEST_FEMALE_NHS_NUMBER)])

    def test_generate_max_rad_etr(self,driver,username,password,ftpnhs):

        #Login Functionality
        #username and password defined in test_data.py
        login_wcp(self,driver,username,password)

        # Search Patient Functionality
        # tpnhs will search for test patient nhs number defined in test_data.py
        search_female_patient(self, driver, ftpnhs)

        # Navigate to and open Radiology ETR
        navigate_and_open_radiology_etr(self, driver)

        #
        # Input Maximum Data Form Functionality
        #

        # Switch to Iframe drive
        driver.switch_to.frame(driver.find_element(By.ID, "createEdit"))

        # Check for multiple sessions pop up/Bypass
        continue_session_bypass(driver)

        # REQUEST DETAILS
        # Select Urgency - Routine
        select_urgency = driver.find_element(By.ID, "Urgency_04")
        select_urgency.click()

        # Select Patient Category - Fee paying NHS
        select_pat_cat = driver.find_element(By.ID, "AdministrativeCategory_II")
        select_pat_cat.click()

        # Select if patient has capacity to consent - Yes
        select_consent_capacity = driver.find_element(By.ID, "PatientRadiologyCapacityToConsent_Y")
        select_consent_capacity.click()

        #Defer tests until tomorrow
        defer_test_until = driver.find_element(By.ID,"defer-until-tomorrow")
        defer_test_until.click()

        #Report Required By
        report_require_by = driver.find_element(By.ID, "DateReportRequiredBy")
        report_require_by.click()
        next_button = driver.find_element(By.XPATH,"/html/body/div[5]/div/a[2]/span")
        next_button.click()
        select_date = driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[3]/td[2]/a")
        select_date.click()

        #Reason for required by date
        reason_required_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "DateReportRequiredByReason"))
        )
        reason_required_text.send_keys(REASON_FOR_RBD)

        # Select Notification type - Inpatient
        select_noti_type = driver.find_element(By.ID, "PatientClass_I")
        select_noti_type.click()

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

        # Select Walk Around Presentation
        sel_pres = driver.find_element(By.ID, "PresentationToRadiologyDepartment_01")
        sel_pres.click()

        # Select Walking Transport
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
        choose_src = driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div/div/div[7]/div[2]/div/div/div[2]/div/div[1]/div/div/input")
        choose_src.click()
        # Enter SRC Name - Type Sandford and hit enter
        choose_src.send_keys(SRC_NAME)
        choose_src.send_keys(Keys.ENTER)

        # Add Test Set - XR Skull
        # Select Textbox
        add_test_field = driver.find_element(By.ID, "examination-search")
        add_test_field.click()
        # Enter XR Skull - Arrow Down Key and hit enter to select
        add_test_field.send_keys(TEST_EXAM)
        sleep(2)
        add_test_field.send_keys(Keys.ARROW_DOWN)
        add_test_field.send_keys(Keys.ENTER)

        # Enter Clinical Question to be answered
        clin_question = driver.find_element(By.ID, "ReasonForRequest")
        clin_question.send_keys(TEST_CLINICAL_QUESTION_MAXIMUM)

        # OTHER PATIENT INFORMATION
        # Special Requirements (tick all boxes)
        special_requirements_confusion = driver.find_element(By.ID,"SensoryDisabilityNeeds_01")
        special_requirements_confusion.click()
        special_requirements_interp = driver.find_element(By.ID, "SensoryDisabilityNeeds_02")
        special_requirements_interp.click()
        special_requirements_hearing = driver.find_element(By.ID, "SensoryDisabilityNeeds_03")
        special_requirements_hearing.click()
        special_requirements_language = driver.find_element(By.ID, "SensoryDisabilityNeeds_04")
        special_requirements_language.click()
        special_requirements_learning = driver.find_element(By.ID, "SensoryDisabilityNeeds_05")
        special_requirements_learning.click()
        special_requirements_visual = driver.find_element(By.ID, "SensoryDisabilityNeeds_06")
        special_requirements_visual.click()

        # Additional Information (tick all boxes)
        additional_info_drip_stand = driver.find_element(By.ID,"RadiologyLogisticsIssues_02")
        additional_info_drip_stand.click()
        additional_info_oxygen = driver.find_element(By.ID,"RadiologyLogisticsIssues_03")
        additional_info_oxygen.click()
        additional_info_hoist = driver.find_element(By.ID,"RadiologyLogisticsIssues_04")
        additional_info_hoist.click()
        additional_info_barrier = driver.find_element(By.ID,"RadiologyLogisticsIssues_06")
        additional_info_barrier.click()
        additional_info_anticoagulants = driver.find_element(By.ID,"RadiologyLogisticsIssues_07")
        additional_info_anticoagulants.click()

        # Enter Preferred Language
        pref_language = driver.find_element(By.ID, "PreferredLanguage")
        pref_language.click()
        select_english = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[3]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div[2]/div/select/option[2]")
        select_english.click()

        # Clinical Trial
        clinical_trial = driver.find_element(By.XPATH,"/html/body/div[1]/form/div[3]/div/div/div/div[1]/div[3]/div[1]/div[2]/div/div/div[2]/div/div[1]/button")
        clinical_trial.click()
        select_trial = driver.find_element(By.XPATH,"/html/body/div[1]/form/div[3]/div/div/div/div[1]/div[3]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/ul/li[2]/a/span[1]")
        select_trial.click()

        # Any Infection Control Issues
        infection_control_issues = driver.find_element(By.ID,"InfectionControlIssues")
        infection_control_issues.send_keys(INFECTION_CONTROL_ISSUES)

        # Other Relevant Details
        other_rel_non_details = driver.find_element(By.ID,"OtherRelevantDetails")
        other_rel_non_details.send_keys(OTHER_REL_DETAILS)

        # Confirmed with Patient Checkbox
        confirm_w_patient1 = driver.find_element(By.ID, "OtherPatientInformationSectionCheckbox")
        confirm_w_patient1.click()

        #CONTRAST AND BOWEL PREPARATION
        # Recent Relevant results not listed
        recent_relevant_result_not_listed = driver.find_element(By.ID,"RecentRelevantResultsNote")
        recent_relevant_result_not_listed.send_keys(RECENT_REL_RESULTS_NOT_LISTED)

        # Adverse reaction to contrast
        adverse_reaction = driver.find_element(By.ID, "AllergyToContrast_Y")
        adverse_reaction.click()

        # Patient Diabetic
        patient_diabetic = driver.find_element(By. ID, "PatientDiabetesStatus_Y")
        patient_diabetic.click()

        # Patient Suitable for bowel preparation
        bowel_prep = driver.find_element(By.ID, "SuitableForBowelPreparation_Y")
        bowel_prep.click()

        # Is patient: low risk, high risk
        patient_risk = driver.find_element(By.ID, "ContrastRisk_HR")
        patient_risk.click()

        # For diabetics is patient (tick all boxes)
        diabetics_diet = driver.find_element(By.ID,"PatientDiabetesAdditionalInformation_01")
        diabetics_diet.click()
        diabetics_insulin = driver.find_element(By.ID,"PatientDiabetesAdditionalInformation_02")
        diabetics_insulin.click()
        diabetics_other_injectables = driver.find_element(By.ID,"PatientDiabetesAdditionalInformation_03")
        diabetics_other_injectables.click()
        diabetics_metformin = driver.find_element(By.ID,"PatientDiabetesAdditionalInformation_04")
        diabetics_metformin.click()
        diabetics_other_oral = driver.find_element(By.ID,"PatientDiabetesAdditionalInformation_05")
        diabetics_other_oral.click()

        # Confirmed with Patient Checkbox
        contrast_bowel_section_checkbox = driver.find_element(By.ID,"ContrastAndBowelPreparationSectionCheckbox")
        contrast_bowel_section_checkbox.click()

        # MRI SAFETY
        # MRI - Does patient have following (tick all boxes)
        mri_brain = driver.find_element(By.ID,"ContraindicationsToMRI_01")
        mri_brain.click()
        mri_endoscope = driver.find_element(By.ID,"ContraindicationsToMRI_13")
        mri_endoscope.click()
        mri_defib = driver.find_element(By.ID,"ContraindicationsToMRI_03")
        mri_defib.click()
        mri_pacemaker = driver.find_element(By.ID,"ContraindicationsToMRI_02")
        mri_pacemaker.click()
        mri_cochlear = driver.find_element(By.ID,"ContraindicationsToMRI_04")
        mri_cochlear.click()
        mri_claustrophobia = driver.find_element(By.ID,"ContraindicationsToMRI_11")
        mri_claustrophobia.click()
        mri_endoclip = driver.find_element(By.ID,"ContraindicationsToMRI_12")
        mri_endoclip.click()
        mri_iac = driver.find_element(By.ID,"ContraindicationsToMRI_05")
        mri_iac.click()
        mri_intrathecal = driver.find_element(By.ID,"ContraindicationsToMRI_06")
        mri_intrathecal.click()
        mri_prosthesis = driver.find_element(By.ID,"ContraindicationsToMRI_07")
        mri_prosthesis.click()
        mri_shunts_stents_clips = driver.find_element(By.ID,"ContraindicationsToMRI_08")
        mri_shunts_stents_clips.click()
        mri_shrapnel = driver.find_element(By.ID,"ContraindicationsToMRI_09")
        mri_shrapnel.click()


        # Has patient has any of the following (tick all boxes)

        # Has patient had metallic foreign body

        # Other Relevant additional details

        # Confirmed with Patient Checkbox

        # PET-CT
        # Required radio pharmaceutical type

        # Previous tests

        # Cautions and contraindications

        # Is request for a funded indication according to commissioning policy

        # Current and previous treatment

        #PREGNANCY AND BREASTFEEDING
        # Is patient pregnant

        # Is patient breastfeeding

        # Estimated date for delivery

        # Confirmed with Patient Checkbox

        #
        # Form input completed
        #

        #SIGN OFF
        # Sign off Form
        sign_off_form(self,driver, password)

        # Log out functionality
        logout_wcp(self,driver)

