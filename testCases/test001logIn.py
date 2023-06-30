import pytest
from pageObjects.loginPOM import loginPOM
from configurations import config_reader
from logs.loggins import Logs01
@pytest.mark.usefixtures
class Test_loginpage:
    url=config_reader.readConfigurations("basic","url")
    username=config_reader.readConfigurations("basic","username")
    password=config_reader.readConfigurations("basic","password")
    login_page_Title=config_reader.readConfigurations("basic","login_page_Title")
    home_page_Title=config_reader.readConfigurations("basic","home_page_Title")
    logger = Logs01()
    log = logger.logs()


    def testLogin_page_title_validation(self,setup):
        self.driver=setup
        self.driver.get(self.url)

        self.log.info("web application opend")
        if self.driver.title==self.login_page_Title:
            assert True
            self.log.info("login page title verification succesful")
        else:
            self.log.error("login page title verification failed")


    def test_login_validation(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        loginPOM01=loginPOM(self.driver)
        loginPOM01.enter_UserName(self.username)
        self.log.info("username enterd in the password textbox field")
        loginPOM01.enter_Password(self.password)
        self.log.info("password enterd in the password textbox field")
        loginPOM01.clickLogin()
        self.log.info("login button clicked")
        if self.driver.title == self.home_page_Title:
            assert True
            self.log.info("home page title validation succesfull")
        else:
            self.log.warning("home page title validation failed")
            assert False




