# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:24:06 2020

@author: José Manuel Vera Lillo
"""

import pandas as pd

url = 'https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/b2a3a3f9-1f82-42c2-89c7-cbd3ef801412/download/covid19_tia_muni_y_distritos.csv'

def aux_data():
    merged_covid = pd.read_csv(url, encoding="ANSI", sep=';')

    for x in range(len(merged_covid['tasa_incidencia_acumulada_total'])):
        merged_covid.loc[x, 'tasa_incidencia_acumulada_ultimos_14dias'] = float(
        merged_covid.loc[x, 'tasa_incidencia_acumulada_ultimos_14dias'].replace(",", "."))
        merged_covid.loc[x, 'tasa_incidencia_acumulada_total'] = float(
        merged_covid.loc[x, 'tasa_incidencia_acumulada_total'].replace(",", "."))
        merged_covid.loc[x, 'fecha_informe'] = merged_covid.loc[x, 'fecha_informe'].replace(" 07:00:00", "")
    return(merged_covid)