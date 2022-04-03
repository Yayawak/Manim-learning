import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        #old
        p2 = np.array([+4,-4,0])
        p1 = np.array([-2,2,0])
        #new
        p3 = np.array([7,0,0])
        p4 = np.array([-5,-3,0])

        l = mnm.Line(p1,p2)
        self.play(
            mnm.Write(l),
            run_time=2
        )
        self.play(
            l.animate.set_points_by_ends(p3,p4),
            run_time=3

        )
        self.play(
            l.animate.set_stroke(width=70,
                                   color='#b86fe7',
                                   opacity=1),

        )
