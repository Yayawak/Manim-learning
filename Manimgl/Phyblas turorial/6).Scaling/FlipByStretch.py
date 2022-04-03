import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text1 = mnm.Text('พลิกแนวนอน',color='#d3e3fa',size=3)
        text2 = mnm.Text('พลิกแนวตั้ง',color='#bffaa3',size=3)

        self.play(
            text1.animate.stretch(-1,0),
            text2.animate.stretch(-1,-1),
            run_time=3
        )
