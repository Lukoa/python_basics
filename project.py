import csv 
import pandas as pd
import PIL
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial
import re

hum = []
tem = []
PATH = r'C:\Users\SEVENS\data_analysis.csv
fieldnames = ['Humidity','Temperature']
pattern = re.compile(r'-?\d+\.?\d*')

def extract_data():
  hum_empty_list = []
  tem_empty_list = []
  with open(PATH,'r') as rf:
    data = csv.reader(rf)
    #hum_vals = data['Humidity'].values.tolist()
    #tem_vals = data['Temperature'].values.tolist()
    #Df_hum = pd.DataFrame(int(hum_vals))
    #Df_hum = pd.DataFrame(int(tem_vals))
    #print(type(Df_hum.values.tolist()))
    big_list = list(data)
    for h_t_list in big_list:
      if len(h_t_list) == 0 or h_t_list == ['Humidity', 'Temperature']:
        pass
      else:
        hum_variabs,tem_variabs = float(h_t_list[0]),float(h_t_list[1])
        hum_empty_list.append(hum_variabs)
        tem_empty_list.append(tem_variabs)
  return [hum_empty_list,tem_empty_list]

def plot_live_graph(i):
  ser = serial.Serial('COM5', 9600)  # Replace 'COM#' with the appropriate port number
  line = ser.readline().decode('utf-8').strip()
  s = [float(s) for s in pattern.findall(line)]
  hum.append(s[0])
  tem.append(s[1])
  print(line)
  with open (PATH,'w') as fp:
    writer = csv.DictWriter(fp,fieldnames=fieldnames)
    writer.writeheader()
    for index,value in enumerate(range(len(hum))):
      writer.writerow({'Humidity':hum[index],'Temperature':tem[index]})

  variables = extract_data()
  humty = variables[0]
  tempr = variables[1]
  plt.cla()
  plt.plot(humty,tempr,color='red',linewidth=1,linestyle='--')
  plt.legend(loc='upper left', fontsize=16, facecolor='blue')
  plt.xlabel('Humidity ')
  plt.ylabel('Temperature')
  


ani = FuncAnimation(plt.gcf(),plot_live_graph,interval=3000)
plt.show()
plt.tight_layout()