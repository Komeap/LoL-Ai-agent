from langchain_core.tools import tool

@tool
def analyze_lane_phase(lane: str, time_minute: int) -> str:
    """
    Analyse la phase de lane pour un joueur donné à un instant T (en minutes).
    Retourne des données mockées sur l'état de la wave.
    """
    if lane.lower() == "bot" and time_minute >= 10:
        return "Statut: La wave bot est push sous la T1 ennemie. Vision: River bot non wardée."
    elif lane.lower() == "mid":
        return f"Statut: À {time_minute} minutes, la wave Mid est en slow-push vers la tour alliée. Le midlaner ennemi a disparu de la vision depuis 15 secondes."
    return f"La lane {lane} à {time_minute} minutes est en état neutre."

@tool
def get_player_stats(summoner_name: str, role: str) -> str:
    """
    Récupère les statistiques actuelles d'un joueur dans la partie (KDA, CS/min, Golds).
    """
    if summoner_name.lower() == "mitross" and role.lower() == "mid":
        return "Joueur: Mitross (Mid) | KDA: 2/1/0 | CS/min: 8.5 | État: Avantage en golds (+400g sur le vis-à-vis)."
    return f"Joueur: {summoner_name} ({role}) | KDA: 0/0/0 | CS/min: 6.0 | État: Égalité."

@tool
def evaluate_objective_control(time_minute: int) -> str:
    """
    Évalue le contrôle des objectifs neutres (Drakes, Nashor, Grubs) sur la carte.
    """
    if time_minute >= 10 and time_minute < 15:
        return "Objectif critique: Le 2ème Drake (Infernal) spawn dans 45 secondes. Le Jungler ennemi a été repéré Top side il y a 20 secondes."
    return "Aucun objectif majeur contesté dans l'immédiat."

# Bloc de test pour vérifier l'ensemble des outils
if __name__ == "__main__":
    print("--- Test des outils mockés ---")
    print(get_player_stats.invoke({"summoner_name": "Mitross", "role": "Mid"}))
    print(analyze_lane_phase.invoke({"lane": "mid", "time_minute": 12}))
    print(evaluate_objective_control.invoke({"time_minute": 12}))