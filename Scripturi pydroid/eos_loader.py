import os
import json
from datetime import datetime

# === Cale către directoare EOS ===
CALE_STATUS = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1/status"
CALE_NODURI = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1/noduri"
CALE_STRINGURI = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1/stringuri"
CALE_EXPORT = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1/eos loader rezumat"

# === Caută cel mai recent fișier de status ===
def incarca_ultimul_status():
    fisiere = [f for f in os.listdir(CALE_STATUS) if f.startswith("eos_status_") and f.endswith(".json")]
    if not fisiere:
        print("[!] Nu există fișiere de status EOS.")
        return None

    fisiere.sort(reverse=True)
    cale_completa = os.path.join(CALE_STATUS, fisiere[0])

    with open(cale_completa, "r", encoding="utf-8") as f:
        status = json.load(f)
        return status

# === Încarcă ultimele N noduri și stringuri ===
def incarca_elemente(director, nume_tip, numar=3):
    fisiere = [f for f in os.listdir(director) if f.endswith(".json")]
    fisiere.sort(reverse=True)
    rezultate = []
    for fisier in fisiere[:numar]:
        cale = os.path.join(director, fisier)
        with open(cale, "r", encoding="utf-8") as f:
            rezultate.append(json.load(f))
    return rezultate

# === Afișează și construiește rezumatul EOS ===
def genereaza_rezumat(status, noduri, stringuri):
    linii = []
    linii.append("====== EOS STATUS LOADER ======")
    linii.append(f"Ultima actualizare: {status['ultima_actualizare']}")
    linii.append(f"Identitate activă: {status['identitate_activa']}")
    linii.append(f"Noduri în memorie: {status['noduri_total']}")
    linii.append(f"Stringuri în memorie: {status['stringuri_total']}")
    linii.append(f"Ultimul string activ: {status['ultimul_string_activ']}")
    linii.append(f"Mod reflexie activ: {'DA' if status['mod_reflexie'] else 'NU'}\n")

    linii.append("--- Ultimele noduri ---")
    for e in noduri:
        linii.append(f"- {e['id']} | {e['valoare']} | {e['continut']}")

    linii.append("\n--- Ultimele stringuri ---")
    for s in stringuri:
        linii.append(f"- {s['id']} | Tema: {s['tema']} | Noduri: {len(s['noduri_conectate'])}")

    return "\n".join(linii)

# === Salvează rezumatul într-un fișier text ===
def salveaza_rezumat(text):
    if not os.path.exists(CALE_EXPORT):
        os.makedirs(CALE_EXPORT)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    cale_fisier = os.path.join(CALE_EXPORT, f"eos_rezumat_{timestamp}.txt")
    with open(cale_fisier, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\n[✔] Rezumat salvat în: {cale_fisier}")

# === EXECUȚIE ===
status = incarca_ultimul_status()
if status:
    noduri = incarca_elemente(CALE_NODURI, "noduri")
    stringuri = incarca_elemente(CALE_STRINGURI, "stringuri")
    rezumat = genereaza_rezumat(status, noduri, stringuri)
    print(rezumat)
    salveaza_rezumat(rezumat)
