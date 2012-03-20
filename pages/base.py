#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class BasePage(Page):

    _page_title_locator = (By.CSS_SELECTOR, "h1.page-title")
    
    @property
    def is_logged_in(self):
        return self.login_region.is_logout_visible

    @property
    def login_region(self):
        from regions.login import LoginRegion
        return LoginRegion(self.testsetup)

    @property
    def page_title(self):
        return self.selenium.find_element(*self._page_title_locator).text

    @property
    def header_region(self):
        from regions.header import HeaderRegion
        return HeaderRegion(self.testsetup)
        