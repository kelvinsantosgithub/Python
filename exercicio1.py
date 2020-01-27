import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv(r"C:\Users\kelvin\Desktop\a8_d_Bebida.csv")

plt.plot(x["Time"], x["Bebida"])

plt.xticks(rotation=90)

plt.title('Grafico')
plt.xlabel('Time')
plt.ylabel('Bebida')

plt.grid(True)

plt.show()
