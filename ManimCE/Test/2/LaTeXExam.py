from typing_extensions import runtime
from manim import *
from numpy import dot, gradient

class L1(Scene):
      def construct(self):
            arrow = MathTex(r'\overrightarrow{mn}')
            self.play(Write(arrow))
            self.play(Uncreate(arrow))
            
            # equal
            tex = MathTex(r'x =')
            num = DecimalNumber(0).add_updater(lambda num_,dt:num_.set_value(dt))
            group = VGroup(tex,num).scale(3)
            group.arrange()
            self.add(group)
            self.play(ShrinkToCenter(group))
            self.wait()
            
            # not equal
            tex = MathTex(r'3 \neq 2').scale(3)
            self.play(Write(tex),run_time=3)
            self.play(Uncreate(tex))
            
            # pair order
            tex = MathTex(r'\left(a,b\right)').scale(3)
            self.play(Write(tex),run_time=3)
            self.play(FadeOut(tex))
            
            # cartesian orders product
            a = MathTex(r'a = \begin{Bmatrix}2,&4,&6\end{Bmatrix}')
            b = MathTex(r'b = \begin{Bmatrix}1,&3\end{Bmatrix}')
            
            vg = VGroup(a,b).arrange(DOWN).scale(3).set_color_by_gradient(BLUE,GREEN)
            self.play(Write(vg),
                  runtime=3)
            self.play(vg.animate.set_color_by_gradient(RED,YELLOW)
                  ,lag_raio=.8

            )
            self.play(
                  vg.animate.set_opacity(.1),
                  run_time=1.5,
                  lag_ratio=.5

            )
            self.wait()
            self.play(Uncreate(vg,lag_raio=.2))
            
class L2(Scene):
      def construct(self):
            # domain 
            equ = MathTex(r'y = \sqrt{x^2-9}') 
            domain = VGroup(
                        MathTex('\\mathit{Domain :} \\ '),
                        MathTex(r'x^2-9\geq0 \\'),
                        MathTex(r'\left(x-3\right)\left(x+3\right) \geq0 \\'),
                        MathTex(r'\mathit{D_{r}}=(-\infty,-3]\cup[3,\infty)'),

            ).set_color_by_gradient('#dfb9de','#445ba4')
            domain.arrange(DOWN)
            
            vg =VGroup(equ,domain).arrange(DOWN,buff=MED_LARGE_BUFF).scale(1.5)
            self.wait()
            # self.play(Write(vg),run_time=5)
            self.play(Write(equ))
            self.wait()
            
            self.play(Write(domain[0]))
            
            # copy text line to next linn
            interval = 1.5
            temp_n_line = NumberLine()
            self.play(
                  TransformFromCopy(domain[0],domain[1]),
                  Write(temp_n_line),
                  run_time=interval,
            )
            
            dots = VGroup(Dot(temp_n_line.n2p(3),radius=.1),
                        Dot(temp_n_line.n2p(-3),radius=.1)
                        ) # ต้อง scale ให้เลขมากกว่า 1 เพราะว่าเดิมที่ จุดนั้นมีรัศมี < 1 เช่น 0.5 หาก 0.5ยกกพลัง 5 จะได้ว่า
            # = 0.03125 ยิ่งน้อยลงไปซะงั้น
            #! ล่าสุดใช้การ scale ไม่ได้แล้วจร้าไม่งั้นจะไปทำให้ตำแหน่งเลื่อน ทางแก้คือไปเพิ่ม รัศมี โดยตรงจะดีกว่า
            self.play(
                  TransformFromCopy(domain[1],domain[2]),
                  Write(dots),
                  
                  run_time=interval
            )
            
            
            arrow = VGroup(
                  Vector(RIGHT).move_to(dots[0])
                  ,Vector(LEFT).move_to(dots[1])
            ).scale(3)
      
            self.play(
                  TransformFromCopy(domain[2],domain[3])
                  ,Create(arrow),
                  run_time=interval
            )
            
            
            self.wait()      

      