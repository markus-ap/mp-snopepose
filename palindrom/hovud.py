def er_palindrom(tekst : str) -> bool:
    return tekst.lower() == tekst.lower()[::-1]

def hovud():
    if er_palindrom("regninger"):
        print("anagram")
        return

    print("ikkje anagram")

if __name__ == "__main__":
    hovud()