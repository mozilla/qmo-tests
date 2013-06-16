#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class NotFoundPage(BasePage):

    _page_title = u'Not Found | QMO – quality.(mozilla|allizom).org'

    _error_message_locator = (By.CSS_SELECTOR, '.entry-content')

    def go_to_not_found_page(self):
        self.get_relative_path('/this_page_does_not_exist')
        self.is_the_current_page

    @property
    def error_message(self):
        return self.find_element(*self._error_message_locator).text

    def get_page_status_code(self):
        import requests
        r = requests.get(self.get_url_current_page(), verify=False)
        return r.status_code
