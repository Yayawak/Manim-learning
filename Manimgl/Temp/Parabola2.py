import manimlib as mn
import numpy as np

class Parabola(mn.Scene):
    def construct(self):
        axes = mn.NumberPlane()
        axes.add_coordinate_labels()


        self.play(
            mn.Write(axes)
        )
        self.play(
            mn.Write(
                axes.get_graph(lambda x: x**2-2*x+3),
            ),
            mn.Write(
                mn.Tex(r'y = x^2-2x+3').move_to(mn.UR*3)
            )
            ,run_time=2
        )
