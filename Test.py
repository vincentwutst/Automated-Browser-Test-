import unittest
import pageobject

test_page = pageobject.Element()
class JIRATest(unittest.TestCase):
    def test_login(self):
        idlogin = "user-options"
        idusername = "username"
        idpassword = "password"
        idsignin = "login-submit"
        fillusername = "vincent.wu.tst@gmail.com"
        fillpassword = "88888888"
        test_page.login(idlogin,idusername,idpassword,idsignin,fillusername,fillpassword)

    def test_creat(self):
        idcreat = "create_link"
        idproject = "//div[@id='project-single-select']/span"
        idsummary = "summary"
        idcreatbutton = "create-issue-submit"
        fillproject = "Angry Nerds"
        fillsummary = "New Issue Find!"
        test_page.creat(idcreat,idproject,idsummary,idcreatbutton,
              fillproject,fillsummary)

    def test_search(self):
        idname = "quickSearchInput"
        issuename = "ANERDS-4140"
        expected = "[ANERDS-4140] New Issue Find! - Atlassian JIRA"
        result = test_page.search(idname,issuename)
        print result
        self.assertEquals(expected,result)

    def test_update(self):
        idname = "quickSearchInput"
        issuename = "ANERDS-4140"
        idedit = "edit-issue"
        idupdate = "description"
        fillupdate = "update!!"
        
    def tearDown(self):
        test_page.closebrowser()
        
if __name__ == "__main__":
    unittest.main()


