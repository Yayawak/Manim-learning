import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text1 = mnm.Text('๑',color='#d1afe6',size=7)
        text2 = mnm.Text('๒',color='#afe6d7',size=7)
        text3 = mnm.Text('๓',color='#d3e6af',size=7)
        vg = mnm.VGroup(text1,text2,text3)
        vg.arrange(mnm.RIGHT)

        for i in range(10):
            self.play(
                mnm.CyclicReplace(text1,text2,text3),
                run_time=0.2
            )
