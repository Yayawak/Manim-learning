import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        p1 = np.array([-5,3,0])
        p2 = np.array([6,-2,0])

        l = mnm.Line(p1,p2)
        self.play(
            mnm.Write(l),
            run_time=3
        )

