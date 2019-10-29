import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from dash.dependencies import Input, Output
import datetime


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    dcc.Input(id='stock-input', value='BILI'),
    
    html.Div(id='output-graph')
])

@app.callback(
    Output(component_id="output-graph", component_property="children"),
    [Input(component_id='stock-input', component_property='value')]
)
def update_graph(input_data):
    start = datetime.datetime(2018, 1, 1)
    end = datetime.datetime.now()
    stock = input_data
    try:
        df = web.get_data_yahoo(stock, start, end)
    except:
        return "NO SUCH STOCK"
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True, drop=True)

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock},
            ],
            'layout': {
                'title': "Stock Graph of {}".format(stock)
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)