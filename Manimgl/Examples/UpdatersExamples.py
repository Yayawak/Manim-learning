from manimlib import *

class UpdatersExamp(Scene):
    def construct(self):
        sqr = Square()
        sqr.set_fill(BLUE_E,1)
    
        brace = always_redraw(Brace,sqr,UP)
        
        txt,width = label = VGroup(
            Text("Width ="),
            DecimalNumber(0,
                        show_ellipsis=True,
                        num_decimal_places=2,
                        include_sign=True)
        )
        label.arrange(RIGHT)
        
        always(label.next_to,brace,UP) #fixed argument
        
        f_always(width.set_value,sqr.get_width) #argument always changes
        
        self.add(sqr,brace,label)
        
        self.play(
            sqr.animate.scale(2),
            rate_func=there_and_back,
            run_time=2,
        )
        self.play(
            sqr.set_width(5, stretch=True),
            run_time=3,
        )
        self.play(
            sqr.animate.set_width(2)
        )
        
        now = self.time
        w = sqr.get_width()
        
        sqr.add_updater(
            lambda m:m.set_width(w*math.cos(self.time -now))
        )