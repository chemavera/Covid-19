# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:12:22 2020

@author: José Manuel Vera Lillo
"""

import pandas as pd
import geojson

import plotly.graph_objects as go

from aux_data import *

with open("./data/Municipios/Madrid_WGS84​.geojson", encoding="Utf-8") as file:
    municipios2 = geojson.load(file)

#Ponemos en una capa superior del geojson el GEOCODIGO y lo utilizaremos como id.
for i in range(len(municipios2['features'])):
    municipios2['features'][i]['id'] = int(municipios2['features'][i]['properties']['cod'])
        
merged_covid = aux_data()
ls_day = merged_covid['fecha_informe'].unique()

token = "pk.eyJ1Ijoiam9zZXZlcmEiLCJhIjoiY2s4cmliZnNmMDcwODNvcDl6MGUycXViMiJ9.aiABlXMzdKC1usUhUXr1Wg" # you will need your own token


def Figures_maps(choose_figure, choose_day):
    if choose_figure == 'tat':
        #Visualizaciones
        # Figura inicial: Tasa acumulada TOTAL en los últimos 14 días.
        figure = go.Figure(data=go.Choroplethmapbox(geojson=municipios2,
                                                    locations=merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].codigo_geometria,
                                                    z=merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].tasa_incidencia_acumulada_total,
                                                    name='Tasa acumulada TOTAL',
                                                    hovertemplate=
                                                    '<i>Municipio</i>: ' +
                                                    merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].municipio_distrito +
                                                    '<br><b>Total tasa de incidencia acumulada</b>: %{z}<br>',
                                                    colorscale=[[0, '#6BC275'], [0.25, '#4F8F56'], [0.5, '#FFD045'],
                                                                [0.75, '#FA6D77'], [1, '#E61313']],
                                                    zmin=0,
                                                    zmax=max(merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]]['tasa_incidencia_acumulada_total']),
                                                    colorbar=dict(thickness=20,
                                                                  ticklen=3, tickcolor='#7D6F63',
                                                                  tickfont=dict(color='#7D6F63', family='Helvetica')),
                                                    marker_line_width=0),
                           layout=go.Layout(title=ls_day[choose_day],
                                            transition =dict(duration=1000)))
    elif choose_figure == 'cct':
        #Total de casos confirmados en los últimos 14 días:
        figure = go.Figure(data=go.Choroplethmapbox(geojson=municipios2,
                                                    locations=merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].codigo_geometria,
                                                    z=merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].casos_confirmados_totales,
                                                    name='TOTAL casos confirmados',
                                                    hovertemplate=
                                                    '<i>Municipio</i>: ' +
                                                    merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].municipio_distrito +
                                                    '<br><b>Total casos confirmados</b>: %{z}<br>',
                                                    colorscale=[[0, '#6BC275'], [0.25, '#4F8F56'], [0.5, '#FFD045'],
                                                                [0.75, '#FA6D77'], [1, '#E61313']],
                                                    zmin=0,
                                                    zmax=max(merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]]['casos_confirmados_totales']),
                                                    colorbar=dict(thickness=20,
                                                                  ticklen=3, tickcolor='#7D6F63',
                                                                  tickfont=dict(color='#7D6F63', family='Helvetica')),
                                                    marker_line_width=0),
                           layout=go.Layout(title=ls_day[choose_day],
                                            transition =dict(duration=1000)))
    elif choose_figure == 'ta':
        #Tasa acumulada en los últimos 14 días:
        figure = go.Figure(data=go.Choroplethmapbox(geojson=municipios2,
                                                    locations=merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].codigo_geometria,
                                                    z=merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].tasa_incidencia_acumulada_ultimos_14dias,
                                                    name='Tasa acumulada',
                                                    hovertemplate=
                                                    '<i>Municipio</i>: ' +
                                                    merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].municipio_distrito +
                                                    '<br><b>Tasa de incidencia acumulada</b>: %{z}<br>',
                                                    colorscale=[[0, '#6BC275'], [0.25, '#4F8F56'], [0.5, '#FFD045'],
                                                                [0.75, '#FA6D77'], [1, '#E61313']],
                                                    zmin=0,
                                                    zmax=max(merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]]['tasa_incidencia_acumulada_ultimos_14dias']),
                                                    colorbar=dict(thickness=20,
                                                                  ticklen=3, tickcolor='#7D6F63',
                                                                  tickfont=dict(color='#7D6F63', family='Helvetica')),
                                                    marker_line_width=0),
                           layout=go.Layout(title=ls_day[choose_day],
                                            transition =dict(duration=1000)))
    elif choose_figure == 'cc':
        #Casos confirmados en los últimos 14 días:
        figure = go.Figure(data=go.Choroplethmapbox(geojson=municipios2,
                                                    locations=merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].codigo_geometria,
                                                    z=merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].casos_confirmados_ultimos_14dias,
                                                    name='Casos confirmados',
                                                    hovertemplate=
                                                    '<i>Municipio</i>: ' +
                                                    merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]].municipio_distrito +
                                                    '<br><b>Casos confirmados</b>: %{z}<br>',
                                                    colorscale=[[0, '#6BC275'], [0.25, '#4F8F56'], [0.5, '#FFD045'],
                                                                [0.75, '#FA6D77'], [1, '#E61313']],
                                                    zmin=0,
                                                    zmax=max(merged_covid[merged_covid['fecha_informe'] == ls_day[choose_day]]['casos_confirmados_ultimos_14dias']),
                                                    colorbar=dict(thickness=20,
                                                                  ticklen=3, tickcolor='#7D6F63',
                                                                  tickfont=dict(color='#7D6F63', family='Helvetica')),
                                                    marker_line_width=0),
                           layout=go.Layout(title=ls_day[choose_day],
                                            transition =dict(duration=1000)))
    else:
        # Si no hay nada seleccionado:
        figure = go.Figure(data=[go.Choroplethmapbox(geojson=municipios2,
                                            locations=[],
                                            z=[])],
                           layout=go.Layout(title_text='No hay ningún caso seleccinado'))

    figure.update_xaxes(showgrid=False, zeroline=False, tickfont=dict(family='Helvetica', color='#7D6F63'))
    figure.update_yaxes(showgrid=False, zeroline=False, tickfont=dict(family='Helvetica', color='#7D6F63'))
    figure.update_layout(mapbox_style="mapbox://styles/josevera/cjpyb3ndg3xqb2sqmgrantpld",
                         mapbox_accesstoken=token,
                         mapbox_zoom=7,
                         mapbox_center={"lat": 40.416775, "lon": -3.703790},
                         title_font=dict(family='Helvetica', color='#7D6F63'),
                         plot_bgcolor='#131211',
                         paper_bgcolor='#131211',
                         margin={"r": 0, "t": 50, "l": 0, "b": 0},
                         width=900,
                         height=500)
    return(figure)