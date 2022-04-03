import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        t1 = mnm.Text('a',color='#e0afdd')
        t1.set_x(5)

        t2 = mnm.Text('b',color='#afd3e0')
        t2.set_y(2)

        t3 = mnm.Text('c',color='#b5e0af')
        t3.move_to(np.array([-5,2,0]))

        t4 = mnm.Text('d',color='#e0c9af')

        self.add(t1,t2,t3,t4)
