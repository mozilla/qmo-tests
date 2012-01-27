QMO Tests
=========

Automated tests for the QMO website.

Running Tests
-------------

### Java
You will need a version of the [Java Runtime Environment][JRE] installed

[JRE]: http://www.oracle.com/technetwork/java/javase/downloads/index.html

### Python
Before you will be able to run these tests you will need to have Python 2.6 installed.

Run

    easy_install pip

followed by

    sudo pip install -r requirements.txt

__note__

If you are running on Ubuntu/Debian you will need to do following first

    sudo apt-get install python-setuptools
    
to install the required Python libraries.

### Selenium Grid
Once this is all set up you will need to download and start a Selenium Grid instance. Probably the simplest way to do this is to clone the [moz-grid-config][MozGridConfig] repository and follow the instructions in the README to start both a hub and webdriver instance.

[MozGridConfig]: https://github.com/mozilla/moz-grid-config/tree/grid2

### Running tests locally

To run tests locally its a simple case of calling the command below from this directory

    py.test . --browser-name=<BROWSER_NAME> --browser-version=<BROWSER_VERSION> --platform=<PLATFORM>

All parameters are required, and depend on the environments provided by your Selenium Grid instance. For example:

    py.test . --browser-name=FIREFOX --browser-version=4.0 --platform=MAC

Writing Tests
-------------

If you want to get involved and add more tests then there's just a few things
we'd like to ask you to do:

1. Use the [template files][GitHub Templates] for all new tests and page objects
2. Follow our simple [style guide][Style Guide]
3. Fork this project with your own GitHub account
4. Make sure all tests are passing, and submit a pull request with your changes

[GitHub Templates]: https://github.com/AutomatedTester/mozwebqa-test-templates
[Style Guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide

License
-------
    This Source Code Form is subject to the terms of the Mozilla Public
      - License, v. 2.0. If a copy of the MPL was not distributed with this
      - file, You can obtain one at http://mozilla.org/MPL/2.0/.
