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

from selenium.webdriver.common.by import By
from unittestzero import Assert

import base_page


class RegistrationPage(base_page.BasePage):

    _page_title = u"Create an Account | QMO \u2013 quality.mozilla.org"

    _username_locator = (By.ID, "signup_username")
    _username_error_locator = (By.CSS_SELECTOR, "label[for=signup_username] ~ .error")
    _email_locator = (By.ID, "signup_email")
    _password_locator = (By.ID, "signup_password")
    _confirm_password_locator = (By.ID, "signup_password_confirm")
    _display_name_locator = (By.ID, "field_1")
    _humanity_test_locator = (By.ID, "bph_field")
    _submit_locator = (By.ID, "signup_submit")

    def register_new_user(self):
        current_time = str(time.time()).split('.')[0]
        password = "password"
        self.set_username("automatedtest%s" % current_time)
        self.find_element(self._email_locator).send_keys("automatedtest%s@mailinator.com" % current_time)
        self.find_element(self._password_locator).send_keys(password)
        self.find_element(self._confirm_password_locator).send_keys(password)
        self.find_element(self._display_name_locator).send_keys("Automated Test %s" % current_time)
        self.find_element(self._humanity_test_locator).send_keys("nine")
        self.submit_registration()

    def set_username(self, username):
        self.find_element(self._username_locator).clear()
        self.find_element(self._username_locator).send_keys(username)

    @property
    def username_error(self):
        return self.find_element(self._username_error_locator).text

    def submit_registration(self):
        self.find_element(self._submit_locator).click()
