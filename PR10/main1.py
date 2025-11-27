import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.001, 10, 500)
y = np.cos(x**2) / x
plt.figure(figsize=(10, 6))

plt.plot(
    x, y, 
    label=r'$Y(x) = \frac{\cos(x^2)}{x}$', 
    color='darkblue',         
    linestyle='solid',         
    linewidth=2                   
)

plt.title('Графік функції $Y(x) = \cos(x^2)/x$ в діапазоні $x \in [0, 10]$', fontsize=16)
plt.xlabel('Вісь X (Незалежна змінна)', fontsize=12)
plt.ylabel('Вісь Y (Значення функції)', fontsize=12)

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12, loc='upper right')
plt.savefig('task1_function_plot.png')

print("Графік функції збережено як 'task1_function_plot.png'")