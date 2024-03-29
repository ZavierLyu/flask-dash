import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc 
import dash_html_components as html 
import plotly
import random
import plotly.graph_objects as go 
from collections import deque

random.seed(42)
X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

external_stylesheets = ['https://www.w3schools.com/w3css/4/w3.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)

@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph_scatter(input_data):
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

    data = go.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
        )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                yaxis=dict(range=[min(Y),max(Y)]))}


if __name__ == "__main__":
    app.run_server(debug=True)