# Final project

The final project consists of two parts - API tests for https://swapi.dev and UI tests for https://demo.nopcommerce.com/.

## Table of Contents


- [API](#swapi-api-tests)
- [UI](#nopcommerce-ui-tests) 
- [CICD](#cicd) 

## SWAPI API Tests

This repository contains API tests for the Star Wars universe API. The tests aim to validate the functionality and responses of various API endpoints.

## Table of Contents


- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Generate allure report](#generate-allure-report)


## Prerequisites

Before running the tests, make sure you have the following prerequisites:

- Python 3.x installed on your system
- `pip` package manager installed

## Installation

To install the necessary dependencies, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/chipolina/Otus_final.git
   ```

2. Navigate to the project directory:

   ```shell
   cd Otus_final
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate.bat
     ```

   - For Unix or Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Running the Tests

To run the API tests, use the following command:

```shell
pytest -m api
```

This command will execute all the tests defined in the `test_api.py` file and display the test results in the console.

You can also run test in several threeds using flag -n {number of threeds or auto}

```shell
pytest -m api -n 4
```

## Generate-allure-report
To generate allure report use 

```shell
allure serve
```

Report will be available on address 127.0.0.1:port. You can see full address in your terminal

## Nopcommerce UI Tests

This repository contains UI tests for Nopcommerce using Selenium with Python. The tests aim to validate the functionality and behavior of several pages in the Nopcommerce e-commerce platform.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Running the Tests](#running-the-tests)


## Prerequisites

Before running the tests, make sure you have the following prerequisites:

- Chrome WebDriver or Firefox WebDriver installed, depending on your preferred browser and installed in folder Otus_final/drivers

## Running the Tests

To run the API tests, use the following command:

```shell
pytest -m ui
```

This command will execute all the tests defined in the `test_ui.py` file and display the test results in the console.

You can also run test in several threeds using flag -n {number of threeds or auto}

```shell
pytest -m ui -n 4
```



To run the tests with the `pytest_addoption` function options, you can follow these instructions:

1. Run the tests using the `pytest` command and specify the options:

   ```shell
   pytest --browser chrome --drivers_folder /path/to/chromedriver -m ui
   ```

   Replace the following options with your desired values:
   - `--browser`: Specify the browser to run the tests (e.g., `chrome`, `firefox`).
   - `--drivers_folder`: Specify the path to the WebDriver executable.
   - `--stage`: Local or remote run (Selenoid).
   - `--remote_url`: Specify the Selenoid endpoint URL. By default, 127.0.0.1:4444
   

   All option you can see in conftest.py

  Note: Make sure to provide the correct paths and URLs for your setup.

2. The tests will be executed using the specified options, and the results will be displayed in the console.

   You can also add additional flags or options as needed for your testing environment.

## CICD

To run test in Jenkins you need to set up jenkins server and start it using official documentation

1. **Access the Jenkins Server:**
   - Open your web browser and go to the Jenkins server URL: [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

2. **Create Pipeline:**
   - Click on "New Item" to create a new Jenkins Pipeline.
   - Choose "GitHub project" and enter the project URL as [https://github.com/chipolina/Otus_final.git](https://github.com/chipolina/Otus_final.git).
   - Configure project parameters: Create 'browser' and 'network' parameters with default values 'chrome' and 'host'.

3. **Pipeline Configuration:**
   - In the Pipeline configuration, select "Pipeline script from SCM".
   - Set the Repository URL to [https://github.com/chipolina/Otus_final.git](https://github.com/chipolina/Otus_final.git).
   - Specify the Branch as */main.
   - Set the Script Path to 'Jenkinsfile'.

4. **Save Changes:**
   - Click "Save" to save your Pipeline configuration changes.

5. **Build Job:**
   - Build the Jenkins job by clicking on "Build with Parameters". Choose the desired values for 'browser' and 'network' parameters 'chrome' and 'host'

6. **Report:**
   - After the build is done you can open attached allure report.