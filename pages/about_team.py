#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import BasePage


class AboutTeamPage(BasePage):

    _team_name_locator = (By.CSS_SELECTOR, '.intro > h1')

    @property
    def _page_title(self):
        return u'%s | Groups | QMO' % self.team

    @property
    def team_name(self):
        return self.find_element(*self._team_name_locator).text
