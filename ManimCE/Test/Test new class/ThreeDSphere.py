from manim import *

class SSphere(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            x_range=([-5,5,1]),
            y_range=([-6,6,1]),
            z_range=([-3,3,1])
            ,width=5,height=4,
            depth=3,
            
        ).scale(2.5)
        self.add(ax)
        self.set_camera_orientation(
            phi=60*DEGREES,
            theta=135*DEGREES,
            gamma=0*DEGREES
        )
        sphere = Sphere(radius=1.8,
                resolution=(101,51),
                color=BLUE,
                )
        sphere.set_opacity(.8)
        self.play(Create(sphere),run_time=4)
        self.wait()
        

