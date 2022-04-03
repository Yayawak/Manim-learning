import manimlib as mnm
from manimlib.constants import DEGREES

class TransfromToPresent(mnm.Scene):
    def construct(self):
        circ = mnm.Circle()
        circ.set_fill(mnm.BLUE, opacity=0.5)
        circ.set_stroke(mnm.BLUE,width=4)
        
        sqr = mnm.Square()
        
        self.play(mnm.ShowCreation(sqr))
        self.wait()
        
    #   self.embed()
        
        self.play(mnm.ReplacementTransform(sqr,circ))
        self.wait()
        
        self.play(circ.animate.stretch(4,0))
        self.play(mnm.Rotate(circ,90*DEGREES))
        self.play(circ.animate.shift(mnm.RIGHT*2).scale(0.25))
        
        text = mnm.Text("""
            In general, using the interactive shell
            is very helpful when developing new scenes
        """)
        self.play(mnm.Write(text))

        
        mnm.always(circ.move_to, self.mouse_point)
        