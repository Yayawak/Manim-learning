import manimlib as mnm
import numpy as np

class NoTextButGoDecnum(mnm.Scene):
    def construct(self):
        num = mnm.DecimalNumber(99.99,
        num_decimal_place=3,
        include_sign=True,
        edge_to_fix=mnm.RIGHT,
        font_size=200)

        self.add(num)
        self.play(
            num.animate.set_value(-3.534),
            run_time=2
        )
        
class DecNum_Update(mnm.Scene):
    def construct(self):
        dot = mnm.Dot(np.array([-3,2,0]),radius=.5)
        num = mnm.DecimalNumber(0,num_decimal_place=4,font_size=140)
        num.add_updater(lambda m: num.set_value(dot.get_x()))
        self.add(num)
        self.play(
            dot.animate.shift(mnm.RIGHT*8),
            run_time=2
        )
        
class Move_tellPos_byDecNum(mnm.Scene):
    def construct(self):
        dot = mnm.Dot(np.array([-1,0,0]))
        Pos = mnm.VGroup(
            mnm.Text('x='),
            mnm.DecimalNumber(0,include_sign=True),
            mnm.Text('y='),
            mnm.DecimalNumber(0,include_sign=True)
        )
        Pos.arrange(mnm.RIGHT)
        Pos.next_to(dot,mnm.UP)
        
        def setPos(m):
            m.next_to(dot,mnm.UP)
            m[1].set_value(dot.get_x())
            m[3].set_value(dot.get_y())
            
        Pos.add_updater(setPos)
        self.add(Pos)
        self.play(dot.animate.shift(mnm.DR*4),run_time=2)