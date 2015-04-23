import sublime, sublime_plugin

class LoadTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print(self.view.sel())




'''
User executes shortcut
    Immediately load viewport text for processing

User hits two keys
    String search for character pair
        If only 1 match, send cursor
    For each match, display 'jump char' on top of 2nd char
    Grey out all text except for jump char


User hits valid jump char
    Move cursor, in command mode, to jump char position
User hits invalid jump char
    Ignore command
'''
