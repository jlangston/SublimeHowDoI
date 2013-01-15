# How Do I Code Search for Sublime Text 2

A plugin leveraging [howdoi - a unix code search tool](https://github.com/gleitz/howdoi) terminal command to be useable from sublime text.

Look for How Do I: code search in command palette entery query and the response is shown in a new tab or view when the query returns

# Install
Until this is availible on package control you'll have to either 
git clone: https://github.com/jlangston/SublimeHowDoI into your packages folder or
download the zip of the repository and place that in your packages folder

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
Default shortcut key super + alt + h to show How Do I: search box

Settings file:
  syntaxes: List of languages with syntax hilighting support that
  the plugin will try to match depending on the howdoi question

  useBuffer: Show howdoi answer in quick panel or new tab


# Disclaimer

This is my first go at a sublime text plugin it's only been tested on OSX and Windows and still has lots of room for improvement and polish.

# Other Notes

Ideally the entire utility could be packaged up into the plugin without having to require having the command line version installed but all the python library dependencies would need to be sorted out to be included with the plugin.

If you like the idea behind this plugin and would like to see improvements pull requests are welcome

