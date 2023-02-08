from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window #import window
from kivy.clock import Clock

from pipe import Pipe

class Background(Widget):
    cloud_texture = ObjectProperty(None)
    floor_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cloud_texture = Image(source="../Texture/cloud.png").texture # เพิ่มรูป
        self.cloud_texture.wrap = 'repeat' #เป็นการทำซ้ำ
        self.cloud_texture.uvsize = (Window.width/self.cloud_texture.width,-1) # บอกขนาด

        self.floor_texture = Image(source="../Texture/floor.png").texture
        self.floor_texture.wrap = 'repeat'
        self.floor_texture.uvsize = (Window.width / self.floor_texture.width, -1)

    def scroll_textures(self,time_passed):

        self.cloud_texture.uvpos =  ((self.cloud_texture.uvpos[0] + time_passed/2)%Window.width , self.cloud_texture.uvpos[1])
        texture = self.property('cloud_texture')
        texture.dispatch(self)

        self.floor_texture.uvpos = ((self.floor_texture.uvpos[0] + time_passed*3)%Window.width,self.floor_texture.uvpos[1])
        texture = self.property('floor_texture')
        texture.dispatch(self)
    pass



class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/40.)

MainApp().run()



