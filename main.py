# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()







# class Produs(BaseModel):
#     id: int
#     nume: str
#     pret: float
#     stoc: int = 0          # valoare implicită
#     descriere: str | None = None   # câmp opțional

# inventar: list[Produs] = []


# @app.post("/produse", status_code=201)
# def adauga_produs(produs: Produs):
#     inventar.append(produs)
#     return produs

# @app.get("/produse/{produs_id}")
# def obtine_produs(produs_id: int):
#     for produs in inventar:
#         if produs.id == produs_id:
#             return produs
#     raise HTTPException(status_code=404, detail=f"Produsul cu ID-ul {produs_id} nu a fost găsit.")


# @app.get("/")
# def radacina():
#     """Endpoint de verificare a stării serviciului."""
#     return {"status": "activ"}

# @app.get("/utilizatori/{user_id}")
# def obtine_utilizator(user_id: int):
#     return {"id": user_id, "mesaj": f"Utilizatorul cu ID-ul {user_id}"}


# @app.get("/produse")
# def lista_produse(pagina: int = 1, per_pagina: int = 10):
#     return {
#         "pagina": pagina,
#         "per_pagina": per_pagina,
#         "mesaj": f"Returnează produsele de pe pagina {pagina}"
#     }

# vizualizare functionare exemple cod in laborator 2


#TLaborator 2 - gestionare inventar




from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Gestiune inventar", version="1.0.0")


class Produs(BaseModel):
    id: int
    nume: str
    pret: float
    stoc: int = 0


inventar: list[Produs] = []


# @app.get("/produse")
# def obtine_toate_produsele():
#     return inventar


@app.get("/produse")
def obtine_toate_produsele(stoc_minim: Optional[int] = None):
    if stoc_minim is None:
        return inventar

    return [produs for produs in inventar if produs.stoc < stoc_minim]

@app.post("/produse", status_code=201)
def adauga_produs(produs: Produs):
    inventar.append(produs)
    return produs


@app.put("/produse/{produs_id}")
def actualizeaza_produs(produs_id: int, produs_nou: Produs):
    for index, produs in enumerate(inventar):
        if produs.id == produs_id:
            inventar[index] = produs_nou
            return produs_nou

    raise HTTPException(
        status_code=404,
        detail=f"Produsul cu ID-ul {produs_id} nu a fost găsit."
    )


@app.delete("/produse/{produs_id}")
def sterge_produs(produs_id: int):
    for index, produs in enumerate(inventar):
        if produs.id == produs_id:
            produs_sters = inventar.pop(index)
            return produs_sters

    raise HTTPException(
        status_code=404,
        detail=f"Produsul cu ID-ul {produs_id} nu a fost găsit."
    )


