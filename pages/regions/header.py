 #!/usr/bin/env python

 # This Source Code Form is subject to the terms of the Mozilla Public
 # License, v. 2.0. If a copy of the MPL was not distributed with this
 # file, You can obtain one at http://mozilla.org/MPL/2.0/.

from page import Page

from selenium.webdriver.common.by import By


class HeaderRegion(Page):
    _community_link_locator = (By.CSS_SELECTOR, '#nav-main li:nth-child(3) a')
    _events_link_locator = (By.CSS_SELECTOR, '#nav-main li:nth-child(4) a')
    _media_link_locator = (By.CSS_SELECTOR, '#nav-main li:nth-child(5) a')
    _docs_link_locator = (By.CSS_SELECTOR, '#nav-main li:nth-child(6) a')
    _search_field_locator = (By.CSS_SELECTOR, '#search input#s' )
    _search_button_locator = (By.CSS_SELECTOR, '#search fieldset input#s')
    
    def click_community_link(self):
        self.selenium.find_element(*self._community_link_locator).click()
        from pages.community import CommunityPage
        return CommunityPage(self.testsetup)

    def click_events_link(self):
        self.selenium.find_element(*self._events_link_locator).click()
        from pages.events import EventsPage
        return EventsPage(self.testsetup)

    def click_media_link(self):
        self.selenium.find_element(*self._media_link_locator).click()
        from pages.media import MediaPage
        return MediaPage(self.testsetup)

    def click_docs_link(self):
        self.selenium.find_element(*self._docs_link_locator).click()
        from pages.docs import DocsPage
        return DocsPage(self.testsetup)

    def click_search_field(self):
        self.selenium.find_element(*self._search_field_locator).click()
        from pages.home import HomePage

    def click_search_button(self):
        self.selenium.find_element(*self._search_button_locator).click()
        from pages.search_results import SearchResultsPage
        return SearchResultsPage(self.testsetup)
