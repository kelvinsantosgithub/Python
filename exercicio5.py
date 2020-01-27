import pandas as pd
import matplotlib.pyplot as plt

z = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
k = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

x = pd.read_csv(r"C:\Users\kelvin\Desktop\a8_d_Bebida.csv")

for i in range(0,30):
	z[i] = x["Time"][i]
	k[i] = x["Bebida"][i]

plt.plot(z,k, color="red")
plt.xticks(rotation=90)

plt.title('Grafico')
plt.xlabel('Time')
plt.ylabel('Bebida')

plt.grid(True)

plt.show()