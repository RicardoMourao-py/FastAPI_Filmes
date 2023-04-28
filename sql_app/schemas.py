from typing import List, Union
from pydantic import BaseModel

########### Classe Filme ###############
class FilmeBase(BaseModel):
    nome: str
    ano: int
    duracao: float
    descricao: str

class FilmeCreate(FilmeBase):
    pass

class FilmeUpdate(FilmeBase):
    pass

class Filme(FilmeBase):
    id_filme: int

    class Config:
        orm_mode = True

########### Classe Avaliacao ###############
class AvaliacaoBase(BaseModel):
    comentario: str
    nota: float
    
class AvaliacaoCreate(AvaliacaoBase):
    id_filme: int

class AvaliacaoUpdate(AvaliacaoBase):
    id_filme: int

class Avaliacao(AvaliacaoBase):
    id_avaliacao: int
    avaliacoes: List[Filme] = []

    class Config:
        orm_mode = True