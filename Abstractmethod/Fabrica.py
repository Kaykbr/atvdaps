from abc import ABC, abstractmethod

# Interface comum para os produtos
class Botao(ABC):
    @abstractmethod
    def render(self):
        pass

class Janela(ABC):
    @abstractmethod
    def exibir(self):
        pass

# Implementações concretas para Windows
class BotaoWindows(Botao):
    def render(self):
        return "Botão renderizado para Windows"

class JanelaWindows(Janela):
    def exibir(self):
        return "Janela exibida para Windows"

# Implementações concretas para macOS
class BotaoMacOS(Botao):
    def render(self):
        return "Botão renderizado para macOS"

class JanelaMacOS(Janela):
    def exibir(self):
        return "Janela exibida para macOS"

# Fábrica abstrata para criar famílias de produtos
class FabricaAbstrata(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass

# Fábrica concreta para Windows
class FabricaWindows(FabricaAbstrata):
    def criar_botao(self) -> Botao:
        return BotaoWindows()

    def criar_janela(self) -> Janela:
        return JanelaWindows()

# Fábrica concreta para macOS
class FabricaMacOS(FabricaAbstrata):
    def criar_botao(self) -> Botao:
        return BotaoMacOS()

    def criar_janela(self) -> Janela:
        return JanelaMacOS()

# Cliente
def criar_interface(fabrica: FabricaAbstrata):
    botao = fabrica.criar_botao()
    janela = fabrica.criar_janela()

    print(botao.render())
    print(janela.exibir())

# Demonstre o uso das fábricas para o sistema operacional atual
if __name__ == "__main__":
    sistema_operacional = "Windows"  # Altere para "macOS" para testar no macOS
    if sistema_operacional == "Windows":
        fabrica = FabricaWindows()
    elif sistema_operacional == "macOS":
        fabrica = FabricaMacOS()
    else:
        raise ValueError(f"Sistema operacional não suportado: {sistema_operacional}")

    criar_interface(fabrica)
