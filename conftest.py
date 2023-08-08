import os.path

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=("chrome", "firefox", "safari"))
    parser.addoption("--headless", action='store_true')
    parser.addoption("--base_url", default="https://demo.nopcommerce.com/")
    parser.addoption("--remote_url", default="127.0.0.1:4444")
    # TODO изменить параметр drivers_folder
    parser.addoption("--drivers_folder", default="drivers")
    parser.addoption("--stage", default='local', choices=("local", "remote"))
    parser.addoption("--bversion", action="store", default="114.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    headless_mode = request.config.getoption("--headless")
    drivers_folder = request.config.getoption('--drivers_folder')
    stage = request.config.getoption("--stage")
    remote_url = request.config.getoption("--remote_url")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    driver = None
    if stage == 'local':
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            if headless_mode:
                options.add_argument('--headless=new')
                options.add_argument('--no-sandbox')
            service = ChromeService(executable_path=os.path.join(f"{drivers_folder}", "chromedriver"))
            driver = webdriver.Chrome(service=service, options=options)
        if browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            if headless_mode:
                options.add_argument('--headless')
            service = FirefoxService(executable_path=os.path.join(f"{drivers_folder}", "geckodriver"))
            driver = webdriver.Firefox(service=service, options=options)
        if browser_name == 'safari':
            driver = webdriver.Safari()

        driver.maximize_window()
    else:
        selenoid_url = f"http://{remote_url}/wd/hub"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.set_capability("browserVersion", version)
        chrome_options.set_capability("screenResolution", "1280x1024")
        chrome_options.set_capability("selenoid:options", {
            "sessionTimeout": "60s",
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs
        })

        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=chrome_options
        )

    yield driver

    driver.close()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        browser = item.funcargs['browser']  # Get the browser instance from the test's fixture
        img = browser.get_screenshot_as_png()
        allure.attach(img, 'Failure screenshot', allure.attachment_type.PNG)
