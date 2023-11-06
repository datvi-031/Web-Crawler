from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class doctorsPage:
    def __init__(self, url) -> None:
        """ Constructor for the class doctorsPage. Basically intantiate web driver to the given url """
        self.url = url
        self.driver = webdriver.Chrome()
        self.names = list()
        self.title = list()

    def get_doctorName_title(self):
        """ Method for getting the name and title of the doctor from the url. appends to respective lists """
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 5)
        self.doctor_title = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "doctor-name")))
        for self.element in self.doctor_title:
            self.doctor = self.element.text.split(',')
            self.names.append(self.doctor[0])

            self.designation = ", ".join(self.doctor[1:])
            self.title.append(self.designation)
        return self.names, self.title
    
    def getProfileLinks(self):
        """ Method for returning the profile links of each doctor in the page as a list. """
        self.profile_url_list = list()
        self.wait = WebDriverWait(self.driver, 10)

        self.doctor_links = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.doctorLink')))
        for self.doctor_link in self.doctor_links:
            self.profile_url = self.doctor_link.get_attribute("href")
            self.profile_url_list.append(self.profile_url)

        return self.profile_url_list

    def reset(self):
        self.names = list()
        self.title = list()
        self.driver.quit()