import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        lis_suan = []
        for i in range(24):
            suan = mnm.Sector(outer_radius=3.7,
                              angle=np.radians(12),
                              start_angle=np.radians(i*15),
                              color='#ef9ddf')
            lis_suan.append(suan)
        vg = mnm.VGroup(*lis_suan)
        self.play(
            mnm.Write(vg),
            run_time=1.5
        )

