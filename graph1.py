import matplotlib.pyplot as plt
import numpy as np

# Erstellen Sie ein Array von x-Werten
x = np.linspace(0, 5, 100)  # Erzeugt 100 Werte von 0 bis 5

# Erstellen Sie eine Funktion y = f(x), z.B. y = x^2
y = x**2

# Erstellen Sie ein Diagramm
plt.plot(x, y)

# Beschriftungen und Titel anpassen
plt.xlabel('quantity', color='white')
plt.ylabel('price', color='white')
plt.title('supply curve', color='white')  # Verwenden von LaTeX für mathematische Symbole

# Beschriftung der Funktion hinzufügen
plt.text(5, 23, '$S$', color='white', fontsize=12)  # Position (2, 10) und Text '$y = x^2'

# Achsenfarben anpassen
ax = plt.gca()
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')

# Achsenticks ausblenden
ax.set_xticks([])
ax.set_yticks([])

# Das Diagramm als PNG-Datei mit transparentem Hintergrund speichern
plt.savefig('supply_curve.png', transparent=True)

# Das Diagramm anzeigen (optional, wenn Sie es sehen möchten)
# plt.show()

# Schließen Sie das Diagramm
plt.close()
