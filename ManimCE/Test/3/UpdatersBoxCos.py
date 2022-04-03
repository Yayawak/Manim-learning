import math
from manim import *

class BoxSizeUpdater(Scene):
    def construct(self):
        s = Square()
        s.set_fill(BLUE_E,1)
        
        brace = Brace(s,UP)
        b = brace.add_updater(
            lambda b_: b_.become(Brace(s,UP))
        )
        #! only make right position not right width scaling
        # always(brace.next_to,s,UP)
        
        
        # Text displays width
        txt,num = label = VGroup(
            Text('Width = '),
            DecimalNumber(
                include_sign=False,
                num_decimal_places=2,
            )
        ).arrange(RIGHT).scale(1.2)
        
        # All objects except 'explain graph'
        animSizing = VGroup(s,*label)  
        # graph to explain sizing
        plane = NumberLine(include_numbers=True).stretch_to_fit_width(animSizing.get_width())
        plane.rotate(90*DEGREES,about_point=plane.get_center())
        for num in plane.numbers:
            num.rotate(-PI/2)
            num.stretch_to_fit_width(.3)
        
        
        twoMain = VGroup(animSizing,plane).arrange(buff=LARGE_BUFF).scale(1.3)
        # Surrounding Rect
        # self.add(*[SurroundingRectangle(mobj
        #                                 ,buff=LARGE_BUFF) for mobj in twoMain])
        
        dotIndicateWidth_Sqr = Dot(color=RED,point=plane.n2p(0),radius=.4)
        # ให้ความสูงต่ำของ dot แสดงถึง ความกว้างของ square
        dotIndicateWidth_Sqr.add_updater(lambda dI ,dt: dI.set_y(plane.n2p(s.get_width())[1])) # [1] means get y of n2p()
        # animation of sizing's graph(size of sqaure)
        
        # label positioning & width updater
        always(label.next_to,brace,UP)
        tempDec = DecimalNumber(0)
        tempDec.z_index = 10
        f_always(tempDec.set_value,s.get_width)
        tempDec.to_corner(DOWN)
        self.add(tempDec)
        
        
        #! FUCKING 'NUM' VARIABLE IS DISABLE FUCK YOU!
        # f_always(num.set_value,s.get_width)
        # f_always(num.set_value,tempDec.get_value)
        # num.add_updater(lambda num,dt: num.set_value(s.get_width()))
    
        #! Don't show 'num' var , tempDec is play instead it!
        self.add(s,brace,label,dotIndicateWidth_Sqr,plane)
        self.remove(num)
        self.play(s.animate.scale(2),rate_func=there_and_back_with_pause,
                        run_time=4)
        self.play(s.animate.set_width(5),rate_func=rate_functions.ease_in_elastic,run_time=3)
        self.play(s.animate.set_height(1),rate_func=smooth,run_time=5)
        self.play(s.animate.stretch_in_place(10,dim=0),rate_func=rate_functions.double_smooth,run_time=5)
        self.play(s.animate.set_width(2),rate_func=rate_functions.ease_in_sine)
        # ultimate cosine
        # w = s.get_width()
        # s.add_updater(lambda s,dt: s.set_width(w*math.cos(dt)))
        self.wait(8)
        
        
        
        
        self.wait()