"""
Final Assignment Part 2 — Automobile Sales Dashboard
XYZ Automotives | Recession Impact Analysis
IBM Data Analysis with Python
"""

import requests
import io
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

# ─────────────────────────────────────────────
# Load Data
# ─────────────────────────────────────────────
URL = ("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
       "d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv")

response = requests.get(URL)
response.raise_for_status()
df = pd.read_csv(io.StringIO(response.text))

year_list = sorted(df['Year'].unique().tolist())

# ─────────────────────────────────────────────
# 4.1: Create Dash App with Meaningful Title
# ─────────────────────────────────────────────
app = Dash(__name__)
app.title = "XYZ Automotives — Recession Impact on Automobile Sales"

# ─────────────────────────────────────────────
# 4.2: Layout with Dropdown Menus
# ─────────────────────────────────────────────
app.layout = html.Div([

    html.H1(
        "XYZ Automotives: Impact of Recession on Automobile Sales",
        style={
            'textAlign': 'center',
            'color': '#1a3a5c',
            'fontFamily': 'Arial, sans-serif',
            'padding': '20px',
            'backgroundColor': '#f0f4f8',
            'marginBottom': '0'
        }
    ),

    html.Div([

        # Dropdown 1 — Report Type
        html.Div([
            html.Label("Select Statistics Report:",
                       style={'fontWeight': 'bold', 'fontFamily': 'Arial'}),
            dcc.Dropdown(
                id='dropdown-statistics',
                options=[
                    {'label': 'Yearly Statistics',      'value': 'Yearly Statistics'},
                    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                ],
                placeholder='Select a report type',
                value='Yearly Statistics',
                style={'width': '100%'}
            )
        ], style={'width': '45%', 'padding': '10px'}),

        # Dropdown 2 — Year
        html.Div([
            html.Label("Select Year:",
                       style={'fontWeight': 'bold', 'fontFamily': 'Arial'}),
            dcc.Dropdown(
                id='select-year',
                options=[{'label': str(y), 'value': y} for y in year_list],
                placeholder='Select a year',
                value=year_list[-1],
                style={'width': '100%'}
            )
        ], style={'width': '45%', 'padding': '10px'})

    ], style={
        'display': 'flex',
        'justifyContent': 'space-around',
        'backgroundColor': '#e8edf2',
        'padding': '10px'
    }),

    # ──────────────────────────────────────────
    # 4.3: Output Container
    # ──────────────────────────────────────────
    html.Div(id='output-container', className='chart-grid',
             style={'padding': '20px'})

], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f9fbfd'})


# ─────────────────────────────────────────────
# 4.4: Callback — Enable/Disable Year Dropdown
# ─────────────────────────────────────────────
@app.callback(
    Output('select-year', 'disabled'),
    Input('dropdown-statistics', 'value')
)
def update_input_container(selected_statistics):
    """Disable year dropdown when Recession report is selected."""
    if selected_statistics == 'Yearly Statistics':
        return False   # year selection is relevant
    return True        # recession report uses all recession years


# ─────────────────────────────────────────────
# 4.5 + 4.6: Callback — Render Charts
# ─────────────────────────────────────────────
@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown-statistics', 'value'),
     Input('select-year', 'value')]
)
def update_output_container(selected_statistics, input_year):

    # ─────────────────────────────────────────
    # 4.5: Recession Period Statistics Charts
    # ─────────────────────────────────────────
    if selected_statistics == 'Recession Period Statistics':

        recession_data = df[df['Recession'] == 1]

        # Chart R1 — Avg Sales Over Recession Years
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(figure=px.line(
            yearly_rec, x='Year', y='Automobile_Sales',
            title='Average Automobile Sales During Recession Years',
            markers=True,
            color_discrete_sequence=['tomato']
        ))

        # Chart R2 — Avg Sales by Vehicle Type
        avg_sales_vt = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(figure=px.bar(
            avg_sales_vt, x='Vehicle_Type', y='Automobile_Sales',
            title='Average Sales by Vehicle Type During Recession',
            color='Vehicle_Type',
            color_discrete_sequence=px.colors.qualitative.Set2
        ))

        # Chart R3 — Ad Expenditure Share (Pie)
        ad_exp = df.groupby('Recession')['Advertising_Expenditure'].sum().reset_index()
        ad_exp['Period'] = ad_exp['Recession'].map({0: 'Non-Recession', 1: 'Recession'})
        R_chart3 = dcc.Graph(figure=px.pie(
            ad_exp, values='Advertising_Expenditure', names='Period',
            title='Ad Expenditure Share: Recession vs Non-Recession',
            color_discrete_sequence=['steelblue', 'tomato']
        ))

        # Chart R4 — Ad Expenditure by Vehicle Type (Pie)
        ad_vt = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart4 = dcc.Graph(figure=px.pie(
            ad_vt, values='Advertising_Expenditure', names='Vehicle_Type',
            title='Ad Expenditure by Vehicle Type (Recession Period)',
            color_discrete_sequence=px.colors.qualitative.Pastel
        ))

        # Chart R5 — Unemployment Rate vs Sales by Vehicle Type
        unemp = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])[
            'Automobile_Sales'].mean().reset_index()
        R_chart5 = dcc.Graph(figure=px.line(
            unemp.sort_values('unemployment_rate'),
            x='unemployment_rate', y='Automobile_Sales',
            color='Vehicle_Type',
            title='Unemployment Rate Effect on Vehicle Sales (Recession)',
            markers=True
        ))

        return [
            html.Div([R_chart1, R_chart2],
                     style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '10px'}),
            html.Div([R_chart3, R_chart4],
                     style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '10px'}),
            html.Div([R_chart5])
        ]

    # ─────────────────────────────────────────
    # 4.6: Yearly Statistics Charts
    # ─────────────────────────────────────────
    elif selected_statistics == 'Yearly Statistics':

        yearly_data = df[df['Year'] == input_year]

        # Chart Y1 — Yearly Automobile Sales Line
        yearly_all = df.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(
            yearly_all, x='Year', y='Automobile_Sales',
            title='Yearly Average Automobile Sales (All Years)',
            markers=True,
            color_discrete_sequence=['steelblue']
        ))

        # Chart Y2 — Monthly Sales for Selected Year
        monthly = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(figure=px.line(
            monthly, x='Month', y='Automobile_Sales',
            title=f'Monthly Automobile Sales in {input_year}',
            markers=True,
            color_discrete_sequence=['darkorange']
        ))

        # Chart Y3 — Vehicle Type Sales for Selected Year (Bar)
        vt_sales = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].sum().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(
            vt_sales, x='Vehicle_Type', y='Automobile_Sales',
            title=f'Total Sales by Vehicle Type in {input_year}',
            color='Vehicle_Type',
            color_discrete_sequence=px.colors.qualitative.Set1
        ))

        # Chart Y4 — Advertising Expenditure by Vehicle Type (Pie)
        ad_vt_yearly = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(figure=px.pie(
            ad_vt_yearly, values='Advertising_Expenditure', names='Vehicle_Type',
            title=f'Ad Expenditure by Vehicle Type in {input_year}',
            color_discrete_sequence=px.colors.qualitative.Pastel
        ))

        return [
            html.Div([Y_chart1, Y_chart2],
                     style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '10px'}),
            html.Div([Y_chart3, Y_chart4],
                     style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '10px'})
        ]

    return html.Div("Please select a report type.", style={'color': 'gray', 'fontSize': '16px'})


if __name__ == '__main__':
    
    app.run(debug=True, port=8050)
