import manimlib as mnm
import numpy as np
import math

class Manimala(mnm.Scene):
    def construct(self):
        axes = mnm.Axes()
        axes.add_coordinate_labels()
        graphLine = axes.get_graph(
            lambda x: 0.0025*x**3,x_range=(-10,10,0.5),
            color='#abe0e5',
            stroke_width=8
        )
        label = axes.get_graph_label(graphLine, r'\frac{25x^3}{1000}')
        self.add(axes)
        self.wait()
        self.play(
            mnm.Write(graphLine),
            mnm.Write(label),
            run_time=4
        )