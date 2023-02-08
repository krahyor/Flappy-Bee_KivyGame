from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image

class Pipe(Widget):
    GAP_SIZE = NumericProperty(60)
    CAP_SIZE = NumericProperty(20) #ความสูงหัวท่อ
    pipe_center = NumericProperty(0)
    bottom_body_position = NumericProperty(0)
    bottom_cap_position = NumericProperty(0)
    top_body_position = NumericProperty(0)
    top_cap_position = NumericProperty(0)

    pipe_body_texture = ObjectProperty(None)
    lower_pipe_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))
    top_pipe_tex_coords = ListProperty((0, 0, 1, 0, 1, 1, 0, 1))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pipe_body_texture = Image(source='../Texture/pipe_body.png').texture
        self.pipe_body_texture.wrap = 'repeat'