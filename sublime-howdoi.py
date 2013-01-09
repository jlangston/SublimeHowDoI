# Jeff Langston
#
# Very early proof of concept utilizing https://github.com/gleitz/howdoi


import sublime
import sublime_plugin
import commands


class HowdoiCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search term
        self.window.show_input_panel('How do I:', '',
            self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
        instructions = commands.getstatusoutput("howdoi " + input)
        inputArr = input.split()
        syntaxes = ("C",
                    "C++",
                    "C#",
                    "CoffeeScript",
                    "CSS",
                    "D",
                    "Erlang",
                    "HTML",
                    "Groovy",
                    "Haskell",
                    "HTML",
                    "Java",
                    "JavaScript",
                    "LaTeX",
                    "Lisp",
                    "Lua",
                    "Markdown",
                    "Matlab",
                    "OCaml",
                    "Perl",
                    "PHP",
                    "Python",
                    "R",
                    "Ruby",
                    "SQL",
                    "TCL",
                    "Textile",
                    "XML")
        matchedSyntax = False
        for searchWord in inputArr:
            print searchWord
            if not matchedSyntax:
                for syntax in syntaxes:
                    if searchWord.lower() == syntax.lower():
                        matchedSyntax = True
                        searchTermSyntax = syntax
                        break
            else:
                break
        # Create an output buffer
        self.output_view = self.window.new_file()
        self.output_view.set_name(input)
        self.output_view.set_scratch(True)
        edit = self.output_view.begin_edit()
        self.output_view.insert(edit, 0, instructions[1])
        self.output_view.end_edit(edit)
        if matchedSyntax:
            self.output_view.set_syntax_file("Packages/" + searchTermSyntax + "/" + searchTermSyntax + ".tmLanguage")

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass


# def load_syntaxes(self):
#         settings = sublime.load_settings('Howdoi.sublime-settings')
#         # load the default syntaxes
#         default_syntaxes = settings.get("syntaxes")
#         if default_syntaxes is None:
#             default_syntaxes = []
