 #!/usr/bin/env python
 # This Source Code Form is subject to the terms of the Mozilla Public
 # License, v. 2.0. If a copy of the MPL was not distributed with this
 # file, You can obtain one at http://mozilla.org/MPL/2.0/.

from page import Page

from selenium.webdriver.common.by import By

class HeaderRegion(Page):
    
    _docs_link_locator = (By.CSS_SELECTOR, '#nav-main li:nth-child(7) a')
    
    def click_docs_link(self):
        self.selenium.find_element(*self._docs_link_locator).click()
        from pages.docs import DocsPage
        return DocsPage(self.testsetup)