import manimlib as mnm
from manimlib.animation.transform_matching_parts import TransformMatchingTex
from manimlib.constants import DOWN

class Manimala(mnm.Scene):
    def construct(self):
        tex1 = mnm.VGroup(
            mnm.Tex('n! =', isolate=['n','!','='],font_size=112)
            ,mnm.Tex(r'n \times (n-1) \times \cdots \times 1',
             isolate=['(',')','n','1','n-1','\cdots','\times','r']
             ,font_size=112)
        )
        tex1.arrange(mnm.RIGHT)
        tex1.set_color('#cfa3d3')
        
        tex2 = mnm.VGroup(
            mnm.Tex('6! =', isolate=['6','!','='],font_size=112)
            ,mnm.Tex(r'6 \times 5 \times 4 \times 3 \times 2 \times 1',
             isolate=['6','5','4','3','2','1','\times','r']
             ,font_size=112)
        )
        tex2.arrange(mnm.RIGHT)
        tex2.set_color('#d0f2a9')  
 

        tex3 = mnm.VGroup(
            mnm.Tex('4! =', isolate=['4','!','='],font_size=112)
            ,mnm.Tex(r'4 \times 3 \times 2 \times 1',
             isolate=['4','3','2','1','\times','r']
             ,font_size=112)
        )
        tex3.arrange()
        tex3.set_color('#d1d3a3')

        vg = mnm.VGroup(tex1,tex3,tex2)
        vg.arrange(mnm.DOWN,buff=1)

        self.add(tex1)
        self.play(
            mnm.TransformMatchingTex(tex1[0].copy(),
                 tex2[0],
                key_map={'n':'6'}),
            mnm.TransformMatchingTex(tex1[1].copy(),
                tex2[1],
                key_map={'n':'6','n-1':'5'})
            ,run_time=1.5
        )
        self.play(
            mnm.TransformMatchingTex(tex1[0].copy(),
                                     tex3[0],
                                     key_map={'n':'4'}),
            mnm.TransformMatchingTex(tex1[1].copy(),
                                     tex3[1],
                                     key_map={'n':'4','n-1':'3'}),
            run_time=1.25
        )
