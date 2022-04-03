from manim import *

class SineLaw(Scene):
    def construct(self):
        vertixs = [[-3,-2,0],[0,2,0],[2,-2,0]]
        dots = [ Dot(p) for p in vertixs]
        l_ab = Line(dots[0].get_center(),dots[1].get_center())
        l_ac = Line(dots[0].get_center(),dots[2].get_center())
        l_bc = Line(dots[2].get_center(),dots[1].get_center())
        lines = VGroup(l_ab,l_ac,l_bc).set_color(YELLOW_E)
        self.add(lines,dots)
        self.wait(4)