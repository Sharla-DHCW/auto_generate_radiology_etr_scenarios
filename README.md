Status: Draft 
Following work to be completed: 
1) Complete form inputs on generate_Maximum_Data_Radiology_ETR.py
2) Start/Complete generate_Special_Character_Data_Radiology_ETR.py

**This code repository allows users to generate Radiology ETR requests from WCP SIT environment automatically for the following test scenarios:**
- Send a Radiology ETR with a standard size data input
- Send a Radiology ETR with the minimum data input required on the form
- Send a Radiology ETR with the maximum data input available on the form
- Send a Radiology ETR with special/numerical characters in all free text fields

These scenarios help test the way in which the messaging fabric and receiving systems handle the different data input possibilities. 

**Prerequisites to execution of code:**
For the code to be executed successfully. The following test data needs to be amended in the **test_data.py** file prior to code execution:
- Value of the TEST_USERNAME variable needs to be changed to the user's NADEX account username
- Value of the TEST_PASSWORD variable needs to be changed to the user's NADEX account password
- Value of the TEST_NHS_NUMBER variable needs to be changed to a test patient's NHS number
- Value of the TEST_FEMALE_NHS_NUMBER variable needs to be changed to a FEMALE test patient's NHS number. This allows for the pregnancy section to generate for the maximum data input scenario. 
- Value of SIGNOFF_NAME variable needs to be changed to users name.

  

