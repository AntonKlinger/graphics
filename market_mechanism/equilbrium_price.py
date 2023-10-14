import matplotlib.pyplot as plt
import numpy as np

# Erstellen Sie ein Array von x-Werten
x = np.linspace(0, 5, 100)  # Erzeugt 100 Werte von 0 bis 5

# Erstellen Sie eine Funktion y = f(x), z.B. y = x^2
y1 = x**2
y2 = (x - 5)**2

# Erstellen Sie ein Diagramm für die erste Funktion (supply curve)
plt.plot(x, y1, color='blue', label='supply curve')

# Erstellen Sie ein Diagramm für die zweite Funktion (demand curve)
plt.plot(x, y2, color='red', label='demand curve')

# Koordinaten für den Punkt
x_point = 2.5
y_point = 6.4

# Legende hinzufügen
plt.legend()

# Punkt plotten
plt.scatter(x_point, y_point, color='white', marker='o', zorder=3, label='Punkt A')

# Beschriftungen und Titel anpassen
plt.xlabel('Menge', color='white')
plt.ylabel('Preis', color='white')
plt.title('Angebotskurve', color='white')  # Verwenden von LaTeX für mathematische Symbole

plt.text(2.7  , 6, 'equilbrium_price', fontsize=12, color='white')
# Achsenfarben anpassen
ax = plt.gca()
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')

plt.xlim(0, 5)  # X-Achse von 0 bis 5

# Achsenticks ausblenden
ax.set_xticks([])
ax.set_yticks([])

plt.ylim(0, 25)  # Y-Achse von 0 bis 25

# Das Diagramm als PNG-Datei mit transparentem Hintergrund speichern
plt.savefig('market_mechanism/equilbrium_price.png', transparent=True)

# Das Diagramm anzeigen (optional, wenn Sie es sehen möchten)
# plt.show()

# Schließen Sie das Diagramm
plt.close()
