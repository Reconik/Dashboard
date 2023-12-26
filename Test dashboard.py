from dash import Dash, dcc, html, Input, Output, callback, dash
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('https://raw.githubusercontent.com/Reconik/Dashboard/Test-dashboard/text.csv')

app = Dash(__name__)

def tttt(a):
    return pd.to_datetime(a, format="%Y-%m-%d")


gg = df['Категория'].unique()
# df['Дата'] = tttt(df['Дата']).astype(int)/ 10**9


TEST = "FFFF"
app.layout = html.Div([


    html.Div([
    html.H1('График рассеивания'),
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            0,
            len(gg) - 1,
            step=None,
            value=0,
            marks={str(i): (str(gg[i])) for i in range(0, len(gg))},
            id='year-slider'
        )], style={'display': 'inline-lobck', 'width': '90%'}),

    html.H1('Круговой и "временной график" по категории'),
    html.Div([
        html.P("Категория:"),
        dcc.Dropdown(id='names',
                     options=df["Категория"].unique(),
                     value='Электроника', clearable=False
                     ),
    ], style={'width': '15%', 'float': 'left', 'display': 'inline-block'}),

    html.Div([dcc.Graph(id="piegraph"), ],
             style={'width': '60%', 'display': 'inline-block', 'padding': '0 20'}),

])

if __name__ == '__main__':
    app.run(debug=True)