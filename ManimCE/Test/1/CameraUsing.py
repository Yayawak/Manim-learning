from manim import *
from numpy import dot

class ZoomCamBackAndForth(MovingCameraScene):
    def construct(self):
        txt = Tex('\\LaTeX').set_color(BLUE_E).scale(3)
        self.add(txt)
        
        self.camera.frame.save_state()
        self.play(
            self.camera.frame.animate.set(
                width=txt.width*.1
            ),
            run_time=3
        )
        self.wait(.9)
        self.play(Restore(self.camera.frame))


class MoveCamToObj(MovingCameraScene):
    def construct(self):
        s = Square(color=RED,fill_opacity=.5).move_to(2*LEFT)
        t = Triangle(color=GREEN,fill_opacity=.5).move_to(2*RIGHT)
        
        self.wait()
        self.add(s,t)
        
        self.play(
            self.camera.frame.animate.move_to(s)
        )
        self.wait()
        
        self.play(
            self.camera.frame.animate.move_to(t)
        )
        self.wait()
        
class MoveToAndZoomTo(MovingCameraScene):
    def construct(self):
        s = Square(color=RED,fill_opacity=.5).move_to(2*LEFT)
        t = Triangle(color=GREEN,fill_opacity=.5).move_to(2*RIGHT)
        self.add(s,t)
        
        self.play(
            self.camera.frame.animate.move_to(s).set(width=s.width*2) # set camera widht to
            # gradually small close to square's width
        )
        
        def BackToNormal():
            self.play(
                self.camera.frame.animate.move_to(ORIGIN).set(width=14)
            )
        BackToNormal()
        
        self.play(
            self.camera.frame.animate.move_to(t).set(width=t.width*2)
        )
        
        BackToNormal()
        
        
        self.wait()
        
class MoveCamOnGraph(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        
        ax = Axes(x_range=[-1,10],y_range=[-1,10])
        graph = ax.get_graph(lambda x: np.sin(x),
                            color=WHITE,x_range=[0,3*PI])
        
        d1 = Dot(ax.i2gp(graph.t_min,graph))
        d2 = Dot(ax.i2gp(graph.t_max,graph))
        
        self.add(ax,graph,d1,d2)
        self.wait()
        # Cam 
        self.play(
            self.camera.frame.animate.scale(.5).move_to(d1)
        )
        self.play(
            self.camera.frame.animate.move_to(d2)
        )
        self.play(
            Restore(self.camera.frame)
        )
        
        self.wait()


class MovingZoomedSceneAround(ZoomedScene):
# contributed by TheoremofBeethoven, www.youtube.com/c/TheoremofBeethoven
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=6,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )

    def construct(self):
        dot = Dot().shift(UL * 2)
        image = ImageMobject(np.uint8([[0, 100, 30, 200],
                                       [255, 0, 5, 33]]))
        image.height = 7
        frame_text = Text("Frame", color=PURPLE).scale(1.4)
        zoomed_camera_text = Text("Zoomed camera", color=RED).scale(1.4)

        self.add(image, dot)
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(PURPLE)
        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        frame_text.next_to(frame, DOWN)

        self.play(Create(frame), FadeIn(frame_text, shift=UP))
        self.activate_zooming()

        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
        self.play(FadeIn(zoomed_camera_text, shift=UP))
        # Scale in        x   y  z
        scale_factor = [0.5, 1.5, 0]
        self.play(
            frame.animate.scale(scale_factor),
            zoomed_display.animate.scale(scale_factor),
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )
        self.wait()
        self.play(ScaleInPlace(zoomed_display, 2))
        self.wait()
        self.play(frame.animate.shift(2.5 * DOWN))
        self.wait()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        self.wait()