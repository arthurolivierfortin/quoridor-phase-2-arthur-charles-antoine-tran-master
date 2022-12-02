"""Module de la classe Quoridor

Classes:
    * Quoridor - Classe pour encapsuler le jeu Quoridor.
"""
from copy import deepcopy

from quoridor_error import QuoridorError

from graphe import construire_graphe

# TODO : créer le fichier quoridor_error.py contenant la classe QuoridorError


class Quoridor:
    """Classe pour encapsuler le jeu Quoridor.

    Vous ne devez pas créer d'autre attributs pour votre classe.

    Attributes:
        état (dict): état du jeu tenu à jour.
    """

    def __init__(self, joueurs, murs=None):
        """Constructeur de la classe Quoridor.

        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.

        Appel la méthode `vérification` pour valider les données et assigne
        ce qu'elle retourne à l'attribut `self.état`.

        Cette méthode ne devrait pas être modifiée.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        """
        self.état = deepcopy(self.vérification(joueurs, murs))

    def vérification(self, joueurs, murs):
        """Vérification d'initialisation d'une instance de la classe Quoridor.

        Valide les données arguments de construction de l'instance et retourne
        l'état si valide.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de list [x, y] uniquement.
        Raises:
            QuoridorError: L'argument 'joueurs' n'est pas itérable.
            QuoridorError: L'itérable de joueurs en contient un nombre différent de deux.
            QuoridorError: Le nombre de murs qu'un joueur peut placer est plus grand que 10,
                            ou négatif.
            QuoridorError: La position d'un joueur est invalide.
            QuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent.
            QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.
            QuoridorError: La position d'un mur est invalide.
        """
        try:
            joueurs[0]
        except TypeError:
            raise QuoridorError("L'argument 'joueurs' n'est pas itérable.")
        
        if type(joueurs) == tuple:
            if len(joueurs) > 2:
                raise QuoridorError("L'itérable de joueurs en contient un nombre différent de deux.")
            joueurs = [{f"nom: {joueurs[0]}, murs: 10, pos: [5, 1]"},
                       {f"nom: {joueurs[1]}, murs: 10, pos: [5, 9]"},]
        if type(joueurs) == list:
            if len(joueurs) > 2:
                raise QuoridorError("L'itérable de joueurs en contient un nombre différent de deux.")
            
            elif joueurs[0]["murs"] < 0 or joueurs[0]["murs"] > 10:
                raise QuoridorError("Le nombre de murs qu'un joueur peut placer est plus grand que 10, ou négatif.")
            
            elif joueurs[1]["murs"] < 0 or joueurs[1]["murs"] > 10:
                raise QuoridorError("Le nombre de murs qu'un joueur peut placer est plus grand que 10, ou négatif.")

            elif joueurs[0]["pos"] != [5, 1] and joueurs[0]["pos"] != [5, 9] and murs == None:
                raise QuoridorError("La position d'un joueur est invalide.")

            elif joueurs[1]["pos"] != [5, 1] and joueurs[1]["pos"] != [5, 9] and murs == None:
                raise QuoridorError("La position d'un joueur est invalide.")
        
        if murs == None:
            murs = {"horizontaux": [], "verticaux": [],}

        if murs != None:
            if type(murs) != dict:
                raise QuoridorError("L'argument 'murs' n'est pas un dictionnaire lorsque présent.")

            if len(murs["horizontaux"]) + len(murs["horizontaux"]) + (joueurs[0]['murs']) + (joueurs[1]['murs']) != 20:
                raise QuoridorError("QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.")
    
            for i in murs["horizontaux"]:
                if (1 <= i[0] <= 8) == False:
                    raise QuoridorError("La position d'un mur est invalide.")
            
                elif (2 <= i[1] <= 9) == False:
                    raise QuoridorError("La position d'un mur est invalide.")
        
            for i in murs["verticaux"]:
                if (2 <= i[0] <= 9) == False:
                    raise QuoridorError("La position d'un mur est invalide.")
            
                elif (1 <= i[1] <= 8) == False:
                    raise QuoridorError("La position d'un mur est invalide.")
        
        état = {"joueurs": joueurs, "murs": murs}
        self.état = état
        return self.état
    
    def formater_légende(self):
        """Formater la représentation graphique de la légende.

        Returns:
            str: Chaîne de caractères représentant la légende.
        """
        
        x = self.état["joueurs"]
        nb_murs_joueur1 = x[0]['murs']
        nb_murs_joueur2 = x[1]['murs']
        nom_joueur1 = x[0]['nom']
        nom_joueur2 = x[1]['nom']
        différence_espace = len(nom_joueur1) - len(nom_joueur2)
        espace_ajoutee_joueur2 = 0
        espace_ajoutee_joueur1 = 0
        if différence_espace > 0:
            espace_ajoutee_joueur2 = 0
            espace_ajoutee_joueur2 = ((' '*(différence_espace)))
            murs_joueur1 = (nb_murs_joueur1*'|')
            murs_joueur2 = (nb_murs_joueur2*'|')
            legende = ("Légende:\n"   f"   1={nom_joueur1}, murs={murs_joueur1}\n"   f"   2={nom_joueur2}, {espace_ajoutee_joueur2}murs={murs_joueur2}\n")
            self.legende = legende
            return self.legende
        if différence_espace < 0:
            espace_ajoutee_joueur1 = 0
            espace_ajoutee_joueur1 = ((' '*(-1*(différence_espace))))
            murs_joueur1 = (nb_murs_joueur1*'|')
            murs_joueur2 = (nb_murs_joueur2*'|')
            legende = ("Légende:\n"   f"   1={nom_joueur1}, {espace_ajoutee_joueur1}murs={murs_joueur1}\n"   f"   2={nom_joueur2}, murs={murs_joueur2}\n")
            self.legende = legende
            return self.legende
        
        murs_joueur1 = nb_murs_joueur1*'|'
        murs_automate = nb_murs_joueur2*'|'
        legende = ("Légende:\n"   f"   1={nom_joueur1}, murs={murs_joueur1}\n"   f"   2={nom_joueur2}, murs={murs_joueur2}\n")
        return legende

    
    
    def formater_damier(self):
        """Formater la représentation graphique du damier.

        Returns:
            str: Chaîne de caractères représentant le damier.
        """
        damier_vide = (
            "   -----------------------------------\n"
            "9 | .   .   .   .   .   .   .   .   . |\n"
            "  |                                   |\n"
            "8 | .   .   .   .   .   .   .   .   . |\n"
            "  |                                   |\n"
            "7 | .   .   .   .   .   .   .   .   . |\n"
            "  |                                   |\n"
            "6 | .   .   .   .   .   .   .   .   . |\n"
            "  |                                   |\n"
            "5 | .   .   .   .   .   .   .   .   . |\n"
            "  |                                   |\n"
            "4 | .   .   .   .   .   .   .   .   . |\n"
            "  |                                   |\n"
            "3 | .   .   .   .   .   .   .   .   . |\n"
            "  |                                   |\n"
            "2 | .   .   .   .   .   .   .   .   . |\n"
            "  |                                   |\n"
            "1 | .   .   .   .   .   .   .   .   . |\n"
            "--|-----------------------------------\n"
            "  | 1   2   3   4   5   6   7   8   9\n"
        )
        
        damier = damier_vide
        murs_verticaux = self.état["murs"]["verticaux"]
        murs_horizontaux = self.état["murs"]["horizontaux"]
        positionnement_joueur1 = self.état["joueurs"][0]['pos']
        positionnement_joueur2 = self.état["joueurs"][1]['pos']
        for i in murs_verticaux:
            x = damier.find(str(i[1]))
            damier = list(damier)
            y = (4+(4*((i[0])-1))-2)
            damier[x+y] = ('|')
            damier[x+y-40] = ('|')
            damier[x+y-80] = ('|')
            z = ''.join(damier)
            damier = (z)
        for i in murs_horizontaux:
            x = damier.find(str(i[1]))
            damier = list(damier)
            y = (+40+4+(4*((i[0])))-5)
            damier[y+x] = ('-')
            damier[y+x+1] = ('-')
            damier[y+x+2] = ('-')
            damier[y+x+3] = ('-')
            damier[y+x+4] = ('-')
            damier[y+x+5] = ('-')
            damier[y+x+6] = ('-')
            z = ''.join(damier)
            damier = (z)
        x = damier.find(str(positionnement_joueur1[1]))
        damier = list(damier)
        y = (4+(4*((positionnement_joueur1[0])-1)))
        damier[y+x] = ('1')
        z = ''.join(damier)
        damier = (z)
        x = damier.find(str(positionnement_joueur2[1]))
        damier = list(damier)
        y = (4+(4*((positionnement_joueur2[0])-1)))
        damier[y+x] = ('2')
        z = ''.join(damier)
        damier = (z)
        return damier

    def __str__(self):
        """Représentation en art ascii de l'état actuel de la partie.

        Cette représentation est la même que celle du projet précédent.

        Returns:
            str: La chaîne de caractères de la représentation.
        """
        damier = self.formater_damier()
        legende = self.formater_légende()
        return(f"{legende}{damier}")
        

    def état_courant(self):
        """Produire l'état actuel du jeu.

        Cette méthode ne doit pas être modifiée.

        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de liste [x, y] uniquement.
        """
        return deepcopy(self.état)

    def est_terminée(self):
        """Déterminer si la partie est terminée.

        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        pass

    def récupérer_le_coup(self, joueur):
        """Récupérer le coup

        Notez que seul 2 questions devrait être posée à l'utilisateur.

        Notez aussi que cette méthode ne devrait pas modifier l'état du jeu.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Le type de coup est invalide.
            QuoridorError: La position est invalide (en dehors du damier).

        Returns:
            tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
        """
        pass

    def déplacer_jeton(self, joueur, position):
        """Déplace un jeton.

        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (List[int, int]): La liste [x, y] de la position du jeton (1<=x<=9 et 1<=y<=9).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La position est invalide (en dehors du damier).
            QuoridorError: La position est invalide pour l'état actuel du jeu.
        """
        pass

    def placer_un_mur(self, joueur, position, orientation):
        """Placer un mur.

        Pour le joueur spécifié, placer un mur à la position spécifiée.

        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (List[int, int]): la liste [x, y] de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Un mur occupe déjà cette position.
            QuoridorError: La position est invalide pour cette orientation.
            QuoridorError: Le joueur a déjà placé tous ses murs.
        """
        pass

    def jouer_le_coup(self, joueur):
        """Jouer un coup automatique pour un joueur.

        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La partie est déjà terminée.

        Returns:
            Tuple[str, List[int, int]]: Un tuple composé du type et de la position du coup joué.
        """
        pass
