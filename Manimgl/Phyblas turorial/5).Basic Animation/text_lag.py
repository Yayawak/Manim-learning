import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('เมงุมิ',size=4,color='#aaeebb')

        self.play(
            text.animate.shift(mnm.UP*2),
            lag_ratio=0.5,
            run_time=3
        )
