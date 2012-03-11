from unittest import TestCase
from stanislaw.browser import Browser
from test.util import response_from_file

BASIC_FORM = "basic_form.html"
URL = "http://example.com/form.html"

def get_browser(url=URL, response_file=BASIC_FORM):
    b = Browser()
    b._set_response(response_from_file(url, response_file))
    return b


class FormFillTest(TestCase):
    def test_fill_all_form_values(self):
        browser = get_browser()
        browser.fill({"#first_name": "Niels",
                      "#last_name": "Bohr",
                      "#email_address": "bohr@lanl.gov"})

        self.assertEquals("Niels", browser.query("#first_name").val())
        self.assertEquals("Bohr", browser.query("#last_name").val())
        self.assertEquals("bohr@lanl.gov", browser.query("#email_address").val())

    def test_fill_some_form_values(self):
        browser = get_browser()
        browser.fill({"#first_name": "Niels",
                      "#last_name": "Bohr"})

        self.assertEquals("Niels", browser.query("#first_name").val())
        self.assertEquals("Bohr", browser.query("#last_name").val())
        self.assertEquals("teller@lanl.gov", browser.query("#email_address").val())

    def test_fill_nonexistant_element(self):
        browser = get_browser()
        browser.fill({"#does_not_exist": "bad_value"})

        self.assertEquals("Edward", browser.query("#first_name").val())
        self.assertEquals("Teller", browser.query("#last_name").val())
        self.assertEquals("teller@lanl.gov", browser.query("#email_address").val())

class FormManagerTest(TestCase):

    def test_form_serialize(self):
        browser = get_browser()
        serialized_form = browser.form_manager.form_value_list()
        print serialized_form
        self.assertTrue(False)

