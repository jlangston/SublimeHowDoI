# Jeff Langston
#
# Very simple proof of concept utilizing https://github.com/gleitz/howdoi to run within the editor

import sublime
import sublime_plugin
import threading
import commands
# import subprocess

#Load Settings
settings = sublime.load_settings("SublimeHowDoI.sublime-settings")


class HowdoiCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search term
        self.window.show_input_panel('How do I:', '',
            self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
        self.cmdThread(settings.get("syntaxes"), input, settings.get("useBuffer"), self.window).start()

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass

    # Seperate thread to run howdoi query in background
    class cmdThread(threading.Thread):
        def __init__(self, syntaxes, query, useBuffer, window):
            self._syntaxes = syntaxes
            self._query = query
            self._useBuffer = useBuffer
            self._window = window
            threading.Thread.__init__(self)

        def run(self):
            query = self._query
            # p = subprocess.Popen("howdoi " + query, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            # stdoutdata = p.communicate().get(0)
            query_response = commands.getstatusoutput("howdoi " + query)
            syntaxes = [x.lower() for x in self._syntaxes]
            matchedSyntax = False
            for searchWord in query.split():
                    if searchWord.lower() in syntaxes:
                        matchedSyntax = True
                        searchTermSyntax = searchWord
                        break
            sublime.set_timeout(lambda: self.show_answer(query, matchedSyntax, query_response, searchTermSyntax, self._useBuffer, self._window), 0)

        # Create an output buffer
        def show_answer(self, query, matchedSyntax, query_response, searchTermSyntax, useBuffer, window):
            if useBuffer:
                output_view = window.new_file()
                output_view.set_name(query)
                output_view.set_scratch(True)
                edit = output_view.begin_edit()
                output_view.insert(edit, 0, query_response[1])
                output_view.end_edit(edit)
            else:
                output_view = window.get_output_panel('howdoi_answer')
                edit = output_view.begin_edit()
                output_view.erase(edit, sublime.Region(0, output_view.size()))
                output_view.insert(edit, 0, query_response[1])
                output_view.end_edit(edit)
                window.run_command('show_panel', {"panel": 'output.howdoi_answer'})
            if matchedSyntax:
                output_view.set_syntax_file("Packages/" + searchTermSyntax + "/" + searchTermSyntax + ".tmLanguage")
