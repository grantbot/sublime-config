import re

import sublime, sublime_plugin

class LoadTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Load viewport text as string
        visible_region = self.view.visible_region()
        visible_region_string = self.view.substr(visible_region)

        region_start = visible_region.begin()

        # Will replace with user input char combo
        start_index = 58
        end_index = 60
        search_string = visible_region_string[start_index:end_index]

        #Search
        self.find_in_string(search_string, visible_region_string, region_start, edit)


    def find_in_string(self, search, target, region_start, edit):
        placeholder_chars = list('abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        # Generate matched regions array
        match_regions = {};
        for m in re.finditer(search, target):
            # Generate region containing matched chars
            target_region = sublime.Region(region_start + m.start() + 1, start + m.end())
            match_regions[placeholder_chars.pop(0)] = target_region

            # print(self.view.substr(target_region))

        # Highlight matched regions
        self.view.add_regions('match_regions', list(match_regions.values()), 'string', '', sublime.DRAW_NO_OUTLINE)

        # Replace matched regions with placeholder char
        for placeholder_char in match_regions.keys():
            #TODO(grant) shouldn't have to pass edit objects around
            self.view.replace(edit, match_regions[placeholder_char], placeholder_char)

class JumpTo(sublime_plugin.WindowCommand):
    def run(self, character=None):
        print(character)

class RemoveHighlightCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Unhighlight matched regions
        self.view.erase_regions('match_regions')


'''
User executes shortcut
    Immediately load viewport text string into memory
    Open up input

User hits two keys
    String search for character pair
        If only 1 match, send cursor
    For each match, display 'jump char' on top of 2nd char
        View.replace()
    Grey out all text except for jump char


User hits valid jump char
    Undo all replaces and highlights
    Move cursor, in command mode, to jump char position
User hits invalid jump char
    Ignore command


TODO
    Ignore text in folded regions
'''
