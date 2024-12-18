import sys
import subprocess


def check_merges():
    try:
        mergeCommits = subprocess.run(  # Haetaan branchit remotesta, koska Github ei löydä brancheja paikallisella komennolla
            ['git', 'log', 'main', '--first-parent', '--merges'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        ).stdout.split('\n')

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)   
    
    merges = []
    for item in mergeCommits: # Etsitään git log-tulosteesta authorit
        if "Merge:" in item:
            merges.append(item)
    return merges

if __name__ == "__main__":
    file_name = "./tests/reflog.txt"

try :
    merges = check_merges()
    if merges :
        print(f"Repositoriosta löytyi {len(merges)} mergeä")
    else :
        print("Repositoriosta ei löytynyt mergejä, tehkää tehtävä ohjeiden mukaisesti")
        sys.exit(1)
except :
    print("Mergejä ei löytynyt")
    sys.exit(1)