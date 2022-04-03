import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('สไลม์',color='#77aacc',size=2.9)
        text.shift(mnm.UL*2)

        textc = text.copy()
        textc.shift(mnm.RIGHT*5)

        self.add(text,textc)
