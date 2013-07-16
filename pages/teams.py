#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import PageRegion
from pages.base import BasePage


class TeamsPage(BasePage):

    _page_title = u'Teams | QMO'

    _team_region_locator = (By.CSS_SELECTOR, '.team')

    def go_to_teams_page(self):
        self.get_relative_path('/teams')
        self.is_the_current_page

    def open_team_page(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team.open_team_page(team_name)
        raise Exception(u'There is no team with such name: %s' % team_name)

    @property
    def teams(self):
        return [TeamRegion(self.testsetup, web_element) for web_element
                in self.find_elements(*self._team_region_locator)]


class TeamRegion(PageRegion):

    _team_avatar_locator = (By.CSS_SELECTOR, '.avatar')
    _team_title_locator = (By.CSS_SELECTOR, '.entry-title > a')
    _team_description_locator = (By.CSS_SELECTOR, '.team-info > p')
    _team_meta_block_locator = (By.CSS_SELECTOR, '.team-meta')

    @property
    def name(self):
        return self.find_element(*self._team_title_locator).text

    def open_team_page(self, team_name):
        self.find_element(*self._team_title_locator).click()
        from pages.about_team import AboutTeamPage
        return AboutTeamPage(self.testsetup, team=team_name)

    @property
    def is_avatar_displayed(self):
        return self.is_element_visible(*self._team_avatar_locator)

    @property
    def description(self):
        return self.find_element(*self._team_description_locator).text

    @property
    def meta_info(self):
        return self.find_element(*self._team_meta_block_locator).text
