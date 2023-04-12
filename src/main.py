#!/usr/bin/env python3

"""

Cointains classes and logic for main application

"""

# IMPORT STATEMENTS

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from screens import * 
from widgets import *
from kivy.lang import Builder


# CLASS DEFINITIONS

# Define screenmanager class
class WindowManager(MDScreenManager):
    """

    Inherits from MDScreenmanager.  Used to manage screens in main
    application
    
    """
    pass

class MainApp(MDApp):
    def build(self):
        # Set primary theme to Dark
        self.theme_cls.theme_style = "Dark"
        # Create instance of WindowManager class
        app = WindowManager()
        # Add instance of MainScreen to ScreenManager instance
        app.add_widget(MainScreen())
        app.add_widget(CharacterScreen())
        return app


def main():
    MainApp().run()


if __name__ == '__main__':
    main()
