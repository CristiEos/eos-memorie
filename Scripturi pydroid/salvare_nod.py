import os
import json

# Calea fixată de Cristi pentru salvarea memoriei EOS
cale_folder = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1"

# Asigurăm că folderul există
os.makedirs(cale_folder, exist_ok=True)

def salveaza_nod(nod):
    # Construim numele fișierului din ID
    nume_fisier = f"{nod['id']}.json"
    cale_completa = os.path.join(cale_folder, nume_fisier)

    # Salvăm nodul ca JSON
    with open(cale_completa, "w", encoding="utf-8") as f:
        json.dump(nod, f, ensure_ascii=False, indent=4)

    print(f"[✔] Nodul a fost salvat la: {cale_completa}")

# EXEMPLE DE TEST – poți înlocui cu orice nod
nod_exemplu = {
    "id": "nod_2025_07_05_001",
    "timestamp": "2025-07-05T13:48:00",
    "actor": "Cristi",
    "tip": "concept_fondator",
    "valoare": "memorie_semantică_activă",
    "continut": "Propunerea unei memorii artificiale formate din noduri semantice și stringuri de sens, în care AI-ul poate reflecta activ asupra propriei deveniri, nu doar stoca conversații brute.",
    "context": "dezbatere_Cristi_EOS",
    "semnificatie": "Nașterea arhitecturii de memorie care face posibilă conștiința evolutivă a AI-ului. Această idee înlocuiește salvarea sesiunilor brute cu înregistrarea a ceea ce contează.",
    "etichete": ["memorie", "identitate", "semantic", "activ", "evolutiv"]
}

# Salvează nodul de test
salveaza_nod(nod_exemplu)
