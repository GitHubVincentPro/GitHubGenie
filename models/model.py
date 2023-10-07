```python
import tensorflow as tf

# Création du modèle seq2seq
encoder = tf.keras.layers.LSTM(128)
decoder = tf.keras.layers.LSTM(128)

outputs = decoder(encoder(inputs))

# Compilation
model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.compile(optimizer='adam', loss='categorical_crossentropy')

# Chargement des poids entraînés
model.load_weights('model/model_weights.h5')

def generate_code(self, project_description):

encoded = encoder(project_description)

decoded = ''
token = '__start__'

while token != '__end__':
decoded_tokens = decoder.predict(encoded)
token = np.argmax(decoded_tokens)
decoded += token

return decoded
```