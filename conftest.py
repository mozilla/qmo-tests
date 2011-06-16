#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Tests.
#
# The Initial Developer of the Original Code is Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Dave Hunt <dhunt@mozilla.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import pytest
import py

from selenium import webdriver


def pytest_runtest_setup(item):
    item.host = item.config.option.host
    item.browser_name = item.config.option.browser_name
    item.browser_version = item.config.option.browser_version
    item.platform = item.config.option.platform
    item.port = item.config.option.port
    TestSetup.base_url = item.config.option.base_url
    TestSetup.skip_selenium = True

    if item.browser_name is None:
        raise Exception("You must specify a browser name.")
    if item.browser_version is None:
        raise Exception("You must specify a browser version.")
    if item.platform is None:
        raise Exception("You must specify a platform.")

    if not "skip_selenium" in item.keywords:
        TestSetup.skip_selenium = False
        
        try:
            capabilities = getattr(webdriver.DesiredCapabilities, item.browser_name.upper())
            capabilities["version"] = item.browser_version
            capabilities["platform"] = item.platform.upper()
            TestSetup.selenium = webdriver.Remote(
                command_executor = "http://%s:%s/wd/hub" % (item.host, item.port),
                desired_capabilities = capabilities)
        except AttributeError:
            valid_browsers = [attr for attr in dir(webdriver.DesiredCapabilities) if not attr.startswith('__')]
            raise AttributeError("Invalid browser name: '%s'. Valid options are: %s" % (item.browser_name, ", ".join(valid_browsers)))


def pytest_runtest_teardown(item):
    if hasattr(TestSetup, "selenium") and not TestSetup.skip_selenium:
        TestSetup.selenium.quit()


def pytest_funcarg__testsetup(request):
    return TestSetup(request)


def pytest_addoption(parser):
    parser.addoption("--host",
                     action="store",
                     default="localhost",
                     help="host that Selenium server is listening on")
    parser.addoption("--port",
                     action="store",
                     default="4444",
                     help="port that Selenium server is listening on")
    parser.addoption("--browser-name",
                     action="store",
                     dest="browser_name",
                     help="target browser")
    parser.addoption("--browser-version",
                     action="store",
                     dest="browser_version",
                     help="target browser version")
    parser.addoption("--platform",
                     action="store",
                     help="target platform")
    parser.addoption("--base-url",
                     action="store",
                     dest="base_url",
                     default="http://quality-new.stage.mozilla.com",
                     help="base URL for the application under test")


class TestSetup:
    def __init__(self, request):
        self.request = request
