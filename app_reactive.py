import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    dcc.Input(id='input', value='Enter something', type='text'),
    html.Div(id='output')
])
@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    return "{}".format(input_data)

if __name__ == "__main__":
    app.run_server(debug=True)