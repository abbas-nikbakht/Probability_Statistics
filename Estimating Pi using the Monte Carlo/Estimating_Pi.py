from dash import Dash, dcc, html, Input, Output, State, callback
import plotly.graph_objects as go
import numpy as np
from scipy.stats import uniform
import math
from dash import ctx,no_update
import random

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
    

    # show "number sample"
    html.Div(
        id='output1_number',children="Number sample = 0",
        style={
            "display": "flex",
            "justifyContent": "center",
            "position": "fixed",
            "bottom": "545px","left": "-5px",
            "width": "100%","fontSize": "20px"
        }
    ),
    
    # show "pi"
    html.Div(
        id='output8_show_pi',children="Estimation π = 0.0000000000000 ",
        style={
            "display": "flex",
            "justifyContent": "center",
            "position": "fixed",
            "bottom": "510px","left": "-5px",
            "width": "100%","fontSize": "22px"
            ,"color": "green",
        }
    ),
    
    # sleep
    dcc.Interval(
    id="input3_sleep",
    interval=100,      # 1000 ms = 1 second
    n_intervals=0,
    disabled=True
                ),
    
    dcc.Store(id='input4_store_x_circle', data=[]),
    dcc.Store(id='input5_store_y_circle', data=[]),
    
    dcc.Store(id='input6_store_Points_inside_circle', data=0),
    dcc.Store(id='input7_store_Points_inside_square', data=0),

    dcc.Store(id='input_store_x_square', data=[]),
    dcc.Store(id='input_store_y_square', data=[]),
    
    dcc.Store(id="fig_store")
])


@callback(
    Output('output1_number', 'children'),
    Output('output2_graph', 'figure'),
    Output('input4_store_x_circle', 'data'),
    Output('input5_store_y_circle', 'data'),
    Output('input3_sleep', 'disabled'),
    Output('input6_store_Points_inside_circle', 'data'), # Output6
    Output('input7_store_Points_inside_square', 'data'), # Output7
    Output('output8_show_pi', 'children'), # Output8
    Output('input_store_x_square', 'data'),
    Output('input_store_y_square', 'data'),
    
    
    Input('input1_button_enter', 'n_clicks'),
    State('input2_number', 'value'),
    Input("input3_sleep", "n_intervals"), # input3
    Input('input4_store_x_circle', 'data'), # input4
    Input('input5_store_y_circle', 'data'), # input5
    Input('input6_store_Points_inside_circle', 'data'), # input6
    Input('input7_store_Points_inside_square', 'data'), # input7
    Input('input_store_x_square', 'data'), # input8
    Input('input_store_y_square', 'data'), # input9
)


def show_number(input1_button_enter, input2_number,input3_sleep,input4_store_x_circle,input5_store_y_circle,input6_store_Points_inside_circle,
                input7_store_Points_inside_square,input_store_x_square,input_store_y_square):

    # when button click
    if ctx.triggered_id == "input1_button_enter":
        
        # If the input2_number box does not contain a value
        if input2_number==None:
            disabled=True
    
        else:
            disabled=False

        return (no_update,no_update,no_update,no_update,disabled,no_update,no_update,no_update,
                no_update,no_update,)

    # when sleep
    if ctx.triggered_id == "input3_sleep":
        
        ##################### Square and circle drawing section ##################### 
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
           
        
        
        ################## The Pi calculation section and figure ##################
        distribution_p_x = uniform(loc=-1, scale=2)
        sample_x = distribution_p_x.rvs(size=1)[0] 
        
        distribution_p_y = uniform(loc=-1, scale=2)
        sample_y = distribution_p_y.rvs(size=1)[0] 



        # Checking if (x, y) lies inside the circle
        # How to draw a circle using circle equation x^2+y^2=r^2
        radius=math.sqrt(sample_x**2+sample_y**2)
        if radius <= 1:
            input6_store_Points_inside_circle= input6_store_Points_inside_circle+1
                
            # Store for after
            input4_store_x_circle.append(sample_x)
            input5_store_y_circle.append(sample_y)     
            

        else:
    
            # Store for after
            input_store_x_square.append(sample_x)
            input_store_y_square.append(sample_y)     
            
        # inside the square
        input7_store_Points_inside_square= input7_store_Points_inside_square+1
        
        
        ###################### Dot color and dot display section ######################
        colors="red"
        fig=fig.add_scatter(x=input_store_x_square, y=input_store_y_square, mode='markers',
                            showlegend=False,marker=dict(
                                color=colors,symbol="square",
                                size=10
                                ),)
                
        
        colors="blue"
        fig=fig.add_scatter(x=input4_store_x_circle, y=input5_store_y_circle, mode='markers',
                            showlegend=False,marker=dict(
                                color=colors,
                                size=10
                                ),)
    
        output2_graph=fig        
    
        
        ###################### Estimating value of pi ######################
        pi = 4 * input6_store_Points_inside_circle / input7_store_Points_inside_square
        output8_show_pi=f"Estimation π = {pi:.13f}"
        ####################################################################
        
        disabled=False
        
        number_sample= input7_store_Points_inside_square # all dot display
        output1_number=f"Number sample = {number_sample}"

        if number_sample >= input2_number:
            disabled=True
            
        return (output1_number,output2_graph,input4_store_x_circle,input5_store_y_circle,disabled,
                input6_store_Points_inside_circle,input7_store_Points_inside_square,output8_show_pi,
                input_store_x_square,input_store_y_square)
    
    return (
        no_update,
        no_update,
        no_update,
        no_update,
        no_update,
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