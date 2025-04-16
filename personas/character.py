from personas import philosopher

def Persona(desc):
    
    match desc:
        case "life coach":
            return philosopher.new()
        case "tech bro":
            return "needs implimented"
        case "health coach":
            return "needs implimented"
        case _:
            return "We haven't gotten to that yet."

class Character:
    def __init__(self, title) -> None:
        self.persona = Persona(title)
