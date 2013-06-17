#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class AuthorPage(BasePage):

    _posted_by_locator = (By.CSS_SELECTOR, 'div.entry-meta .vcard > a')

    @property
    def _page_title(self):
        return u'Posts by %s | QMO' % self.author_name

    def go_to_author_page(self):
        self.get_relative_path('/author/%s' % self.author_name)
        self.is_the_current_page

    @property
    def posted_by(self):
        return self.find_elements(*self._posted_by_locator)
