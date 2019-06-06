import unittest
import os, sys
from appium import webdriver


class SimpleAndroidUITests(unittest.TestCase):

    def setUp(self):
        apk_file =  os.path.abspath(os.path.join(os.path.dirname(__file__),'sample_apk_debug.apk'))
        apk_file = "/tmp/sample_apk_debug.apk"
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'automationName': 'UIAutomator2',
            'app': apk_file,
            'browserName': 'android',
            'avd': 'nexus_5_7.1.1'
        }

        p = os.path.abspath(os.path.join(os.path.dirname(__file__) ) )
        print("Path is {0}".format(p))
        #sys.exit(0)
        self.driver = webdriver.Remote('http://172.18.0.2:4444/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_calculation(self):
        text_fields = self.driver.find_elements_by_class_name('android.widget.EditText')
        text_fields[0].send_keys(4)
        text_fields[1].send_keys(6)

        btn_calculate = self.driver.find_element_by_class_name('android.widget.Button')
        btn_calculate.click()

        self.assertEqual('10', text_fields[2].text)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidUITests)
    unittest.TextTestRunner(verbosity=2).run(suite)
