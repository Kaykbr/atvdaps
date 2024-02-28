class Configuracao:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = "light"  # Configuração padrão: tema claro
            cls._instance.language = "English"  # Configuração padrão: idioma inglês
            cls._instance.font_size = 12  # Configuração padrão: tamanho da fonte 12
        return cls._instance

    def set_theme(self, theme):
        self.theme = theme

    def set_language(self, language):
        self.language = language

    def set_font_size(self, font_size):
        self.font_size = font_size

    def get_settings(self):
        return f"Theme: {self.theme}, Language: {self.language}, Font Size: {self.font_size}"

# Demonstre o uso da classe Configuracao
config = Configuracao()

# Acesse e modifique as configurações
config.set_theme("dark")  # Alterando o tema para escuro
config.set_language("Spanish")  # Alterando o idioma para espanhol
config.set_font_size(14)  # Alterando o tamanho da fonte para 14

# Acesse as configurações atualizadas
print(config.get_settings())

# Exemplo adicional: Modificando o tema de volta para claro
config.set_theme("light")
print(config.get_settings())
