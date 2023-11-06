import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class doctorPage:
    def __init__(self, url) -> None:
        """ Constructor for the class doctorPage. Basically intantiate web driver to the given url """
        self.url = url
        self.driver2 = webdriver.Chrome()
        self.exp_list = list()
        self.res_list = list()
    
    def getGender(self):
        """ Method for setting the gender of the doctor. and append to the list."""
        self.driver2.get(self.url)
        self.sex = self.driver2.find_elements(By.CSS_SELECTOR, "gender")

        if self.sex:
            return self.sex[0].text 
        return "Not Found"
    
    def getExpertiseResearchInterests(self):
        """ Method for setting the expertise of the doctor. and append to the list."""
        self.driver2.get(self.url)

        try:
            self.link_element = WebDriverWait(self.driver2, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "...read more"))
            )
            try:
                self.link_element.click()
            except:
                try:
                    self.exp = WebDriverWait(self.driver2, 5).until(
                        EC.visibility_of_all_elements_located((By.CLASS_NAME, "expertise"))
                    )
                    self.exp_list.append(self.exp[0].text[:-13])
                except selenium.common.exceptions.TimeoutException:
                    self.exp_list.append("Not Found")
                try:
                    self.res = WebDriverWait(self.driver2, 5).until(
                        EC.visibility_of_all_elements_located((By.CLASS_NAME, "research"))
                    )
                    self.res_list.append(self.exp[1].text[:-13])
                except selenium.common.exceptions.TimeoutException:
                    self.res_list.append("Not Found")
                return
            try:
                self.bundle = WebDriverWait(self.driver2, 10).until(
                    EC.visibility_of_all_elements_located((By.CLASS_NAME, "read-more-wrapper"))
                )
                string = "Expertise"
                expFound = False; researchFound = False
                for _ in self.bundle:
                    if string == "Expertise":
                        self.exp_list.append(_.text[:-13])
                        expFound = True
                        string = "Research"
                    else:
                        self.res_list.append(_.text[:-13])
                        researchFound = True
                if not expFound:
                    self.exp_list.append("Not Found")
                if not researchFound:
                    self.res_list.append("Not Found")
                    
            except selenium.common.exceptions.TimeoutException:
                self.exp_list.append("Not Found")
                self.res_list.append("Not Found")
        except selenium.common.exceptions.TimeoutException:
            try:
                self.exp = WebDriverWait(self.driver2, 5).until(
                    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".expertise p"))
                )
                self.exp_list.append(self.exp[0].text)
            except selenium.common.exceptions.TimeoutException:
                self.exp_list.append("Not Found")
            try:
                self.res = WebDriverWait(self.driver2, 5).until(
                    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".research p"))
                )
                self.res_list.append(self.res[0].text)
            except selenium.common.exceptions.TimeoutException:
                self.res_list.append("Not Found")
        return self.exp_list, self.res_list
    
    def getContactNo(self):
        """ Method for setting the contact number of the doctor. and append to the list."""
        self.driver2.get(self.url)
        try:
            self.cnct = WebDriverWait(self.driver2, 5).until(
                    EC.visibility_of_all_elements_located((By.CLASS_NAME, "phone"))
                )
            return self.cnct[0].text
        except selenium.common.exceptions.TimeoutException:
            return "Not Found"
        
    def getLocation(self):
        """ Method for setting the location of the doctor. and append to the list."""
        self.driver2.get(self.url)
        try:
            self.loc = WebDriverWait(self.driver2, 5).until(
                    EC.visibility_of_all_elements_located((By.CLASS_NAME, "address"))
                )
            self.addr = str()
            for self.x in self.loc[0].text.split():
                self.addr += self.x + " "
            return self.addr[:-1]
        except selenium.common.exceptions.TimeoutException:
            return "Not Found"

    def getEducation(self):
        """ Method for setting the education of the doctor. and append to the list."""
        self.driver2.get(self.url)
        try:
            self.edu = WebDriverWait(self.driver2, 5).until(
                    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#Education ul:nth-child(3) li"))
                )
            return self.edu[0].text
        except selenium.common.exceptions.TimeoutException:
            return "Not Found"

    def reset(self):
        self.exp_list = list() 
        self.res_list = list()
        self.driver2.quit()