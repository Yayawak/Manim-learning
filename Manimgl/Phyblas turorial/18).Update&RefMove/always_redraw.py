import manimlib as mnm
import numpy as np
from numpy.core.defchararray import add
from numpy.core.fromnumeric import size

class Manimala(mnm.Scene):
    def construct(self):
        circ = mnm.Circle(arc_center=np.array([-4,-2,0]),radius=0.5)

        # def addXPos(m):
        #     return mnm.Text(f'x = {m.get_x():.1f}',size=3)
        # xPos = mnm.always_redraw(addXPos, circ)
        xPos = mnm.always_redraw(
            lambda m:mnm.Text(f'x = {m.get_x():.1f}',size=3)
            ,circ
        )
        self.add(xPos)
        self.play(
            circ.animate.shift(mnm.RIGHT*20),
            run_time=2
        )

class XYPos_by_always_redraw(mnm.Scene):
    def construct(self):
        dot = mnm.Dot(np.array([2,-2,0]),radius=1)

        def addPos(m):
            x,y = m.get_x(),m.get_y()
            text = mnm.Text(f'x = {x:.1f}, y = {y:.1f}')

            if(x<0):
                text.set_color('#d6baf3')
            else:
                text.set_color('#c67982')
            text.next_to(dot,mnm.UP) if y<0 else text.next_to(dot,mnm.DOWN)

            return text
        
        PosTxt = mnm.always_redraw(addPos,dot)
        self.add(PosTxt)
        self.play(
            dot.animate.move_to([-2,2,0]),
            run_time=2
        )