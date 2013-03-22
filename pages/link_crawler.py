#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests
from requests.exceptions import RequestException, ConnectionError
from bs4 import BeautifulSoup
from unittestzero import Assert

from page import Page


class LinkCrawler(Page):

    def collect_links(self, url, name=True, **kwargs):

        """ Collects links for given page URL.

        If name is True, then links will be collected for whole page.
        Use name argument to pass tag name of element.
        Use kwargs to pass id of element or its class name.
        Because 'class' is a reserved keyword in Python,
        you need to pass class as: **{'class': 'container row'}.

        """

        # support for relative URL
        if not url.startswith('http'):
            url = u'%s%s' % (self.base_url, url)

        # get the page and verify status code is OK
        r = requests.get(url, verify=False)

        Assert.true(
            r.status_code == requests.codes.ok,
            u'{0.url} returned: {0.status_code} {0.reason}'.format(r))

        # parse page and collect links
        parsed_html = BeautifulSoup(r.text)
        urls = (anchor['href'] for anchor in parsed_html.find(name, attrs=kwargs).find_all('a'))

        # prepend base_url to relative links
        return map(lambda u: u if not u.startswith('/') else '%s%s' % (self.base_url, u), urls)

    def verify_status_code_is_ok(self, url):
        # don't fail if something went wrong
        try:
            r = requests.get(url, verify=False)
        except (RequestException, ConnectionError), e:
            return u'request to {0} failed due {1}'.format(url, e)

        if r.status_code == requests.codes.ok:
            return True
        else:
            return u'{0.url} returned: {0.status_code} {0.reason}'.format(r)
