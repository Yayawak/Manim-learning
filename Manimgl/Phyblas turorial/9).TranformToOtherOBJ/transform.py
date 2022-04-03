import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text1 = mnm.Text('พีคาชู',color='#88ffbb',size=3)
        text2 = mnm.Text('ไรชู',color='#bb88ff',size=3)

        self.play(
            mnm.Transform(text1,text2),
            run_time=4
        )
