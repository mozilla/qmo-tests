#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.teams import TeamsPage

TEAM_NAMES = [
    u'Automation',
    u'Desktop Firefox',
    u'Web QA',
    u'Thunderbird',
    u'Services QA',
    u'Mobile QA',
    u'Firefox OS QA']


class TestTeamsPage:

    @pytest.mark.nondestructive
    def test_teams_page_consistency(self, mozwebqa):
        teams_page = TeamsPage(mozwebqa)
        teams_page.go_to_teams_page()
        listed_teams = teams_page.teams

        # check that all teams are listed
        Assert.equal(
            sorted(TEAM_NAMES),
            sorted([team.name for team in listed_teams]),
            u'Not all expected teams are present.')

        # check for avatar, description and meta info
        for team in listed_teams:
            Assert.true(team.is_avatar_displayed, u'Team avatar is not displayed.')
            #Assert.greater(len(team.description), 0, u'Team description is blank')
            #Assert.greater(len(team.meta_info), 0, u'Team meta info is blank')

    @pytest.mark.parametrize(
        ('team_name'), TEAM_NAMES)
    @pytest.mark.nondestructive
    def test_that_current_team_links_match_up_and_work(self, mozwebqa, team_name):
        teams_page = TeamsPage(mozwebqa)
        teams_page.go_to_teams_page()
        about_team_page = teams_page.open_team_page(team_name)

        Assert.true(about_team_page.is_the_current_page)
        Assert.contains(
            about_team_page.team_name, team_name,
            u'''Wrong team name.
                Expected: %s, but got: %s''' % (about_team_page.team_name, team_name))
