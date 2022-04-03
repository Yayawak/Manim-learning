import math
from manim import *

class NumberPln(Scene):
    def construct(self):
        a = Axes(
            x_range=[-3,3],
            y_range=[-3,6],
            axis_config={
                'include_tip':False
            }
        )
        f = FunctionGraph(self.func, x_range=[-math.sqrt(3),math.sqrt(3)],
                        color=BLUE)
        self.add(a,f)
    
    def func(self,x):
        return x ** 2