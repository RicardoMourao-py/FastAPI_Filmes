from sqlalchemy.orm import Session

from . import models, schemas

############################### CRUD Filmes ################################################
def read_filme(db: Session, filme_id: int):
    return db.query(models.Filme).filter(models.Filme.id_filme == filme_id).first()
  
def read_filmes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Filme).offset(skip).limit(limit).all()

def create_filme(db: Session, filme: schemas.FilmeCreate):
    db_filme = models.Filme(**filme.dict())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme

def update_filme(db: Session, filme_id: int, filme: schemas.FilmeUpdate):
    db_filme = db.query(models.Filme).filter(models.Filme.id_filme == filme_id).first()
    for key, value in filme.dict().items():
        setattr(db_filme, key, value)
    db.commit()
    db.refresh(db_filme)
    return db_filme

def delete_filme(db: Session, filme_id: int):
    db_filme = db.query(models.Filme).filter(models.Filme.id_filme == filme_id).first()
    db.delete(db_filme)
    db.commit()
    return {"Filme deletado": db_filme}

############################### CRUD Avaliacoes ###########################################
def read_avaliacoes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Avaliacao).offset(skip).limit(limit).all()

def read_avaliacao(db: Session, filme_id: int):
    return db.query(models.Avaliacao).filter(models.Avaliacao.id_filme == filme_id).all()

def create_avaliacao(db: Session, avaliacao: schemas.AvaliacaoCreate):
    db_avaliacao = models.Avaliacao(**avaliacao.dict())
    db.add(db_avaliacao)
    db.commit()
    db.refresh(db_avaliacao)
    return db_avaliacao

def update_avaliacao(db: Session, avaliacao_id: int, avaliacao: schemas.AvaliacaoUpdate):
    db_avaliacao = db.query(models.Avaliacao).filter(models.Avaliacao.id_avaliacao == avaliacao_id).first()
    for key, value in avaliacao.dict().items():
        setattr(db_avaliacao, key, value)
    db.commit()
    db.refresh(db_avaliacao)
    return db_avaliacao

def delete_avaliacao(db: Session, avaliacao_id: int):
    db_avaliacao = db.query(models.Avaliacao).filter(models.Avaliacao.id_avaliacao == avaliacao_id).first()
    db.delete(db_avaliacao)
    db.commit()
    return {"Avaliação deletada": db_avaliacao}