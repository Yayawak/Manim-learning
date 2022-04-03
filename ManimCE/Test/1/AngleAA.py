from manim import *
from numpy import angle

class AngleMidPoint(Scene):
    def construct(self):
        l_ref = Line(ORIGIN,5*RIGHT)
        l_mov = l_ref.copy().rotate(angle=80*DEGREES,about_point=l_ref.get_start()).set_color(YELLOW)

        a = Angle(l_ref,l_mov,radius=1.5,other_angle=False)
        d = Dot(a.get_midpoint()).set_color(RED)
        
        
        self.add(l_ref,l_mov,a,d,PolarPlane())
        # Try to rotate reference line
        l_ref.add_updater(lambda lref,dt: lref.rotate_about_origin(dt*DEGREES*30))
        # Not only rotate BUT! SHIFT POSITION
        # l_ref.add_updater(lambda l,dt: l.shift(DOWN*dt)) #! พะพะพะพัง!!
        # move l_mov
        l_mov.add_updater(lambda line,dt:line.rotate(dt*DEGREES*180,about_point=l_ref.get_start()))
        
        # extend length of Angle(arc) Object
        a.add_updater(lambda a_: a_.become(Angle(l_ref,l_mov,radius=1.5,other_angle=False)))
        # move dot to center of arc line
        d.add_updater(lambda d_: d_.become(Dot(a.point_from_proportion(.5)).set_color(RED)))
        
        self.wait(10)