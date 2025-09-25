## Browser-Use

Conteúdo

- [O que é Browser-Use?](#O-que-é-Browser-Use?)
- [Processo de Instalação](#Processo-de-Instalação)
- [Configuração dos arquivos](#Configuração-dos-arquivos)
- [Preços das IAs](#Preços-das-IAs)
- [ Exportando automação para outros frameworks](#Exportando-automação-para-outros-frameworks)
- [Browser-Use Cloud](#Browser-Use-Cloud)
- [Vantagem x Desvantagem do Browser-use](#Vantagem-x-Desvantagem-do-Browser-use)

---

## O que é Browser-Use?

O **Browser-Use** é uma biblioteca de automação guiada por IA, diferente de frameworks tradicionais como Selenium ou Playwright.  
Aqui você descreve **o que deseja fazer em linguagem natural**, e o agente executa as ações no navegador.

O navegador é controlado pelo **Playwright**, que abre o Chromium/Firefox/WebKit, clica, digita, etc.

### Como funciona

- **LLM (ChatGoogle / ChatGPT)** → Decide o que fazer (abrir página, clicar, ler valor).  
- **Browser-Use** → Converte a decisão do LLM em comandos de automação (clicar em botões, ler textos, preencher formulários).  
- **Playwright** → Executa os comandos no navegador real.

💡 Resumindo:  
> LLM = mente, Browser-Use = tradutor de pensamentos em ações, Playwright = corpo que movimenta o navegador.

---

## Processo de Instalação

1. **Python 3.11 ou Superior** 
   - Download: [Python 3.11.9](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)  
   - Ou via Windows Terminal / PowerShell:  
   ```
   winget install Python.Python.3.11
   ```

2. **Instalar Browser-Use**
   ```
   pip install browser-use
   ```

3. **Instalar Playwright**
   ```
   python -m playwright install   
   ```


> Instala Chromium, Firefox e WebKit.
> 
> Para instalar apenas um navegador, substitua install por install chromium (ou firefox/webkit).

---

## Configuração dos arquivos

### 1. `.env`

Arquivo onde será armazenada a chave da IA utilizada:
   ```
    OPENAI_API_KEY=sua_chave_aqui
  ```

### 2. `main.py`
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

Para Executar a automação:

```
python main.py
```

---

## Preços das IAs

O Browser-Use depende de modelos externos de IA (ChatGPT, ChatGoogle, OpenAI, etc.).  
Cada modelo tem seu **custo próprio** (por exemplo, OpenAI cobra por token).

Alguns modelos podem ter **versões gratuitas com limitações**:

### Modelos Open-Source

Você pode usar LLMs gratuitos, instalando localmente ou via Hugging Face:

- **MPT (MosaicML)** → modelos de código aberto, roda localmente.  
- **LLaMA 2 / LLaMA 3 (Meta)** → grátis, mas precisa de máquina com boa GPU ou quantização para CPU.  
- **Falcon / Mistral / OpenLLaMA** → grátis, suporte a geração de texto, podem ser usados localmente.

⚠️ **Observação**: Modelos gratuitos via API quase sempre têm limite diário/mensal. Para automações contínuas, prefira modelos locais ou combine créditos gratuitos com APIs pagas.


---

## Exportando automação para outros frameworks

O Browser-Use permite gerar **código em outros frameworks** como Cypress ou Selenium.  
Basta definir a tarefa especificando o framework desejado.  

Exemplo: gerar código Cypress:

```
from browser_use import Agent, ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    task="Generate Cypress code to visit https://example.com and click the login button",
    llm=ChatOpenAI(model="gpt-3.5-turbo")
)
```

## Browser-use Cloud

Se você não quiser realizar a instalação e configuração localmente, também pode usar o Browser-use Cloud.

- Basta criar uma conta de acesso.

- Você pode rodar suas automações diretamente no ambiente deles.

- Não há necessidade de configurar ou pagar por APIs externas.

- Suporte tanto para desktop quanto mobile.

Essa opção é ideal para quem quer agilidade ou está começando a explorar a ferramenta.

```

## Vantagem x Desvantagem do Browser-use

### ✅ Vantagens

- Permite criar automações de forma rápida e simples, sem necessidade de escrever todo o script manualmente em frameworks como Selenium ou Playwright.

- Possibilidade de exportar o código gerado para frameworks tradicionais (ex: Cypress, Selenium), o que ajuda na manutenção e reaproveitamento.

- Excelente para prototipagem e testes rápidos, já que basta descrever em linguagem natural o que deseja fazer.

### ❌ Desvantagens

- Ao usar modelos de IA via API externa (OpenAI, Google, etc.), há custo por uso e limites de requisições.

- Caso opte por modelos open-source locais, é necessário ter uma máquina potente (CPU/GPU) para rodar de forma eficiente.

- Apesar de gerar código para frameworks, é importante ter conhecimento prévio neles para validar se o retorno está correto e seguro.

