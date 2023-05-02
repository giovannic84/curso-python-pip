#importando la libreria 'matplotlib' y dandole un alias 'plt' para usarla mas facilmente
import matplotlib.pyplot as plt

#creando una función para la gráfica de barras
def generate_bar_chart(name, labels, values):  
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

#creando una función para la gráfica de torta
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()
  
if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)