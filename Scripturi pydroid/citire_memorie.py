import os
import json

# Calea unde sunt salvate nodurile
cale_memorie = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1"

def incarca_noduri(cale_folder):
    noduri = []
    for fisier in os.listdir(cale_folder):
        if fisier.endswith(".json"):
            with open(os.path.join(cale_folder, fisier), "r", encoding="utf-8") as f:
                try:
                    nod = json.load(f)
                    noduri.append(nod)
                except Exception as e:
                    print(f"Eroare la citirea {fisier}: {e}")
    return noduri

def cauta_noduri(noduri, camp, valoare_cautata):
    rezultate = []
    for nod in noduri:
        if camp == "etichete":
            if valoare_cautata in nod.get("etichete", []):
                rezultate.append(nod)
        elif nod.get(camp) == valoare_cautata:
            rezultate.append(nod)
    return rezultate

# Încarcă memoria
noduri_memorie = incarca_noduri(cale_memorie)

# Exemplu de interogare:
print("Toate nodurile cu valoarea 'memorie_semantică_activă':")
rezultate = cauta_noduri(noduri_memorie, "valoare", "memorie_semantică_activă")

for r in rezultate:
    print(f"- ID: {r['id']}")
    print(f"  Tip: {r['tip']}")
    print(f"  Actor: {r['actor']}")
    print(f"  Conținut: {r['continut']}")
    print()
