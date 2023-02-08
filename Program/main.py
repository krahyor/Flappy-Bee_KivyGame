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

from random import randint



class MainApp(App):
    pipes = []
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/40.)

    def start_game(self):
        self.pipes = [] 
        #สร้างpipes
        num_pipes = 5
        distance_between_pipes = Window.width/(num_pipes-1)
        for i in range(num_pipes):
            pipe = Pipe()
            pipe.pipe_center = randint(96+100,self.root.height - 100)
            pipe.size_hint = (None,None)
            pipe.pos = (i*distance_between_pipes,96)
            pipe.size = (64,self.root.height - 96)

            self.pipes.append(pipe)
            self.root.add_widget(pipe)
        #move pipes
        Clock.schedule_interval(self.move_pipes,1/60.)
    
    def move_pipes(self, time_passed):
        #move pipes
        for pipe in self.pipes:
            pipe.x -= time_passed * 100

        #Check if we need to reposition the pipe at the right side
        num_pipes = 5
        distance_between_pipes = Window.width / (num_pipes - 1)
        pipe_xs = list(map(lambda pipe: pipe.x, self.pipes))
        right_most_x = max(pipe_xs)
        if right_most_x <= Window.width - distance_between_pipes:
            most_left_pipe = self.pipes[pipe_xs.index(min(pipe_xs))]
            most_left_pipe.x = Window.width 
        


MainApp().run()



