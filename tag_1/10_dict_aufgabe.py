"""
Gegeben sind zwei Listen:
Wir brauchen: for-loop, enumerate


geraete = ["Kühlschrank", "Fernseher", "Waschmaschine"]
stromverbrauch = ["1.2", "0.3", "2.0"]  # Angaben in kWh

Es soll ein Dict erstellt werden mit folgendem Aussehen:
{
'Fernseher': 0.3,
 'Kühlschrank': 1.2,
 'Waschmaschine': 2.0
 }
"""

geraete = ["Kühlschrank", "Fernseher", "Waschmaschine"]
stromverbrauch = ["1.2", "0.3", "2.0"]  # Angaben in kWh


verbrauch = {}  # leeres Dict erstellen

for i, geraet in enumerate(geraete):
    verbrauch[geraet] = float(stromverbrauch[i])
    # verbrauch["Kühl"] = 1.2

######################################################################

# Wir füllen ein leeres Dict mit neuen Schlüssel-Werte-Paar
verbrauch = {}

# 1. Iteration
g = "Kühlschrank"
i = 0
verbrauch[g] = stromverbrauch[i]

# 2. Iteration
g = "Fernseher"
i = 1
verbrauch[g] = stromverbrauch[i]

print(verbrauch)
