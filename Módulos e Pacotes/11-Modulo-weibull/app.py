import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Parâmetros da distribuição Weibull
shape_k = 1.5  # Parâmetro de forma (shape)
scale_lambda = 1  # Parâmetro de escala (scale)

# Valores de x
x = np.linspace(0, 3, 1000)

# Função de densidade de probabilidade (PDF) da Weibull
pdf = weibull_min.pdf(x, shape_k, scale=scale_lambda)

# Plotar o gráfico
plt.plot(x, pdf, label=f'Weibull (k={shape_k}, λ={scale_lambda})')
plt.title('Distribuição Weibull')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
