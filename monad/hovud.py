class Jobb:
    def __init__(sjølv, tittel: str, lønn: int):
        sjølv.tittel = tittel
        sjølv.lønn = int(lønn)

    def bind(sjølv, funksjon):
        return funksjon(sjølv)

class Person:
    def __init__(sjølv, namn: str, bursdag:str, stilling: Jobb):
        sjølv.namn = namn
        sjølv.bursdag = bursdag
        sjølv.stilling = stilling
    
    def bind(sjølv, funksjon):
        return funksjon(sjølv)

def hent_jobb(person: Person) -> Jobb:
    return person.stilling

def hent_lønn(jobb: Jobb) -> int :
    return jobb.lønn

def hovud():
    markus = Person(namn="Markus", bursdag="1991-12-25", stilling=Jobb(tittel="Utvikler", lønn=710000))
    lønn = markus.bind(hent_jobb).bind(hent_lønn)
    print(lønn)

if __name__ == "__main__":
    hovud()