import manimlib as mnm

class AAAAA(mnm.Scene):
    def construct(self):
        t1 = mnm.Text('a')
        t2 = mnm.Text('b')
        t3 = mnm.Text('c')

        t2.next_to(t2,mnm.LEFT,buff=3)
        t3.next_to(t2,mnm.UP,buff=-5)

        self.add(t1,t2,t3)
