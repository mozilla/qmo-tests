#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.community import CommunityPage
from pages.tag_results import TagResultsPage


class TestTagSearchPage:

    @pytest.mark.nondestructive
    def test_search_tag(self, mozwebqa):
        community_page = CommunityPage(mozwebqa)
        community_page.go_to_community_page()

        tag_results_page = community_page.click_first_tag_link

        Assert.contains('Posts and pages tagged', tag_results_page.page_title)
        Assert.greater(len(tag_results_page.results), 0)
