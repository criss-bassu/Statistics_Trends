# -*- coding: utf-8 -*-
"""
@author: Cristina Baron Suarez
Student ID: 23069038
"""

import requests
import pandas as pd
# from datetime import datetime

# Lista de sitios de Andalucía en formato Python
# Dividiendo los sitios por provincias
andalucia = {
    "Sevilla": [
        "LA RODA DE ANDALUCÍA",
        "SEVILLA AEROPUERTO",
        "TOMARES, ZAUDÍN",
        "ALMADÉN DE LA PLATA"
    ],
    "Almería": [
        "ROQUETAS DE MAR",
        "ADRA",
        "ALMERÍA AEROPUERTO"
    ],
    "Cádiz": [
        "SAN FERNANDO",
        "TARIFA",
        "VEJER DE LA FRONTERA",
        "CHIPIONA",
        "SAN ROQUE"
    ],
    "Málaga": [
        "FUENGIROLA",
        "MÁLAGA, CENTRO METEOROLÓGICO",
        "NERJA",
        "RONDA INSTITUTO",
        "MARBELLA",
        "TORREMOLINOS",
        "BENAHAVÍS",
        "MANILVA",
        "COÍN",
        "ALGARROBO",
        "VÉLEZ-MÁLAGA"
    ],
    "Jaén": [
        "SANTA ELENA",
        "BAILÉN",
        "ANDÚJAR",
        "CAZORLA",
        "VILLANUEVA DEL ARZOBISPO",
        "LINARES"
    ],
    "Córdoba": [
        "ÉCIJA",
        "DOÑA MENCÍA",
        "PRIEGO DE CÓRDOBA",
        "MONTORO",
        "VILLARRASA",
        "CÓRDOBA AEROPUERTO"
    ],
    "Granada": [
        "GRANADA BASE AÉREA",
        "GRANADA AEROPUERTO",
        "MOTRIL, PUERTO",
        "GRAZALEMA",
        "ALCALÁ LA REAL"
    ],
    "Huelva": [
        "HUELVA, RONDA ESTE",
        "ALMONTE",
        "VALVERDE DEL CAMINO"
    ]
}

api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjYmFyb25zdWFyZXpwdWJAZ21haWwuY29tIiwianRpIjoiYzFmYmY2OTYtMTIyZS00NTQxLWIyNDAtNzQ0NDI3OTY3NzQyIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3Mjk1MDk5ODgsInVzZXJJZCI6ImMxZmJmNjk2LTEyMmUtNDU0MS1iMjQwLTc0NDQyNzk2Nzc0MiIsInJvbGUiOiIifQ.Glh-rQMx3viXlwbu9D7n-wBkpyKF-XwxnhQPzxH4Ua4'
base_url = 'https://opendata.aemet.es/opendata/api'

# Define the start and end dates for the data retrieval in AAAA-MM-DDTHH:MM:SSUTC format
fechaIniStr = '2023-04-01T00:00:00UTC'  # Start date
fechaFinStr = '2023-04-15T23:59:59UTC'  # End date

# Build the request URL
endpoint = f'/valores/climatologicos/diarios/datos/fechaini/{fechaIniStr}/fechafin/{fechaFinStr}/todasestaciones'
url = f'{base_url}{endpoint}'

# Set up headers with the API key
headers = {
    'api_key': api_key
}

# Make the GET request
response = requests.get(url, headers=headers)


# Check if the request was successful
if response.status_code == 200:
    data_url = response.json().get('datos')
    # Making a request to the URL that contains the data.
    if data_url:
        data_response = requests.get(data_url)
        # If the request is successful
        if data_response.status_code == 200:
            data = data_response.json() # Gets the data
            df_all = pd.DataFrame(data) # Transforms the data into a DataFrame
            # print(df_all.head())
            
            
            # Prueba
            df_andalucia = pd.DataFrame()   # Initializing empty dataset
            df_cities = pd.DataFrame()      # Initializing empty dataset
            for cities in andalucia.values():
                df_cities = df_all[df_all['nombre'].isin(cities)]   # Gets andalusian cities from the province that's being studied
                df_andalucia = pd.concat([df_andalucia, df_cities]) # Concats all cities
            
            #print(df_andalucia['nombre'].unique())
            #print(df_andalucia.columns)
            print(df_andalucia.loc[:, 'prec'])
        else:
            print(f"Failed to retrieve data: {data_response.status_code}")
    else:
        print("The URL for the data was not found.")
else:
    print(f"Error in the request: {response.status_code}")


