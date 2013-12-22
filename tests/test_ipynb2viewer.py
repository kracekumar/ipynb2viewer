#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ipynb2viewer
----------------------------------

Tests for `ipynb2viewer` module.
"""

import unittest

from docopt import docopt, DocoptExit
import requests

from ipynb2viewer import ipynb2viewer


class TestIpynb2viewer(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.ipynb'
        self.path = "tests"
        self.usage = """
Usage:
  ipynb2viewer all
  ipynb2viewer file <filename>
  ipynb2viewer file <filename> --open
  ipynb2viewer file <filename> --open --userid <cookie>
  ipynb2viewer all --open
"""

    def test_empty_argv(self):
        with self.assertRaises(DocoptExit):
            docopt(ipynb2viewer.__doc__, argv=[])

    def test_all_ipynb_files(self):
        self.assertEquals(len(ipynb2viewer.get_all_ipynb_files('tests')), 1)
        self.assertEquals(len(ipynb2viewer.get_all_ipynb_files('/')), 0)

    def test_upload_file_to_gist(self):
        details = ipynb2viewer.upload_file_to_gist(self.filename, self.path)
        assert 'html_url' in details
        details = ipynb2viewer.upload_file_to_gist(self.path + "/" + self.filename)
        assert 'html_url' in details

    def test_create_nbviewer_url(self):
        with self.assertRaises(requests.HTTPError):
            ipynb2viewer.create_nbviewer_url("http://goo.gl")

        ipynb2viewer.create_nbviewer_url("https://gist.github.com/anonymous/8080069")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
