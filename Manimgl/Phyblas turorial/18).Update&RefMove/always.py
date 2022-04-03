import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        rect = mnm.Rectangle(7,3)
        text = mnm.Text('Rectagle')
        mnm.always(text.next_to,rect,mnm.UP)
        self.add(text)
        self.play(
            mnm.FadeOutToPoint(rect,np.array([-3,-3,0]),run_time=2)
        )