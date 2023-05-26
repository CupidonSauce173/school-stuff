prix_articles = 0
nbre_articles = 0

# Entrées
nbre_total_articles = int(input())
min_prix = int(input())
max_prix = int(input())
# Suite. À faire

i = 0
while i < nbre_total_articles:
    prix_article = int(input())
    if prix_article in range(min_prix, max_prix + 1):
        print(prix_article)
        nbre_articles += 1
    # end if
    i += 1
# end while

print(nbre_articles)
