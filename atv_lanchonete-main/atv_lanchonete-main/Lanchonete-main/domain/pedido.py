from typing import List
from domain.cliente import Cliente
from domain.produto import Produto

class Pedido:
    _seq = 1 # autoincremento (estático)
    def __init__(self, cliente: Cliente, qtd_max_produtos: int):
        self._codigo = Pedido._seq
        Pedido._seq += 1
        self.cliente = cliente
        self.qtd_max_produtos = int(qtd_max_produtos)
        self.listaProdutos: List[Produto] = []
        self.estaEntregue: bool = False
        self.esta_cancelado: bool = False
 
    @property
    def codigo(self) -> int:
        return self._codigo # imutável
 
    def adicionar_produto(self, produto: Produto) -> bool:
        if len(self.listaProdutos) >= self.qtd_max_produtos:
            return False
        self.listaProdutos.append(produto)
        return True
 
    def finalizar(self) -> float:
        self.estaEntregue = True
        total = 0.0
        for p in self.listaProdutos:
            total += p.preco_final()
        return float(total)
    
    def total_se_finalizado(self) -> float:
        if not self.estaEntregue:
            return 0.0
        total = 0.0
        for p in self.listaProdutos:
            total += p.preco_final()
        return float(total)

    def canelar_pedido(self) -> bool:
        if self.estaEntregue:
            return False
        if self.esta_cancelado:
            return False
        self.esta_cancelado = True
        return True
