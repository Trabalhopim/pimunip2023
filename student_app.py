from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.toolbar import MDToolbar


KV = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        id: toolbar
        title: 'Sistema de Notas'
        left_action_items: [['menu', lambda x: app.menu.open()]]

    MDLabel:
        text: ''
        id: content_label
        halign: 'center'
        valign: 'middle'
'''

class StudentApp(MDApp):
    content_label = None
    toolbar = None

    def build(self):
        self.root = Builder.load_string(KV)
        self.content_label = self.root.ids.content_label
        self.toolbar = self.root.ids.toolbar  # Atribua a toolbar a uma variável
        self.menu = self.create_menu()
        return self.root

    def create_menu(self):
        menu = MDDropdownMenu(caller=self.toolbar, items=[
            {"text": "Notas", "viewclass": "OneLineListItem", "on_release": self.view_notes},
            {"text": "Disciplinas", "viewclass": "OneLineListItem", "on_release": self.view_disciplines},
            {"text": "Faltas", "viewclass": "OneLineListItem", "on_release": self.view_faltas},
        ])
        return menu

    def view_notes(self, *args):
        self.content_label.text = "Aqui estão as notas."

    def view_disciplines(self, *args):
        self.content_label.text = "Aqui estão as disciplinas."

    def view_faltas(self, *args):
        self.content_label.text = "Aqui estão as faltas."

if __name__ == '__main__':
    StudentApp().run()
