import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv(r"C:\Users\kelvin\Desktop\a8_d_Bebida.csv")

z = [0,0,0,0,0,0,0,0,0,0]
k = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,10):
	z[i] = x["Time"][i]
	k[i] = x["Bebida"][i]


plt.plot(z,k)

plt.xticks(rotation=90)

plt.title('Grafico')
plt.xlabel('Time')
plt.ylabel('Bebida')

plt.grid(True)

plt.show()
