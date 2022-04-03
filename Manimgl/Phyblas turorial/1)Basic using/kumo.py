import manimlib as mnm

class Kumodesuga(mnm.Scene):
    def construct(self):
        text = mnm.Text('แมงมุมแล้วไง\n\nข้องใจเหรอคะ',size=2.5,color='#dad1e2')
        self.play(mnm.Write(text), run_time=2)
