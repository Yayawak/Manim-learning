import manimlib as mnm
import numpy as np
import random as rm

class Manimala(mnm.Scene):
    def construct(self):
        cent = np.array([2,-2,0])
        arc = mnm.Arc(
            np.radians(30),
            np.radians(180),
            radius=4,
            arc_center=cent,
            color='#eeaaaa',
            stroke_width=20
        )
        self.play(
            mnm.Write(arc)
            ,run_time=3
        )
