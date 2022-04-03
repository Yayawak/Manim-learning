from manim import *

class Param(ThreeDScene):
    def construct(self):
        axis_config = {
            'x_range': [-5,5],
            'y_range': [-5,5],
            'z_range': [-3,3]
        }
        a = ThreeDAxes(**axis_config)
        surff = ParametricFunction(self.surf)
        self.move_camera(.8*np.pi/2, -.45*np.pi)
        self.add(a,surff)

    def surf(self,u):
        return [u,u**2,u**2]
    
class ParamSpring(ThreeDScene):
    def construct(self):
        curve = ParametricFunction(
            lambda u: np.array(
                [1.2 * np.cos(u),
                 1.2 * np.sin(u),
                 u *.3]
            ),color=RED,
            t_range=np.array([-3*TAU,5*TAU,.01])
        ).set_shade_in_3d(True)
        
        axes = ThreeDAxes()
        self.add(axes,)
        self.set_camera_orientation(phi=45*DEGREES,
                theta=-60*DEGREES)
        self.play(Create(curve),run_time=5,rate_func=double_smooth)
        
        self.wait(3)



