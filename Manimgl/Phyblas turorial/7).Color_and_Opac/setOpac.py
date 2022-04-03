import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('เลือนราง\n\nจนเกือบหายไป',color='#d8d9ff',size=3)
        self.add(text)

        self.play(
            text.animate.set_opacity(0.1),
            run_time=3,
            lag_ratio=0.5
        )
