import sys
import subprocess
    
def get_branches():
    try:
        fetch = subprocess.run(
            ['git', 'fetch'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print(fetch)

        result = subprocess.run(
            ['git', 'branch'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


    gitlog = subprocess.run(
        ['git', 'log'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )    
    print(gitlog.stdout)    

    branches = result.stdout.split("\n")
    branches.pop()
    print(branches)
    return branches

def check_recipe_content():
    html = open("recipe.html", 'r')
    file_content = html.read()
    encoded_file = file_content.encode()
    return encoded_file.lower()

def compareNames(branchNames, recipe_content):
    seen = set()
    matches = []

    for name in branchNames :
        iterable = name.lower().strip().encode()
        if recipe_content.count(iterable) :
            matches.append(iterable)
    
    return matches  
         
def main():
    branchNames = get_branches()
    recipe_content = check_recipe_content()
    matches = compareNames(branchNames, recipe_content)

    print(matches)
    print(len(matches))

if __name__ == "__main__":
    main()
