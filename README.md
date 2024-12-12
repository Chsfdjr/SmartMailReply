# SmartMailReply

SmartMailReply est une application Python qui automatise la gestion des emails. Elle surveille les emails entrants, détecte les messages non lus, et répond à ceux-ci en générant des réponses personnalisées en fonction des informations extraites du contenu du mail. L'application sauvegarde ensuite ces réponses dans le dossier des brouillons.

## Fonctionnalités

- **Surveillance des emails entrants** : L'application écoute en permanence les nouveaux emails dans votre boîte de réception.
- **Réponses personnalisées** : En fonction des informations trouvées dans un email, une réponse toute faite est générée et sauvegardée dans les brouillons.
- **Support de l'IMAP** : L'application utilise le protocole IMAP pour accéder aux emails et gérer les brouillons.

## Installation

### Prérequis

1. **Python 3.x** : Assurez-vous d'avoir Python 3 installé sur votre machine.
2. **Variables d'environnement** : Mettre à jour le fichier `.env` à la racine de votre projet avec vos informations de connexion au serveur IMAP.

#### Installation

- **Linux** : Exécutez le script `config/install.sh` pour installer les dépendances et configurer l'environnement.
  
  ```bash
    ./install.sh
  ```

- **Windows** : Exécutez le script `config\install.bat` pour installer les dépendances.

  ```batch
    config\install.bat
  ```

## Utilisation

1. **Configuration des variables d'environnement** :
   - Créez/modifiez un fichier `.env` à la racine de votre projet avec les informations suivantes :

```env
IMAP_SERVER=imap.votre-serveur.com
SMTP_SERVER=smtp.votre-serveur.com
EMAIL=votre-email@example.com
PASSWORD=votre-mot-de-passe
```

2. **Lancer l'application** :
   - Exécutez le script principal pour démarrer la surveillance des emails et répondre aux messages :

```bash
    ./run
```

ou

```bash
    python src/run
```

L'application va alors commencer à écouter les nouveaux emails et à répondre automatiquement selon les paramètres définis.

## Pourquoi SmartMailReply ?

Ce projet est à l'initiative d'un projet durant mon stage de 3ème année au sein d'EPITECH. L'objectif était de mettre en place un système de réponse automatique aux emails entrants en fonction de leur contenu pour une entreprise.

## License

Distribué sous la licence MIT. Voir le fichier `LICENSE` pour plus d'informations.
