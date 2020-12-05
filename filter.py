import pandas as pd
            
epitope_data = pd.read_csv('Эпитопы.csv')
epitope_data['score'] = pd.to_numeric(epitope_data['score'], errors='coerce', downcast='float'
)
epitope_data['rank'] = pd.to_numeric(epitope_data['rank'], errors='coerce', downcast='float')

new_data = epitope_data[(epitope_data['rank'] < 2) & (epitope_data['score'] > 0.8)]

new_data.to_csv('new_epitope.csv')
