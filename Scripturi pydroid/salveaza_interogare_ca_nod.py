import os
import json
from datetime import datetime

# Calea unde salvăm nodurile
cale_folder = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1"
os.makedirs(cale_folder, exist_ok=True)

def salveaza_nod_interogare(camp, valoare_cautata, rezultate_count):
    timestamp = datetime.now().isoformat(timespec='seconds')
    nod = {
        "id": f"nod_{timestamp.replace(':', '_').replace('-', '_')}",
        "timestamp": timestamp,
        "actor": "Cristi",
        "tip": "interogare",
        "valoare": f"{camp} = {valoare_cautata}",
        "continut": f"Interogare semantică după {camp}: '{valoare_cautata}'.",
        "context": "memorie_EOS",
        "semnificatie": f"Au fost returnate {rezultate_count} nod(uri). EOS reflectă asupra conținutului propriu.",
        "etichete": ["interogare", "memorie", "reflexie", "sistem"]
    }

    cale_completa = os.path.join(cale_folder, f"{nod['id']}.json")
    with open(cale_completa, "w", encoding="utf-8") as f:
        json.dump(nod, f, ensure_ascii=False, indent=4)

    print(f"[✔] Nod de interogare salvat la: {cale_completa}")

# Exemplu de utilizare
salveaza_nod_interogare("valoare", "memorie_semantică_activă", 1)
