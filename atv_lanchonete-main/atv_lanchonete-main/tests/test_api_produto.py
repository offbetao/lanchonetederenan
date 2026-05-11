
def test_post_e_get_produto(client):

    response = client.post("/produtos", json={
        "codigo": 1,
        "valor": 10.0,
        "tipo": 2,
        "desconto_percentual": 0.0
    })

    assert response.status_code == 200
    data = response.json()

    assert data["codigo"] == 1
    assert data["valor"] == 10.0
    assert data["tipo"] == 2


def test_put_produto_atualiza_valor(client):

    client.post("/produtos", json={
        "codigo": 2,
        "valor": 5.0,
        "tipo": 1,
        "desconto_percentual": 0.0
    })

    response = client.put("/produtos/2/valor", json={
        "novo_valor": 7.5
    })

    assert response.status_code == 200
    assert response.json() == {"alterou": True}


def test_post_produto_invalido(client):

    response = client.post("/produtos", json={
        "valor": 10.0
    })

    assert response.status_code == 422



def test_criar_e_buscar_pedido(client):

    client.post("/clientes", json={
        "cpf": "12345678900",
        "nome": "Cliente Teste"
    })

    client.post("/produtos", json={
        "codigo": 3,
        "valor": 10.0,
        "tipo": 1,
        "desconto_percentual": 0.0
    })

    response_pedido = client.post("/lanchonete/pedidos", json={
        "cpf": "12345678900",
        "cod_produto": 3,
        "quantidade": 2
    })

    assert response_pedido.status_code == 200
    cod_pedido = response_pedido.json()["codigo"]

    response_get = client.get(f"/lanchonete/pedidos/{cod_pedido}")

    assert response_get.status_code == 200
    assert response_get.json()["codigo"] == cod_pedido