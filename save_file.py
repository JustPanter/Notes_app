import read_file
from read_file import read_file

def save_file(): # сохранение
    name_file = input("Как назвать файл?: ")
    df = read_file()
    return df.to_csv(name_file + ".csv", sep=";", index=False)
