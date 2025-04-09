from botcity.core import WebBot, BotCityAPI # type: ignore

#Configuracoes de comunciacao com o o Orchestrator
API_KEY = "sua_api_key_aqui" # Substitua pela sua chave de API
ORCHESTRATOR_URL = "https://orchestrator.botcity.com.br" # URL do Orchestrator

# Criacao do objeto BotCityAPI para comunicacao com o Orchestrator
botcity_api = BotCityAPI(api_key=API_KEY, orchestrator_url=ORCHESTRATOR_URL)

class MyBot(WebBot):

    def action(self, arg):
        # Um exemplo de automacao para abrir um site
        self.browse("https://botcity.com.br")
        self.find_element("div#header h1")
        self.write("BotCity Bot")

        # Enviar o screenshot para o Orchestrator
        botcity_api.upload_file("screenshot.png", "screenshot.png")

if __name__ == '__main__':
    bot = MyBot()
    bot.set_web_driver_path("chromedriver")  # Caminho para o driver do Chrome
    bot.start()  # Inicia o bot
    bot.action(None)  # Executa a ação definida no método action
    bot.stop()  # Para o bot