import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text1 = mnm.Text('แมงมุม',size=3.2,color='#ffddff')
        text2 = mnm.Text('เมฆ',size=4.2,color='#ffffdd')
        text3 = mnm.Text('คุโมะ',size=3.7,color='#ddffff')
        vg = mnm.VGroup(text1,text2,text3)
        vg.arrange(mnm.DOWN)

        self.play(
            mnm.AnimationGroup(
                text1.animate.shift(mnm.DL*3),runtime=4
            ),
            mnm.AnimationGroup(
                text2.animate.shift(mnm.UR*3),runtime=2
            ),
            mnm.AnimationGroup(
                text3.animate.shift(mnm.RIGHT*2),runtime=1
            ),
        )
