import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        p1 = np.array([6.5,3,0])
        p2 = np.array([-6.5,-2.5,0])
        senpra = mnm.DashedLine(
            p1,p2,
            dash_length=0.2,
            color='#d4b1f2',
            stroke_width=19
        )
        self.play(
            mnm.Write(senpra),
            run_time=2
        )
