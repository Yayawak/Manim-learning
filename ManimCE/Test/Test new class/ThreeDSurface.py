from manim import *

class ThreeDSurface(ThreeDScene):
    def construct(self):
        resolution_fa = 42
        self.set_camera_orientation(
            phi=75*DEGREES,
            theta=-30*DEGREES
        )
        
        def param_gauss(u, v):
            x = u
            y = v
            d = np.sqrt(x * x + y * y)
            sigma, mu = 0.4, 0.0
            z = np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])
        
        gauss_plane = ParametricSurface(
            param_gauss,
            resolution=(resolution_fa,resolution_fa)
            ,v_max=2,v_min=-2,
            u_max=-2,u_min=2
        )
        
        gauss_plane.scale_about_point(2,ORIGIN)
        gauss_plane.set_style(fill_opacity=1,stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE,BLUE,opacity=.5)
        
        ax = ThreeDAxes()
        self.add(ax,gauss_plane)
        
    