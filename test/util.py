import os
from StringIO import StringIO
import mimetools
from urllib import addinfourl

DEFAULT_HEADERS = [("Content-type", "text/html")]

def _headers(headers_list):
    # This is so stupid.
    # Have you ever looked at the source to urllib2?
    # Sweet mercy, it's awful in there.
    header_lines = []
    for key, value in headers_list:
        header_lines.append("%s: %s" % (key, value))

    header_handle = StringIO("\n".join(header_lines))
    return mimetools.Message(header_handle)


def mock_response(url, response_text, headers=DEFAULT_HEADERS):
    all_headers = headers + [("Content-length", len(response_text))]
    headers_obj = _headers(all_headers)
    return addinfourl(StringIO(response_text), headers_obj, url)


def response_from_file(url, file_name):
    if os.path.abspath(file_name) == file_name:
        file_path = file_name
    else:
        # Assume it's in the test/responses directory
        my_path = os.path.abspath(__file__)
        my_dir = os.path.dirname(my_path)
        responses_dir = os.path.join(my_dir, "responses")
        file_path = os.path.join(responses_dir, file_name)

    handle = open(file_path, "rb")
    content = handle.read()
    handle.close()

    return mock_response(url, content)

