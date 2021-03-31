import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_proces(url):
    df1 = (
        pd.read_csv(url, sep=';', decimal=',')
        .dropna(axis=1, how='all')
        .dropna(how='all')
    )
    df1['CO(GT)'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['PT08.S1(CO)'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['NMHC(GT)'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['C6H6(GT)'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['PT08.S2(NMHC)'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['NOx(GT)'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['PT08.S3(NOx)'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['NO2(GT)'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['PT08.S4(NO2)'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['PT08.S5(O3)'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['T'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['RH'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1['AH'].replace(to_replace=-200, value=np.NaN, inplace=True)
    df1.columns=['Date', 'Time', 'Cobalt (GT)', 'Tin Oxide (CO)', 'Non-metallic Hydrocarbons (GT)', 'Benzene (GT)', 'Titania (NMHC)', 'Nitrogen Oxide (GT)', 'Tungsten Oxide (NOx)', 'Nitric Oxide (GT)', 'Tungsten Oxide (NO2)', 'Indium Oxide (O3)', 'Temperature (C)', 'Relative Humidity (%)', 'Absolute Humidity (%)']
    return df1

© 2021 GitHub, Inc.