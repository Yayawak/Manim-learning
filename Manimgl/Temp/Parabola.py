from manimlib import *
import numpy as np
from math import *

class A(Scene):
    def construct(self):
        axes = NumberPlane()
        axes.add_coordinate_labels()
        self.play(
            Write(axes),
            run_time=1.5
        )
        funcs = []

        a = np.linspace(-10,10,10)

        def drawFunction(a,h=0,k=0):
            f = axes.get_graph(lambda x:a*(x-h)**2+k)
            return f

        funcs = []
        for i in range(len(a)):
            funcs.append(drawFunction(a[i]))

        vg = VGroup(
            *funcs
        )

        num = DecimalNumber(0,include_sign=True)
        num.move_to(UR*3)
        self.add(
            num
        )

        for i in range(len(a)):
            self.play(
                Write(
                    vg[len(a)-1-i]
                ),
                num.animate.set_value(a[len(a)-1-i])
                ,run_time=.9
            )
            self.play(
                ReplacementTransform(
                    vg[len(a)-1-i],
                    vg[len(a)-2-i]
                ),
                run_time=0.1
            )
