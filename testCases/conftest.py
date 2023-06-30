import pytest
from pageObjects.loginPOM import loginPOM
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup(browser):
    if browser=="chrome":
      driver=webdriver.Chrome()
    elif browser=="firefox":
      driver=webdriver.Firefox()
    elif browser=="edge":
      driver=webdriver.Edge()
    else:
     driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


