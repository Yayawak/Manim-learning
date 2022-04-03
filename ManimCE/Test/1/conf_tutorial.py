import manim as mn
from manim.animation.creation import Write
from manim.constants import DOWN, RIGHT
# ManimConfig class
# mn.config is global configuration

class ShowScreenResolution(mn.Scene):
    def construct(self):
        pix_h = mn.config['pixel_height']
        pix_w = mn.config['pixel_width']
        f_h = mn.config['frame_width']
        f_w = mn.config['frame_height']
        
        self.add(
            mn.Dot()
        )
        l_hori = mn.Line(
            f_w*mn.LEFT/2,f_w*RIGHT/2
        ).to_edge(mn.DOWN)
        self.play(mn.Write(l_hori))
        self.add(
            mn.Text(str(pix_w)).next_to(l_hori,mn.UP)
        )
        
        l_ver = mn.Line(
            f_h*mn.UP/2,f_w*DOWN/2
        ).to_edge(mn.LEFT)
        self.play(mn.Write(l_ver))
        self.add(
            mn.Text(str(pix_h)).next_to(l_ver,mn.RIGHT)
        )
        
        
        
        
        