from manimlib import *
from math import *
class AA(Scene):
    def construct(self):
        axes = Axes()
        l = axes.get_graph(lambda x: abs(x-5))
        self.play(Write(axes))
        self.play(Write(l))

