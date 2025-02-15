# Configuração do SQLAlchemy e Banco de Dados
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresas'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    endereco = Column(String, unique=True, index=True)
    telefone = Column(String, unique=True, index=True)
    cnpj = Column(String, unique=True, index=True)
   
   
    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")
    
class ObrigacaoAcessoria(Base):
    __tablename__= "obrigacoes_acessorias"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    periodicidade = Column(String)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    
    
    empresa = relationship("Empresa", back_populates="obrigacoes")