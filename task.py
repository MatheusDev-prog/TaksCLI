import sys
import json
from pathlib import Path

PATH = Path("data.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("sem argumentos necessários")
        sys.exit(1)

    comand = sys.argv[1]

    # ADD
    if comand == "add" and len(sys.argv) >= 4:
        desc = sys.argv[2]
        id_ = sys.argv[3]

        if not PATH.exists():
            with PATH.open("w", encoding="utf-8") as f:
                json.dump([], f)

        with PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            if item["id"] == id_:
                print("esse id já existe")
                sys.exit(1)

        newData = {
            "id": id_,
            "description": desc,
            "status": "todo"
        }

        data.append(newData)

        with PATH.open("w", encoding="utf-8") as f:
            json.dump(data, f)

        for key, value in newData.items():
            print(f"{key}: {value}")

    # UPDATE
    elif comand == "update" and len(sys.argv) >= 5:
        id_ = sys.argv[2]
        arg = sys.argv[3]
        val = sys.argv[4]

        with PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)

        found = False
        for i in range(len(data)):
            if data[i]["id"] == id_:
                if arg == "--description":
                    data[i]["description"] = val
                    found = True
                elif arg == "--status":
                    if val not in ("todo", "done", "in-progress"):
                        print("status inválido")
                        sys.exit(1)
                    data[i]["status"] = val
                    found = True
                else:
                    print("argumento inválido")
                    sys.exit(1)
                break

        if not found:
            print("id não encontrado")
            sys.exit(1)

        with PATH.open("w", encoding="utf-8") as f:
            json.dump(data, f)

        print(f"tarefa {id_} atualizada:")
        for key, value in data[i].items():
            print(f"{key}: {value}")

    # DELETE
    elif comand == "delete" and len(sys.argv) >= 3:
        id_ = sys.argv[2]

        with PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)

        found = False
        for i in range(len(data)):
            if data[i]["id"] == id_:
                found = True
                print("item encontrado:")
                for key, value in data[i].items():
                    print(f"{key}: {value}")
                esc = input("tem certeza que quer deletar? (Y/N): ").upper()
                if esc == "Y":
                    del data[i]
                    with PATH.open("w", encoding="utf-8") as f:
                        json.dump(data, f)
                    print("deletado com sucesso")
                else:
                    print("cancelado")
                break

        if not found:
            print("id não encontrado")

    # READER
    elif comand == "reader" and len(sys.argv) >= 3:
        alvo = sys.argv[2]

        with PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if alvo == "all":
            for item in data:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print()
        else:
            found = False
            for item in data:
                if item["id"] == alvo:
                    for key, value in item.items():
                        print(f"{key}: {value}")
                    found = True
                    break
            if not found:
                print("id não encontrado")

    else:
        print("comando inválido ou argumentos insuficientes")
