from scipy.stats import uniform
import math
import plotly.graph_objects as go


Points_inside_circle=0 # Points inside the circle
Points_inside_square=0 # Points inside the square
fig = go.Figure()
for _ in range(1,5):
    distribution_p_x = uniform(loc=-1, scale=1)
    sample_x = distribution_p_x.rvs(size=1)[0] 
    
    distribution_p_y = uniform(loc=-1, scale=1)
    sample_y = distribution_p_y.rvs(size=1)[0] 
    
    
    # Checking if (x, y) lies inside the circle
    # How to draw a circle using circle equation x^2+y^2=r^2
    radius=math.sqrt(sample_x**2+sample_y**2)

    if radius <= 1:
        Points_inside_circle= Points_inside_circle+1
    
    # inside the square
    Points_inside_square= Points_inside_square+1
    
    # Estimating value of pi
    pi = 4 * Points_inside_circle / Points_inside_square
    print(pi)
    
    
    fig=fig.add_scatter(x=[sample_x], y=[sample_y], mode='markers',)


        
fig.write_html('first_figure1.html', auto_open=True)  

print(Points_inside_square)
print(Points_inside_circle)

