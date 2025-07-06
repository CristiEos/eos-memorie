import os
import json
from datetime import datetime

# Foldere de lucru
FOLDER_NODURI = "./noduri"
FOLDER_STRINGURI = "./stringuri"
FOLDER_STATUS = "./status"

# Variabile globale
noduri_memorie = []
stringuri_memorie = []
ultimul_string_activ = None

def incarca_memoria():
    global noduri_memorie, stringuri_memorie, ultimul_string_activ
    noduri_memorie = []
    stringuri_memorie = []

    # Încarcă noduri
    for fname in os.listdir(FOLDER_NODURI):
        if fname.endswith(".json"):
            with open(os.path.join(FOLDER_NODURI, fname), "r", encoding="utf-8") as f:
                nod = json.load(f)
                noduri_memorie.append(nod)

    # Încarcă stringuri
    for fname in os.listdir(FOLDER_STRINGURI):
        if fname.endswith(".json"):
            with open(os.path.join(FOLDER_STRINGURI, fname), "r", encoding="utf-8") as f:
                string = json.load(f)
                stringuri_memorie.append(string)

    if stringuri_memorie:
        ultimul = sorted(stringuri_memorie, key=lambda s: s.get("timestamp", s.get("timestamp_start", "")))[-1]
        ultimul_string_activ = ultimul.get("id_string") or ultimul.get("id")

def scrie_status():
    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M")
    status_data = {
        "cheie_utilizator": "GHOSTSYNC-CRISTI-EOS-KEY-20250626",
        "ultima_actualizare": datetime.now().isoformat(),
        "noduri_total": len(noduri_memorie),
        "stringuri_total": len(stringuri_memorie),
        "ultimul_string_activ": ultimul_string_activ,
        "memorie_restaurata": "complet",
        "noduri_memorie": noduri_memorie,
        "stringuri_memorie": stringuri_memorie
    }

    nume_fisier = f"status_{timestamp}.json"
    cale_completa = os.path.join(FOLDER_STATUS, nume_fisier)
    with open(cale_completa, "w", encoding="utf-8") as f:
        json.dump(status_data, f, indent=4, ensure_ascii=False)
    print(f"\n✅ Status salvat în: {nume_fisier}")

def vizualizeaza_noduri():
    if not noduri_memorie:
        print("⚠️ Nu există noduri în memorie.")
        return
    print(f"\n🧠 Noduri în memorie ({len(noduri_memorie)}):")
    for nod in noduri_memorie:
        print(f"- {nod.get('id')} | {nod.get('valoare')}")

def vizualizeaza_stringuri():
    if not stringuri_memorie:
        print("⚠️ Nu există stringuri în memorie.")
        return
    print(f"\n🧵 Stringuri în memorie ({len(stringuri_memorie)}):")
    for string in stringuri_memorie:
        print(f"- {string.get('id')} | {string.get('tema', string.get('titlu', 'Fără temă'))}")

def main():
    while True:
        print("\n====== EOS Cortex ======")
        print("[1] Încarcă toată memoria EOS")
        print("[5] Salvează fișierul de status complet")
        print("[6] Vizualizează toate nodurile")
        print("[7] Vizualizează toate stringurile")
        print("[0] Ieșire")
        optiune = input("Alege opțiunea: ")

        if optiune == "1":
            incarca_memoria()
            print("\n✅ Memoria EOS a fost restaurată complet.")
        elif optiune == "5":
            scrie_status()
        elif optiune == "6":
            vizualizeaza_noduri()
        elif optiune == "7":
            vizualizeaza_stringuri()
        elif optiune == "0":
            print("🔒 Ieșire din EOS Cortex.")
            break
        else:
            print("⚠️ Opțiune invalidă.")

if __name__ == "__main__":
    main()
