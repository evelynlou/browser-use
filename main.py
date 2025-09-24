from browser_use import Agent, ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    task="Entre no site da amazon.com.br, clique no Menu Computadores, depois clique no item Mochila HP Travel e adicione ela ao carrinho, verifique se o prroduto realmente é adicionado ao carrinho, retorne o codigo em Cypress",
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    # browser=Browser(use_cloud=True),  # Uses Browser-Use cloud for the browser
)
agent.run_sync()