import manimlib as mnm


class Basic(mnm.Scene):
    def construct(self):
        axes = mnm.Axes()
        axes.add_coordinate_labels()
        self.play(
            mnm.Write(axes), run_time=4
        )


class CustomizedGraph(mnm.Scene):
    def construct(self):
        axes = mnm.Axes(x_range=(-5, 2, 0.5),
                        y_range=(-3, 5, 0.5),
                        width=13,
                        heigth=7,
                        axis_config={
                            'stroke_color': '#e7b0ef'

                        })
        axes.add_coordinate_labels(font_size=25,
                                num_decidmal_place=1,
                                include_sign=True)
        self.play(
            mnm.Write(axes), run_time=5
        )


class PositionINGraph(mnm.Scene):
    def construct(self):
        axes = mnm.Axes(x_range=(0, 50, 5),
                        y_range=(0, 100, 20))
        axes.add_coordinate_labels(font_size=32)

        pInit = axes.c2p(0, 5)
        pEnd = axes.c2p(40, 100)
        dot = mnm.Dot(pInit)
        self.add(axes)
        self.play(
            dot.animate.move_to(pEnd),
            run_time=3
        )


class p2c(mnm.Scene):
    def construct(self):
        axes = mnm.Axes(x_range=(0, 70, 5),
                        y_range=(0, 55, 5))
        axes.add_coordinate_labels(font_size=28)
        p1 = axes.c2p(15, 20)  # จุดเริ่มต้น
        chut = mnm.Dot(p1)  # วัตถุจุด
        # ฟังก์ชันสร้างเลขแสดงตำแหน่ง

        def sailek():
            # เอาค่าตำแหน่งจุดภายในภาพมาแปลงเป็นพิกัดในระนาบแกน
            x, y = axes.p2c(chut.get_center())
            xy = mnm.Text(f'({x:.0f},{y:.0f})')
            xy.next_to(chut, mnm.DOWN)  # วางไว้ด้านล่างของจุด
            return xy
        # ตัวเลขแสดงตำแหน่ง ให้สร้างใหม่ทุกเฟรม
        text = mnm.always_redraw(sailek)
        p2 = axes.c2p(55, 45)  # จุดที่จะย้ายไป

        self.add(axes, text)
        self.play(
            chut.animate.move_to(p2),
            run_time=1.5
        )
        self.wait(0.5)


class ProjectlineToAxes(mnm.Scene):
    def construct(self):
        axes = mnm.Axes(x_range=(-30,25,5),
                        y_range=(0,25,5),
                        axis_config={'stroke_width':5,'color':'#908ecb'})
        axes.add_coordinate_labels(font_size=36,color='#908ecb')
        
        pInit = axes.c2p(15,20)
        pEnd = axes.c2p(-20,5)
        dot = mnm.Dot(pInit,radius=0.2)
        
        v_line = mnm.always_redraw(lambda m:
            axes.get_v_line(dot.get_center()),0)
        h_line = mnm.always_redraw(lambda m:
            axes.get_h_line(dot.get_center()),0)
        
        self.add(axes,v_line,h_line)
        self.play(
            dot.animate.move_to(pEnd),
            run_time=2
        )
        self.play(
            dot.animate.move_to(axes.c2p(25,0))
        )
