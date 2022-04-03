import manimlib as mnm

class Arifureta(mnm.Scene):
    def construct(self):
        text = mnm.Text('อาชีะกระจอก\nแล้วทำไม\nยังไไงข้าก็เทพ',size=1.6,color='#db266e')
        self.play(mnm.Write(text), run_time=5)

class Mushoku(mnm.Scene):
    def construct(self):
                        text = mnm.Text('เกิดขาินี้พี่ต้องเทพ',size=3.3,color="317b8d")
                        self.play(mnm.Write(text), run_time=1.8)
