from manim import *

class A(Scene):
    def construct(self):
        circle = Circle()                   # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        
        sqr = Square()
        sqr.flip(RIGHT)
        sqr.rotate(-3*TAU/8)
        
        
        self.play(Create(sqr))     # show the circle on screen
        self.play(Transform(sqr,circle))
        self.play(FadeOut(sqr))
        
import manim as mn
class B(mn.Scene):
    def construct(self):
        sqr = Square().set_fill(mn.RED,opacity=1)
        self.add(sqr)
        
        # change color
        self.play(ApplyMethod(sqr.set_fill,mn.WHITE))
        
        self.play(ApplyMethod(sqr.shift,mn.UP))
        
class C(mn.Scene):
    def construct(self):
        p1 = [-1,-1,0]
        p2 = [1,-1,0]
        p3 = [1,1,0]
        p4 = [-1,1,0]
        a = Line(p1,p2).append_points(Line(p2,p3).get_points()).append_points(Line(p3,p4).get_points())
        point_start= a.get_start()
        point_end  = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}").scale(0.5).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}").scale(0.5).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}").scale(0.5).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.get_points()])
        self.add(a)