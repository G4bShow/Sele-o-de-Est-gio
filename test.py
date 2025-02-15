from fastapi.testclient import TestClient
from fastapi import FastAPI
from database import SessionLocal, get_db
from main import app

client = TestClient(app)

def test_criar_empresa():
    empresa = {"nome": "Empresa de Teste", "cnpj": "98765432109876", ...}
    response = client.post("/empresas", json=empresa)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Empresa de Teste"
    assert "id" in data

def test_listar_obrigacoes():
    # Assumindo que já existe uma empresa no banco de dados
    response = client.get("/obrigacoes_acessorias/1")
    assert response.status_code == 200
    assert len(response.json()) > 0