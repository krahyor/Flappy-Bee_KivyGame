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

        self.cloud_texture.uvpos =  ((self.cloud_texture.uvpos[0] + time_passed/2.0)%Window.width , self.cloud_texture.uvpos[1])
        texture = self.property('cloud_texture')
        texture.dispatch(self)

        self.floor_texture.uvpos = ((self.floor_texture.uvpos[0] + time_passed)%Window.width,self.floor_texture.uvpos[1])
        texture = self.property('floor_texture')
        texture.dispatch(self)

from random import randint
from kivy.properties import NumericProperty

class Bee(Image):
    velocity = NumericProperty(0)

    def on_touch_down(self, touch):
        self.source = "../Texture/bee2.png"
        self.velocity = 150
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.source = "../Texture/bee1.png"
        super().on_touch_up(touch)


class MainApp(App):
    pipes = []
    GRAVITY = 300
    was_colliding = False

    #def on_start(self):
        #Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/40.)

    def move_bee(self, time_passed):
        bee = self.root.ids.bee
        bee.y = bee.y + bee.velocity * time_passed
        bee.velocity = bee.velocity - self.GRAVITY * time_passed
        self.check_collision()

    def check_collision(self):
        bee = self.root.ids.bee
        #ตรวจสอบว่าชนท่อมั้ย
        is_colliding = False
        for pipe in self.pipes:
            if pipe.collide_widget(bee):
                is_colliding = True
                
                #ตรวจสอบการอยู่ระหว่างท่อ
                if bee.y < (pipe.pipe_center - pipe.GAP_SIZE/2.0):
                    self.game_over()
                if bee.top > (pipe.pipe_center + pipe.GAP_SIZE/2.0):
                    self.game_over() 
        if bee.y < 96:
            self.game_over()
        if bee.top > Window.height:
            self.game_over()
        if self.was_colliding and not is_colliding:
            self.root.ids.score.text = str(int(self.root.ids.score.text)+1)
        self.was_colliding = is_colliding
        

    def game_over(self):
        self.root.ids.bee.pos = (20, (self.root.height - 96) / 2.0)
        for pipe in self.pipes:
            self.root.remove_widget(pipe)
        self.frames.cancel()    
        self.root.ids.start_button.disabled = False
        self.root.ids.start_button.opacity = 1
        

    def next_frame(self, time_passed):
        self.move_bee(time_passed)
        self.move_pipes(time_passed)
        self.root.ids.background.scroll_textures(time_passed)   
    
    def start_game(self):
        self.root.ids.score.text = "0"
        self.was_colliding = False
        #Clock.schedule_interval(self.move_bee, 1/60. )
        self.frames = Clock.schedule_interval(self.next_frame, 1/60.)
        self.pipes = [] 
        #สร้างpipes
        num_pipes = 5
        distance_between_pipes = Window.width/(num_pipes-1)
        for i in range(num_pipes):
            pipe = Pipe()
            pipe.pipe_center = randint(96+100,self.root.height - 100)
            pipe.size_hint = (None,None)
            pipe.pos = (Window.width + i*distance_between_pipes,96)
            pipe.size = (64,self.root.height - 96) 

            self.pipes.append(pipe)
            self.root.add_widget(pipe)
        #move pipes
        #Clock.schedule_interval(self.move_pipes,1/60.)
    
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



