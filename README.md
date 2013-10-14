
A plugin leveraging [howdoi - a unix code search tool](https://github.com/gleitz/howdoi) terminal command to be useable from sublime text.

Look for How Do I: code search in command palette entery query and the response is shown in a new tab or view when the query returns

# Install
Install from Package Control or 
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

# Contributors
  dnatag

Change Log
* Rewrite much of the code base to make it compatible with ST3. Borrowed some codes from kemayo's sublime-text-2-goto-documentation at https://github.com/kemayo/sublime-text-2-goto-documentation.git 
* Add support of howdoi options except --color since ST3 have better syntax highlight scheme.
* Add status message for user notification
* Add main menu of Preferences 

