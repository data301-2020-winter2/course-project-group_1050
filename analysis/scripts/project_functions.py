import pandas as pd
import numpy as np


url = 'https://raw.githubusercontent.com/data301-2020-winter2/course-project-group_1050/main/data/raw/AirQualityUCI.csv'

def load_and_process(url):
    
    import pandas as pd
    import numpy as np
    

    url = 'https://raw.githubusercontent.com/data301-2020-winter2/course-project-group_1050/main/data/raw/AirQualityUCI.csv'

    
    ## Read data from url
    raw_data = pd.read_csv(url, sep=';', decimal=',')

    ## Method chain 1
    ## drop rows and columns that consist entirely of NaN
    tidier_data = raw_data.dropna(axis=1, how='all').dropna(how='all')
    
    ## replace values of -200 (specified as missing values) with NaN
    tidier_data['NMHC(GT)'].replace(to_replace=-200, value='NaN', inplace=True)
    
    ## rename columns into more more readable column names
    tidier_data.columns=['Date', 'Time', 'Cobalt (GT)', 'Tin Oxide (CO)', 'Non-metallic Hydrocarbons (GT)', 'Benzene (GT)', 'Titania (NMHC)', 'Nitrogen Oxide (GT)', 'Tungsten Oxide (NOx)', 'Nitric Oxide (GT)', 'Tungsten Oxide (NO2)', 'Indium Oxide (O3)', 'Temperature (C)', 'Relative Humidity (%)', 'Absolute Humidity (%)']
    
    ## convert absolute humidity to percentage
    tidier_data['Absolute Humidity (%)'] *= 100
    
    
    return tidier_data