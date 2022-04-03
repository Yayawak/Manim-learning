import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text1 = mnm.Text('แดงกลายเป็นฟ้า',size=2,color='#ff3333')
        text2 = mnm.Text('ฟ้า',size=4,color='#33ffff')
        vg = mnm.VGroup(text1,text2)
        vg.arrange(mnm.UP)

        self.add(vg)
        self.play(
            text1.animate.match_color(text2),
            lag_ratio=0.9,
            run_time=3
        )
