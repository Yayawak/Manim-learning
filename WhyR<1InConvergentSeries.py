from manim import *
import numpy as np
class Sequence(Scene):
    def construct(self):
        def sequenceA(x,n):
            return (x+3)**2*n
        
        n_array = range(8)
        output = []
        for i in range(len(n_array)-1):
            output.append(sequenceA(-4,n_array[i]))
        seriesCum_output = np.cumsum(output)
        print(output)
        print(seriesCum_output)
        