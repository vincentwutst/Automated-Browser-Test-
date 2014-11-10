from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get("https://jira.atlassian.com/browse/TST")

class Element(object):
    #Jira login
    def login(self,id_login,id_username,id_password,id_signin,fill_username,fill_password):
        driver.find_element_by_id(id_login).click()
        driver.find_element_by_id(id_username).clear()
        driver.find_element_by_id(id_username).send_keys(fill_username)
        driver.find_element_by_id(id_password).clear()
        driver.find_element_by_id(id_password).send_keys(fill_password)
        driver.find_element_by_id(id_signin).click()
        
    #test new issue can be created
    def creat(self,id_creat,id_project,id_summary,id_creatbutton,fill_project,fill_summary):
        driver.find_element_by_id(id_creat).click()
        driver.find_element_by_xpath(id_project).click()
        driver.find_element_by_link_text(fillproject).click()
        driver.find_element_by_id(id_summary).clear()
        driver.find_element_by_id(id_summary).send_keys(fill_summary)
        driver.find_element_by_id(id_creatbutton).click()

    #test exsisting issue can be found via jira's search
    def search(self,id_name,issue_name):
        driver.find_element_by_id(id_name).clear()
        driver.find_element_by_id(id_name).send_keys(issue_name,Keys.ENTER)
        return driver.title

    #test existing issue can be updated
    def update(self,id_name,issue_name,id_edit,id_update,fill_update):
        driver.find_element_by_id(id_name).clear()
        driver.find_element_by_id(id_name).send_keys(issue_name,Keys.ENTER)
        driver.find_element_by_id(id_edit).click()
        driver.find_element_by_id(id_update).clear()
        driver.find_element_by_id(id_update).send_keys(fill_update)

    def closebrowser(self):
        driver.quit()
