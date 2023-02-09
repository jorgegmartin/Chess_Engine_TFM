import tensorflow as tf

class Model:
    def __init__(self, difficulty='easy'):
        self.difficulty = difficulty
        self.model_path_d3 = 'engine/engine_models/depth3_model.h5'
        self.model_path_d6 = 'engine/engine_models/depth6_model.h5'
        self.model_path_d10 = 'engine/engine_models/depth10_model.h5'
        self.model_path_d10re = 'engine/engine_models/depth10_model_residuals.h5'

        self.model_path = {
            'easy': self.model_path_d3,
            'medium': self.model_path_d6,
            'hard': self.model_path_d10,
            'extreme': self.model_path_d10re
        }
        self.model = tf.keras.models.load_model(self.model_path[self.difficulty])
        