import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('ไล่สีจากแดง\n\nไปเขียว',color='#000033',size=3)

        self.play(
            text.animate.set_color_by_gradient('#ff0000','#00ff00'),
            run_time=4,
            lag_ratio=0.9
        )
