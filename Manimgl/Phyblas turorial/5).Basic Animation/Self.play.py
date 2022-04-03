import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        t = mnm.Text('Nani!!!',size=2.5)
        ####!!! NO NEED SELF.ADD() ANYMORE
        self.play(
            t.animate.shift([3,4,0]),
            run_time=2

        )
        text = mnm.Text('แมงมุม\n\nเข้ามุมขวาล่าง',size=2.4)
        self.play(
            mnm.ApplyMethod(text.shift,mnm.DOWN*1.2+mnm.RIGHT*1.5),
            run_time=1.5
        )
