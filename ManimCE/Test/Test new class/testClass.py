from manim import *

class Indicator(Scene):
    def construct(self):
        text = Text('Indicates').scale(2)
        # TextIO()
        self.add(text)
        
        self.play(
            Indicate(text),
            # Indicator
            # ,CircleIndicate
            run_time=3
        )
        self.wait(2)
        # self.play(
            # Indicator()
        # )
    
class FocusOnDot(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).shift(DOWN)
        self.add(dot)
        self.play(
            FocusOn(dot,color=ORANGE,opacity=1,
                    rate_func=smooth)
            ,run_time=3
        )        
        self.wait()

class AlwayDrawHVline(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-1,10],
            y_range=[-2,2,0.5],
            height=6,
            width=10,
            axis_config={
                'stroke_color':GREY_A,
                'stroke_width':2
            },y_axis_config={
                'include_tip':False,
            }
        )
        ax.add_coordinates(
        )
        self.add(ax)
        
        dot = Dot(color=RED)
        dot.move_to(ax.c2p(0,0))
        self.play(FadeIn(dot,scale=.5))
        self.play(dot.animate.move_to(ax.c2p(5,3)))
        self.wait()
        self.play(dot.animate.move_to(ax.c2p(2,-3)))
        self.wait()
        
        h_l = always_redraw(lambda: ax.get_horizontal_line(dot.get_left()))
        v_l = always_redraw(lambda: ax.get_vertical_line(dot.get_bottom()))
        self.play(
            Create(VGroup(h_l,v_l))
        )
        
        self.play(dot.animate.move_to(ax.c2p(0,7)))
        self.wait()
        self.play(dot.animate.move_to(ax.c2p(1,1)))
        self.wait()
        
        # move ax then 'dot' can move along with new ax
        f_always(dot.move_to,lambda: ax.c2p(1,1))
        self.play(
            ax.animate.scale(.75).to_corner(UL),
            run_time=3
        )
        self.wait()
        self.play(FadeOut(VGroup(ax,dot,h_l,v_l)))