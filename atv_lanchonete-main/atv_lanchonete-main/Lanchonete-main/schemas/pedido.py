from pydantic import BaseModel
from typing import List
class PedidoCreate(BaseModel):
    cpf: str
    cod_produto: int
    qtd_max_produtos: int = 10

class PedidoAddItem(BaseModel):
    cod_produto: int

class PedidoOut(BaseModel):
    codigo: int
    cpf: str
    esta_cancelado: bool
    esta_entregue: bool
    produtos: List[int]