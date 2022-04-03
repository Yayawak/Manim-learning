import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('วาดขอบ\n\nแล้วเติม',size=3.2,color='#f4c1b4')
        self.play(
            mnm.DrawBorderThenFill(text),
            run_time=4.5
        )
