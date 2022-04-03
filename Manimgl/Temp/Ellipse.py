import manimlib as mn
import numpy as np
import math
class A(mn.Scene):
    def construct(self):

        plane = mn.NumberPlane()
        plane.add_coordinate_labels()

        a,b = 2,4
        '''ell = plane.get_graph(
            lambda x: math.sqrt(((a*b)**2-(b*x)**2)/a)
        )
        '''
        self.wait()
        self.play(
            mn.Write(
                #ell square root make problem
                mn.Ellipse(width=a,heigth=b)
            )
        )
