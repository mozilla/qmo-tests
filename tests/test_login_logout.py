#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert

from pages.home import HomePage


class TestLoginLogout:

    def test_login(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.login_region.login()
        Assert.true(home_pg.is_logged_in)

    def test_logout(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.login_region.login()
        Assert.true(home_pg.is_logged_in)
        home_pg.login_region.logout()
        Assert.false(home_pg.is_logged_in)
