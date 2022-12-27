# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/shivam5992/temp-datasets/master/covid19_sg.csv");

print(df.columns)
print(df.tail(2))

fig = px.line(df, x="Date", y=["Cumulative Confirmed", "Cumulative Deaths"], title="Confirmed/Death Report")

app.layout = html.Div(children=[
    html.H2(
        children='Data Analysis - Covid 19 (Singapore)',
        style={
            'textAlign': 'center',
        }
    ),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')