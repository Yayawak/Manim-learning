import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        t1 = mnm.Text('Left',size=3)
        t2 = mnm.Text('Right',size=4)

        vg = mnm.VGroup(t1,t2)
        vg.arrange(mnm.RIGHT)

        self.add(vg)
