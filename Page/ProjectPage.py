from selenium.webdriver.common.by import By

from Base.BasePage import BasePage


class ProjectPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.btn_welcome_email_id = "com.todoist:id/btn_welcome_email"
        self.email_exists_input = "com.todoist:id/email_exists_input"
        self.btn_continue_with_email_id = "com.todoist:id/btn_continue_with_email"
        self.log_in_password_id = "com.todoist:id/log_in_password"

    def click_button_welcome_email(self):
        self.clickElement(self.driver.find_element(By.ID, self.btn_continue_with_email_id))

    def enter_email(self):
        self.sendkeyElement(self.driver.find_element(By.ID, self.email_exists_input), "01112000hda@gmail.com")
