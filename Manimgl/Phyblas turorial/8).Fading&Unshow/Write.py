import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('เขียนนนนน\ndfksjdfkd\nsdfsdgdfhhน',size=2,color='#cba7ec')
        self.play(
            mnm.Write(text),
            run_time=3,
        )
