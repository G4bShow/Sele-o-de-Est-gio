from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, get_db
from models import Empresa, ObrigacaoAcessoria
from schemas import EmpresaCreate, ObrigacaoAcessoriaCreate
from typing import List

app = FastAPI(
    title="API de Empresas",
    description="API para gerenciar empresas e obrigações acessórias",
    version="1.0.0",
    contact={
        "name": "Seu Nome",
        "email": "seu_email@example.com",
    },
)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/empresas/")
def read_empresas(db: SessionLocal = Depends(get_db)):
    return db.query(Empresa).all()

@app.post("/empresas/")
def create_empresa(empresa: EmpresaCreate, db: SessionLocal = Depends(get_db)):
    db_empresa = Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresas/{empresa_id}")
def read_empresa(empresa_id: int, db: SessionLocal = Depends(get_db)):
    return db.query(Empresa).filter(Empresa.id == empresa_id).first()

@app.put("/empresas/{empresa_id}")
def update_empresa(empresa_id: int, empresa: EmpresaCreate, db: SessionLocal = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    db_empresa.nome = empresa.nome
    db_empresa.cnpj = empresa.cnpj
    db_empresa.endereco = empresa.endereco
    db_empresa.email = empresa.email
    db_empresa.telefone = empresa.telefone
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.delete("/empresas/{empresa_id}")
def delete_empresa(empresa_id: int, db: SessionLocal = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    db.delete(db_empresa)
    db.commit()
    return {"mensagem": "Empresa excluída com sucesso"}

@app.post("/obrigacoes-acessorias/")
def create_obrigacao_acessoria(obrigacao_acessoria: ObrigacaoAcessoriaCreate, db: SessionLocal = Depends(get_db)):
    db_obrigacao_acessoria = ObrigacaoAcessoria(**obrigacao_acessoria.dict())
    db.add(db_obrigacao_acessoria)
    db.commit()
    db.refresh(db_obrigacao_acessoria)
    return db_obrigacao_acessoria

@app.get("/obrigacoes-acessorias/")
def read_obrigacoes_acessorias(db: SessionLocal = Depends(get_db)):
    return db.query(ObrigacaoAcessoria).all()

@app.get("/obrigacoes-acessorias/{obrigacao_acessoria_id}")
def read_obrigacao_acessoria(obrigacao_acessoria_id: int, db: SessionLocal = Depends(get_db)):
    return db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_acessoria_id).first()

@app.put("/obrigacoes-acessorias/{obrigacao_acessoria_id}")
def update_obrigacao_acessoria(obrigacao_acessoria_id: int, obrigacao_acessoria: ObrigacaoAcessoriaCreate, db: SessionLocal = Depends(get_db)):
    db_obrigacao_acessoria = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_acessoria_id).first()
    db_obrigacao_acessoria.nome = obrigacao_acessoria.nome
    db_obrigacao_acessoria.periodicidade = obrigacao_acessoria.periodicidade
    db.commit()
    db.refresh(db_obrigacao_acessoria)
    return db_obrigacao_acessoria