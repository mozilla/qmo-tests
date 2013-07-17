#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.rss_feed import RSSFeed


class TestRSSFeed:

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_checks_rss_feed(self, mozwebqa):

        feed = RSSFeed(mozwebqa)

        # check basic values of channel element
        Assert.equal(feed.title, u'QMO - quality.mozilla.org')
        Assert.equal(feed.description, u'The Home of Mozilla QA')
        Assert.equal(feed.link, mozwebqa.base_url)
        Assert.greater_equal(feed.items_count, 10, 'where are all published articles?')

        # check that items in feed have some content
        for item in feed.items:
            Assert.true(all(len(item[key]) > 5 for key in item),
                        u'some content of "%s" item is missing or is too short' % item['title'])
