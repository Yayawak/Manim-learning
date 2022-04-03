from manim import *

class ThreeDFrame(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES,
            theta=-45*DEGREES)
        txt = Text('This is 3D Frame')
        self.add_fixed_in_frame_mobjects(txt)
        txt.to_corner(UL)
        self.add(ax)
        self.wait(4)