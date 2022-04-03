from math import degrees
from os import write
from typing_extensions import runtime
from manim import *
from manim.utils import tex_templates


class ExValueTracker(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        num = DecimalNumber(0)
        num.add_updater(
            lambda m:m.set_value(tracker.get_value())
        )
        self.add(num)
        self.play(
            tracker.animate.set_value(1000),run_time=5
        )
        
class FunctionTracker(Scene):
    def construct(self):
        # f(x) = x^2
        fx = lambda x: x.get_value()**2 # get_value is method of ValueTracker
        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))
        
        # decimalNumber
        x_tex = DecimalNumber(x_value.get_value()).add_updater(
            lambda v: v.set_value(x_value.get_value()) # v is instance of DecimatNumber or x_tex
        )
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(
            lambda v: v.set_value(fx_value) 
        )
        
        # Tex labelsM
        x_label = Tex(r'x =')
        fx_label = Tex(r'x^2 = ')
        
        #grouping labels and nums
        group = VGroup(x_tex,fx_tex,x_label,fx_label).scale(2.6)        
        VGroup(x_tex,fx_tex).arrange_submobjects(DOWN,buff=3)
        
        # align lables and nums
        x_label.next_to(x_tex,LEFT,buff=.7,aligned_edge=x_label.get_bottom())
        fx_label.next_to(fx_tex,LEFT,buff=.7,aligned_edge=fx_label.get_bottom())
        
        self.add(
            group.move_to(ORIGIN)
        )
        self.wait()
        self.play(
            x_value.animate.set_value(30),
            rate_func=linear,
            run_time=10
        )


class TwoMovingDots(Scene):
    def construct(self):
        d1,d2 = Dot(color=BLUE),Dot(color=GREEN)
        dot_g = VGroup(d1,d2).arrange(RIGHT,buff=1)
        l1 = Line(d1.get_center(),d2.get_center()).set_color(RED)

        x = ValueTracker(0)
        y = ValueTracker(0)
        
        d1.add_updater(lambda z: z.set_x(x.get_value()))
        d2.add_updater(lambda z: z.set_y(y.get_value()))
        l1.add_updater(lambda z: z.become(Line(d1.get_center(),d2.get_center())))
        
        self.add(d1,d2,l1)
        self.play(x.animate.set_value(5))
        self.play(y.animate.set_value(4))
        self.wait()
        
class MovingFrameBox(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX").scale(3)
        self.play(Write(tex))
        self.play(Uncreate(tex))
        
        # tex = Tex(r'$\xrightarrow{Hello}$ \LaTeX').scale(3)
        mTex = Tex(r'$\xrightarrow{Hello}$ \LaTeX').scale(3)
        self.play(
            Write(mTex)
        )
        self.play(FadeOut(mTex))
        
        
        tex3 = MathTex(r'\xrightarrow{lim}\text{\LaTeX}').scale(3)
        self.play(Write(tex3))
        self.play(Uncreate(tex3))
        

        self.wait()
# extra latex package
class ExtraLaTeXPackage(Scene):
    def construct(self):
        myTemp = TexTemplate()
        myTemp.add_to_preamble(r'\usepackage{mathrsfs}')
        tex = MathTex(r'\mathscr{H} \rightarrow \mathbb{H}',tex_templates=myTemp).scale(3)
        self.wait()
        self.play(Write(tex),runtime=4)
        self.wait()
        
class Example7LaTeX(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &=5 + 1\\ &=6').scale(2)
        self.wait()
        self.play(Write(tex),run_time=4)