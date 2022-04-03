import manimlib as mnm
import numpy as np

class Arrow(mnm.Scene):
    def construct(self):
        p1 = np.array([-6,0,0])
        p2 = np.array([6,0,0])
        ar = mnm.Arrow(
            p1,p2,fill_color='#efa5c4'
        )
        self.add(
            mnm.Dot(p1),mnm.Dot(p2)
        )
        self.play(
            mnm.Write(ar),
            run_time=3
        )
class ArrowComprehensiveList(mnm.Scene):
    def construct(self):
        p1 = np.array([-6,0,0])
        p2 = np.array([6,0,0])
        arrow = mnm.VGroup(*[mnm.Arrow(p1,p2,buff=i*0.1,fill_color='#a76fe0') for i in range(11)])
        arrow.arrange(mnm.UP) #this will arrange from overlap line to be arraged properly
        self.play(
            mnm.Write(arrow),
            run_time=3
        )


class ChangeHeadArrow(mnm.Scene):
    def construct(self):
        p1 = np.array([-4,-3,0])
        p2 = np.array([4,3,0])
        p3 = np.array([3,-2,0])
        arr = mnm.Arrow(p1,p2,buff=0,fill_color='#c4efa5')

        self.add(
            mnm.Dot(p1),mnm.Dot(p2),mnm.Dot(p3)
        )
        self.play(
            arr.animate.set_points_by_ends(p1,p3),
            run_time=3
        )
