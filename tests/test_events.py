#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.link_crawler import LinkCrawler
from pages.home import HomePage


class TestEventsPage:

    @pytest.mark.nondestructive
    def test_events_title(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_home_page()
        events_page = home_page.header_region.click_events_link()
        Assert.true(events_page.is_the_current_page)

    @pytest.mark.nondestructive
    def test_events_page_link(self, mozwebqa):
        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('/category/events', id='content')
        bad_urls = []

        Assert.greater(
            len(urls), 0, u'something went wrong. no links found.')

        for url in urls:
            check_result = crawler.verify_status_code_is_ok(url)
            if check_result is not True:
                bad_urls.append(check_result)

        Assert.equal(
            0, len(bad_urls),
            u'%s bad links found. ' % len(bad_urls) + ', '.join(bad_urls))
