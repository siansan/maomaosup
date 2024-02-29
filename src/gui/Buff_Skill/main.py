"""Displays the current minimap as well as various information regarding the current routine."""

import tkinter as tk
from src.gui.Buff_Skill.Buff_Skill import Buff_Skill
from src.gui.interfaces import Tab


class Buff_(Tab):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, '輔助技能', **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.Buff_Skill = Buff_Skill(self)
        self.Buff_Skill.grid(row=0, column=2, sticky=tk.NSEW, padx=10, pady=10)
