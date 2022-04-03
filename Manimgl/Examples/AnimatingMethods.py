from manimlib import *

class AnimatingMethods(Scene):
    def construct(self):
        grid = Tex(r'\pi').get_grid(10,10,height=5)
        self.add(grid)
        
        self.play(grid.animate.shift(LEFT))
        
        self.play(grid.animate.set_color(YELLOW))
        self.play(grid.animate.set_submobject_colors_by_gradient(BLUE,GREEN))
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()
        
        self.play(grid.animate.apply_complex_function(np.exp),run_time=5)
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.9 * math.sin(p[1]),
                    p[1] + 0.5 * math.sin(p[0]),
                    p[2]
                ]
            )
            ,run_time=2
        )