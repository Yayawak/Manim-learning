from manimlib import *
class SimpleGraph(Scene):
    def construct(self):
        axes = Axes()
        axes.add_coordinate_labels(
            font_size=25,
            color='#b0dbef'
        )
        lines = VGroup(
            axes.get_graph(lambda x: 2),
            axes.get_graph(lambda x:2*x),
            axes.get_graph(lambda x: 2*x+3),
            axes.get_graph(lambda x: (2*x+3)/3),
            axes.get_graph(lambda x: (2*x+3)/(3*x)),
            axes.get_graph(lambda x: (2*x+3)/(3*x-5))
        )
        self.play(Write(axes))
        for i in range(5):

            j = i+1
            self.play(
                ReplacementTransform(lines[i],lines[j])
            )
