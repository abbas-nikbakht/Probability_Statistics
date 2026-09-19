from scipy.stats import uniform
import math

circle_points=0
for _ in range(1,50):
    distribution_p_x = uniform(loc=-1, scale=1)
    sample_x = distribution_p_x.rvs(size=1)[0] 
    
    distribution_p_y = uniform(loc=-1, scale=1)
    sample_y = distribution_p_y.rvs(size=1)[0] 
    
    
    # Checking if (x, y) lies inside the circle
    # How to draw a circle using circle equation x^2+y^2=r^2
    radius=math.sqrt(sample_x**2+sample_y**2)

    if radius <= 1:
        circle_points= circle_points+1
    
    