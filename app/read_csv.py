import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    
    #obteniendo los encabezados de cada columna
    header = next(reader)
    #print(header)
    data = []
    
    #creando la lista de diccionarios
    for row in reader:
      #se une el encabezado y el dato de la fila en tuplas
      iterable = zip(header, row)
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
      #print(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])