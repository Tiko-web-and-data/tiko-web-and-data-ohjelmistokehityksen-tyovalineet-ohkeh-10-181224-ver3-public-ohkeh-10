import sys

def check_recipe_content():
        html = open("recipe.html", 'r')
        file_content = html.read()
        default = file_content.count("*nimi")
        print(default)
        
        if  default > 0 : # Tarkistetaan löytyykö html-tiedostosta *nimi tähän* -tekstiä"
            print(f"Lisätkää nimenne ja lempitäytteenne ohjeiden mukaan")
            sys.exit(1)
        else:
            print(f"Tiedot lisätty onnistuneesti!")

try :
    check_recipe_content()
except :
    print("Lisätkää nimenne ja lempitäytteenne ohjeiden mukaan")
    sys.exit(1)