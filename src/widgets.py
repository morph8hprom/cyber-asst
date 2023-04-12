#!/usr/bin/env python3

"""

File used to define classes and logic for the widgets used in main
application

"""

# IMPORT STATEMENTS

from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton

class MenuContainer(MDBoxLayout):
    pass

class MenuButton(MDRectangleFlatButton):
    def __init__(self, **kwargs):
        super(MenuButton, self).__init__(**kwargs)
        #self.ripple_color='black'
        #self.ripple_duration_out=.1
        self.ripple_scale=0

        


class HomeButton(MDFloatingActionButton):
    def __init__(self, **kwargs):
        super(HomeButton, self).__init__(**kwargs)
        self.icon_color='black'
        self.icon_size='36dp'
