import manimlib as mnm
import numpy as np
class Manimala(mnm.Scene):
    def construct(self):
        lis_suan = []
        for i in range(40):
            suan = mnm.AnnularSector(inner_radius=0.2*i,
                                     outer_radius=0.1*i,
                                     angle=np.radians(25),
                                     start_angle=np.radians(i*15),
                                     color='#81c9'+str(i**5))
            lis_suan.append(suan)
        vg = mnm.VGroup(*lis_suan)
        self.play(
            mnm.Write(vg),
            run_time=4
        )
