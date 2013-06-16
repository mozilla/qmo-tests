#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from base import BasePage


class HomePage(BasePage):

    _page_title = u'QMO \u2013 quality.(mozilla|allizom).org | The Home of Mozilla QA'

    def go_to_home_page(self):
        self.get_relative_path('/')
        self.is_the_current_page

    @property
    def favicon_url(self):
        import requests
        from bs4 import BeautifulSoup

        r = requests.get(self.base_url, verify=False)
        html = BeautifulSoup(r.content)
        return html.find(attrs={'rel': 'shortcut icon'}).get('href')

    @property
    def paginator(self):
        from pages.regions.paginator import Paginator
        return Paginator(self.testsetup)
