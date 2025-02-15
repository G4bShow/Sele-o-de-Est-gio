from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel, Field

from database import Base

class ObrigacaoAcessoria(BaseModel):
    id: int = Field(default=None, alias="id")
    nome: str
    periodicidade: str
    empresa_id: int

class ObrigacaoAcessoriaDB(Base):
    __tablename__ = 'obrigacoes_acessorias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    periodicidade = Column(String, nullable=False)
    empresa_id = Column(Integer, ForeignKey('empresas.id'))


class EmpresaDB:
    pass