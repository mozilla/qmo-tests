#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.community import CommunityPage


class TestCommunityPage:

    @pytest.mark.nondestructive
    def test_community_title(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_home_page()
        community_page = home_page.header_region.click_community_link()
        Assert.true(community_page.is_the_current_page)

    @pytest.mark.nondestructive
    def test_that_search_by_tag_works(self, mozwebqa):
        tag_name = u'firefox'
        community_page = CommunityPage(mozwebqa)
        community_page.go_to_community_page()
        tag_results_page = community_page.click_tag_link(tag_name)

        Assert.true(tag_results_page.is_the_current_page)
        Assert.equal(
            u'Posts and pages tagged “%s”' % tag_name,
            tag_results_page.page_title)

        found_articles = tag_results_page.results
        Assert.greater(len(found_articles), 0)

        for article in found_articles:
            Assert.contains(tag_name, article.related_tags)
