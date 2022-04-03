from manim import *

class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        d = Dot()
        path.set_points_as_corners([d.get_center(),d.get_center()]) # parameter is array of point
        
        def update_path(path_):
            prev_path = path_.copy()
            prev_path.add_points_as_corners(
                [d.get_center()]
            )
            path_.become(prev_path)
        
        path.add_updater(update_path)
        
        self.add(path,d)
        
        self.play(Rotating(d,radians=PI, about_point=RIGHT,run_time=2))
        self.wait()
        
        self.play(d.animate.shift(UP*5))
        self.play(d.animate.shift(DOWN*8+LEFT*4))
        self.wait()