import sys
import subprocess
    
def get_branches():
    try:
        result = subprocess.run(  # Haetaan branchit remotesta, koska Github ei löydä brancheja paikallisella komennolla
            ['git', 'branch', '-r'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)   

    branches = result.stdout.split("\n")
    branches.remove("  origin/main") # Poistetaan origin/main listasta
    branches.pop() # Poistetaan tyhjä solu listasta
    print(branches)
    return branches

def check_recipe_content(): # Otetaan talteen HTML-tiedosto ja muutetaan kirjainkoko pieneksi
    html = open("recipe.html", 'r')
    file_content = html.read()
    encoded_file = file_content.encode()
    return encoded_file.lower()

def compareNames(branchNames, recipe_content): # Verrataan löytyykö branchien opiskelijatunnukset html-tiedostosta
    matches = []

    for name in branchNames :
        iterable = name.lower().strip().encode()
        print(iterable[7:])
        if recipe_content.count(iterable[7:]) :
            matches.append(iterable)
    
    return matches  
         
def main():
    branchNames = get_branches() # Haetaan branchit
    recipe_content = check_recipe_content() # Haetaan HTML
    matches = compareNames(branchNames, recipe_content) # Tarkistetaan yhtäläisyydet
    print(len(branchNames))
    print(f"{len(matches)} opiskelijaa on lisännyt pitsatäytteet omalta haaraltaan")
    if len(matches) == len(branchNames) and len(matches) > 1 :
        print("Reseptejä on lisätty tarpeeksi")
    else: 
        print("Lisätkää reseptit omilta haaroiltanne ja käyttäkää opiskelijatunnusta haaran nimenä sekä pitsareseptin otsikossa")
        sys.exit(1)

if __name__ == "__main__":
    main()
