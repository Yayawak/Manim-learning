from manim import *

class Circ3D(ThreeDScene):
    def construct(self):
        cir = Circle()
        ax = ThreeDAxes()
        self.set_camera_orientation(
            phi=75*DEGREES,
            theta=30*DEGREES
        )
        self.add(cir,ax)
        self.begin_ambient_camera_rotation(rate=2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait()
    
class ThreeDIllustion(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes()
        cir = Circle(2)
        
        self.set_camera_orientation(
            phi=75*DEGREES, theta=30*DEGREES
        )
        self.add(ax)
        self.play(Create(cir),run_time=4)
        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(4)
        self.stop_3dillusion_camera_rotation()
        self.wait()