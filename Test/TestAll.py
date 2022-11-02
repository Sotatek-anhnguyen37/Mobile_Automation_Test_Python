from Base.BaseSetUp import BaseSetUp
from Page.ProjectPage import ProjectPage


class TestAll(BaseSetUp):
    def test_abc(self):
        driver = self.driver
        print("day la test")
        projectpage = ProjectPage(driver)
        projectpage.click_button_welcome_email()
        projectpage.enter_email()