from .state import CoachState

# -----------------------------
# ROUTING FUNCTION
# -----------------------------

def route_intent(state: CoachState) -> str:
    return state["currunt_intent"]