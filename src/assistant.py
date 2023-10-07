# src/assistant.py

class Assistant:

def __init__(self):
self.model = models.load_model()

def generate_project(self, description):

code = self.model.generate_code(description)

# Créer le dépôt GitHub
github = GitHubApi()
github.create_repo(code)

# Ajouter documentation
readme = MarkdownGenerator.generate_readme(description)
github.update_readme(readme)

def train(self):

# Récupérer données d'entraînement
data = Dataset.load_data()

# Entraîner le modèle
self.model.train(data)

# Sauvegarder les poids mis à jour
self.model.save_weights()