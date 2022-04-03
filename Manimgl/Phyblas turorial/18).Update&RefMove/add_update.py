import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        dot = mnm.Dot(np.array([-2,-1,0]),radius=1)
        txt = mnm.Text('Hear',size=2)
        txt.add_updater(lambda m:txt.next_to(dot,mnm.LEFT))

        self.add(txt)
        self.play(
            mnm.Rotate(dot,np.radians(-120),about_point=np.array([1,-1,0])),
            run_time=2
        )
    