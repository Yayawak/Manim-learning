from manim import *

class MatchPointsScene(Scene):
      def construct(self):
            circ = Circle(fill_color=RED, fill_opacity=0.8)
            square = Square(fill_color=BLUE, fill_opacity=0.2)
            self.add(circ)
            self.wait(0.5)
            self.play(circ.animate.match_points(square))
            self.wait(0.5)
            
            
class ShuffleSubMObj(Scene):
      def construct(self):
            s = VGroup(*[ Dot().shift(i*RIGHT*0.3) for i in range(-20,20) 
                        ] 
                        )
            s2 = s.copy()
            s2.shuffle_submobjects()
            s2.shift(DOWN)
            
            self.play(
                  Write(s),
                  Write(s2),
                  run_time=3,
                  lag_ratio=0.2
            )
            
            self.wait()