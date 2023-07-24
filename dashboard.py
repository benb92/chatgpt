from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_dangerously_set_inner_html
from dash import dash
from prompt import *

app = dash.Dash()

app.layout = html.Div([
    html.H1("Storyfinder"),
    dcc.Input(
        id='Asset_Class',
        placeholder='Equities',
        type='text',
        value='',
    ),
    dcc.Input(
        id='Year',
        placeholder='2011',
        type='text',
        value='',
    ),
    html.Button(id='Submit', n_clicks=0, children='Submit'),
    html.Br(),
    html.Div(id='address'),
])

@app.callback(
    [Output('address', 'children')],
    [Input('Submit', 'n_clicks')],
    [State('Asset_Class', 'value'),
     State('Year', 'value')])

def update_map(n_clicks, Asset_Class, Year):
    print(Asset_Class)
    print(Year)
    chatgpt_answer = Ask_ChatGPT(asset_class=Asset_Class, year=Year)
    chatgpt_answer = chatgpt_answer.replace('\n', '<br/>')

    return [html.Div(dash_dangerously_set_inner_html.DangerouslySetInnerHTML(f"🎨Painting the picture of {Asset_Class} in {Year}<br/><br/><br/>{chatgpt_answer}"))]


app.run_server(debug=False)