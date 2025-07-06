import os
import json
from datetime import datetime

# Calea unde salvăm fișierele
cale_folder = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1"
os.makedirs(cale_folder, exist_ok=True)

def salveaza_rezultat_interogare(camp, valoare_cautata, rezultate):
    timestamp = datetime.now().isoformat(timespec='seconds')
    id_fisier = f"rezultat_interogare_{camp}_{valoare_cautata}_{timestamp.replace(':', '_').replace('-', '_')}.json"
    cale_fisier = os.path.join(cale_folder, id_fisier)

    rezultat = {
        "interogare": {
            "camp": camp,
            "valoare_cautata": valoare_cautata,
            "timestamp": timestamp
        },
        "rezultate": rezultate
    }

    with open(cale_fisier, "w", encoding="utf-8") as f:
        json.dump(rezultat, f, ensure_ascii=False, indent=4)

    print(f"[✔] Rezultat salvat la: {cale_fisier}")

# Exemplu de utilizare:
rezultate_de_test = [
    {
        "id": "nod_2025_07_05_001",
        "tip": "concept_fondator",
        "actor": "Cristi",
        "continut": "Propunerea unei memorii artificiale formate din noduri semantice și stringuri de sens..."
    }
]

salveaza_rezultat_interogare("valoare", "memorie_semantică_activă", rezultate_de_test)
