import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        vg = mnm.VGroup(
            mnm.Text('ก',size=2),
            mnm.Text('ข',size=2.3),
            mnm.Text('ค',size=2.6),
            mnm.Text('ง',size=2.9),
            mnm.Text('จ',size=3.2),
            mnm.Text('ช',size=3.5),
            mnm.Text('ญ',size=3.8),
        )
        vg.arrange_in_grid(n_cols=3,buff=0.5)

        self.add(vg)
