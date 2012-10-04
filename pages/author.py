#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from base import BasePage


class AuthorPage(BasePage):

    _page_title = u"Posts by %s | QMO \u2013 quality.mozilla.org"

    _posted_by_locator = (By.CSS_SELECTOR, 'div.entry-meta .vcard > a')

    def go_to_author_page(self):
        self.selenium.get(self.testsetup.base_url + '/author/' + self.author)

    def __init__(self, testsetup, author):
        BasePage.__init__(self, testsetup)
        self._page_title = self._page_title % author
        self.author = author

    @property
    def posted_by(self):
        return self.selenium.find_elements(*self._posted_by_locator)
