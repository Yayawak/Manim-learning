import math
from manim import *

class Param(Scene):
    def construct(self):
        a = Axes(
            x_range=[-3,3],
            y_range=[-3,6],
            axis_config={
                'include_tip':False
            }
        )
        
        f = ParametricFunction(self.func, t_range=[-math.sqrt(3),math.sqrt(3)],
                        color=BLUE)
        c = ParametricFunction(self.circ, t_range=[0,PI*1.75])
        self.add(a,f)
        self.wait(3)
        self.remove(f)
        self.add(c)
        self.wait(3)
    
    def func(self,t):
        return [t, t**2,0]
    
    def circ(self,t):
        return [math.sin(t),math.cos(t),0]