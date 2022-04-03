import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        ell = mnm.Ellipse(width=14,height=3)
        w = mnm.DecimalNumber(0,font_size=25) #width of ell
        brace = mnm.Brace(ell,mnm.UP)
        
        mnm.always(w.next_to,brace,mnm.UP)
        mnm.f_always(w.set_value,ell.get_width)
        
        mnm.always(brace.next_to,ell,mnm.UP)
        mnm.f_always(brace.stretch_to_fit_width,ell.get_width)
        
        self.add(w,brace)
        self.play(
            mnm.FadeOutToPoint(ell,np.array([2,-2,0])),
            run_time=6
        )