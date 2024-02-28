from abc import ABC, abstractmethod

# Interface comum para os produtos de renderização
class RenderizadorTextura(ABC):
    @abstractmethod
    def renderizar_textura(self, textura: str):
        pass

class RenderizadorSombra(ABC):
    @abstractmethod
    def renderizar_sombra(self, objeto: str):
        pass

# Implementações concretas para OpenGL
class RenderizadorOpenGLTextura(RenderizadorTextura):
    def renderizar_textura(self, textura: str):
        return f"OpenGL: Renderizando textura {textura}"

class RenderizadorOpenGLSombra(RenderizadorSombra):
    def renderizar_sombra(self, objeto: str):
        return f"OpenGL: Renderizando sombra para {objeto}"

# Implementações concretas para DirectX
class RenderizadorDirectXTextura(RenderizadorTextura):
    def renderizar_textura(self, textura: str):
        return f"DirectX: Renderizando textura {textura}"

class RenderizadorDirectXSombra(RenderizadorSombra):
    def renderizar_sombra(self, objeto: str):
        return f"DirectX: Renderizando sombra para {objeto}"

# Fábrica abstrata para criar famílias de produtos de renderização
class FabricaRenderizacao(ABC):
    @abstractmethod
    def criar_renderizador_textura(self) -> RenderizadorTextura:
        pass

    @abstractmethod
    def criar_renderizador_sombra(self) -> RenderizadorSombra:
        pass

# Fábrica concreta para OpenGL (implementada como Singleton)
class FabricaOpenGL(FabricaRenderizacao):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def criar_renderizador_textura(self) -> RenderizadorTextura:
        return RenderizadorOpenGLTextura()

    def criar_renderizador_sombra(self) -> RenderizadorSombra:
        return RenderizadorOpenGLSombra()

# Fábrica concreta para DirectX (implementada como Singleton)
class FabricaDirectX(FabricaRenderizacao):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def criar_renderizador_textura(self) -> RenderizadorTextura:
        return RenderizadorDirectXTextura()

    def criar_renderizador_sombra(self) -> RenderizadorSombra:
        return RenderizadorDirectXSombra()

# Cliente
def usar_renderizacao(fabrica: FabricaRenderizacao):
    renderizador_textura = fabrica.criar_renderizador_textura()
    renderizador_sombra = fabrica.criar_renderizador_sombra()

    print(renderizador_textura.renderizar_textura("textura1.png"))
    print(renderizador_sombra.renderizar_sombra("modelo3D"))

# Demonstre o uso das fábricas para o sistema de renderização atual
if __name__ == "__main__":
    sistema_renderizacao = "OpenGL"  # Altere para "DirectX" para testar com DirectX
    if sistema_renderizacao == "OpenGL":
        fabrica = FabricaOpenGL()
    elif sistema_renderizacao == "DirectX":
        fabrica = FabricaDirectX()
    else:
        raise ValueError(f"Sistema de renderização não suportado: {sistema_renderizacao}")

    usar_renderizacao(fabrica)
