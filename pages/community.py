#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class CommunityPage(BasePage):

    _page_title = u'Community | QMO \u2013 quality.mozilla.org'
    _tag_locator = (By.CSS_SELECTOR, '#tag_cloud-3 a')

    def go_to_community_page(self):
        self.selenium.get(self.testsetup.base_url + '/community')
        self.is_the_current_page

    @property
    def find_tag_link(self):
        return self.selenium.find_element(*self._tag_locator)
