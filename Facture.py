clients = []
for i in range(3):
    nom_prenom = input(f"Donner le nom et prénom du client n{i+1} : ")
    nb_articles = int(input(f"Donner le nombre d'articles pour le client n{i+1}: "))
    articles = []
    for j in range(nb_articles):
        prix_article = float(input(f"Donner le prix de l'article {j+1} : "))
        articles.append(prix_article)
    clients.append((nom_prenom, articles))
taux_tva = 0.15
remise = 0.02
for client in clients:
    nom_prenom, articles = client
    total_client = sum(articles)
    total_client_ttc = total_client * (1 + taux_tva)
    total_client_remise = total_client_ttc * (1 - remise)
    print(f"Le Total à payer pour le client {nom_prenom} est : {total_client_remise:.2f} DH")
