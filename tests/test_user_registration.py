#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import random

import pytest
from unittestzero import Assert

from pages.home import HomePage


class TestUserRegistration:

    @pytest.mark.xfail(reason=u'QMO has removed registration')
    def test_new_user_can_register(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        registration_pg = home_pg.login_region.click_sign_up()

        registration_pg.register_new_user()
        Assert.equal(registration_pg.page_title, u'Sign Up Complete!')

    def test_username_only_allows_lower_case_letters_and_numbers(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        registration_pg = home_pg.login_region.click_sign_up()

        invalid_characters = range(32, 47) + range(58, 96) + range(123, 127)
        invalid_username = u'automatedtest%s' % chr(random.choice(
                                                    invalid_characters))

        registration_pg.type_username(invalid_username)
        registration_pg.submit_registration()
        Assert.equal(
            registration_pg.username_error,
            u'Only lowercase letters and numbers allowed.')
