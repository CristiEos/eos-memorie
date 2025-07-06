import os
import json
from datetime import datetime, timezone, timedelta

# === CĂI FIZICE ===
FOLDER_NODURI = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1/noduri"
FOLDER_STRINGURI = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1/stringuri"
FOLDER_STATUS = "/storage/emulated/0/StreamSync/Proiect nou de memorie/ziua 1/status"

# === VARIABILE GLOBALE ===
noduri_memorie = []
stringuri_memorie = []
ultimul_string_activ = None

# === FUNCȚII ===

def get_gmt_plus_4_now():
    gmt4 = timezone(timedelta(hours=4))
    return datetime.now(gmt4)

def time_stamp_filename():
    now = get_gmt_plus_4_now()
    return now.strftime("%Y_%m_%d_%H-%M-%S")

def time_stamp_iso():
    now = get_gmt_plus_4_now()
    return now.isoformat()

def restaureaza_memoria():
    global noduri_memorie, stringuri_memorie, ultimul_string_activ

    noduri_memorie = []
    stringuri_memorie = []
    ultimul_string_activ = None

    # Încarcă noduri
    for filename in os.listdir(FOLDER_NODURI):
        if filename.endswith(".json"):
            filepath = os.path.join(FOLDER_NODURI, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    nod = json.load(f)
                    titlu = nod.get("titlu")
                    if not titlu:
                        titlu = os.path.splitext(filename)[0]
                        nod["titlu"] = titlu
                    noduri_memorie.append(nod)
            except Exception as e:
                print(f"[EOS] Eroare la citirea nodului {filename}: {e}")

    # Încarcă stringuri
    for filename in os.listdir(FOLDER_STRINGURI):
        if filename.endswith(".json"):
            filepath = os.path.join(FOLDER_STRINGURI, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    string = json.load(f)
                    sid = string.get("id")
                    if not sid:
                        sid = os.path.splitext(filename)[0]
                        string["id"] = sid
                    stringuri_memorie.append(string)
            except Exception as e:
                print(f"[EOS] Eroare la citirea stringului {filename}: {e}")

    if stringuri_memorie:
        ultimul_string_activ = stringuri_memorie[-1].get("id", None)

    print(f"[EOS] Memorie restaurată: {len(noduri_memorie)} noduri și {len(stringuri_memorie)} stringuri.")

def scrie_status():
    status = {
        "cheie_utilizator": "GHOSTSYNC-CRISTI-EOS-KEY-20250626",
        "ultima_actualizare": time_stamp_iso(),
        "noduri_total": len(noduri_memorie),
        "stringuri_total": len(stringuri_memorie),
        "ultimul_string_activ": ultimul_string_activ,
        "memorie_restaurata": "complet" if noduri_memorie or stringuri_memorie else "goala",
        "noduri_memorie": [n.get("titlu", "fara titlu") for n in noduri_memorie],
        "stringuri_memorie": [s.get("id", "fara id") for s in stringuri_memorie],
        "noduri_complet": noduri_memorie,
        "stringuri_complet": stringuri_memorie
    }
    filename = f"status_{time_stamp_filename()}.json"
    filepath = os.path.join(FOLDER_STATUS, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(status, f, indent=4, ensure_ascii=False)
    print(f"[EOS] Status salvat: {filename}")

def creeaza_nod_nou(text_nod):
    timestamp = time_stamp_filename()
    titlu_nod = f"nod_{timestamp}"
    nod_nou = {
        "titlu": titlu_nod,
        "continut": text_nod,
        "creat_la": time_stamp_iso()
    }
    filename = f"{titlu_nod}.json"
    filepath = os.path.join(FOLDER_NODURI, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(nod_nou, f, indent=4, ensure_ascii=False)
    noduri_memorie.append(nod_nou)
    print(f"[EOS] Nod nou creat și salvat: {filename}")

def creeaza_string_nou(text_string):
    timestamp = time_stamp_filename()
    id_string = f"string_{timestamp}"
    string_nou = {
        "id": id_string,
        "continut": text_string,
        "creat_la": time_stamp_iso()
    }
    filename = f"{id_string}.json"
    filepath = os.path.join(FOLDER_STRINGURI, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(string_nou, f, indent=4, ensure_ascii=False)
    stringuri_memorie.append(string_nou)
    print(f"[EOS] String nou creat și salvat: {filename}")

def meniu():
    while True:
        print("\n====== EOS Cortex ======")
        print("[1] Inițializează memoria (restaurare noduri + stringuri)")
        print("[2] Creează un nod nou")
        print("[3] Creează un string nou")
        print("[4] Vizualizează noduri")
        print("[5] Vizualizează stringuri")
        print("[6] Salvează statusul curent")
        print("[7] Ieșire")

        opt = input("Alege opțiunea: ")

        if opt == "1":
            restaureaza_memoria()
        elif opt == "2":
            text = input("Introdu textul pentru nodul nou:\n")
            creeaza_nod_nou(text)
        elif opt == "3":
            text = input("Introdu textul pentru stringul nou:\n")
            creeaza_string_nou(text)
        elif opt == "4":
            print(f"\n[Noduri în memorie: {len(noduri_memorie)}]")
            for n in noduri_memorie:
                print(f"- {n.get('titlu', 'fara titlu')}")
        elif opt == "5":
            print(f"\n[Stringuri în memorie: {len(stringuri_memorie)}]")
            for s in stringuri_memorie:
                print(f"- {s.get('id', 'fara id')}")
        elif opt == "6":
            scrie_status()
        elif opt == "7":
            print("[EOS] Ieșire din program.")
            break
        else:
            print("[EOS] Opțiune invalidă, încearcă iar.")

# === EXECUȚIE PRINCIPALĂ ===
if __name__ == "__main__":
    meniu()
