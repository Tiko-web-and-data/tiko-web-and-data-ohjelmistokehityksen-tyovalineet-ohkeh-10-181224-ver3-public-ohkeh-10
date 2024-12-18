import sys
import subprocess
    
def get_authors():
    try:

        result = subprocess.run(
            ['git', 'log'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            sys.exit(1)

        authors = get_emails(result) # haetaan sähköpostiosoitteet git logista
        individualAuthors = sort_authors(authors) # etsitään uniikit postit
        
        return individualAuthors

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def get_emails(result): # funktio erittelee sähköpostit git logista
    emailsInCommits = []
    for item in result.stdout.split("\n"): # Etsitään git log-tulosteesta authorit
        if "Author:" in item:
            authorItems = item.split()
            emailsInCommits.append(authorItems[-1])
           
    return emailsInCommits

def sort_authors(authors): # funktio etsii uniikit ilmentymät sähköpostiosoitteista
    seen = set()
    uniqueItems = []
    for item in authors:
        if item not in seen :
            uniqueItems.append(item)
            seen.add(item)       
                           
    return uniqueItems

def main():
    authors = get_authors()

    if len(authors) >= 3:
        print(authors)
        print(len(authors))
    else:
        print(authors)
        print(len(authors))
        print(f"Virheilmoitus tähän.")
        sys.exit(1)

if __name__ == "__main__":
    main()
