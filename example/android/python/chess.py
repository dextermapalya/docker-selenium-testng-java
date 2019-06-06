import os
import unittest
from appium import webdriver
from time import sleep
 
class ChessAndroidTests(unittest.TestCase):
    "Class to run tests against the Chess Free app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Android Emulator'
        #desired_caps['browserName'] = 'Android'
        desired_caps['avd'] = 'nexus_5_7.1.1'
        
        # Returns abs path relative to this file and not cwd
        #desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/chess.apk'))
        desired_caps['app'] = '/root/tmp/sample_apk/chess.apk'
        desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        desired_caps['appActivity'] = '.ChessFreeActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_single_player_mode(self):
        "Test the Chess app launches correctly and click on Play button"
        element = self.driver.find_element_by_id("uk.co.aifactory.chessfree:id/ButtonPlay")
        element.click()
        sleep(5)
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
