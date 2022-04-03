import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        t = mnm.Text('ขยายยยย',color='#EE7733')
        self.play(
            t.animate.scale(4),
            lag_ratio=0.8,
            run_time=3
        )
        self.play(
            t.animate.scale(0.5),
            #t.animate.flip(),
            lag_ratio=0.1,
            run_time=2
        )
