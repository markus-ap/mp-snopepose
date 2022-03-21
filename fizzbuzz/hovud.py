oppslag = {
    3: "trier",
    5: "femmer",
    7: "syver"
}

def fizzbuzz(nummer: int) -> str:
    resultat = ""
    for nøkkel, verdi in oppslag.items():
        if nøkkel > nummer:
            break
        if nummer % nøkkel == 0:
            resultat += verdi 

    if resultat is "":
        return str(nummer)

    return resultat

def hovud():
    for tall in range(1, 22):
        fb = fizzbuzz(tall)
        print(tall, fb)

if __name__ == "__main__":
    hovud()