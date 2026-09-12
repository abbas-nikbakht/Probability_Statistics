from dash import Dash, dcc, html, Input, Output, callback,State
import numpy as np
import plotly.graph_objects as go
from scipy.stats import rv_discrete
from dash import ctx,no_update

app = Dash()

app.layout = html.Div([
    dcc.Store(id='sample_list', data=[]),
    dcc.Store(id='date_Expected_list', data=[]),

    dcc.Graph(id='graph',figure=go.Figure(
                            layout=dict(
                                title='Monte Carlo Simulation',
                                xaxis_title='Number of Samples',
                                yaxis_title='Expected Value'
                            )
                        )
              
              
              
              ),
    html.Div(
        html.Button("Rolling the dice", n_clicks=0, id="button_one_Rolling_dice", style={
                "fontSize": "20px",
                "padding": "10px 25px"}),
        style={
            "display": "flex",
            "justifyContent": "center",
            "position": "fixed",
            "bottom": "20px",
            "width": "100%"
        }
        ),
    
    html.Div(
        id='Score_value',children="Outcome = 1",

        style={
            'textAlign': 'center',
            'position': 'relative',
            'top': '-20px','fontWeight': 'bold','fontSize': '18px'
            }
        ),
    html.Div(
        html.Img(
            id='dice_image',src="/assets/dice_1.png",
            style={
                'width': '65px',
                'height': '65px',}
            ),
        style={
            'textAlign': 'center',
            'marginTop': '-15px'
            }
        ),
    
    # box input number (LEFT)
    html.Div(

        dcc.Input(
            id="num_rolls",
            type="number",placeholder="Number of rolls",min=1,step=1,
            style={"width": "150px","fontSize": "17px"}
        ),

        style={
            "position": "absolute",
            "left": "200px",
            "top": "480px",

        }
    ),
    html.Div(
        html.Button("Reset", n_clicks=0, id="reset_button", style={
                "fontSize": "17px",
                }),
        style={
            "position": "absolute",
            "left": "200px",
            "top": "510px",

        }
        ),
    html.Div(
        html.Button("Enter", n_clicks=0, id="Enter_button", style={
                "fontSize": "17px",
                }),
        style={
            "position": "absolute",
            "left": "300px",
            "top": "510px",

        }
        ),
    
    # sleep
    dcc.Interval(
    id="rolling_interval",
    interval=50,      # 1000 ms = 1 second
    n_intervals=1,
    disabled=True
                )
    
    ])
    
@callback(
    Output('graph', 'figure'),
    Output('Score_value', 'children'),
    Output('sample_list', 'data'),
    Output('date_Expected_list', 'data'),
    Output('dice_image', 'src'),
    Output("rolling_interval", "disabled"),
    
    Input('button_one_Rolling_dice', 'n_clicks'), # input1
    Input('sample_list', 'data'),   # input2
    Input('date_Expected_list', 'data'),     # input3
    Input('reset_button', 'n_clicks'), # input4
    Input('Enter_button', 'n_clicks'), # input5
    Input("num_rolls", "n_submit"), # input6
    State("num_rolls", "value"),# input7
    Input("rolling_interval", "n_intervals"), # input8
    )

def function1(input1, input2, input3,input4,input5,input6,input7,input8):
    
    # Reset
    if ctx.triggered_id == "reset_button":
        output6=True
        return (
            go.Figure(layout=dict(title='Monte Carlo Simulation',xaxis_title='Number of Samples',
                                  yaxis_title='Expected Value')),   # graph
            "Outcome= 1",  # Score
            [],            # sample_list
            [],            # expected_list
            "/assets/dice_1.png",# dice image
            output6
        )
    
    
    if ctx.triggered_id == "button_one_Rolling_dice":
   
        x = np.array([1, 2, 3, 4, 5, 6])
        p_x = np.array([1/6,1/6,1/6,1/6,1/6,1/6])
        
        # Discrete probability distribution (Probability Density Function) p(x) 
        distribution_p_x = rv_discrete(values=(x, p_x))
      
        # Generating a random number OR x_i for size number
        sample_distribution_p_x = distribution_p_x.rvs(size=1)[0] # x_i ~ p(x_i)
        input2.append(sample_distribution_p_x)
        ## Expected value
        Expected = sum(input2)/len(input2)
        input3.append(Expected)
    
        ## plot    
        y=input3
        x = list(range(1, len(input2) + 1))
    
        data=go.Scatter(x=x,y=y,mode='lines+markers',
                marker = dict(color = 'red',  size = 7,symbol = 'circle'),
                line = dict(color= 'red',width=1)
                )
    
        fig=go.Figure(data)
        
        fig.add_hline(
            y=3.5,
            line_width=3,
            line_color="green",
            line_dash="dash")
        
        fig.add_annotation(
            x=0.5,
            y=3.6,
            text="E[X]= μ= 3.5",
            showarrow=False,
            yshift=10,
            font=dict(size=16, color="green")
        )
            
        fig.update_layout(
        title='Monte Carlo Simulation',
        xaxis_title='Number of Samples',
        yaxis_title='Expected Value')
        
        ##
        output2=f"Outcome= {sample_distribution_p_x}"
        
        ## place image Dice
        output4= f'/assets/dice_{sample_distribution_p_x}.png'
        output6=True
        return fig,output2,input2,input3,output4,output6
    
    
    # Enter
    if ctx.triggered_id == "Enter_button":
        print(2222)
        output6=False
        return no_update,no_update,no_update,no_update,no_update,output6
    
    if ctx.triggered_id == "rolling_interval":
        print(input8)
        print()
   
        # for i in range(1,input7+1):
        x = np.array([1, 2, 3, 4, 5, 6])
        p_x = np.array([1/6,1/6,1/6,1/6,1/6,1/6])
        
        # Discrete probability distribution (Probability Density Function) p(x) 
        distribution_p_x = rv_discrete(values=(x, p_x))
      
        # Generating a random number OR x_i for size number
        sample_distribution_p_x = distribution_p_x.rvs(size=1)[0] # x_i ~ p(x_i)
        input2.append(sample_distribution_p_x)
        ## Expected value
        Expected = sum(input2)/len(input2)
        input3.append(Expected)
    
        ## plot    
        y=input3
        x = list(range(1, len(input2) + 1))
    
        data=go.Scatter(x=x,y=y,mode='lines+markers',
                marker = dict(color = 'red',  size = 7,symbol = 'circle'),
                line = dict(color= 'red',width=1)
                )
    
        fig=go.Figure(data)
        
        fig.add_hline(
            y=3.5,
            line_width=3,
            line_color="green",
            line_dash="dash")
        
        fig.add_annotation(
            x=0.5,
            y=3.6,
            text="E[X]= μ= 3.5",
            showarrow=False,
            yshift=10,
            font=dict(size=16, color="green")
        )
            
        fig.update_layout(
        title='Monte Carlo Simulation',
        xaxis_title='Number of Samples',
        yaxis_title='Expected Value')
        
        ##
        output2=f"Outcome= {sample_distribution_p_x}"
        
        ## place image Dice
        output4= f'/assets/dice_{sample_distribution_p_x}.png'
        
        
        if len(input2) == input7:
            output6 = True
        else:
            output6 = False
        
        return fig,output2,input2,input3,output4,output6



    
    return (
        no_update,
        no_update,
        no_update,
        no_update,
        no_update,
        no_update
    )

if __name__ == '__main__':
    app.run(
        debug=False,
        port=8051
    )
    
    
    