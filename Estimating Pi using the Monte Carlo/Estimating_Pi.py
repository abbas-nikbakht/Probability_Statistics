from dash import Dash, dcc, html, Input, Output, State, callback
import plotly.graph_objects as go
import numpy as np
from scipy.stats import uniform
import math
from dash import ctx,no_update

app = Dash()



# # Square
data_Square= go.Scatter(
    x=[-1, 1, 1, -1, -1],
    y=[-1, -1, 1, 1, -1],
    mode='lines',showlegend=False,line = dict(color= 'black',width=4))
###### Circle: x² + y² = 1 ######
# circle_upper
# y=sqrt(1-x**2)
x = np.linspace(-1, 1, 500)

data_circle_upper = go.Scatter(
    x=x,
    y=np.sqrt(1 - x**2),
    mode='lines',
    showlegend=False,line = dict(color= 'blue',width=3)

)

# circle_lower
# y= - sqrt(1-x**2)
data_circle_lower = go.Scatter(
    x=x,
    y=-np.sqrt(1 - x**2),
    mode='lines',
    showlegend=False,line = dict(color= 'blue',width=3)
)

# plot Square and circle_upper and circle_upper
fig = go.Figure(data=[data_Square, data_circle_upper, data_circle_lower])
fig.update_xaxes(range=[-1.05, 1.05])
fig.update_yaxes(
    range=[-1.05, 1.05],
    scaleanchor="x",
    scaleratio=1
)



    
app.layout = html.Div([
    dcc.Graph(
        id='output2_graph',
        figure=fig,  
    style={
        'width': '99vw',
        'height': '94vh',
        'margin': 'auto'
    }
    ),
    html.Div(
        dcc.Input(
            id='input2_number',
            type='number',
            placeholder='Enter a number'
        ),
        style={
            "display": "flex",
            "justifyContent": "center",
            "position": "fixed",
            "bottom": "55px",
            "width": "100%"
        }
    )
    
    ,
    
    html.Div(
        html.Button("Enter", n_clicks=0, id="input1_button_enter", style={
                "fontSize": "20px",
                "padding": "10px 25px"}),
        style={
            "display": "flex",
            "justifyContent": "center",
            "position": "fixed",
            "bottom": "3px",
            "width": "100%"
        }
        ),
    


    html.Div(
        id='output1_number',
    ),
    # sleep
    dcc.Interval(
    id="input3_sleep",
    interval=100,      # 1000 ms = 1 second
    n_intervals=0,
    disabled=True
                ),
    
    dcc.Store(id='input4_store_x', data=[]),
    dcc.Store(id='input5_store_y', data=[]),

])


@callback(
    Output('output1_number', 'children'),
    Output('output2_graph', 'figure'),
    Output('input4_store_x', 'data'),
    Output('input5_store_y', 'data'),
    Output('input3_sleep', 'disabled'),

    Input('input1_button_enter', 'n_clicks'),
    State('input2_number', 'value'),
    Input("input3_sleep", "n_intervals"), # input3
    Input('input4_store_x', 'data'), # input4
    Input('input5_store_y', 'data') # input5

)


def show_number(input1_button_enter, input2_number,input3_sleep,input4_store_x,input5_store_y):

    # when button click
    if ctx.triggered_id == "input1_button_enter":
        # print("Enter clicked")

        disabled=False

        return no_update,no_update,no_update,no_update,disabled

    # when sleep
    if ctx.triggered_id == "input3_sleep":
        # print("Enter input3_sleep")
        
        output1_number=input2_number
        print(output1_number)
        # # Square
        data_Square= go.Scatter(
            x=[-1, 1, 1, -1, -1],
            y=[-1, -1, 1, 1, -1],
            mode='lines',showlegend=False,line = dict(color= 'black',width=4))
        
        
        
        ###### Circle: x² + y² = 1 ######
        # circle_upper
        # y=sqrt(1-x**2)
        x = np.linspace(-1, 1, 500)
        
        data_circle_upper = go.Scatter(
            x=x,
            y=np.sqrt(1 - x**2),
            mode='lines',
            showlegend=False,line = dict(color= 'blue',width=3)
        
        )
        
        # circle_lower
        # y= - sqrt(1-x**2)
        data_circle_lower = go.Scatter(
            x=x,
            y=-np.sqrt(1 - x**2),
            mode='lines',
            showlegend=False,line = dict(color= 'blue',width=3)
        )
        
        # plot Square and circle_upper and circle_upper
        fig = go.Figure(data=[data_Square, data_circle_upper, data_circle_lower])
        fig.update_xaxes(range=[-1.05, 1.05])
        fig.update_yaxes(
            range=[-1.05, 1.05],
            scaleanchor="x",
            scaleratio=1
        )
        # output2_graph=fig
        
            
        Points_inside_circle=0 # Points inside the circle
        Points_inside_square=0 # Points inside the square
        # fig = go.Figure()
        
        
        # for _ in range(1,100):
        distribution_p_x = uniform(loc=-1, scale=2)
        sample_x = distribution_p_x.rvs(size=1)[0] 
        
        distribution_p_y = uniform(loc=-1, scale=2)
        sample_y = distribution_p_y.rvs(size=1)[0] 
        
        # Store for after
        input4_store_x.append(sample_x)
        input5_store_y.append(sample_y)
    
        # print(input4_store_x)
        # Checking if (x, y) lies inside the circle
        # How to draw a circle using circle equation x^2+y^2=r^2
        radius=math.sqrt(sample_x**2+sample_y**2)
    
        if radius <= 1:
            Points_inside_circle= Points_inside_circle+1
        
        # # inside the square
        # Points_inside_square= Points_inside_square+1
        
        # # Estimating value of pi
        # pi = 4 * Points_inside_circle / Points_inside_square
        # print(pi)
        
        
        fig=fig.add_scatter(x=input4_store_x, y=input5_store_y, mode='markers',
                            showlegend=False)
    
        output2_graph=fig
            
    
        output3=input4_store_x
        output4=input5_store_y
        
        disabled=False
        
        if len(input4_store_x)>=input2_number:
            disabled=True
            
        return output1_number,output2_graph,output3,output4,disabled
    
    return (
        no_update,
        no_update,
        no_update,
        no_update,
        no_update,
    )

if __name__ == '__main__':
    app.run(
        debug=False,
        port=8051
    )