from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout

class MyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        start = Button(text = " ", background_normal="MainMenu.jpg")
        self.box = BoxLayout(orientation="vertical",spacing=8)
        self.box.add_widget(start)
        self.add_widget(self.box)
        start.on_press = self.StartPressed

    def StartPressed(self):
        self.manager.transition.duration = 0.5
        self.manager.transition.direction = "left"
        self.manager.current = "game"

class Book(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Book1 = Image(source="Book1.jpg")
        DoctorButton = Button(text=" ",pos_hint={"x":.23, "y":.65},size_hint=(0.07,0.14))
        self.Exit = Button(text=" ",pos_hint={"x":.08, "y":.78},size_hint=(0.052,0.09))
        self.add_widget(DoctorButton)
        self.add_widget(self.Exit)
        self.add_widget(Book1)
        DoctorButton.on_release = self.DoctorPressed
        self.Exit.on_release = self.ExitPressed

    def DoctorPressed(self):
        self.manager.transition.duration = 0.5
        self.manager.transition.direction = "left"
        self.manager.current = "doctor"

    def ExitPressed(self):
        self.manager.transition.duration = 0.5
        self.manager.transition.direction = "right"
        self.manager.current = "scr"

class Doctor(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Book1 = Image(source="doctor.jpg")
        DoctorTrait1 = Button(text=" ",pos_hint={"x":.532, "y":.70},size_hint=(0.052,0.09))
        DoctorTrait2 = Button(text=" ",pos_hint={"x":.595, "y":.70},size_hint=(0.052,0.09))
        DoctorTrait3 = Button(text=" ",pos_hint={"x":.652, "y":.70},size_hint=(0.054,0.09))
        DoctorTrait4 = Button(text=" ",pos_hint={"x":.715, "y":.70},size_hint=(0.052,0.09))
        self.Exit = Button(text=" ",pos_hint={"x":.08, "y":.78},size_hint=(0.052,0.09))
        self.add_widget(self.Exit)
        self.add_widget(DoctorTrait1)
        self.add_widget(DoctorTrait2)
        self.add_widget(DoctorTrait3)
        self.add_widget(DoctorTrait4)
        self.add_widget(Book1)
        DoctorTrait1.on_press = self.DoctorTrait1Pressed
        DoctorTrait1.on_touch_up = self.DoctorTrait1Released
        DoctorTrait2.on_press = self.DoctorTrait2Pressed
        DoctorTrait2.on_touch_up = self.DoctorTrait2Released
        DoctorTrait3.on_press = self.DoctorTrait3Pressed
        DoctorTrait3.on_touch_up = self.DoctorTrait3Released
        DoctorTrait4.on_press = self.DoctorTrait4Pressed
        DoctorTrait4.on_touch_up = self.DoctorTrait4Released
        self.Exit.on_release = self.ExitPressed

    def DoctorTrait1Pressed(self):
        self.manager.transition.duration = 0
        self.manager.current = "DoctorTrait1"

    def DoctorTrait1Released(self, touch):
        self.manager.current = "doctor"

    def DoctorTrait2Pressed(self):
        self.manager.transition.duration = 0
        self.manager.current = "DoctorTrait2"

    def DoctorTrait2Released(self, touch):
        self.manager.current = "doctor"

    def DoctorTrait3Pressed(self):
        self.manager.transition.duration = 0
        self.manager.current = "DoctorTrait3"

    def DoctorTrait3Released(self, touch):
        self.manager.current = "doctor"

    def DoctorTrait4Pressed(self):
        self.manager.transition.duration = 0
        self.manager.current = "DoctorTrait4"

    def DoctorTrait4Released(self, touch):
        self.manager.current = "doctor"

    def ExitPressed(self):
        self.manager.transition.duration = 0.5
        self.manager.transition.direction = "right"
        self.manager.current = "game"

class DoctorTrait1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Book1 = Image(source="DoctorTrait1.jpg")
        self.box = BoxLayout()
        self.box.add_widget(Book1)
        self.add_widget(self.box)

class DoctorTrait2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Book1 = Image(source="DoctorTrait2.jpg")
        self.box = BoxLayout()
        self.box.add_widget(Book1)
        self.add_widget(self.box)

class DoctorTrait3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Book1 = Image(source="DoctorTrait3.jpg")
        self.box = BoxLayout()
        self.box.add_widget(Book1)
        self.add_widget(self.box)

class DoctorTrait4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Book1 = Image(source="DoctorTrait4.jpg")
        self.box = BoxLayout()
        self.box.add_widget(Book1)
        self.add_widget(self.box)

class MyApp(App):
    def build(self): 
        sm = ScreenManager()
        scr1 = MyScreen(name="scr")
        Book1 = Book(name="game")
        Doctor1 = Doctor(name="doctor")
        DoctorTrait11 = DoctorTrait1(name="DoctorTrait1")
        DoctorTrait22 = DoctorTrait2(name="DoctorTrait2")
        DoctorTrait33 = DoctorTrait3(name="DoctorTrait3")
        DoctorTrait44 = DoctorTrait4(name="DoctorTrait4")
        sm.add_widget(scr1)
        sm.add_widget(Book1)
        sm.add_widget(Doctor1)
        sm.add_widget(DoctorTrait11)
        sm.add_widget(DoctorTrait22)
        sm.add_widget(DoctorTrait33)
        sm.add_widget(DoctorTrait44)
        return sm
        self.manager.current = "scr"

app = MyApp()
app.run()