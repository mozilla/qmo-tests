#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time

from selenium.webdriver.common.by import By

from base import BasePage


class RegistrationPage(BasePage):

    _page_title = u'Create an Account | QMO \u2013 quality.(mozilla|allizom).org'

    _username_locator = (By.ID, 'signup_username')
    _username_error_locator = (By.CSS_SELECTOR, 'label[for=signup_username] ~ .error')
    _email_locator = (By.ID, 'signup_email')
    _password_locator = (By.ID, 'signup_password')
    _confirm_password_locator = (By.ID, 'signup_password_confirm')
    _display_name_locator = (By.ID, 'field_1')
    _humanity_test_locator = (By.ID, 'bph_field')
    _submit_locator = (By.ID, 'signup_submit')

    def register_new_user(self):
        current_time = str(time.time()).split('.')[0]
        password = 'password'
        self.type_username('automatedtest%s' % current_time)
        self.type_in_element(self._email_locator, 'automatedtest%s@mailinator.com' % current_time)
        self.type_in_element(self._password_locator, password)
        self.type_in_element(self._confirm_password_locator, password)
        self.type_in_element(self._display_name_locator, 'Automated Test %s' % current_time)
        self.submit_registration()

    def type_username(self, username):
        self.type_in_element(self._username_locator, username)

    @property
    def username_error(self):
        return self.find_element(*self._username_error_locator).text

    def submit_registration(self):
        self.find_element(*self._submit_locator).click()
