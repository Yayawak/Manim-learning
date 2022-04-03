import manimlib as mnm
from numpy.core.fromnumeric import size

class Manimala(mnm.Scene):
    def construct(self):
        tex = mnm.Tex('7-x','+','3i+yi',font_size=190)
        brace = mnm.Brace(tex, mnm.UP)
        text = mnm.Text('complex number',size=1.6)
        text.next_to(brace,mnm.UP)

        self.add(tex)
        self.play(
            mnm.ClockwiseTransform(tex.copy(),brace),
            mnm.Write(text),
            run_time=1.5
        )