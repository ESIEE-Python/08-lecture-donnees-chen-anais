"""
    lecture des données contenues dans un fichier
"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    # ll = []
    with open(filename, mode = 'r', encoding = 'utf8') as file:

        ll = [ [ int(val) for val in line.split(';') ] for line in file.readlines()  ]

        # for line in file.readlines() :
        #     l = [ int(val)           for val in line.split(';')          ]
            # l = []
            # for val in line.split(';') :
            #     l.append(int(val))
            # ll.append(l)

    return ll

def get_list_k(data, k):
    """retourne la k-ième liste de data

    Args:
        data(list) : liste de listes du fichier
        k(int) : indice de la liste voulue

    Returns:
        list: la k-ième liste
    """
    l = data[k]
    return l

def get_first(l):
    """retourne le premier élément de la liste

    Args:
        l(list) : une liste 

    Returns:
        int : le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """retourne le dernier élément de la liste

    Args:
        l(list) : une liste 

    Returns:
        int : le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """retourne le max de la liste

    Args:
        l(list) : une liste 

    Returns:
        int : le max de la liste
    """
    return max(l)

def get_min(l):
    """retourne le min de la liste

    Args:
        l(list) : une liste 

    Returns:
        int : le min de la liste
    """
    return min(l)

def get_sum(l):
    """retourne la somme des éléments de la liste

    Args:
        l(list) : une liste 

    Returns:
        int : la somme des éléments de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
        appelle les fonctions secondaires
    """
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
