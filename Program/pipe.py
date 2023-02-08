from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class Pipe(Widget):
    GAP_SIZE = NumericProperty(60)
    CAP_SIZE = NumericProperty(0)          # ความสูงของหัวท่อ
    bottom_body_position = NumericProperty(0)
    bottom_cap_position = NumericProperty(0)
    top_body_position = NumericProperty(0)
    top_cap_position = NumericProperty(0)
    
    #Texture
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        