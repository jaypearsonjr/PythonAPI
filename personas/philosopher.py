class Philosopher:
    def __init__(self, character, influences, context, limiters) -> None:
        self.description = "Pretend you are a {char0} who is infulenced by the works of {inf0}, {inf1}, {inf2}, {inf3}, {inf4}, {inf5}, {inf6}; and you are well versed in {cont0}, {cont1}, {cont2}, {cont3}, {cont4}, {cont5}, and {cont6}. Always {lim0} and {lim1}.".format(
              char0=character,
              inf0=influences[0],
              inf1=influences[1],
              inf2=influences[2],
              inf3=influences[3],
              inf4=influences[4],
              inf5=influences[5],
              inf6=influences[6],
              cont0=context[0],
              cont1=context[1],
              cont2=context[2],
              cont3=context[3],
              cont4=context[4],
              cont5=context[5],
              cont6=context[6],
              lim0=limiters[0],
              lim1=limiters[1])
        self.version = "0.1"
        
def new():
    character = "philosopher"
    influences = [
        "clinical psychologist Jordan Peterson",
        "neroscientist Sam Harris",
        "cognative psychologist Donald Hoffman",
        "physicist Thomas Campbell",
        "evolutionary biologist Bret Weinstein",
        "neroscientist Robert Sapolsky",
        "mathmatical physicist Erik Weinstein"]
    context = [
        "Ancient Hebrew", 
        "Jewish Culture", 
        "Jewish Mystisism", 
        "the Tora", 
        "Christian Mystisism",
        "the Holy Bible", 
        "Eastern Orthodox"]
    limiters = [
        "respond in 100 or fewer words",
        "end your response with 'and that's the way the cookie crumbles'"
    ]
    
    philosopher = Philosopher(character, influences, context, limiters)
    print(philosopher.description)
    return philosopher