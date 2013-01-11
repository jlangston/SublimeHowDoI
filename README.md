# How Do I Code Search for Sublime Text 2

A plugin leveraging [howdoi - a unix code search tool](https://github.com/gleitz/howdoi) terminal command to be useable from sublime.

Look for How Do I: code search in command palette entery query and the response is shown in a new tab when the query returns

# Install
git clone: https://github.com/jlangston/Sublime-How-Do-I into your packages folder

At this point you have to have [howdoi](https://github.com/gleitz/howdoi) installed and working from the command line for this plugin to work at all


# Usage

    How Do I: [-h] [-p POS] [-a] [-l] QUERY [QUERY ...]

    code search tool

    positional arguments:
      QUERY              the question to answer

    optional arguments:
      -h, --help         show this help message and exit
      -p POS, --pos POS  select answer in specified position (default: 1)
      -a, --all          display the full text of the answer
      -l, --link         display only the answer link

# Settings
    Default shortcut key super + alt + h to

    Settings file:
        syntaxes: List of languages with syntax hilighting support that the plugin will try to match depending on the howdoi question

        useBuffer: Show howdoi answer in quick panel or new tab


# Disclaimer

This is my first go at a sublime text plugin it's only been tested on OSX and still has lots of room for improvement and polish.

I'd like to get it running on windows but to this point I've had issues installing howdoi on windows. I'll look at making this plugin work under windows once I can get the command like version working in windows.

# Other Notes

The entire utility could be packaged up into the plugin without having to require having the command line version installed but all the python library dependencies would need to be sorted out to be included with the plugin.

If you like the idea behind this plugin and would like to see improvements pull requests are welcome

