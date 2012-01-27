#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class LoginRegion(Page):

    _sign_up_link_locator = (By.CSS_SELECTOR, ".signup a")

    def click_sign_up(self):
        self.selenium.find_element(*self._sign_up_link_locator).click()
