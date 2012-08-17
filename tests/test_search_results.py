#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.search_results import SearchResultsPage


class TestSearchPage:

    @pytest.mark.nondestructive
    def test_no_results_returned_from_blank_search(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_home_page()

        search_results_page = home_page.header_region.click_search_button()
        Assert.true(home_page.is_the_current_page)
