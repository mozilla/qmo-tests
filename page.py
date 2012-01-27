#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
import base64


class Page(object):

    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium

    @property
    def is_the_current_page(self):
        page_title = self.selenium.title
        if not page_title == self._page_title:
            print "Expected page title: %s" % self._page_title
            print "Actual page title: %s" % page_title
            raise Exception("Expected page title does not match actual page title.")
        else:
            return True
