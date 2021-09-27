from kivy.app import App
from kivy.uix.widget import Widget


class NoteEditor(Widget):
    pass


class NoteApp(App):
    def build(self):
        return NoteEditor()


if __name__ == '__main__':
    NoteApp().run()