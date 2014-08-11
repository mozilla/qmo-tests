#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class HeaderRegion(Page):

    _community_link_locator = (By.CSS_SELECTOR, '#nav-main li:nth-child(3) a')
    _events_link_locator = (By.CSS_SELECTOR, '#nav-main li:nth-child(4) a')
    _docs_link_locator = (By.CSS_SELECTOR, '#nav-main li:nth-child(5) a')
    _search_button_locator = (By.CSS_SELECTOR, '#search button')
    _search_field_locator = (By.CSS_SELECTOR, '#search input#s')

    def click_community_link(self):
        self.find_element(*self._community_link_locator).click()
        from pages.community import CommunityPage
        return CommunityPage(self.testsetup)

    def click_events_link(self):
        self.find_element(*self._events_link_locator).click()
        from pages.events import EventsPage
        return EventsPage(self.testsetup)

    def click_docs_link(self):
        self.find_element(*self._docs_link_locator).click()
        from pages.docs import DocsPage
        return DocsPage(self.testsetup)

    def click_search_button(self):
        self.find_element(*self._search_button_locator).click()
        from pages.search_results import SearchResultsPage
        return SearchResultsPage(self.testsetup)

    def click_search_field(self):
        self.find_element(*self._search_field_locator).click()
        from pages.search_results import SearchResultsPage
        return SearchResultsPage(self.testsetup)

    def type_in_search_field(self, text):
        self.type_in_element(self._search_field_locator, text)
