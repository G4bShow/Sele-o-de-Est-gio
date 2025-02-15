# Pydantic Schemas
from pydantic import BaseModel
from typing import List, Optional

# Esquemas de validação para cada entidade
class EmpresaBase(BaseModel):
    name: str
    cnpj: str 
    endereco: str
    email: str
    telefone: str
    
    
class Empresa(EmpresaBase):
    id: int  
    obrigacoes: List["ObrigacaoAcessoria"] = []
    
    class Config:
        orm_mode = True

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str
    
class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int 
    empresa_id: int 
    
    
    class Config:
        orm_mode = True