from sqlalchemy import Float, Column, ForeignKey, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship

from .database import Base

################################## Filme ############################################
class Filme(Base):
    __tablename__ = "filmes"

    id_filme = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True)
    nome = Column(String, nullable=True, unique=True)
    ano = Column(Integer, nullable=True)
    duracao = Column(Float, nullable=True)
    descricao = Column(String, nullable=True)

    avaliacoes = relationship("Avaliacao", backref='parent', passive_deletes=True)

################################## Avaliacao ########################################
class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id_avaliacao = Column(Integer, primary_key=True, nullable=True, unique=True, autoincrement=True)
    comentario = Column(String, nullable=True)
    nota = Column(Float, nullable=True)
    id_filme = Column(Integer, ForeignKey("filmes.id_filme", ondelete='CASCADE'))

    filme = relationship("Filme", back_populates="avaliacoes")

    __table_args__ = (
        CheckConstraint('nota >= 0 AND nota <= 10', name='check_nota'),
    )