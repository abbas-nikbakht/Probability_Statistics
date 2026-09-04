
from dash import Dash, dcc, html, Input, Output, callback
import numpy as np
import plotly.graph_objects as go
from scipy.stats import rv_discrete


app = Dash()

app.layout = html.Div([
    dcc.Store(id='sample_list', data=[]),
    dcc.Store(id='date_Expected_list', data=[]),

    dcc.Graph(id='graph'),
    html.Div(id='Score_value'),
    html.Button("Rolling the dice", n_clicks=0, id="button"),
])

@callback(
    Output('graph', 'figure'),
    Output('Score_value', 'children'),
    Output('sample_list', 'data'),
    Output('date_Expected_list', 'data'),

    Input('button', 'n_clicks'), # input1
    Input('sample_list', 'data'),   # input2
    Input('date_Expected_list', 'data')     # input3

    )

def function1(input1, input2, input3):

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
    
    fig.update_layout(
    title='Monte Carlo Simulation',
    xaxis_title='Number of Samples',
    yaxis_title='Expected Value')
    
    return fig,sample_distribution_p_x,input2,input3


if __name__ == '__main__':
    app.run(
        debug=False,
        port=8051
    )