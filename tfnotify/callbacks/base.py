from tensorflow import keras


class BaseNotificationCallback(keras.callbacks.Callback):
    def on_train_end(self, logs=None):
        raise NotImplementedError
