# Jeff Langston
#
# Very early proof of concept utilizing https://github.com/gleitz/howdoi

import sublime
import sublime_plugin
import commands
# import subprocess
# from threading import Thread

#Load Settings
settings = sublime.load_settings("SublimeHowDoI.sublime-settings")


class HowdoiCommand(sublime_plugin.WindowCommand):

    def run(self):
        # Get the search term
        self.window.show_input_panel('How do I:', '',
            self.on_done, self.on_change, self.on_cancel)

    # def get_anwser(self, query):
        # p = subprocess.Popen("howdoi " + query,
                         # stdout=subprocess.PIPE,
                         # stderr=subprocess.STDOUT)
        # return iter(p.stdout.readline, b'')

    def handle_query(self, syntaxSettings, query):
        instructions = commands.getstatusoutput("howdoi " + str(query))
        # instructions = self.get_anwser(self, query)
        syntaxes = [x.lower() for x in syntaxSettings]
        matchedSyntax = False
        for searchWord in query.split():
                if searchWord.lower() in syntaxes:
                    matchedSyntax = True
                    searchTermSyntax = searchWord
                    break

        # Create an output buffer
        self.output_view = self.window.new_file()
        self.output_view.set_name(query)
        self.output_view.set_scratch(True)
        edit = self.output_view.begin_edit()
        self.output_view.insert(edit, 0, instructions[1])
        self.output_view.end_edit(edit)
        if matchedSyntax:
            self.output_view.set_syntax_file("Packages/" + searchTermSyntax + "/" + searchTermSyntax + ".tmLanguage")

    def on_done(self, input):
        # t = Thread(target=lambda: sublime.set_timeout(self.handle_query(settings.get("syntaxes"), input), 100), args=())
        # t.start()
        self.handle_query(settings.get("syntaxes"), input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
