import re

import sublime, sublime_plugin

class LoadTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Load viewport text as string
        visible_region = self.view.visible_region()
        visible_region_string = self.view.substr(visible_region)

        global start
        start = visible_region.begin()

        start_index = 50
        end_index = 55

        search = visible_region_string[start_index:end_index]
        print(search)

        self.find_in_string('core', visible_region_string)

        target_region = sublime.Region(start + start_index, start + end_index)
        # print(self.view.substr(target_region))
        # print(visible_region_string[start_index:end_index])


    def find_in_string(self, search, target):
        for m in re.finditer(search, target):
            target_region = sublime.Region(start + m.start(), start + m.end())

            print(self.view.substr(target_region))



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
