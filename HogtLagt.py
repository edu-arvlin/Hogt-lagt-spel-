import random
import json   

def ladda_highscore():
    try:
        with open("hogt_lagt.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("highscore", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

def spara_highscore(highscore):
    data = {"highscore": highscore}
    with open("hogt_lagt.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return highscore

    
def hogt_lagt():
    hemligt_tal = random.randint(1, 100)
    antal = 0

    while True:
        try:
            gissa = int(input("Gissa ett tal mellan 1 och 100: "))
            if gissa < 1 or gissa > 100:
                print("Ange ett tal mellan 1 och 100!")
                continue
            antal += 1
            if gissa < hemligt_tal:
                print("För lågt!")
            elif gissa > hemligt_tal:
                print("För högt!")
            else:
                print(f"Rätt! {antal} gissningar.")
                return antal
        except ValueError:
            print("Ogiltig inmatning. Ange ett heltal.")

def main():
    while True:
        print("\n---- HÖGT OCH LÅGT ----")
        print("1. Spela")
        print("2. Visa highscore")
        print("3. Avsluta")

        val = input("Välj: ")

        if val == "1":
            antal_gissningar = hogt_lagt()
            namn = input("Ange ditt username: ")
            
            current_highscore = ladda_highscore()
            if antal_gissningar < current_highscore or current_highscore == 0:
                spara_highscore(antal_gissningar)
                print(f"Nytt highscore sparades! {antal_gissningar} gissningar.")
            
            print(f"{namn} gissade rätt på {antal_gissningar} gissningar.")
        elif val == "2":
            highscore = ladda_highscore()
            if highscore == 0:
                print("Inget högscore sparat än.")
            else:
                print(f"Aktuellt highscore: {highscore} gissningar.")
        elif val == "3":
            print("Tack för att du spelade!")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()

