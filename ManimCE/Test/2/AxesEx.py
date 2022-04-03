from manim import *

class ProjLineToAxes(Scene):
      def construct(self):
            ax = Axes(x_range=[-30,25,5]
                  ,y_range=[0,25,5],
                  axis_config={
                        'stroke_width':5
      ,'color':GREEN
      })
            p1 = ax.c2p(15,20)
            p2 = ax.c2p(-20,5)
            
            d = Dot(p1,radius=.2,color='#82c5b8')
            
            
            hori_l = always_redraw(
                  lambda l:l.get_horizontal_line(d.get_center(),
                        color='#dfb0ef',stroke_width=3)
            )
            ver_l = always_redraw(
                  lambda l:l.get_vertical_line(d.get_center(),
                        color='#dfb0ef',stroke_width=3)
            )
            
            self.add(ax,hori_l,ver_l)
            
            self.play(
                  d.animate.move_to(p2),
                  run_time=3
            )
            
class ElbowExample(Scene):
      def construct(self):
            triangle = Polygon(ORIGIN, RIGHT, RIGHT+UP)
            elbow = Elbow(color=RED)
            elbow.set_points_as_corners([ORIGIN, RIGHT, RIGHT+UP])
            # elbow.set_width(elbow.width, about_point=RIGHT+np.array([-0.1, 0.1, 0.0]))
            # vector
            v = Vector()
            v.set_angle(90*DEGREES)
            
            # double arrow
            da = DoubleArrow(ORIGIN,LEFT*3)
            
            #! arrow tip
            # at = ArrowTip()
            
            # Tangent Line
            c = Circle()
            tl =TangentLine(c,alpha=0.5,length=20)
            
            self.add(triangle,v,)
            self.play(ShowCreationThenFadeAround(da),run_time=3)
            
            self.play(Create(c))
            self.play(Write(tl),run_time=5)
            
            self.add(elbow)
            self.wait(2)