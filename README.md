# Sublime Text 2 How Do I Code Search

A plugin leveraging [howdoi - a unix code search tool](https://github.com/gleitz/howdoi) terminal command to be useable from sublime.

Look for How Do I: code search in command palette entery query and the response is shown in a new tab when the query returns

# Install
git clone: https://github.com/jlangston/Sublime-How-Do-I into your packages folder

At this point you have to have [howdoi](https://github.com/gleitz/howdoi) installed and working from the command line for this plugin to work at all


# Usage
::
    How Do I: [-h] [-p POS] [-a] [-l] QUERY [QUERY ...]

    code search tool

    positional arguments:
      QUERY              the question to answer

    optional arguments:
      -h, --help         show this help message and exit
      -p POS, --pos POS  select answer in specified position (default: 1)
      -a, --all          display the full text of the answer
      -l, --link         display only the answer link

# Disclaimer

Very early proof of concept only initally tested on OSX and still in need of lots of work and polish

