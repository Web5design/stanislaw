import urllib2

from lxml import html
from pyquery import PyQuery

from stanislaw.forms import FormManager

class Browser(object):
    def __init__(self, debug=False):
        self.debug = debug
        self.tree = None
        self.current_response = None
        self.current_html = None
        self._pyquery = None
        self.form_manager = FormManager(self)

    def _set_response(self, response):
        self.current_response = response
        self.current_html = response.read()
        self.tree = html.fromstring(self.current_html)
        self._pyquery = PyQuery(self.tree)

    def visit(self, url):
        response = urllib2.urlopen(url)
        self._set_response(response)

    def fill(self, selector_value_dict):
        return self.form_manager.fill(selector_value_dict)

    def submit(self, form_selector=None):
        pass

    def query(self, selector):
        return self._pyquery(selector)

    def html(self, selector):
        pass
