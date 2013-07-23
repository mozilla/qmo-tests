#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests
from bs4 import BeautifulSoup

from base import BasePage


class RSSFeed(BasePage):

    def __init__(self, mozwebqa):

        super(BasePage, self).__init__(mozwebqa)
        feed_url = mozwebqa.base_url + '/feed/'
        r = requests.get(feed_url, verify=False)

        # throw exception if status code is not 200
        r.raise_for_status()

        # ideally we need to pass 'xml' to BeautifulSoup
        # but it requires lxml installed which has external dependencies
        self.parsed_feed = BeautifulSoup(r.content)

    @property
    def title(self):
        return self.parsed_feed.title.text

    @property
    def description(self):
        return self.parsed_feed.description.text

    @property
    def link(self):
        return self.parsed_feed.link.text

    @property
    def items_count(self):
        return len(self.parsed_feed.find_all('item'))

    @property
    def items(self):
        """Returns list of dictionaries

        where each dictionary represents one item in feed with
        keys - tag names of child elements and
        values - text values of child elements.
        Note: that only few of all possible child elements
        are included into dictionary.
        """
        # we want to check only following elements
        required_els = ['title', 'link', 'dc:creator', 'description', 'content:encoded']

        items_ = []
        for item in self.parsed_feed.find_all('item'):
            temp_dict = {}
            for el in item.children:
                try:
                    tag = el.name
                    if tag in required_els:
                        temp_dict[tag] = el.get_text()
                except AttributeError:
                    # some child elements don't have any tag name
                    pass
            items_.append(temp_dict)
        return items_
