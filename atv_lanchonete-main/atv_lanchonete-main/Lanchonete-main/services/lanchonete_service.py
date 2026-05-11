from domain.cliente import Cliente
from domain.produto import Produto
from domain.pedido import Pedido
from repositories.memory import db

class LanchoneteService:
    def criar_cliente(self, cpf: str, nome: str = "") -> Cliente:
        #regra simples: se já existe, retorna o mesmo
        if cpf in db.clientes_por_cpf:
            return db.clientes_por_cpf[cpf]
        cliente = Cliente(cpf=cpf, nome=nome)
        db.clientes_por_cpf[cpf] = cliente
        return cliente

    def obter_cliente(self, cpf: str) -> Cliente | None:
        return db.clientes_por_cpf.get(cpf)

    def criar_produto(self, codigo: int, valor: float, tipo: int, desconto_percentual: float = 0.0) -> Produto:
        produto = Produto(codigo=codigo, valor=valor, tipo=tipo, desconto_percentual=desconto_percentual)
        db.produtos_por_codigo[codigo] = produto
        return produto

    def obter_produto(self, codigo: int) -> Produto | None:
        return db.produtos_por_codigo.get(codigo)

    def alterar_valor_produto(self, codigo: int, novo_valor: float) -> bool:
        produto = self.obter_produto(codigo)
        if not produto:
            return False
        produto.valor = novo_valor
        return True

    def criar_pedido(self, cpf: str, cod_produto: int, qtd_max_produtos: int) -> Pedido | None:
        cliente = self.obter_cliente(cpf)
        produto = self.obter_produto(cod_produto)
        if not cliente or not produto:
            return None
        pedido = Pedido(cliente=cliente, qtd_max_produtos=qtd_max_produtos)
        if not pedido.adicionar_produto(produto):
            return None
        db.pedidos_por_codigo[pedido.codigo] = pedido
        return pedido

    def cancelar_pedido(self, cod_pedido: int) -> bool:
        pedido = self.pedido_repository.buscar_por_codigo(cod_pedido)

        if pedido is None:
            return False

        cancelado = pedido.canelar_pedido()
        return False


def listar_pedidos_cancelados(self):
    pedidos = self.pedido_repository.listar_todos()

    pedidos_cancelados = []

    for pedido in pedidos:

        if pedido.esta_cancelado:
            pedidos_cancelados.append(pedido)

        if pedidos_cancelados:
            return pedidos_cancelados

    return []


service = LanchoneteService()