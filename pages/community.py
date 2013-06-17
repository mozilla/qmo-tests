#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class CommunityPage(BasePage):

    _page_title = u'Community | QMO'

    _tag_locator = (By.CSS_SELECTOR, '#tag_cloud-3 a')

    def go_to_community_page(self):
        self.get_relative_path('/community')
        self.is_the_current_page

    def click_tag_link(self, tag_name):
        for tag in self.find_elements(*self._tag_locator):
            if tag.text == tag_name:
                tag.click()
                from pages.tag_results import TagResultsPage
                return TagResultsPage(self.testsetup, tag_name=tag_name)
        raise Exception(u'%s tag is not found' % tag_name)
