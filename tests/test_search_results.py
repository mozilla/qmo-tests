#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage


class TestSearchPage:

    @pytest.mark.nondestructive
    def test_no_results_returned_from_blank_search(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_home_page()

        search_results = home_page.header_region.click_search_button()
        Assert.true(search_results.is_the_current_page)
        Assert.true(search_results.get_url_current_page().endswith(u'/?s='))

    @pytest.mark.nondestructive
    def test_search_results_returned(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_home_page()

        home_page.header_region.type_in_search_field(u'job board')
        search_results_page = home_page.header_region.click_search_button()

        expected_text = u'Search results'
        Assert.contains(expected_text, search_results_page._page_title)
        Assert.greater(len(search_results_page.results), 0)
