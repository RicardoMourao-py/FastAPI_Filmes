from fastapi import APIRouter,Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
################################ FILMES #############################################################
@router.get("/filmes", summary="Liste todos os filmes")
def listar_filmes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Responsável por retornar todas os filmes do nosso banco de dados

    Não possui argumentos.
    """

    filmes = crud.read_filmes(db, skip=skip, limit=limit)
    return filmes

@router.get("/filmes/{id_filme}", summary="Obtenha o seu filme")
def obter_filme(id_filme: int, db: Session = Depends(get_db)):
    """
    Obtenha um filme específico com seu determinado id.
    """

    db_filme = crud.read_filme(db=db, filme_id=id_filme)
    if db_filme is None:
        raise HTTPException(status_code=404, detail="Filme not found")
    return db_filme

@router.post("/filmes", summary="Adicione um filme")
def adicionar_filme(filme: schemas.FilmeCreate, db: Session = Depends(get_db)):
    """
    Adiciona filmes com suas características.

    - id_filme => Apesar de não estar visível, ele está autoincrementado no database.
    - nome => Nome do filme 
    - ano => Ano de lançamento do filme 
    - duracao => Duração em horas do filme 
    - descricao => Descrição da sinopse do filme 
    """

    # TODO: Não faz sentido verificar se o id nao existe entao 
    #       poderia fazer verificação por nome

    return crud.create_filme(db=db, filme=filme)
        

@router.put("/filmes/{id_filme}", summary="Atualize um filme")
async def atualizar_filme(id_filme: int, filme: schemas.FilmeUpdate, db: Session = Depends(get_db)):
    """
    Atualize um determinado filme com todas as suas caracteríticas.
    """

    db_filme = crud.update_filme(db=db, filme_id=id_filme, filme=filme)
    if db_filme is None:
        raise HTTPException(status_code=404, detail="Filme not found")
    return db_filme

@router.delete("/filmes/{id_filme}", summary="Delete um filme")
async def remover_filme(id_filme: int, db: Session = Depends(get_db)):
    """
    Delete um filme com o seu determinado Identificador. Lembre que caso remova um filme,
    não haverá mais comentários relacionados a ele.
    """

    db_filme = crud.delete_filme(db=db, filme_id=id_filme)
    if db_filme is None:
        raise HTTPException(status_code=404, detail="Filme not found")
    return db_filme
