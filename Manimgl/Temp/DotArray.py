import manimlib as mnm
import numpy as np

class Manimala(mnm.Scene):
    def construct(self):
        list_chut = []
        for i in range(15):
            xy = np.array([i-6,(i-9)/3,0]) # ตำแหน่งจุด
            r = 0.2+0.02*i**2 # รัศมี เพิ่มขึ้นเรื่อยๆ
            c = '#c1e9%s'%(10+i**1)
            chut = mnm.Dot(xy,radius=r,color=c)
            list_chut.append(chut)
        # นำมาจัดรวมกลุ่ม
        vg = mnm.VGroup(*list_chut)
        self.play(
            mnm.Write(vg),
            run_time=5
        )
