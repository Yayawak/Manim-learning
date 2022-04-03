import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        c = mnm.Circle(arc_center=np.array([3,0,0])
            ,radius=3
            ,strokr_width=12,color='#aaffaa')
        self.play(
            mnm.Write(c),
            run_time=3
        )
