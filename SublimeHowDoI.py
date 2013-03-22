# Jeff Langston
#
# Very simple proof of concept utilizing https://github.com/gleitz/howdoi
# to run within the editor


import sublime
import sublime_plugin

import threading
import subprocess
import functools

# Load Settings
# settings = sublime.load_settings('SublimeHowDoI.sublime-settings')


def get_settings(key, default=None, view=None):
    # sublime.load_settings is silent in startup period
    # this lazy loader is to overcome this problem
    try:
        if view is None:
            view = sublime.active_window().active_view()
        s = view.settings()
        if s.has(key):
            return s.get(key)
    except:
        pass
    return sublime.load_settings("SublimeHowDoI.sublime-settings").get(key, default)


class CommandThread(threading.Thread):
    # Seperate thread to run howdoi query in background

    def __init__(self, command, on_done, syntaxes, query):
        threading.Thread.__init__(self)
        self.command = command
        self.on_done = on_done
        self._syntaxes = syntaxes
        self._query = query

    def run(self):
        query = self._query

        syntaxes_lc = [x.lower() for x in self._syntaxes]
        searchTermSyntax = ""
        for searchWord in query.split():
                if searchWord.lower() in syntaxes_lc:
                    searchTermSyntax = self._syntaxes[
                        syntaxes_lc.index(searchWord.lower())]
                    break

        try:
            p = subprocess.Popen(
                self.command + ' ' + query, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, shell=True)
            output = p.communicate()[0]

            sublime.set_timeout(
                functools.partial(self.on_done, output.decode('utf-8'),
                                  searchTermSyntax), 0)
        except subprocess.CalledProcessError as e:
            sublime.set_timeout(
                functools.partial(self.on_done, e.returncode), 0)


class HowdoiCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        # TODO: google autocomplete in input panel
        # Get the search term
        active_window = sublime.active_window()
        active_window.show_input_panel('How do I:', '',
                                       self.on_done, self.on_change, self.on_cancel)

    def on_done(self, query):
        command = 'howdoi'
        options = get_settings("options")
        if options is not None:
            for k, v in options.items():
                command += ' '
                # options without store
                if v == "":
                    command += '--' + k
                else:
                    command += '--' + k + ' ' + str(v)

        thread = CommandThread(
            command, self.panel, get_settings("syntaxes"), query)
        thread.start()
        sublime.status_message("Retrieving answer ...")

    def on_change(self, query):
        pass

    def on_cancel(self):
        pass

    def panel(self, output, searchTermSyntax):
        active_window = sublime.active_window()

        if not hasattr(self, 'output_view'):
            self.output_view = active_window.create_output_panel(
                "howdoi_answer")

        # if not hasattr(self, 'output_view'):
        # self.output_view = active_window.get_output_panel("howdoi_answer")
        self.output_view.settings().set("word_wrap", True)
        self.output_view.settings().set("line_numbers", True)
        self.output_view.settings().set("gutter", True)
        self.output_view.settings().set("scroll_past_end", False)
        # if searchTermSyntax != '':
        # self.view.assign_syntax("Packages/" + searchTermSyntax + "/" +
        # searchTermSyntax + ".tmLanguage")

        self.output_view.set_read_only(False)
        self.output_view.run_command('howdoi_show', {
            'output': output,
            'searchTermSyntax': searchTermSyntax,
            'clear': True
        })
        self.output_view.set_read_only(True)
        active_window.run_command(
            'show_panel', {"panel": 'output.howdoi_answer'})


class HowdoiShowCommand(sublime_plugin.TextCommand):

    def run(self, edit, searchTermSyntax, output='', clear=False):
        if clear:
            region = sublime.Region(0, self.view.size())
            self.view.erase(edit, region)

        self.view.insert(edit, 0, output)

        if searchTermSyntax != '':
            self.view.set_syntax_file("Packages/" + searchTermSyntax +
                                      "/" + searchTermSyntax + ".tmLanguage")
