from manim import *
from numpy.random import uniform

class ProjectionLine(Scene):
      def construct(self):
            grid = NumberPlane(
                  axis_config={
                        
                  }
            )
            num_l = NumberLine()
            num_l.add_updater(
                  lambda l,dt: l.rotate_about_origin(dt*DEGREES*45)
            )            
            
            dots = VGroup(*[ Dot(point=np.array([np.random.uniform(-5,5),np.random.uniform(-5,5),0]) 
                              ,radius=.005*i) for i in range(100)])
            
            
            # self.add(grid,num_l)
            self.play(Write(dots,run_time=5,lag_raio=.3))
            self.wait()
            self.play(ShrinkToCenter(dots),lag_ratio=.3,run_time=2)
            self.wait(5)
            
class AnimationAddTextWordByWord(Scene):
      def construct(self):
            text = Text(r"Hello World !\\This should be written word by word.")
            anno = Text("Add text word by word")
            anno.shift(2*DOWN)
            self.add(anno)
            self.play(AddTextWordByWord(text, run_time=5.0))