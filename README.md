# Browser-Use

## O que é Browser-Use

O **Browser-Use** é uma biblioteca de automação guiada por IA, diferente de frameworks tradicionais como Cypress ou Playwright.  
Aqui você descreve **o que deseja fazer em linguagem natural**, e o agente executa as ações no navegador.

O navegador é controlado pelo **Playwright**, que abre o Chromium/Firefox/WebKit, clica, digita, etc.

### 🔹 Como funciona

- **LLM (ChatGoogle / ChatGPT)** → Decide o que fazer (abrir página, clicar, ler valor).  
- **Browser-Use** → Converte a decisão do LLM em comandos de automação (clicar em botões, ler textos, preencher formulários).  
- **Playwright** → Executa os comandos no navegador real.

💡 Resumindo:  
> LLM = mente, Browser-Use = tradutor de pensamentos em ações, Playwright = corpo que movimenta o navegador.

---

## Processo de Instalação

1. **Python 3.11 ou 3.10**  
   - Download: [Python 3.11.9](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)  
   - Ou via Windows Terminal / PowerShell:  
     ```cmd
     winget install Python.Python.3.11
     ```

2. **Instalar Browser-Use**
   ```bash
   pip install browser-use

3° **Instalar Playwright**
  ```
   python -m playwright install   
   
  ```

> Instala Chromium, Firefox e WebKit.
> Caso queira apenas um navegador, substitua install por install chromium (ou firefox/webkit).

## Configuração dos arquivos

1° .env

Arquivo onde será armazenada a chave da IA utilizada:
   ```
    OPENAI_API_KEY=sua_chave_aqui
  ```

2° main.py
Arquivo principal do agente:

 ```

from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    task="Find the number of stars of the browser-use repo",
    llm=ChatGoogle(model="gemini-2.5-flash"),
    # browser=Browser(use_cloud=True),  # opcional: usar Browser-Use Cloud
)

agent.run_sync()

  ```

💡 O agente vai:

1 - Interpretar a tarefa usando o LLM.

2 - Converter a decisão em ações no navegador via Browser-Use.

3 - Executar os comandos no browser real com Playwright.

Preços das IAs

O Browser-Use depende de modelos externos de IA (ChatGPT, ChatGoogle, etc.).

Cada modelo tem custo próprio (ex.: OpenAI cobra por token).

Alguns modelos podem ter versões gratuitas com limitações.

Pontos positivos e negativos
Pontos	Browser-Use	Playwright/Selenium
Facilidade de uso	Alta (linguagem natural)	Média/baixa (scripts detalhados)
Velocidade	Média/baixa	Alta
Robustez	Média	Alta
Flexibilidade	Alta	Média
Custo	Pago (IA externa)	Gratuito

Resumo:

Browser-Use é ótimo para automações rápidas, fluxos complexos ou testes exploratórios.

Frameworks tradicionais são mais rápidos, robustos e gratuitos, mas exigem scripts detalhados.
