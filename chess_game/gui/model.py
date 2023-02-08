import tensorflow as tf

class Model():
    def __init__(self):
        self.model_path = r'C:\Users\Usuario\Desktop\Data Science Projects\Chess_Engine_TFM\engine\engine_models\depth3_model.h5'
        self.model = tf.keras.models.load_model(self.model_path)

    # def load_model(model_path):
    #     self.model = tf.keras.models.load_model(model_path)
