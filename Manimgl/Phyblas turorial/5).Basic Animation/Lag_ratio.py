import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        m1 = mnm.Triangle(color='#22bbbb')
        m2 = mnm.Square(color='#cc7777')
        m3 = mnm.Circle(color='#bbee33')
        vg = mnm.VGroup(m1,m2,m3)

        self.play(
            vg.animate.shift(mnm.LEFT*3),
            lag_ratio=0.5,
            run_time=4
        )
