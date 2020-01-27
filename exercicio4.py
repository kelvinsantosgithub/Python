import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv(r"C:\Users\kelvin\Desktop\a8_d_Bebida.csv")

plt.boxplot(x["Bebida"])

plt.title('Grafico')
plt.xlabel('Time')
plt.ylabel('Bebida')

plt.grid(True)

plt.show()
