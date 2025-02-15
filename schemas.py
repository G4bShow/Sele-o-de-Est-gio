from pydantic import BaseModel

class EmpresaSchemaIn(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class EmpresaSchemaOut(BaseModel):
    id: int
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str


class ObrigacaoAcessoriaSchemaIn:
    pass


class ObrigacaoAcessoriaSchemaOut:
    pass