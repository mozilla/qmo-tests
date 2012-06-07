#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from base import BasePage


class CommunityPage(BasePage):

    _page_title = u'Community | QMO \u2013 quality.mozilla.org'

    def go_to_community_page(self):
        self.selenium.get(self.testsetup.base_url + '/community')
        self.is_the_current_page
