# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:30:21 2020

@author: José Manuel Vera Lillo
"""
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from Figures_series import *
from Figures_maps import *
from aux_data import *

merged_covid = aux_data()

ls_day = merged_covid['fecha_informe'].unique()
ls_municipios = merged_covid['municipio_distrito'].unique()

ls_cc = []
ls_ta = []
ls_cct = []
ls_tat = []
for i in range(len(ls_day)):
    ls_CC = sum(merged_covid[merged_covid['fecha_informe'] == ls_day[i]]['casos_confirmados_ultimos_14dias'])
    ls_cc.append(ls_CC)
    ls_TA = sum(merged_covid[merged_covid['fecha_informe'] == ls_day[i]]['tasa_incidencia_acumulada_ultimos_14dias'])
    ls_ta.append(ls_TA)
    ls_CCT = sum(merged_covid[merged_covid['fecha_informe'] == ls_day[i]]['casos_confirmados_totales'])
    ls_cct.append(ls_CCT)
    ls_TAT = sum(merged_covid[merged_covid['fecha_informe'] == ls_day[i]]['tasa_incidencia_acumulada_total'])
    ls_tat.append(ls_TAT)

max_T = max(merged_covid['casos_confirmados_totales'].fillna(0))
max_c = max(merged_covid['casos_confirmados_ultimos_14dias'].fillna(0))
max_tT = max(merged_covid['tasa_incidencia_acumulada_total'].fillna(0))
max_t = max(merged_covid['tasa_incidencia_acumulada_ultimos_14dias'].fillna(0))

max_m_T = merged_covid[merged_covid['casos_confirmados_totales'] == max_T]['municipio_distrito'].unique()
max_m_c = merged_covid[merged_covid['casos_confirmados_ultimos_14dias'] == max_c]['municipio_distrito'].unique()
max_m_tT = merged_covid[merged_covid['tasa_incidencia_acumulada_total'] == max_tT]['municipio_distrito'].unique()
max_m_t = merged_covid[merged_covid['tasa_incidencia_acumulada_ultimos_14dias'] == max_tT]['municipio_distrito'].unique()

app = dash.Dash(__name__,
                requests_pathname_prefix='/app1/')
app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True
app.layout = html.Div([
    html.Div(id='top', children = [html.H1('Covid-19')]),
    html.Div(id='left', children = [
            dcc.Dropdown(
                    id='covid-dropdown',
                    options=[
                            {'label': 'Tasa acumulada TOTAL en los últimos 14 días', 'value': 'tat'},
                            {'label': 'TOTAL casos confirmados en los últimos 14 días', 'value': 'cct'},
                            {'label': 'Tasa acumulada en los últimos 14 días', 'value': 'ta'},
                            {'label': 'Casos confirmados en los últimos 14 días', 'value': 'cc'},
                        ],
                        value='tat',
                        placeholder='Selecciona el item a visualizar...'
                    ),
            html.Div(id='covid-graph-maps'),
            dcc.Slider(id='covid-slider',
                    min=0,
                    max=len(ls_day)-1,
                    marks={
                            0: ls_day[0],
                            len(ls_day)-1: str(ls_day[-1])
                        },
                    step=1,
                    value=0,
                )
            ]),

    html.Div(id='right', children = [html.Div(id='right-top',  children=[html.Div(id='covid-graph-series')]),
                                    html.Hr(),
                                    html.Div(id='right-back',children = [
                                            dbc.Row(dbc.Col(html.P("Máximo TOTAL casos confirmados:"), width="auto")),
                                            dbc.Row(dbc.Col(html.P(str(max_T) + ' - ' + str(max_m_T[0])), width="auto")),
                                            dbc.Row(dbc.Col(html.P("Máximo casos confirmados:"), width="auto")),
                                            dbc.Row(dbc.Col(html.P(str(max_c) + ' - ' + str(max_m_c[0])), width="auto")),
                                            dbc.Row(dbc.Col(html.P("Nota: La asa de Incidencia Acumulada (Casos confirmados por 100.000 habitantes)"), width="auto")),
                                            dbc.Row(dbc.Col(html.P("Máxima tasa de incidencia acumulada TOTAL:"), width="auto")),
                                            dbc.Row(dbc.Col(html.P(str(max_tT) + ' - ' + str(max_m_tT[0])), width="auto")),
                                            dbc.Row(dbc.Col(html.P("Máxima tasa de incidencia acumulada:"), width="auto")),
                                            dbc.Row(dbc.Col(html.P(str(max_t) + ' - ' + str(max_m_t[0])), width="auto")),
            ])
        ])
])

@app.callback(
    dash.dependencies.Output('covid-graph-maps', 'children'),
    [dash.dependencies.Input('covid-dropdown', 'value'),
     dash.dependencies.Input('covid-slider', 'value')])
def figure_maps(value, select):
    fig_map = Figures_maps(value, select)
    children = dcc.Graph(figure=fig_map)
    return (children)

@app.callback(
    dash.dependencies.Output('covid-graph-series', 'children'),
    [dash.dependencies.Input('covid-dropdown', 'value')])
def figure_series(value):
    fig_series = Figures_series(value)
    children = dcc.Graph(figure=fig_series)
    return (children)

#if __name__ == '__main__':
#    app.run_server(debug=False)
