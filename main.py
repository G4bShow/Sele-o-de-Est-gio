# Configuração da Base de Dados e FastAPI
from fastapi import FastAPI, Depends, HTTPException
from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from . import models, schemas, crud


# Conexão com o Banco de Dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # ou use outro banco, como PostgreSQL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # Para SQLite

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# Config do SQLAlquemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Criar as tabelas no banco de dados
models.base.metadata.create_all(bind=engine)

app = FastAPI()


# Para obter a conexão no banco

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()    
        
# Endpoint para empresa
@app.post("/empresas/", response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaBase, db: Session = Depends(get_db)):
    return crud.create_empresa(db=db, empresa=empresa)

# Endpoint para todas as empresas
@app.get("/empresas/", response_model= list[schemas.Empresa])
def read_empresa(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_empresas(db=db, skip=skip, limit=limit)

# Endpoint para criar uma obrigação acessória
@app.post("/empresas/{empresa_id}/obrigacoes/", response_model=schemas.ObrigacaoAcessoria)
def create_obrigacao(empresa_id: int, obrigacao: schemas.ObrigacaoAcessoriaBase, db: Session = Depends(get_db)):
    return crud.create_obrigacao_acessoria(db=db, obrigacao=obrigacao, empresa_id=empresa_id)

# Endpoint para obter todas as obrigações acessórias de uma empresa
@app.get("/empresas/{empresa_id}/obrigacoes/", response_model=list[schemas.ObrigacaoAcessoria])
def get_obrigacoes(empresa_id: int, db: Session = Depends(get_db)):
    return crud.get_obrigacoes_por_empresa(db=db, empresa_id=empresa_id)