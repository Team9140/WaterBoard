#!/usr/bin/env python3
import kivy, robotpy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Network:
  def getIP(team):
    team = str(team)
    return f'10.{team[:2]}.{team[2:]}.2'

class SettingsManager(App):
  class View(GridLayout):
    class Left(GridLayout):
      def __init__(self, **kwargs):
        super(SettingsManager.View.Left, self).__init__(**kwargs)
        self.cols = 2
        self.reset = Button(text='Load Defaults')
        self.add_widget(self.reset)

    class Right(GridLayout):
      def __init__(self, **kwargs):
        super(SettingsManager.View.Right, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Team:'))
        self.team = TextInput(text='0')
        self.add_widget(self.team)


    def __init__(self, **kwargs):
      super(SettingsManager.View, self).__init__(**kwargs)
      self.cols = 2
      self.add_widget(SettingsManager.View.Left())
      self.add_widget(SettingsManager.View.Right())
      # self.add_widget(Label(text=''))
      # self.save = Button(text='Save')
      # self.add_widget(self.save)

  def build(self):
    return SettingsManager.View()

try:
  SettingsManager().run()
except KeyboardInterrupt:
  pass
