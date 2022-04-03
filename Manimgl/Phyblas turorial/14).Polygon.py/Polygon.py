import manimlib as mnm
import numpy as np

class Ngon(mnm.Scene):
    def construct(self):
        p1 = np.array([2,-2,0])
        p2 = np.array([-2,-2,0])
        p3 = np.array([0,2,0])

        trig = mnm.Polygon(
            p1,p2,p3,
            fill_color='#6644ff',
            fill_opacity=1,
            color='#ffaaaa',
            stroke_width=12
        )
        self.play(
            mnm.Write(trig),
            run_time=3
        )
        self.play(
            mnm.ShrinkToCenter(trig)
        )
class RoundCorner(mnm.Scene):
    def construct(self):
        samliam = mnm.Polygon(np.array([6,-2,0]),
                              np.array([-6.5,-3,0]),
                              np.array([1,3,0]),
                              fill_color='#893e7c',
                              fill_opacity=1,
                              color='#d7bae8')
        self.play(

            mnm.Write(samliam)
            ,run_time=2
        )
        self.play(
            samliam.animate.round_corners(0.9),
            run_time=4
        )

class Square(mnm.Scene):
    def construct(self):
        list_sq = []
        for i in range(11):
            sq = mnm.Square(
                (2+i)/8,
                fill_color='#72c7d6',
                fill_opacity=0.8
            )
            list_sq.append(sq)
        vg = mnm.VGroup(*list_sq)
        vg.arrange(mnm.LEFT)
        self.play(
            mnm.Write(vg),run_time=4
        )
class RegularPolygon(mnm.Scene):
    def construct(self):
        list = []
        for i in range(8):
            nGon = mnm.RegularPolygon(3+i,
                                         fill_color='#d672b6',
                                         fill_opacity=1-0.1*i,
                                            start_angle=np.radians(15*i))
            list.append(nGon)
        vg = mnm.VGroup(*list)
        vg.arrange_in_grid(n_cols=4)
        self.play(
            mnm.Write(vg),
            run_time=3
        )
