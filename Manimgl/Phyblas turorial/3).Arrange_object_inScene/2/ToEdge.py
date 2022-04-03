import manimlib as mnm

class Malacore(mnm.Scene):
    def construct(self):
        t1 = mnm.Text('alibaba')
        t2 = mnm.Text('Alohadance')

        t1.to_edge(mnm.UP)
        t2.to_edge(mnm.DOWN)

        self.add(t1,t2)
