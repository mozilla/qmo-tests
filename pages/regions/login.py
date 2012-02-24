#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from page import Page


class LoginRegion(Page):

    _sign_up_link_locator = (By.CSS_SELECTOR, '.signup a')
    _login_username_field_locator  = (By.ID, 'log')
    _login_password_field_locator  = (By.ID, 'pwd')
    _login_submit_button_locator  = (By.CSS_SELECTOR, '.login .submit button')
    _logout_link_locator  = (By.CSS_SELECTOR, '.howdy .user-logout a')

    @property
    def is_logout_visible(self):
        try:
            return self.selenium.find_element(*self._logout_link_locator).text == 'Log Out'
        except NoSuchElementException:
            return False

    def click_sign_up(self):
        self.selenium.find_element(*self._sign_up_link_locator).click()
        from pages.registration import RegistrationPage
        return RegistrationPage(self.testsetup)

    def login(self, user='default'):
        credentials = self.testsetup.credentials[user]
        self.selenium.find_element(*self._login_username_field_locator).send_keys(credentials['username'])
        self.selenium.find_element(*self._login_password_field_locator).send_keys(credentials['password'])
        self.selenium.find_element(*self._login_submit_button_locator).click()

    def logout(self):
        self.selenium.find_element(*self._logout_link_locator).click()
