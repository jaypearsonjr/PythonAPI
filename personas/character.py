from personas import philosopher as nerd

def Persona(desc):
    
    match desc:
        case "philospher":
            return nerd.new()
        case "techbro":
            return "techbro"
        case "healthCoach":
            return "health coach"
        case _:
            return "Something's wrong"

class Character:
    def __init__(self, title) -> None:
        self.persona = Persona(title)
