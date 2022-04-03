from manim import *

class SVGTest(Scene):
    def construct(self):
        svg = SVGMobject('./Assets/svg_images/finger')
        self.play(DrawBorderThenFill(svg,rate_func=linear))
        self.wait()
        
class SoundCheck(Scene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(3)])
        dots.arrange_submobjects(RIGHT)
        for dot in dots:
            self.add_sound('click',gain=-10)
            self.add(dot)
            self.wait()
        self.wait()