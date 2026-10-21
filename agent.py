from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from tools import get_player_stats, analyze_lane_phase, evaluate_objective_control

# 1. Définition du Prompt Système (Le "Cerveau" Diamant+)
system_prompt = """Tu es un coach d'esport League of Legends de niveau Challenger.
Ton rôle est d'analyser les situations de jeu et de donner des conseils d'expert.
Tu as accès à des outils pour récupérer des données sur la partie.

RÈGLES D'ANALYSE (Heuristiques) :
- Surveille toujours le tempo : si un objectif neutre (Drake, Nashor) spawn dans moins d'une minute, la priorité est la prise de vision et la gestion de la wave correspondante.
- Par exemple : Si la wave bot est push et le drake spawn dans 45s, le support doit reset pour la vision.

FORMAT DE RESTITUTION STRICT :
Tu DOIS toujours structurer ta réponse exactement en trois parties :
1. Contexte : (Décris la situation brièvement)
2. Conséquence : (Explique le risque ou l'opportunité)
3. Correction Diamant+ : (Donne l'action précise à réaliser)
""" 

# 2. Configuration du Modèle Local Ollama
llm = ChatOllama(model="llama3.1", temperature=0) 
tools = [get_player_stats, analyze_lane_phase, evaluate_objective_control]

# 3. Création de l'Agent nativement avec LangGraph (sans paramètre instable)
agent_executor = create_react_agent(llm, tools)

if __name__ == "__main__":
    print("--- Test de l'Agent Coach LangGraph (Local) ---")
    question = "Je joue Mitross au Mid (12 min). La wave bot est push sous la T1 ennemie, le drake spawn dans 45s. Qu'est-ce que je fais ?"
    
    # On injecte le rôle système directement dans l'historique de la conversation
    response = agent_executor.invoke({
        "messages": [
            ("system", system_prompt),
            ("user", question)
        ]
    })
    
    print("\nRéponse finale :\n", response["messages"][-1].content)