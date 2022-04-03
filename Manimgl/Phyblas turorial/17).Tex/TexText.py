import manimlib as mnm
from manimlib.utils.tex_file_writing import tex_to_dvi

class Manimala(mnm.Scene):
    def construct(self):
        tt = mnm.TexText(r'''Geometrinen jakauma \\
                             $p(1-p)^{x-1}$ \\
                             Negatiivinen binomijakauma \\
                             $C(x+r-1,x)(1-p)^rp^x$''',
                         color='#f2a9e0',
                         font_size=100     
        )
        self.play(
            mnm.Write(tt),
            run_time=1.5
        )
