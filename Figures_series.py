# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:30:23 2020

@author: veral
"""
import pandas as pd

import plotly.graph_objects as go

from aux_data import *
        
merged_covid = aux_data()

ls_day = merged_covid['fecha_informe'].unique()
ls_municipios = merged_covid['municipio_distrito'].unique()

ls_cc = []
ls_ta = []
ls_cct = []
ls_tat = []
for i in range(len(ls_day)):
    ls_CC = sum(merged_covid[merged_covid['fecha_informe'] == ls_day[i]]['casos_confirmados_ultimos_14dias'].fillna(0))
    ls_cc.append(ls_CC)
    ls_TA = sum(merged_covid[merged_covid['fecha_informe'] == ls_day[i]]['tasa_incidencia_acumulada_ultimos_14dias'].fillna(0))
    ls_ta.append(ls_TA)
    ls_CCT = sum(merged_covid[merged_covid['fecha_informe'] == ls_day[i]]['casos_confirmados_totales'].fillna(0))
    ls_cct.append(ls_CCT)
    ls_TAT = sum(merged_covid[merged_covid['fecha_informe'] == ls_day[i]]['tasa_incidencia_acumulada_total'].fillna(0))
    ls_tat.append(ls_TAT)

def Figures_series(choose_figure):
    fig = go.Figure()
    if choose_figure == 'tat':
        #Series temporales.
        #Tasa acumulada TOTAL en los últimos 14 días:
        fig = go.Figure((go.Scatter(
            x=ls_day,
            y=ls_tat,
            name='Total Madrid',
            mode="lines"
        )))
        for i in range(len(ls_municipios)):
            fig.add_trace(go.Scatter(
                x=merged_covid[merged_covid['municipio_distrito'] == ls_municipios[i]]['fecha_informe'],
                y=merged_covid[merged_covid['municipio_distrito'] == ls_municipios[i]]['tasa_incidencia_acumulada_total'],
                name=ls_municipios[i],
                mode="lines",
                visible='legendonly'
            ))
    elif choose_figure == 'cct':
        #Total casos confirmados en los últimos 14 días:
        fig = go.Figure((go.Scatter(
            x=ls_day,
            y=ls_cct,
            name='Total Madrid',
            mode="lines"
        )))
        for i in range(len(ls_municipios)):
            fig.add_trace(go.Scatter(
                x=merged_covid[merged_covid['municipio_distrito'] == ls_municipios[i]]['fecha_informe'],
                y=merged_covid[merged_covid['municipio_distrito'] == ls_municipios[i]]['casos_confirmados_totales'],
                name=ls_municipios[i],
                mode="lines",
                visible='legendonly'
            ))
    elif choose_figure == 'ta':
        #Tasa acumulada en los últimos 14 días:
        fig = go.Figure((go.Scatter(
            x=ls_day,
            y=ls_ta,
            name='Total Madrid',
            mode="lines"
        )))
        for i in range(len(ls_municipios)):
            fig.add_trace(go.Scatter(
                x=merged_covid[merged_covid['municipio_distrito'] == ls_municipios[i]]['fecha_informe'],
                y=merged_covid[merged_covid['municipio_distrito'] == ls_municipios[i]]['tasa_incidencia_acumulada_ultimos_14dias'],
                name=ls_municipios[i],
                mode="lines",
                visible='legendonly'
            ))
    elif choose_figure == 'cc':
        #Casos confirmados en los últimos 14 días:
        fig = go.Figure((go.Scatter(
            x=ls_day,
            y=ls_cc,
            name='Total Madrid',
            mode="lines"
        )))
        for i in range(len(ls_municipios)):
            fig.add_trace(go.Scatter(
                x=merged_covid[merged_covid['municipio_distrito'] == ls_municipios[i]]['fecha_informe'],
                y=merged_covid[merged_covid['municipio_distrito'] == ls_municipios[i]]['casos_confirmados_ultimos_14dias'],
                name=ls_municipios[i],
                mode="lines",
                visible='legendonly'
            ))
    else:
        fig.add_trace(go.Scatter(
            x = [],
            y = []
        ))
    fig.update_layout(title_text="Serie temporal por Municipio/distrito",
                      title_font=dict(family='Helvetica', color='#7D6F63'),
                      margin={"r":0,"t":25,"l":0,"b":100},
                      paper_bgcolor='#131211',
                      plot_bgcolor='#292E33',
                      xaxis_tickangle=-45,
                      width=600,
                      height=275
                     )
    fig.update_layout(
        legend=dict(
            traceorder="normal",
            font=dict(
                family="Helvetica",
                size=12,
                color="#7D6F63"
            )
        )
    )

    fig.update_xaxes(showgrid=False, zeroline=False, tickfont=dict(family='Helvetica', color='#7D6F63'))
    fig.update_yaxes(showgrid=False, zeroline=False, tickfont=dict(family='Helvetica', color='#7D6F63'))
    return(fig)