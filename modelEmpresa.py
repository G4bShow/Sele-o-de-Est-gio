from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field

from database import Base

class Empresa(BaseModel):
    id: int = Field(default=None, alias="id")
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class EmpresaDB(Base):
    __tablename__ = 'empresas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    endereco = Column(String)
    email = Column(String)
    telefone = Column(String)


class ObrigacaoAcessoria:
    pass