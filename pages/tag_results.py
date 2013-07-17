#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage
from page import PageRegion


class TagResultsPage(BasePage):

    _search_result_item_locator = (By.CSS_SELECTOR, '#content-main > article')

    @property
    def _page_title(self):
        return u'%s | QMO' % self.tag_name

    @property
    def results(self):
        return [Article(self.testsetup, web_element)
                for web_element in self.find_elements(*self._search_result_item_locator)]


class Article(PageRegion):

    _related_tag_locator = (By.CSS_SELECTOR, '.entry-tags > a')

    @property
    def related_tags(self):
        return [tag.text for tag in self.find_elements(*self._related_tag_locator)]
