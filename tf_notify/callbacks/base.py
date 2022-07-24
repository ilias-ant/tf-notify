from tensorflow import keras


class BaseNotificationCallback(keras.callbacks.Callback):
    def on_train_end(self, logs=None):
        raise NotImplementedError(
            "BaseNotificationCallback should not be used directly - instead use callbacks that inherit from this callback."
        )
