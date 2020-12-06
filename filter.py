import pandas as pd


num_of_rank = float(input("Введите рамку на rank(<): "))
num_of_score = float(input("Введите рамку на score(>): "))
file_name = input("Введите имя файла, в котором будет список эпитопов: ")
with open(file_name, 'w') as f:
    pass

dir_name = input('Укажите папку с данными: ')
a = int(input('Введите цифру на первом файле с результатом. Пример: result-15.csv => 15: '))
b = int(input('Введите цифру на последнем файле: '))


array_of_files = [f'result-{i}.csv' for i in range(a, b+1)]

df = pd.DataFrame()

for i in array_of_files:
    try:
        epitope_data = pd.read_csv(f'{dir_name}/{i}')
        epitope_data['score'] = pd.to_numeric(epitope_data['score'], errors='coerce', downcast='float'
)
        epitope_data['rank'] = pd.to_numeric(epitope_data['rank'], errors='coerce', downcast='float')
        new_data = epitope_data[(epitope_data['rank'] < num_of_rank) & (epitope_data['score'] > num_of_score)]

        df = pd.concat([df, new_data])
    except:
        pass


df.to_csv(file_name)
