import manimlib as mnm

class Manila(mnm.Scene):
    def construct(self):
        t1 = mnm.Text('a')
        t2 = mnm.Text('b')
        t3 = mnm.Text('c')
        t4 = mnm.Text('d')
        t5 = mnm.Text('e')

        t1.shift(mnm.RIGHT * 6)
        t2.shift(mnm.UP*3)
        t3.shift(mnm.LEFT*3+mnm.DOWN*7)
        t4.shift([3,-5,0])

        self.add(t1,t2,t3,t4,t5)
