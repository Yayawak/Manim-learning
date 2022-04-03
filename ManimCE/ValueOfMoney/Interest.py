from manim import *

class Interest(Scene):
    def clear(self):
    
        
        sum_money_each_year = []
        year = 10
        principle_money=50000
        # คิดดกเบี้ยทบต้นทีละปี
        # rate per year
        rate = 5 # %
        for i in range(year):
            current_sum = principle_money
            interest_ = current_sum * (rate/100)
            sum_ = interest_ + current_sum
            
            sum_money_each_year.append(sum_)
            current_sum = sum_
        
        
        sum_money_each_year = np.array(sum_money_each_year)
        bar =BarChart(sum_money_each_year,
                    width=10,height=6,
                    bar_colors=['#99ff99','#c094d5'])
        # self.add(bar)
        self.play(Create(bar),
                run_time=5,rate_func=smooth
                )
        self.wait()
        self.play(
            bar.change_bar_values(sum_money_each_year*.5),run_time=5,rate_funct=double_smooth
        )
        self.wait()
            
        
        