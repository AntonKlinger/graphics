import matplotlib.pyplot as plt
import numpy as np

# Erstellen Sie ein Array von x-Werten
x = np.linspace(0, 6, 100)  # Erzeugt 100 Werte von 0 bis 5

# Erstellen Sie eine Funktion y = f(x), z.B. y = x^2
y = (x-6)**2

# Erstellen Sie ein Diagramm für die erste Funktion (Standardfarbe und Linienstil)
plt.plot(x, y, color='blue', label='original curve')

# Erstellen Sie eine Funktion y = f(x), z.B. y = x^2
x = np.linspace(0, 6, 100)  # Erzeugt 100 Werte von 0 bis 5

y = 0.8*(x-7)**2

# Erstellen Sie ein Diagramm für die erste Funktion (Standardfarbe und Linienstil)
plt.plot(x, y, color='blue', linestyle='--', label='new curve')

# Beschriftungen und Titel anpassen
plt.xlabel('Menge', color='white')
plt.ylabel('Preis', color='white')
plt.title('Nachfragekurve', color='white')  # Verwenden von LaTeX für mathematische Symbole

# Achsenfarben anpassen
ax = plt.gca()
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')

plt.xlim(0, 6)  # X-Achse von 0 bis 5
plt.ylim(0, 25)  # Y-Achse von 0 bis 25

# Achsenticks ausblenden
ax.set_xticks([])
ax.set_yticks([])

# Legende hinzufügen
plt.legend()

# Das Diagramm als PNG-Datei mit transparentem Hintergrund speichern
plt.savefig('demand_curve/to_the_right.png', transparent=True)

# Das Diagramm anzeigen (optional, wenn Sie es sehen möchten)
# plt.show()

# Schließen Sie das Diagramm
plt.close()
