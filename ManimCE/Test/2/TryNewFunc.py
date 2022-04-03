from typing_extensions import runtime
from manim import *
from manim.mobject.geometry import ArrowCircleTip, ArrowTriangleTip
import numpy as np

class UsingCircumscribe(Scene):
    def construct(self):
        txt = Tex(r'Circlum-\\scribe').scale(2)
        
        self.add(txt)
        self.play(
            Circumscribe(txt,buff=LARGE_BUFF)
        )
        self.play(Circumscribe(txt,Circle,buff=MED_LARGE_BUFF))
        self.play(Circumscribe(txt,fade_out=True))
        self.play(Circumscribe(txt,time_width=4))
        self.play(Circumscribe(txt,Circle,True))
        
class FireworkFlash(Scene):
    def construct(self):
        dot = Dot(color=YELLOW)
        self.add(dot)
        self.play(Flash(dot,line_length=4,num_lines=20,run_time=5,color=ORANGE,rate_func=rate_functions.ease_out_expo))
        self.wait()
        
class FlashOnCirc(Scene):
    def construct(self):
        r = 2
        c = Circle(radius=r)
        self.add(c)
        self.play(
            Flash(
                c,line_length=1,num_lines=50,color=RED,
                flash_radius=r+SMALL_BUFF,time_width=.3,
                run_time=3,rate_func=rush_from
            )
        )
        
class Annotations(Scene):
    def construct(self):
        d = Dot()
        ad = AnnotationDot()
        ld= LabeledDot("EE")
        ld1 = LabeledDot(MathTex(r'\beta')).set_color(ORANGE)
        ca = CurvedArrow(2*LEFT,2*RIGHT,radius=-5)
        cda = CurvedDoubleArrow(ORIGIN, 2*RIGHT)
        
        self.add(d,ad,ld,ld1,ca,cda)
        
        for i,mobj in enumerate(self.mobjects):
            mobj.shift(DOWN*(i-3))
                
class Geo1(Scene):
    def construct(self):
        # ps = points
        a = [0, 0, 0]
        b = [2, 0, 0]
        c = [0, 2, 0]
        ap1 = ArcPolygon(a, b, c, radius=2)
        ap2 = ArcPolygon(a, b, c, angle=45*DEGREES)
        VGroup(ap1,ap2).arrange()
        
        self.play(*[Create(ap,run_time=2) for ap in [ap1,ap2]])
        self.wait()
        
class Geo2(Scene):
    def construct(self):
        arr = ArrowCircleTip(fill_opacity=.5,length=5,start_angle=1) # 1 radian or about 45 deg
        self.play(Create(arr))
        self.play(Uncreate(arr))
        
        a2 = ArrowTriangleTip(fill_opacity=.5,length=5,start_angle=45*DEGREES)
        self.play(ShowCreationThenDestructionAround(a2))
        
class Wave(Scene):
    def construct(self):
        tex = Tex(r'WaHaLaLa\LaTeX').scale(2)
        self.play(ApplyWave(tex,lag_ratio=.3))
        self.play(ApplyWave(
            tex,
            direction=RIGHT,
            time_width=.5,
            amplitude=.9
        ))
        self.play(ApplyWave(
            tex,
            rate_func=rush_into,
            amplitude=.3,
            ripples=3
        ))
        
class TrackPathEx(Scene):
    def construct(self):
        cir = Circle(color=RED).shift(4*LEFT)
        dot = Dot(color=YELLOW).move_to(cir.get_start())
        rolling_cir = VGroup(cir,dot)
        trace = TracedPath(cir.get_start())
        # this rolling circle just 'rotate' on its own point
        rolling_cir.add_updater(
            lambda rc:rc.rotate(-.3)
        )
        self.add(trace,rolling_cir)
        # but this below make it moves!!
        self.play(rolling_cir.animate.shift(8*RIGHT),run_time=8,rate_func=linear)
        self.wait()
        
class TracedPathEX2(Scene):
    def construct(self):
        circ = Circle(color=RED,radius=2).shift(4*LEFT)
        dot = Dot(color=YELLOW).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start).set_color(GREEN)
        
        # UPDATERS
        rolling_circle.add_updater(lambda m: m.rotate(25*DEGREES))

        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8*RIGHT)
                ,Flash(dot,line_length=5,num_lines=20)
                ,run_time=8, rate_func=there_and_back)
        self.wait()
        
class CutOutEx(Scene):
    def construct(self):
        main = Square().scale(2.5)
        trig = Triangle().shift(RIGHT).scale(.5)
        regP = RegularPolygon(5).shift(LEFT).scale(.7)
        c = Cutout(main,trig,regP,fill_opacity=1,color=GREEN,stroke_color=PURPLE)
        self.play(Write(c),run_time=4)
        self.wait()
        
class Vec(Scene):
    def construct(self):
        plane = NumberPlane()
        v1 = Vector([1,2])
        v2 = Vector([-3,-2])
        
        self.play(*[Write(v) for v in [v1,v2] ]  ,lag_ratio=.2,run_time=10)
        self.wait()