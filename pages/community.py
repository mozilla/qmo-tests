#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

from base import BasePage


class CommunityPage(BasePage):

    _page_title = u'Community | QMO \u2013 quality.mozilla.org'
    _tag_locator = (By.CSS_SELECTOR, '#tag_cloud-3 a')

    def go_to_community_page(self):
        self.get_relative_path('/community')
        self.is_the_current_page

    def click_tag_link(self, tag_name):
        for tag in self.find_elements(*self._tag_locator):
            if tag.text == tag_name:
                tag.click()
                from pages.tag_results import TagResultsPage
                return TagResultsPage(self.testsetup, tag_name=tag_name)
        raise Exception(u'%s tag is not found' % tag_name)


class CommunityPageFeed(BasePage):

    def __init__(self, mozwebqa):

        super(BasePage, self).__init__(mozwebqa)
        feed_url = mozwebqa.base_url + '/community/feed/'
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
    def items_count(self):
        return len(self.parsed_feed.find_all('item'))

    @property
    def items(self):
        return self.parsed_feed.find_all('item')
