import manimlib as mnm

class BasicLaTex(mnm.Scene):
    def construct(self):

       # ฟังก์ชันการแจกแจงเบตา
        beta = mnm.Tex(r'f(\alpha,\beta) = \frac{x^{\alpha-1}(1-x)^{\beta-1} }{B(\alpha,\beta)}',font_size=96)
        # แทนค่า α=2, β=3 ลงสมการ
        beta23 = mnm.Tex(r'f(2,3) = \frac{x^{2-1}(1-x)^{3-1} }{B(2,3)}',font_size=96,color='#a4ff9a')
        self.play(
            mnm.Transform(beta,beta23),run_time=2
        )
class Try(mnm.Scene):
    def construct(self):

        func = mnm.Tex(r'f(\theta) = \frac{theta^{\beta)}}{\sin(\theta)}',font_size=96)
        self.play(
            mnm.Write(func)
            ,run_time=3
        )
class Possion(mnm.Scene):
    def construct(self):
        poisson = mnm.Tex(r'f(\lambda) = \frac{\lambda^x \exp(-\lambda)}{x!}'
                          ,font_size=96,fill_opacity=0,stroke_width=4)
        poisson6 = mnm.Tex(r'f(6) = \frac{6^x \exp(-6)}{x!}',
                           font_size=96,color='#9addff',fill_opacity=0,stroke_width=4)
        self.play(
            mnm.Transform(poisson, poisson6),
            run_time=2
        )

class Isolate(mnm.Scene):
    def construct(self):
        bernouli = mnm.Tex(r'f(p) = p^x(1-p)^{1-x}',isolate=['f','p','=','x','1','-'])
        bernouli.set_color_by_gradient('#ff0add','#a9f2be')
        self.play(
            bernouli.animate.set_width(12),
            run_time=3
        )

class TransfromMatchingText(mnm.Scene):
    def construct(self):
        bernouli= mnm.Tex(
            r'f(p) = p^x(1-p)^{1-x}',
            isolate=['f','p','x','1','-'],
            font_size=144
        )
        bernouli07 = mnm.Tex(
            r'f(0.7) = 0.7^x(1-0.7)^{1-x}',
            isolate=['f','0.7','x','1','-'],
            font_size=114

        )
        self.play(
            mnm.TransformMatchingTex(bernouli,
                                     bernouli07,
                                     key_map={'p':'0.7'})
            ,run_time=1.5
        )
