#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from unittestzero import Assert

from pages.home import HomePage
from pages.not_found import NotFoundPage


class TestHomePage:

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_favicon_present(self, mozwebqa):

        home_page = HomePage(mozwebqa)
        favicon_url = home_page.favicon_url
        r = requests.get(favicon_url, verify=False)

        Assert.equal(
            r.status_code, 200,
            u'request to %s responded with %s status code' % (favicon_url, r.status_code))

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_robots_txt_present(self, mozwebqa):

        home_page = HomePage(mozwebqa)
        robots_url = u'%s/%s' % (home_page.base_url, 'robots.txt')
        r = requests.get(robots_url, verify=False)

        Assert.equal(
            r.status_code, 200,
            u'request to %s responded with %s status code' % (robots_url, r.status_code))

    @pytest.mark.nondestructive
    def test_that_proper_404_error_page_displayed(self, mozwebqa):

        not_found_page = NotFoundPage(mozwebqa)
        not_found_page.go_to_not_found_page()

        Assert.equal(not_found_page.page_title, u'Sorry, we couldn’t find that')

        Assert.equal(not_found_page.get_page_status_code(), 404,
                     u'GET request to this page should return 404 status code')

        err_msg_parts = []
        err_msg_parts.append(u'We looked everywhere, but we couldn’t find the page or file you were looking for. A few possible explanations:')
        err_msg_parts.append(u'You may have followed an out-dated link or bookmark.')
        err_msg_parts.append(u'If you entered the address by hand, you might have mistyped it.')
        err_msg_parts.append(u'Maybe you found a bug. Good work!')
        error_message = '\n'.join(err_msg_parts)

        Assert.equal(not_found_page.error_message, error_message)
