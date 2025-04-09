<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BotCity Web Automation</title>
</head>
<body>
    <h1>BotCity Web Automation</h1>
    <p>Este é um exemplo de um bot simples que utiliza a biblioteca <strong>BotCity</strong> para realizar automações em navegadores, como abrir um site e interagir com ele. Este bot também envia screenshots para o Orchestrator da BotCity.</p>

    <h2>Requisitos</h2>
    <p>Antes de começar, você precisa ter o Python instalado e as dependências necessárias para rodar o bot.</p>
    
    <h3>Dependências</h3>
    <ul>
        <li>Python 3.x</li>
        <li><code>chromedriver</code> (certifique-se de que o <code>chromedriver</code> está na versão correta para o seu navegador Chrome)</li>
        <li><code>BotCity</code> (instalar o pacote necessário)</li>
    </ul>
    <p>Você pode instalar as dependências com o seguinte comando:</p>
    <pre><code>pip install botcity-core</code></pre>

    <h3>Obtendo a API Key do Orchestrator</h3>
    <p>Para interagir com o Orchestrator da BotCity, você precisa de uma chave de API. Crie uma conta no <a href="https://orchestrator.botcity.com.br" target="_blank">BotCity Orchestrator</a> e obtenha a chave de API.</p>

    <h2>Configuração</h2>
    <ol>
        <li>Clone este repositório ou copie o código para um arquivo Python no seu projeto.</li>
        <li>Substitua o valor da variável <code>API_KEY</code> pela chave obtida do Orchestrator.</li>
        <li>Certifique-se de que o <code>chromedriver</code> está disponível no caminho especificado (<code>bot.set_web_driver_path("chromedriver")</code>).</li>
    </ol>

    <pre><code>
API_KEY = "sua_api_key_aqui"  # Substitua pela sua chave de API
ORCHESTRATOR_URL = "https://orchestrator.botcity.com.br"  # URL do Orchestrator
    </code></pre>

    <h2>Como Rodar</h2>
    <ol>
        <li>Coloque o <code>chromedriver</code> no mesmo diretório do seu script ou forneça o caminho completo.</li>
        <li>Execute o script Python.</li>
    </ol>
    <pre><code>python nome_do_arquivo.py</code></pre>
    <p>O bot irá abrir o site do <a href="https://botcity.com.br" target="_blank">BotCity</a>, interagir com o elemento identificado e enviar uma captura de tela para o Orchestrator.</p>

    <h2>Descrição do Código</h2>

    <h3>Comunicação com o Orchestrator</h3>
    <p>O bot usa a <code>BotCityAPI</code> para se comunicar com o Orchestrator. Ele envia um arquivo de screenshot para o Orchestrator após executar a automação.</p>

    <pre><code>
botcity_api = BotCityAPI(api_key=API_KEY, orchestrator_url=ORCHESTRATOR_URL)
botcity_api.upload_file("screenshot.png", "screenshot.png")
    </code></pre>

    <h3>Ação do Bot</h3>
    <p>A função <code>action</code> define o que o bot vai fazer. No exemplo, o bot abre o site do BotCity, encontra o título da página e escreve "BotCity Bot". Depois, ele envia a captura de tela para o Orchestrator.</p>

    <pre><code>
def action(self, arg):
    self.browse("https://botcity.com.br")
    self.find_element("div#header h1")
    self.write("BotCity Bot")
    botcity_api.upload_file("screenshot.png", "screenshot.png")
    </code></pre>

    <h3>Início e Parada do Bot</h3>
    <p>O bot é iniciado e a ação é executada dentro do bloco <code>if __name__ == '__main__'</code>.</p>

    <pre><code>
if __name__ == '__main__':
    bot = MyBot()
    bot.set_web_driver_path("chromedriver")  # Caminho para o driver do Chrome
    bot.start()  # Inicia o bot
    bot.action(None)  # Executa a ação definida no método action
    bot.stop()  # Para o bot
    </code></pre>

    <h2>Contribuições</h2>
    <p>Sinta-se à vontade para contribuir com melhorias ou abrir issues caso encontre problemas!</p>

    <h2>Licença</h2>
    <p>Este projeto é licenciado sob a <a href="LICENSE" target="_blank">MIT License</a>.</p>

</body>
</html>