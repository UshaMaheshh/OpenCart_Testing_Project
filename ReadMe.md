**Project Title**: Automated Testing of Practice Website \- https://demo-opencart.com/

 

**Project Overview:** d**emo-openCart.com** is an interactive demo site for OpenCart, an open-source e-commerce platform. This repository provides a detailed guide to exploring and testing the demo site to better understand its core functionalities. The demo environment enables users to experience OpenCart’s features, including store management, product handling, and customer account operations.

 

**Objective:** The objective of this project is to provide a comprehensive overview and documentation of testing the **My Account** menu within the OpenCart demo site. Specifically, the focus has been on validating the **Register** and **Login** functionalities. By conducting these tests, we aim to ensure that users can seamlessly create new accounts and log in to their existing profiles, confirming that these core account management features work as expected. This project serves as a resource for developers, testers, and businesses looking to understand and assess the account functionality in OpenCart before integrating it into their own e-commerce solutions.

**Testing Approach:**

Automated Testing: Utilized Selenium WebDriver for browser automation and Python as the primary scripting language. Pytest was used for running test cases and generating comprehensive test reports. The automation framework was structured using the Page Object Model (POM) design pattern, which ensured maintainability and scalability. Data-Driven Testing (DDT) was applied to handle user account and login data sourced from Excel, enabling comprehensive test coverage.

Integrated Development Environment (IDE): The automation scripts were developed using PyCharm (Community Edition), which provided an efficient and user-friendly environment for coding and managing the project.

 

**Tools and Technologies Used:**

Selenium WebDriver: Automated browser interactions and user actions.

Python: The primary language for scripting the automated test cases.

Pytest: Ran the test cases and generated test reports.

Excel: Managed test data for Data-Driven Testing (DDT).

Page Object Model (POM): Applied as a design pattern to organize test scripts, improving code reusability and maintainability.

Data-Driven Testing (DDT): Enabled testing with multiple data sets sourced from Excel.

PyCharm (Community Edition): Used as the IDE for developing, debugging, and managing the Python-based automation scripts.

GitHub: Used for version control and repository management to track changes and facilitate collaboration

 

**Setup & configure WebDriver in Pycharm**

**Pre-requisites:**

o   Python

o   Pycharm

 

1\) Download browser specific drivers using below links....

Chrome:      	https://chromedriver.chromium.org/downloads

Edge:           	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox:        	https://github.com/mozilla/geckodriver/releases

 

Once you donwloaded, extract .zip files then you will see .exe files ( they are drivers)

2\) setup selenium webdriver

        	Appraoch\#1:

                    	pip install selenium==4.0.0.b4

                    	pip install selenium

        	Appraoch\#2:

                    	or through Pycharm project settings...

 

         	

**Run Tests on Desired Browser(Cross Browser Testing)/Parallel**

   
update conftest.py with required fixtures which will accept command line argument (browser).

Pass browser name as argument in command line

 

**To Run tests on desired browser**

pytest \-s \-v .\\testCases\\path\\your test filename \--browser edge  
   
**To Run tests parallel**

pytest \-s \-v **\-n=3** .\\testCases\\path\\your test filename \--browser edge

   
**Generate pytest HTML Reports**

 

Update conftest.py with pytest hooks

**pytest \-s \-v \--html=reports\\report.html \--capture=tee-sys .\\testCases\\your test file name \--browser chrome**

**Example report:**

[http://localhost:63342/OpencartProject/reports/14-08-2024%2020-32-16.html?\_ijt=re330lrd433mqmvp38guejict6&\_ij\_reload=RELOAD\_ON\_SAVE\&sort=result](http://localhost:63342/OpencartProject/reports/14-08-2024%2020-32-16.html?_ijt=re330lrd433mqmvp38guejict6&_ij_reload=RELOAD_ON_SAVE&sort=result)

 

   
