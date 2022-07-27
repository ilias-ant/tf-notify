import json

import responses
import tensorflow as tf

from tf_notify import TelegramCallback


class TestTelegramCallback:
    @responses.activate
    def test_callback_occurs_on_train_end(self):

        responses.add(
            responses.POST,
            url="https://api.telegram.org/botXXXX:YYYY/sendMessage",
            status=200,
        )

        # define tf.keras model to add callback to
        model = tf.keras.Sequential(name='neural-network')
        model.add(tf.keras.layers.Dense(1, input_dim=784))
        model.compile(
            optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.1),
            loss="mean_squared_error",
            metrics=["mean_absolute_error"],
        )

        # load example MNIST data and pre-process it
        (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
        x_train = x_train.reshape(-1, 784).astype("float32") / 255.0

        # limit the data to 1000 samples
        x_train = x_train[:1000]
        y_train = y_train[:1000]

        # initiate training
        model.fit(
            x_train,
            y_train,
            batch_size=128,
            epochs=2,
            verbose=0,
            validation_split=0.5,
            callbacks=[TelegramCallback(token='XXXX:YYYY', chat_id=-1234)],
        )

        assert len(responses.calls) == 1

        payload = json.loads(responses.calls[0].request.body)
        assert (
            responses.calls[0].request.url
            == "https://api.telegram.org/botXXXX:YYYY/sendMessage"
        )
        assert "text" in payload
        assert payload["text"] == "model <neural-network> has completed its training!"
