# La variable quote devra stocker la valeur “Ecoutez-moi, Monsieur Shakespeare: Nous avons beau être ou ne pas être, nous sommes ! ”.

quote="Ecoutez-moi, Monsieur Shakespare: Nous avons beau être ou ne pas être, nous sommes!"

# Créez différentes variables pour stocker les éléments suivants : le nom de votre groupe de musique préféré, l'année de formation du groupe,  sont-ils encore ensemble ?, la liste de leurs albums, un tuple qui stocke le nom des membres fondateurs,un dictionnaire qui contient les chansons de leurs albums.

group="DaftPunk"
year=1993
still_together=True
albums=["Discovery","Homework"]
founding_members=("Thomas Bangalter","Guy-Manuel de Homem-Christo")
songs={"Discovery":["Digital Love","One More Time"]}

#créez une fonction create_message qui prend deux paramètres : character et quote. A l'intérieur, utilisez la méthode .format() pour créer une chaîne de caractère sur ce modèle : "{character} a dit : {quote}". Enfin, exécutez la fonction avec le personnage et la citation de votre choix.

def create_message(character,quote):
    "{} a dit : {}".format(character, quote)
create_message("Inspecteur Gadget", "Nom d'un gadget")

# Créez une liste qui s'appelle characters et qui contient 5 personnages de dessin animé. Supprimez un des personnages de la liste. Ajoutez un personnage à votre liste. Remplacez "Mowgli" par "Balou".

characters=["Mickey", "Homer", "Donald", "Babar", "Simba","Mowgli"]
characters.remove("Babar")
characters.insert(3, "Rahan")
characters[4] = "Balou"

# Créez un dictionnaire friends qui stocke l'adresse de vos amis.

friends={"Willy":"Londres","Margot":"Sydney"}

# Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.

rayon = float(input("Rayon du cone (m) :"))
hauteur = float(input("Hauteur du cone (m) :"))

volume = (3,14*rayon*rayon*hauteur)/3.0
print("Volume du cone =", volume, "m3")

# 2eme solution 

def volume(r, h):
    return 3.14*r*r*h/3
>>> volume (1,1) #par exemple

# L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est divisible par 2, IMPAIR sinon.

n = int(input("Entrez un entier strictement positif :"))
while n < 1:
    n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))

if n%2 == 0:
    print(n, "est pair.")
else :
    print(n, "est impair.")

# Un permis de chasse à points remplace désormais le permis de chasse traditionnel. Chaque chasseur possède au départ un capital de 100 points. S'il tue une poule, il perd 1 point, 3 points pour un chien, 5 points pour une vache et 10 points pour un ami. Le permis coûte 200 euros.

Écrire une fonction qui reçoit le nombre de victimes du chasseur et qui renvoie la somme due.

Utilisez cette fonction dans un programme principal qui saisit le nombre de victimes et qui affiche la somme que le chasseur doit débourser.


def permisSup(p, c, v, a) :
    pointsPerdus = p + 3*c + 5*v + 10*a
    nbrePermis = pointsPerdus/100.0
    return 200*nbrePermis

poules = int(input("Combien de poules ?"))
chiens = int(input("Combien de chiens ?"))
vaches = int(input("Combien de vaches ?"))
amis = int(input("Combien d'amis ?"))

payer = permisSup(poules, chiens, vaches, amis)

if payer == 0:
    print("rien à payer")
else :
    print(payer, "euros")
