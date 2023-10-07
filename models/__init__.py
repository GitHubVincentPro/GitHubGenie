```python
from .model import Model

# Charger le modèle quand le fichier est importé
model = Model()
model.load_weights('model_weights.h5')

# Exporter le modèle comme objet global
__model = model

def generate_code(project_description):
return __model.generate_code(project_description)
```