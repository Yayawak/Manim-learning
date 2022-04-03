import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('แสดงการสร้าง',size=3.2,color='#969ec9')
        self.play(
            mnm.ShowCreation(text),
            run_time=4
        )
        self.play(
            mnm.Uncreate(text),
            run_time=2
        )
