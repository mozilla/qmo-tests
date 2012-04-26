 #!/usr/bin/env python

 # This Source Code Form is subject to the terms of the Mozilla Public
 # License, v. 2.0. If a copy of the MPL was not distributed with this
 # file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert

from pages.media import MediaPage
from pages.home import HomePage


class TestMediaPage:

    def test_media_title(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_home_page()
        media_page = home_page.header_region.go_to_media_page()
        Assert.true(media_page.is_the_current_page)
