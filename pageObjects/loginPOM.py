from selenium.webdriver.common.by import By


class loginPOM:
    userName = "//*[@id='Email']"
    password = "//*[@id='Password']"
    loginBtn = "//*[@class='button-1 login-button']"
    signout = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def enter_UserName(self,username):
        user_text_box=self.driver.find_element(By.XPATH,self.userName)
        user_text_box.clear()
        user_text_box.send_keys(username)

    def enter_Password(self,paswd):
        paswd_box=self.driver.find_element(By.XPATH,self.password)
        paswd_box.clear()
        paswd_box.send_keys(paswd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.loginBtn).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT,self.signout).click()

