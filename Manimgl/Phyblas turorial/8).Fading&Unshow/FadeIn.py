import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('มาแล้ว',size=6.2,color='#93b8d4')
        self.play(
            text.animate.set_color_by_gradient('#ff0000','#00ff00'),
            mnm.FadeIn(text),
            run_time=3,
        )
