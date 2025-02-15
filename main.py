from fastapi import FastAPI, Depends, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
from modelEmpresa import Empresa, ObrigacaoAcessoria
from schemas import (
    EmpresaSchemaIn,
    EmpresaSchemaOut,
    ObrigacaoAcessoriaSchemaOut,
)

app = FastAPI()
db = SessionLocal()  # Inicialize a sessão do banco de dados

@app.post("/empresas", response_model=EmpresaSchemaOut)
def criar_empresa(empresa: EmpresaSchemaIn):
    db_empresa = Empresa(**empresa.dict())  # Converte para o modelo SQLAlchemy
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresas/{empresa_id}", response_model=EmpresaSchemaOut)
def obter_empresa(empresa_id: int):
    db_empresa = db.get(Empresa, empresa_id)
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

# Rotas similares para outras operações CRUD...

@app.get("/obrigacoes_acessorias/{empresa_id}", response_model=list[ObrigacaoAcessoriaSchemaOut])
def listar_obrigacoes(empresa_id: int):
    obrigacoes = db.query(ObrigacaoAcessoria).filter_by(empresa_id=empresa_id).all()
    if not obrigacoes:
        raise HTTPException(status_code=404, detail="Obrigações não encontradas")
    return obrigacoes


app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    ...
    openapi_schema = get_openapi(
        title="API de Gestão de Obrigações",
        version="1.0.0",
        description="API para gerenciar empresas e suas obrigações acessórias.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi()

