"""Visar at alle tall minus summen av deira siffere er delbare ved 9."""

def tallting(tall):
    return (tall - sum([int(siffer) for siffer in str(tall)])) % 9 == 0

if __name__ == "__main__":
    for i in range(1, 10**6):
        if not tallting(i):
            print(f"Ikkje rett for {i}.")