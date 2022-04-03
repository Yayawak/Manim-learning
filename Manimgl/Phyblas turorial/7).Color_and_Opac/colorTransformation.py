import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('แดงขึ้น',color='#11ff33',size=4)

        self.play(
#            text.animate.set_color('#ff0000'),
            mnm.FadeToColor(text, '#ff0000'),
            run_time=5
        )
