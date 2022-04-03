import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text1 = mnm.Text('ยาดอน',color='#ff9ada',size=4)
        text2 = mnm.Text('ยาโดรัน',color='#c09aff',size=4)
        text3 = mnm.Text('ยาโดคิง',color='#ff9ab9',size=4)
        text4 = mnm.Text('คิงดรา',color='#9ac2ff',size=4)
        self.wait()
        self.play(
            mnm.TransformMatchingShapes(text1,text2)
        )
        self.play(
            mnm.TransformMatchingShapes(text2,text3),
            run_time=1
        )
        self.play(
            mnm.TransformMatchingShapes(text3,text4),
            run_time=1
        )
