from abc import ABC, abstractmethod

# Interface comum para os diferentes tipos de log
class ILog(ABC):
    @abstractmethod
    def registrar(self, msg: str):
        pass

# Implementação concreta para o log em arquivo
class LogArquivo(ILog):
    def registrar(self, msg: str):
        with open("log.txt", "a") as file:
            file.write(f"[Arquivo] {msg}\n")

# Implementação concreta para o log no console
class LogConsole(ILog):
    def registrar(self, msg: str):
        print(f"[Console] {msg}")

# Implementação concreta para o log em banco de dados
class LogBancoDeDados(ILog):
    def registrar(self, msg: str):
        # Simulação: aqui você conectaria ao banco de dados e registraria a mensagem
        print(f"[Banco de Dados] {msg}")

# Factory Method para criar diferentes tipos de logs
class LogFactory:
    def criar_log(self, tipo: str) -> ILog:
        if tipo == "arquivo":
            return LogArquivo()
        elif tipo == "console":
            return LogConsole()
        elif tipo == "banco":
            return LogBancoDeDados()
        else:
            raise ValueError(f"Tipo de log inválido: {tipo}")

# Demonstre o uso do Factory Method
if __name__ == "__main__":
    factory = LogFactory()

    # Criando diferentes tipos de logs
    log_arquivo = factory.criar_log("arquivo")
    log_console = factory.criar_log("console")
    log_banco = factory.criar_log("banco")

    # Registrando mensagens
    log_arquivo.registrar("Mensagem de log no arquivo")
    log_console.registrar("Mensagem de log no console")
    log_banco.registrar("Mensagem de log no banco de dados")
