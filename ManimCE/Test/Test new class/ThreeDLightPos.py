from manim import *

class ThreeDLight(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes()
        sphere = ParametricSurface(
            lambda u,v: np.array(
                [
                    1.5 * np.cos(u) * np.cos(v),
                    1.5 * np.cos(u) * np.sin(v),
                    1.5 * np.sin(u)
                ]
            ),v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2,
            checkerboard_colors=[RED_D,RED_E],
            resolution=(15,32)
        )
        self.renderer.camera.light_source.move_to(-3*IN)
        self.set_camera_orientation(phi=45*DEGREES,theta=0*DEGREES)
        self.add(ax,sphere)

        # self.begin_ambient_camera_rotation(rate=.5)
        self.wait(8)
