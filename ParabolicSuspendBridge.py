from manim import *
import numpy as np
class Bridge(ZoomedScene):
    def __init__(self,**kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=.8,
            zoomed_display_height=5,
            zoomed_display_width=2,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                'default_frame_stroke_width':3
            },
            **kwargs
        )
    def construct(self):
        
        # Draw staight line horizontally
        axes = Axes(x_range=[-200,200,50],y_range=[-4,20,4]
                    ,axis_config={
                        'include_tip':False
                    })
        axes.add_coordinates()
        ul_point = axes.c2p(-100,12)
        ur_point = axes.c2p(100,12)
        # self.add(axes)
        temp_l = Line(ul_point,ur_point,color=BLUE)
        self.play(Write(temp_l),rate_func=smooth,run_time=1.5)
        
        # write parabola
        mid_p = axes.c2p(0,4)
        c = 312.5
        parabola = axes.get_graph(lambda x:4+(x**2)/(4*312.5),color=BLUE)
        # self.play(Write(parabola),rate_func=smooth,run_time=3)
        self.wait()
        # Transfrom to be parabola (head down) : use bouncing rate function
        ## road
        start_road = axes.c2p(-180,0)
        end_road = axes.c2p(180,0)
        road_l = Line(start_road,end_road).set_stroke(width=7)
        road_l.set_color_by_gradient(PINK)
        # @ #  pillars 
        pil_n = 8
        interval_pill = np.linspace(-100,100,pil_n,endpoint=True)
        pillars = []
        for i in range(pil_n):
            m_p = axes.get_vertical_line(axes.i2gp(interval_pill[i],parabola))
            pillars.append(m_p)
        pillars[0].set_color(YELLOW)
        pillars[len(pillars)-1].set_color(YELLOW)

        pillars = VGroup(*pillars)
        
        # Given 3 points
        l_dot = Dot(axes.i2gp(-100,parabola))
        r_dot = Dot(axes.i2gp(100,parabola))
        almost_mid_dot = Dot(axes.i2gp(50,parabola))
        # special pillar 
        special_pil = axes.get_vertical_line(almost_mid_dot.get_center())
        first_pill= pillars[0]
        last_pill = pillars[len(pillars)-1]
        for pill in [special_pil,first_pill,last_pill]:
            pill.set_stroke(width=7).set_color(YELLOW)
        
        group_dot = VGroup(l_dot,r_dot,almost_mid_dot).set_color(ORANGE)
        self.play(AnimationGroup(
                ReplacementTransform(temp_l,parabola),run_time=4,
                rate_func=rate_functions.smooth
            ),
            AnimationGroup(
                Create(pillars),lag_ratio=.3,rate_func=rate_functions.double_smooth
            ),
            AnimationGroup(
                Create(road_l),rate_func=double_smooth
            ),
            run_time=4,lag_ratio=.7)
        
        self.play(Create(group_dot),run_time=2,lag_ratio=.5)
        self.play(Write(special_pil))

        # car drive anim
        car = SVGMobject('car',height=.6)
        car.set_color(WHITE).flip()
        car.move_to(road_l.get_start())
        self.play(Create(car),run_time=2)
        self.wait()
        self.play(car.animate.move_to(road_l.get_end()),
                rate_func=double_smooth,run_time=5)
        self.play(FadeOut(car))
        
        # add brace and label of each distance
        l_brace = BraceLabel(pillars[0],'12 m',LEFT)
        r_brace = BraceLabel(pillars[len(pillars)-1],'12 m',RIGHT)
        invis_down_line = Line(pillars[0].get_start(),pillars[len(pillars)-1].get_start())
        d_brace =  BraceLabel(invis_down_line,'200 m', DOWN)
        mid_r_brace = BraceLabel(special_pil,'6m',RIGHT)
        invis_mid_dot_down2right_line = Line(special_pil.get_start(),pillars[len(pillars)-1].get_start())
        mid_d_brace = BraceLabel(invis_mid_dot_down2right_line,'50m', DOWN)
        
        d_brace.shift(DOWN)
        two_down_braces = VGroup(d_brace,mid_d_brace).reverse_direction()
        all_braces = VGroup(l_brace,r_brace,mid_r_brace,two_down_braces)
        # set color to all braces 
        for b in all_braces:
            b.set_color(ORANGE)
            
        self.play(Create(all_braces),lag_ratio=.4,run_time=6)
        
        # Ask how to get minimum parabola to road 
        self.zoomed_camera.frame.move_to(road_l)
        self.activate_zooming(animate=True)
        self.wait()
        self.play(self.zoomed_camera.frame.animate.scale(.7))
        self.play(self.zoomed_camera.frame.animate.move_to(special_pil.get_center()+RIGHT*.5))
        self.wait()
        self.get_zoomed_display_pop_out_animation()
        self.zoomed_camera.reset()
        self.play(ShrinkToCenter(self.zoomed_camera.frame))
        # Given axes coordinate to picture
        self.play(Create(axes),run_time=3)
        # then hightlights 3 dots with FLASH funtion
        for i in range(3):
            self.play(Flash(group_dot[i]),lag_tio=.3,run_time=1)
            
        # gives coordinate to 3 points
        coord_3_dots = []
        for i in range(3):
            txt = VGroup(MathTex('\\big({x},{y}\\big)'.format(
                x = round(axes.p2c(group_dot[i].get_center())[0],0),
                y = round(axes.p2c(group_dot[i].get_center())[1],0)
            )))
            txt.next_to(group_dot[i],UP)
            coord_3_dots.append(txt)
            self.play(Create(coord_3_dots[i]))
        
        # temporaly write (x-h)^2 = 4c(y-k)
        equ = VGroup(MathTex(r'(x-h)^2 = 4c(y-k)'),
                    MathTex(r'x^2=4c(y-k)'),
                    MathTex(r'')
        )
        # given h = 0
        # gives first point to be first equ
        # gives second point(-100,12) to be fail 
        # show why second p is fail (try to divind by first equ)
        # gives third point to be equ
        # then solve equ to find c,k
        # got k & draw apply to suspend bridge image
        
        self.wait()