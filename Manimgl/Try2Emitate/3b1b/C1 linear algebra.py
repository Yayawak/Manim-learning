import manimlib as mn
from manimlib.animation.fading import Fade
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.scene.scene import Scene
import numpy as np

# quote on intro and song


class Introduction(mn.Scene):
    def construct(self):
        introTxt = mn.Text('"The introduction of number as\ncoordinates is an act of violence."',
                    t2c={'coordinate': mn.GREEN})
        name = mn.Text('-Hermann Wey', color='#FFFF00')

        # introTxt.set_height(0)
        self.wait()
        introTxt.to_edge(mn.UP)
        introTxt.scale(.75)
        name.next_to(introTxt, mn.DOWN)
        self.play(
            mn.FadeIn(introTxt),
            run_time=2
        )
        self.play(mn.Write(name),
                run_time=3,
                lag_ratio=0.1)
        self.wait()
        self.play(mn.FadeOut(introTxt),
                mn.FadeOut(name))
        self.wait(1)
# draw number plane 3 sec
        plane = mn.NumberPlane(
            axis_config={'stroke_width': 5}
        )
        self.play(mn.Write(plane), run_time=2)
# draw yellow vector to [1,2]
        pFi = plane.c2p(1, 2, 0)
        pIni = plane.c2p(0, 0, 0)
        vec = mn.Arrow(pIni, pFi, fill_color=mn.YELLOW, buff=0)
        self.wait()
        self.play(
            mn.Write(vec),
            lag_ratio=0.9,
            run_time=2,

        )
# draw  number labels
        l = plane.add_coordinate_labels()
        vecMat = mn.Tex(r'\begin{bmatrix}1\\2\end{bmatrix}').next_to(
            vec, mn.RIGHT)
        vecSign = mn.Tex(r'\vec{v}').next_to(vec, mn.UR)
        self.play(mn.Write(l),
                mn.Write(
                    vecMat
        ),
            mn.Write(
                    vecSign
        ),
            run_time=2,
            lag_ratio=0.3
        )
# split arrow,vect v, [1,2] and fade all others

        # Fade bg
        self.play(
            mn.FadeOut(plane), 
            vec.animate.move_to(np.array([-4, 2, 0])),
            vecMat.animate.move_to(np.array([4, 2, 0])), 
            vecSign.animate.move_to(np.array([0, 2, 0])),
            lag_ratio=0.3
        )
# add 3 student characters
# show creation 
        threeSign = VGroup(vec,vecMat,vecSign)
        dist = 6
        phys = mn.Text('Physics Student').next_to(vec,mn.DOWN*dist)
        cs = mn.Text('CS Student').next_to(vecMat,mn.DOWN*dist)
        mat = mn.Text('Mathematician').next_to(vecSign,mn.DOWN*dist)
        
        self.play(mn.ShowCreation(phys))
        self.play(mn.ShowCreation(cs))
        self.play(mn.ShowCreation(mat))
        
        self.play(
            mn.FadeOut(cs),
            mn.FadeOut(mat),
    
            mn.FadeOut(vecMat),
            mn.FadeOut(vecSign)
        )
        
        
class PhysicsView(Scene):
    def construct(self):
        
# physics view
# draw yel vec >  rotate vec > write brace and length
# move vec on 3 pos > animate pi char & draw more vector & write text
# write 3d vector field and move camera planing

# CS view
