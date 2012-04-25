 #!/usr/bin/env python

 # This Source Code Form is subject to the terms of the Mozilla Public
 # License, v. 2.0. If a copy of the MPL was not distributed with this
 # file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert

from pages.docs import DocsPage

from pages.home import HomePage

class TestDocsPage:

    def test_docs_title(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_home_page()
        docs_page = home_page.header_region.click_docs_link()
        Assert.true(docs_page.is_the_current_page)

