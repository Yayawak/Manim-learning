from os import path
from typing_extensions import runtime
from manim import *

class AnimateMatrix(Scene):
      def construct(self):
            mat = [
                  [1,2],
                  [3,2]
            ]
            
            txt = Text('Apply Matrix')
            txt.to_corner(DOWN)
            self.add(txt)
            
            ax = NumberPlane()
            mat_ax = ax.copy()
            mat_ax.set_color(GREEN)
            self.add(ax)
            self.wait()
            
            self.play(
                  ApplyMatrix(mat,ax),run_time=4)
            
            self.wait(8)
            
      
