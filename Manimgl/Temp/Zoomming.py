import manimlib as mn
from manimlib.constants import DEGREES, RED_D, RED_E
from manimlib.mobject.types.surface import ParametricSurface
import numpy as np

class Examp3DNo1(mn.ThreeDScene):
    def construct(self):
        axes = mn.ThreeDAxes()
        sphere = ParametricSurface(
            lambda u,v: np.array(
                [
                    1.5*np.cos(u)*np.cos(v),
                    1.5*np.cos(u)*np.sin(v),
                    1.5*np.sin(u)
                ]
            ),v_min=0,v_max=mn.TAU,u_min=-PI/2,u_max=PI/2,
            checkerboard_colors=[RED_D,RED_E],resolution=(15,32)
        )
        self.set_camera_orientation(phi=75*mn.DEGREES,theta=30*DEGREES)
        self.add(axes,sphere)