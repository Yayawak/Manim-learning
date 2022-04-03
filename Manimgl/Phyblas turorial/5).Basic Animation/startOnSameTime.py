import manimlib as mnm

class Manimala(mnm.Scene):

    def construct(self):
        text1 = mnm.Text('แมงมุมบน',size=3.5)
        text2 = mnm.Text('แมงมุมล่าง',size=3)

        self.play(
            text1.animate.shift(mnm.UP*2),
            text2.animate.shift(mnm.DL*3),
            run_time=1.5
        )
