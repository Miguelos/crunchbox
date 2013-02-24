from subprocess import call
from os.path import expanduser
from os import listdir

class Sublimetext:

    def __init__(self, base):
        self.base = base

        # This is where this program store its config file(s) in your system.
        user_dir = expanduser("~/.config/sublime-text-2/Packages/User")
        files = listdir(user_dir)
        self.cfg = []
        for elem in files:
            self.cfg.append(expanduser('~/.config/sublime-text-2/Packages/User/' + elem ))
        
        # This is the path to where crunchbox stores all this plugin's cfg
        self.class_name = self.__class__.__name__
        self.plugin_cfg_dir = expanduser('~/.config/crunchbox/configs/' + self.class_name)


    def save(self, profile_name, plugin_obj):
        self.base.save(profile_name, self.class_name, plugin_obj)

    def load(self, profile_name, plugin_obj):
        self.base.load(profile_name, self.class_name, plugin_obj)
        
