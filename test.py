import pytest # type: ignore
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_empresa():
    empresa = {"nome": "Empresa Teste", "cnpj": "12345678901234", "endereco": "Rua Teste, 123", "email": "teste@example.com", "telefone": "1234567890"}
    response = client.post("/empresas/", json=empresa)
    assert response.status_code == 201
    assert response.json()["nome"] == empresa["nome"]

def test_read_empresas():
    response = client.get("/empresas/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_empresa():
    empresa = {"nome": "Empresa Teste", "cnpj": "12345678901234", "endereco": "Rua Teste, 123", "email": "teste@example.com", "telefone": "1234567890"}
    response = client.post("/empresas/", json=empresa)
    empresa_id = response.json()["id"]
    empresa_update = {"nome": "Empresa Teste Update", "cnpj": "12345678901234", "endereco": "Rua Teste, 123", "email": "teste@example.com", "telefone": "1234567890"}
    response = client.put(f"/empresas/{empresa_id}", json=empresa_update)
    assert response.status_code == 200
    assert response.json()["nome"] == empresa_update["nome"]

def test_delete_empresa():
    empresa = {"nome": "Empresa Teste", "cnpj": "12345678901234", "endereco": "Rua Teste, 123", "email": "teste@example.com", "telefone": "1234567890"}
    response = client.post("/empresas/", json=empresa)
    empresa_id = response.json()["id"]
    response = client.delete(f"/empresas/{empresa_id}")
    assert response.status_code == 200
    assert response.json()["mensagem"] == "Empresa excluída com sucesso"