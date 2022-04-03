import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        axes = mnm.NumberPlane()
        axes.add_coordinate_labels()
        graphLines = mnm.VGroup(
            mnm.FunctionGraph(np.sin),
            mnm.FunctionGraph(lambda x:np.cos(x*3)*2+x/3
                                ,color='#99bbdd'),
            mnm.FunctionGraph(lambda x:np.exp(x)/6)
        )
        self.add(axes)
        self.play(
            mnm.Write(graphLines),
            run_time=5,
            lag_ratio=0.5
        )