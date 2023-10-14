import matplotlib.pyplot as plt

# Daten für den Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 6]

# Erstellen Sie ein Diagramm
plt.plot(x, y)

# Beschriftungen und Titel hinzufügen
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Einfacher Linienplot')

# Das Diagramm als PNG-Datei speichern
plt.savefig('linienplot.png')

# Das Diagramm anzeigen (optional, wenn Sie es sehen möchten)
# plt.show()

# Schließen Sie das Diagramm
plt.close()
