import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        p1 = np.array([-5,0,0]) # จุดเริ่ม
        p2 = np.array([5,-1,0]) # จุดปลาย
        # วาดหลายเส้นให้มีจุดต้นจุดปลายที่เดียวกันแต่มุมกวาดต่างกัน
        lis_arc = []
        for i in range(30):
            a = np.radians(180-(i*25))
            arc = mnm.ArcBetweenPoints(p1,p2,
                                       angle=a,
                                       color='#ffee'+str(i),
                                       stroke_width=3)
            lis_arc.append(arc)
        # รวมเส้นทั้งหมดเข้าไว้ในกลุ่ม
        vg = mnm.VGroup(*lis_arc)
        # ใส่จุดเริ่มกับจุดปลายไว้ก่อน
        self.add(mnm.Dot(p1),mnm.Dot(p2))
        # ทำการวาดเส้นโค้ง
        self.play(
            mnm.Write(vg),
            run_time=4
        )
