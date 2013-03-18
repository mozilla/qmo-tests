#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from base import BasePage


class MediaPage(BasePage):

    _page_title = u'QMO Videos | QMO \u2013 quality.mozilla.org'

    def go_to_media_page(self):
        self.get_relative_path('/media')
        self.is_the_current_page
