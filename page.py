#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Tests.
#
# The Initial Developer of the Original Code is Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Dave Hunt <dhunt@mozilla.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

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
            self.record_error()
            print "Expected page title: %s" % self._page_title
            raise Exception("Expected page title does not match actual page title.")
        else:
            return True

    def find_element(self, locator):
        return self.selenium.find_element(locator[0], locator[1])

    def record_error(self):
        print "-------------------"
        print "Error at: %s" % self.selenium.current_url
        print "Page title: %s" % self.selenium.title.encode('utf-8')
        print "-------------------"
        filename = "%s.png" % str(time.time()).split('.')[0]

        print "Screenshot of error in file: %s" % filename
        f = open(filename, "wb")
        f.write(base64.decodestring(self.selenium.get_screenshot_as_base64()))
        f.close()
