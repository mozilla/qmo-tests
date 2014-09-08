#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class SearchResultsPage(BasePage):

    _page_title = u'Search Results'

    _search_text_locator = (By.ID, 'content-main')
    _search_result_item_locator = (By.CSS_SELECTOR, "#content-main > article")

    def search_results_page(self):
        self.get_relative_path('/?s')
        self.is_the_current_page

    @property
    def search_text(self):
        return self.find_element(*self._search_text_locator).text

    @property
    def results(self):
        return self.find_elements(*self._search_result_item_locator)
