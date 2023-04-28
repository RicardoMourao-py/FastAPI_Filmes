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

################################ AVALIACOES ##########################################################
@router.get("/avaliacoes", summary="Liste todas as avaliações")
async def listar_avaliacoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Responsável por retornar todas as avaliacoes do nosso banco de dados
    Não possui argumentos.
    """
    
    avaliacoes = crud.read_avaliacoes(db, skip=skip, limit=limit)
    return avaliacoes

@router.get("/avaliacoes/{id_filme}", summary="Obtenha a avaliação do seu filme")
async def obter_avaliacao(id_filme: int, db: Session = Depends(get_db)):
    """
    Obtenha uma avaliação específica de um filme com seu determinado id.
    """

    db_filme = crud.read_avaliacao(db=db, filme_id=id_filme)
    if db_filme is None:
        raise HTTPException(status_code=404, detail="Filme not found")
    return {"Avaliações do Filme escolhido": db_filme}

@router.post("/avaliacoes", summary="Adicione uma avaliação")
async def adicionar_avaliacao(avaliacao: schemas.AvaliacaoCreate, db: Session = Depends(get_db)):
    """
    Adiciona avaliações com suas características.
    - id_avaliacao => Apesar de não visível, está autoincrementado no database
    - id_filme => Identificador do Filme 
    - comentario => Deixe sua opinião sobre esse filme
    - nota => Forneça uma nota de 0 a 10 para o seu filme
    """
    db_filme = crud.read_filme(db=db, filme_id=avaliacao.id_filme)
    if db_filme is None:
        raise HTTPException(status_code=404, detail="Filme not found")
    return crud.create_avaliacao(db=db, avaliacao=avaliacao)
    

@router.put("/avaliacoes/{id_avaliacao}", summary="Atualize a sua avaliação do filme")
async def atualizar_avaliacao(id_avaliacao: int, avaliacao: schemas.AvaliacaoUpdate, db: Session = Depends(get_db)):
    """
    Atualize uma determinada avaliação com todas as suas caracteríticas.
    """

    db_avaliacao = crud.update_avaliacao(db=db, avaliacao_id=id_avaliacao, avaliacao=avaliacao)
    if db_avaliacao is None:
        raise HTTPException(status_code=404, detail="Avaliacao not found")
    return db_avaliacao
    
@router.delete("/avaliacoes/{id_avaliacao}", summary="Delete a sua avaliação do filme")
async def remover_avaliacao(id_avaliacao: int, db: Session = Depends(get_db)):
    """
    Delete uma avaliação com o seu determinado Identificador.
    """

    db_avaliacao = crud.delete_avaliacao(db=db, avaliacao_id=id_avaliacao)
    if db_avaliacao is None:
        raise HTTPException(status_code=404, detail="Avaliacao not found")
    return db_avaliacao