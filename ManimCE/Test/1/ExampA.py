from logging import logMultiprocessing
from math import degrees, log
from typing_extensions import runtime
from manim import *
from numpy import array, dot

class ManimLogo(Scene):
    def construct(self):
        self.camera.background_color = '#ece6e2'
        logo_green = '#87c2a5'
        logo_blue = '#525893'
        logo_red = '#e07a5f'
        logo_black = '#343434'
        M = MathTex(r'\mathbb{M}',fill_color=logo_black).scale(7)
        M.shift(2.25*LEFT+1.5*UP)
        circ = Circle(color=logo_green,fill_opacity=1).shift(LEFT)
        sqr = Square(color=logo_blue,fill_opacity=1).shift(UP)
        trig = Triangle(color=logo_red,fill_opacity=1).shift(RIGHT)
        logo = VGroup(trig,sqr,circ,M)
        logo.move_to(ORIGIN)
        self.add(logo)
        
class BraceB(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        # self.add(line, dot, dot2, b1, b2, b1text, b2text)
        self.play(
            Write(dot),Write(dot2)
        )
        self.play(
            Write(line)
        )
        self.play(Write(b1),Write(b1text))
        self.play(Write(b2),Write(b2text))
        
class NumberPlaneA(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arw = Arrow(dot.get_center(),[1,2,0],buff=0)
        plane = NumberPlane()
        
        origin_txt = Text('(0,0)').next_to(dot,DOWN)
        tip_arw_txt = Text('(1,2)').next_to(arw.get_end(),RIGHT)
        
        self.play(Write(plane))
        self.play(Create(dot))
        self.play(Write(arw))
        self.play(
            Write(origin_txt),
            Write(tip_arw_txt),
            lag_ratio=.2
        )
        
class MovePointOnShape(Scene):
    def construct(self):
        circ = Circle(radius=1,color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)
        
        l = Line([3,0,0],[5,0,0])
        self.add(l)
        
        self.play(GrowFromCenter(circ))
        self.play(Transform(dot,dot2))

        self.play(MoveAlongPath(dot,circ),run_time=3,rate_func=linear)
        self.play(Rotating(dot,about_point=[2,0,0]),runtime=2)
        self.wait(2)


class changeAngel(Scene):
    def construct(self):
        rotation_cent = LEFT
        
        # i dont get it
        theta_tracker = ValueTracker(110)
        l1 = Line(rotation_cent,RIGHT)
        l_moving = Line(rotation_cent,RIGHT)
        l_ref = l_moving.copy()
        
        l_moving.rotate(
            theta_tracker.get_value() * DEGREES,about_point=rotation_cent
        )
        a = Angle(l1,l_moving,radius=0.5,other_angle=False)
        # i dont get it
        tex = MathTex(r'\theta').move_to(
            Angle(
                l1,l_moving,radius=0.5+3*SMALL_BUFF,other_angle=False
            ).point_from_proportion(0.5)
        )
        
        self.add(l1, l_moving, a, tex)
        self.wait()
        
        l_moving.add_updater(
            lambda x: x.become(l_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_cent
            )
        )
        
        a.add_updater(
            lambda x: x.become(Angle(l1, l_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    l1, l_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))
        