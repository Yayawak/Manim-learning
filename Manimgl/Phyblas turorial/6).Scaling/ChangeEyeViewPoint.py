import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        text1 = mnm.Text('ขยายไปทางขวาล่าง',color='#d3a3ef')
        text2 = mnm.Text('ยืดไปทางซ้าย',color='#efd3a3')

        self.play(
            text1.animate.scale(2,about_point=np.array([-3,1,0])),
            text2.animate.stretch(3,0,about_point=np.array([3,1,0])),
            run_time=3
        )
