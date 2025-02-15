from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cnpj = Column(String, unique=True)
    endereco = Column(String)
    email = Column(String)
    telefone = Column(String)

    obrigacoes_acessorias = relationship("ObrigacaoAcessoria", backref="empresa")

class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    periodicidade = Column(String)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))