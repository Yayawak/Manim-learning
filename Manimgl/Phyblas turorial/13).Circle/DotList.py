import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        list_chut = []
        for i in range(15):
            pos = np.array([(i-10)/2,(i-9)/3,0])
            r = 0.1+0.02*i**2
            chut = mnm.Dot(pos,radius=r,color='#ff00ff')
            list_chut.append(chut)

        vg = mnm.VGroup(*list_chut)
        self.play(
            mnm.Write(vg),

            run_time=3
        )
