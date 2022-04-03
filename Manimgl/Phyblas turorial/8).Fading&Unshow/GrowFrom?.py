import manimlib as mnm
import numpy as np
class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('Ora-ora-ora' ,size=2.9,color='#d1a88f')
        self.play(
            mnm.GrowFromEdge(text, mnm.DL),
           # mnm.Write(text),
            run_time=5
        )
        self.play(text.animate.set_color_by_gradient('#ff00ff'),
            mnm.FadeOutToPoint(text,np.array([3,0,0]))
        )
