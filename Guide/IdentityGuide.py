from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
class MyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #mainmenu = Image(source="MainMenu.png", size=(100,100))
        txt = Label(text="Sticman Run")
        version = Label(text="v0.0")
        start = Button(text = " ", background_normal="MainMenu.jpg")
        self.box = BoxLayout(orientation="vertical",spacing=8)
        #self.box.add_widget(txt)
        #self.box.add_widget(version)
        self.box.add_widget(start)
        self.add_widget(self.box)
        #self.add_widget(mainmenu)
        start.on_press = self.StartPressed
        

    def StartPressed(self):
        self.manager.current = "game"

class MyScreen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(rgba=(.5, .5, .5))
            Rectangle(size=(1000,1000), pos=self.pos)
        Book1 = Image(source="Book1.jpg")
        self.box = BoxLayout()
        self.box.add_widget(Book1)
        self.add_widget(self.box)
        Window.bind(on_touch_down =self.mouse_pos)

    def mouse_pos(self, window, pos):
        self.ax = (pos.pos[0])
        self.ay = (pos.pos[1])
        print(self.ax)
        print(self.ay)
        #print(pos.pos[1])
        if self.ax < 227 and self.ax > 171:
            if self.ay > 367 and self.ay < 491:
                self.manager.current = "doctor"


class MyScreen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(rgba=(.5, .5, .5))
            Rectangle(size=(1000,1000), pos=self.pos)
        Book1 = Image(source="doctor.jpg")
        self.box = BoxLayout()
        self.box.add_widget(Book1)
        self.add_widget(self.box)

class MyScreen4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(rgba=(.5, .5, .5))
            Rectangle(size=(1000,1000), pos=self.pos)
        Book1 = Image(source="Book1.jpg")
        self.box = BoxLayout()
        self.box.add_widget(Book1)
        self.add_widget(self.box)

class MyScreen5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(rgba=(.5, .5, .5))
            Rectangle(size=(1000,1000), pos=self.pos)
        Book1 = Image(source="Book1.jpg")
        self.box = BoxLayout()
        self.box.add_widget(Book1)
        self.add_widget(self.box)

class MyScreen6(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(rgba=(.5, .5, .5))
            Rectangle(size=(1000,1000), pos=self.pos)
        Book1 = Image(source="Book1.jpg")
        self.box = BoxLayout()
        self.box.add_widget(Book1)
        self.add_widget(self.box)

class MyScreen7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(rgba=(.5, .5, .5))
            Rectangle(size=(1000,1000), pos=self.pos)
        Book1 = Image(source="Book1.jpg")
        self.box = BoxLayout()
        self.box.add_widget(Book1)
        self.add_widget(self.box)

class MyApp(App):
    def build(self):
        #self.clearcolor = (0, 0, 0, 1)
        sm = ScreenManager()
        scr1 = MyScreen(name="scr")
        scr2 = MyScreen2(name="game")
        scr3 = MyScreen3(name="doctor")
        sm.add_widget(scr1)
        sm.add_widget(scr2)
        sm.add_widget(scr3)
        return sm
        self.manager.current = "scr"

app = MyApp()
app.run()