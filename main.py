from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window #import window

class Background(Widget):
    cloud_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cloud_texture = Image(source="cloud.png").texture # เพิ่มรูป
        self.cloud_texture.wrap = 'repeat' #เป็นการทำซ้ำ
        self.cloud_texture.uvsize = (Window.width/self.cloud_texture.width,-1) # บอกขนาด


    pass

class MainApp(App):
    pass

MainApp().run()