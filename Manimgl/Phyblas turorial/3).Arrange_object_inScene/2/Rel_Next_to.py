import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text1 = mnm.Text('1')
        text2 = mnm.Text('2')
        text3 = mnm.Text('3')
        text4 = mnm.Text('4')
        text5 = mnm.Text('5')

        text2.next_to(text1,mnm.RIGHT)
        text3.next_to(text2,mnm.UP)
        text4.next_to(text3,mnm.LEFT)
        text5.next_to(text4,mnm.UP)

        self.add(text1,text2,text3,text4,text5)
