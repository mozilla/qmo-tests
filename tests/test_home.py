#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from unittestzero import Assert

from pages.home import HomePage


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
