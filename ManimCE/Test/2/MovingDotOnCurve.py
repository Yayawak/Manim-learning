from manim import *

class Ex1(Scene):
    def construct(self):
        ax =Axes(x_range=[-5,20],y_range=[-10,30])
        
        #vt is x value ( or independent value)
        vt = ValueTracker(0)
        
        # this function is 'y' or dependent value 
        def graph(x):
            return .5*x**2-3
        
        c1 = ax.get_graph(graph,x_range=[-2,10],color=BLUE)
        
        def move_dot():
            x = vt.get_value()
            d = Dot().move_to(ax.c2p(x,graph(x)))
            return d
        dotMove = always_redraw(move_dot)
        
        self.add(dotMove,c1,ax)
        self.play(vt.animate.set_value(7),rate_func=rate_functions.ease_in_elastic,run_time=5)
        
        self.wait()