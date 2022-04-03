from manim import *


class MoveFrameBox(Scene):
    def construct(self):
        tex = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(tex))
        
        box1 = SurroundingRectangle(tex[1],buff=.1)
        box2 = SurroundingRectangle(tex[3],buff=.1)
        self.play(
            Create(box1)
        )
        self.wait()
        self.play(
            
            ReplacementTransform(box1,box2)
        )
        self.wait()
        
class RotationUpdater(Scene):
    def construct(self):
        
        l_ref = Line(ORIGIN,LEFT).set_color(WHITE)
        l_mov = Line(ORIGIN,LEFT).set_color(YELLOW)
        
        #! what is dt ?
        def updater_forth(mobj,dt):
            mobj.rotate_about_origin(dt) # dt is angle
        def updater_back(mobj,dt):
            mobj.rotate_about_origin(-dt) # backward angle
            
        # start rotate forward
        l_mov.add_updater(updater_forth)
        # add static line & movable line
        self.add(l_ref,l_mov)
        self.wait()
        
        # stop rotate forward
        l_mov.remove_updater(updater_forth)
        # start rotate back
        l_mov.add_updater(updater_back)
        self.wait(2)
        l_mov.remove_updater(updater_back)
        
        
        self.wait(2)
        
class NextToUpdater(Scene):
    def construct(self):

        def dot_position(mobj):
            mobj[1].set_value(dot.get_center()[0]) # get x
            mobj.next_to(dot)
        dot = Dot(RIGHT*3)
        vg = VGroup(
            Text('X ='),
            DecimalNumber()
        ).arrange(RIGHT)
        vg.add_updater(dot_position)
        self.add(dot,vg)
        
        self.play(
            Rotating(dot,about_point=ORIGIN,
                    angle=TAU,run_time=TAU,rate_func=linear)
        )
        
class DtUpdater(Scene):
    def construct(self):
        sqr = Square()
        # rotate 90 deg per sec
        # ตัวแปร dt น่าจะเป็นตัวแปรตามเวลา เพิ่มจาก1,2,3,4,5 ไปเรื่อยๆ
        sqr.add_updater(
            lambda mobj,dt: mobj.rotate(dt*90*DEGREES)
        )
        self.add(sqr)
        self.wait(5)
        
class AnimateEx(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.scale(2))
        self.play(s.animate.rotate(PI/2))
        self.play(Uncreate(s))