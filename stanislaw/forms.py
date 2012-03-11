import re

# Borrowed from jQuery
INPUT_TYPES = re.compile("^(color|date|datetime|datetime-local|email|"
                         "hidden|month|number|password|range|search|"
                         "tel|text|time|url|week)$", re.IGNORECASE)
SELECT_TEXTAREA = re.compile("^(select|textarea)$", re.IGNORECASE)


class SubmitException(Exception):
    pass


class FormManager(object):
    def __init__(self, browser):
        self.browser = browser

    def fill(self, selector_value_dict):
        for selector, value in selector_value_dict.items():
            self.browser.query(selector).val(value)

    def find_form(self, form_selector=None):
        if form_selector:
            form = self.browser.query(form_selector)
        else:
            form = self.browser.query("form")

        if not form:
            msg = "Could not find any form on this page to submit."
            if form_selector:
                msg = "Could not find form: %s" % form_selector
            raise SubmitException(msg)

        if len(form) > 1:
            raise SubmitException("Found %d forms on this page, "
                                  "please explicitly select one to submit "
                                  "by passing form_selector to submit()."
                                  % len(form))
        return form[0]

    def _is_submittable_form_element(self, element):
        attributes = element.attrib
        if "name" not in attributes:
            return False
        if "type" not in attributes:
            return False
        if "disabled" in attributes:
            return False
        if "checked" in attributes:
            return True
        if re.match(SELECT_TEXTAREA, element.tag):
            return True
        if re.match(INPUT_TYPES, attributes["type"]):
            return True

        return False

    def form_value_list(self, form_selector=None):
        form = self.find_form(form_selector)
        value_list = [] # (input_name, value)

        for descendant in form.getiterator():
            if self._is_submittable_form_element(descendant):
                attributes = descendant.attrib
                value_list.append((attributes["name"],
                                   attributes.get("value", "")))

        return value_list

