from manimlib import *

class HalfCircle(Scene):
    def construct(self):
        x1 = lambda x: x**2
        x2 = lambda x: x**2-9
        x3 = lambda x: math.sqrt(x**2)

        axes = Axes()
        axes.add_coordinate_labels()


        lines = VGroup(
            axes.get_graph(x1,color='#00AAAA'),
            axes.get_graph(x2,color='#AAAA00'),
            axes.get_graph(x3,color='#AA00AA')
        )
        text = VGroup(
            Tex(r'y = x^2'),
            Tex(r'y = x^2-9'),
            Tex(r'y = \sqrt{x^2}')
        )
        text.move_to(UR*3)
        self.play(
            Write(axes)
        )
        self.play(
            Write(lines[0]),Write(text[0]),lag_ratio=0.7
        )
        for i in range(2):
            self.play(
                ReplacementTransform(lines[i],lines[i+1])
                ,ReplacementTransform(text[i],text[i+1])
                ,lag_ratio=0.7

            )
            self.wait(0.5)
