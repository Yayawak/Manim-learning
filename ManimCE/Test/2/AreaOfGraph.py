from manim import *

class Area(Scene):
      def construct(self):
            # ax = Axes(x_range=[0,6],y_range=[0,8])
            ax = Axes()
            g1 = ax.get_graph(lambda x:4*x**2)
            g2 = ax.get_graph(lambda x:.8*x**2-3*x+4)
            l1 = ax.get_vertical_lines_to_graph(2,g1,DashedLine,color=YELLOW)
            l2 = ax.get_vertical_lines_to_graph(3,g1,DashedLine,color=YELLOW)
            
            area = ax.get_area(g2,2,3,bounded=g1)
            
            self.play(
                  Create(g1),Create(g2),Create(l1),Create(l2)
            )
            self.play(Create(area))
            self.wait()
            
            
class AreaEx2(MovingCameraScene):
      def construct(self):
            # self.camera.background_color = '#ece6e2'
            self.camera.frame.save_state()
            self.wait()
            self.play(self.camera.frame.animate.set_width(20))
            # self.camera.frame_width = 10
            ax = Axes(
                  x_range=[0,5],y_range=[0,10],
                  x_axis_config={
                        'numbers_to_include':[2,3]
                  },
                  tips=False
            )
            labels = ax.get_axis_labels()
            
            c1 = ax.get_graph(lambda x:8*x-x**2,
                              x_range=[0,4],color=BLUE)
            c2 = ax.get_graph(lambda x:.8*x**2-3*x+4,
                              x_range=[0,4],color=PURPLE)
            
            l1 = ax.get_vertical_line(ax.input_to_graph_point(2,c1), # input x = 2 , and c1 is
                                    # function to return y when you inputs 'x'
                                    color=YELLOW)
            l2 = ax.get_vertical_line(ax.i2gp(3,c1),
                                    color=YELLOW)
            # l2.add_updater(lambda l,dt: l.become(l2.get_vertical_line(ax.i2gp(dt,c1))))
            
            area1 = ax.get_area(c1,x_range=[.3,.6],
                              dx_scaling=20,color=ORANGE,opacity=1)
            area2 = ax.get_area(c1,x_range=[2,3],
                              bounded=c2,color=RED,opacity=1)
            
            
            ## ANIMATION PART
            self.play(
                  Write(ax),Write(labels),run_time=2
            )
            self.play(*[Write(mobj) for mobj in [c1,c2,l1,l2]],
                  self.camera.frame.animate.set_width(20),
                  self.camera.frame.animate.move_to(LEFT),
                  run_time=2)
            self.play(
                  self.camera.frame.animate.set_height(30),
                  self.camera.frame.animate.shift(UP*2)
            )
            self.play(
                  Create(area1),Create(area2),
                  Restore(self.camera.frame),run_time=4
            )
            self.wait()
            
            # Learn debug?
            print(            self.animations.count()
)