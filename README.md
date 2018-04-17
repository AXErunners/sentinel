# AXE Sentinel

An all-powerful toolset for AXE.

[![Build Status](https://travis-ci.org/AXErunners/sentinel.svg?branch=master)](https://travis-ci.org/AXErunners/sentinel)
[![Maintainability](https://api.codeclimate.com/v1/badges/cf201db73c11d50c78b4/maintainability)](https://codeclimate.com/github/AXErunners/sentinel/maintainability)

## Installation

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ cd ~ && cd .axecore
    $ git clone https://github.com/axerunners/sentinel.git && cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/.axecore/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /home/YOURUSERNAME/.axecore/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### 4. Test the Configuration

Test the config by runnings all tests from the sentinel folder you cloned into

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with axed and the installation is complete

## Configuration

An alternative (non-default) path to the `axe.conf` file can be specified in `sentinel.conf`:

    axe_conf=/path/to/axe.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

## Contributing

Please follow the [AXE core guidelines for contributing](https://github.com/AXErunners/axe/blob/master/.github/CONTRIBUTING.md).

To contribute a patch, the workflow is as follows

   * Fork repository
   * Create topic branch
   * Commit patches

In general commits should be atomic and diffs should be easy to read. For this reason do not mix any formatting fixes or code moves with actual code changes.
    
Commit messages should be verbose by default, consisting of a short subject line (50 chars max), a blank line and detailed explanatory text as separate paragraph(s); unless the title alone is self-explanatory (like "Corrected typo in main.cpp") then a single title line is sufficient. Commit messages should be helpful to people reading your code in the future, so explain the reasoning for your decisions. Further explanation [here](http://chris.beams.io/posts/git-commit/).

### License

Released under the MIT license, under the same terms as AXE core itself. See [LICENSE](LICENSE) for more info.
