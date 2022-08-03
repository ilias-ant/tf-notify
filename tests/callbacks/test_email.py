import sys
from unittest import mock

import pytest
import tensorflow as tf

from tf_notify import EmailCallback


class TestEmailCallback:
    @pytest.mark.skipif(
        sys.version_info < (3, 8), reason="requires python3.8 or higher"
    )
    def test_callback_occurs_on_train_end(self):

        # define tf.keras model to add callback to
        model = tf.keras.Sequential(name="neural-network")
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

        with mock.patch("smtplib.SMTP", autospec=True) as smtp_mock:
            # initiate training
            model.fit(
                x_train,
                y_train,
                batch_size=128,
                epochs=2,
                verbose=0,
                validation_split=0.5,
                callbacks=[
                    EmailCallback(
                        to="toaddress@yahoo.com",
                        from_="fromaddress@yahoo.com",
                        host="smtp.mail.yahoo.com",
                        port=465,
                        username="my-cool-username",
                        password="my-cool-password",  # one-time app password
                        ssl=False,
                    )
                ],
            )

        # validate smtplib.SMTP was called twice
        assert len(smtp_mock.method_calls) == 2

        login, send_message = smtp_mock.method_calls

        # one time to authenticate against the SMTP server
        assert login.args == (
            "my-cool-username",
            "my-cool-password",
        )  # .args available in py3.8+, this fails on py3.7

        # and another, to send the message
        email = send_message.args[0]
        components = dict(email.items())

        assert components["To"] == "toaddress@yahoo.com"
        assert components["From"] == "fromaddress@yahoo.com"
        assert components["Subject"] == "New mail from 'tf-notify'!"

        payload = email.get_payload()[0].as_string()

        assert "model <neural-network> has completed its training!" in payload

    @pytest.mark.skipif(
        sys.version_info < (3, 8), reason="requires python3.8 or higher"
    )
    def test_callback_occurs_on_train_end_while_both_message_and_subject_are_overridden(
        self,
    ):

        # define tf.keras model to add callback to
        model = tf.keras.Sequential(name="neural-network")
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

        with mock.patch("smtplib.SMTP", autospec=True) as smtp_mock:
            # initiate training
            model.fit(
                x_train,
                y_train,
                batch_size=128,
                epochs=2,
                verbose=0,
                validation_split=0.5,
                callbacks=[
                    EmailCallback(
                        message="This is a custom message!",
                        subject="You have mail!",
                        to="toaddress@yahoo.com",
                        from_="fromaddress@yahoo.com",
                        host="smtp.mail.yahoo.com",
                        port=465,
                        username="my-cool-username",
                        password="my-cool-password",  # one-time app password
                        ssl=False,  # if this is True, patching of smtplib.SMTP_SSL is needed instead
                    )
                ],
            )

        # validate smtplib.SMTP was called twice
        assert len(smtp_mock.method_calls) == 2

        login, send_message = smtp_mock.method_calls

        # one time to authenticate against the SMTP server
        assert login.args == (
            "my-cool-username",
            "my-cool-password",
        )  # .args available in py3.8+, this fails on py3.7

        # and another, to send the message
        email = send_message.args[0]
        components = dict(email.items())

        assert components["To"] == "toaddress@yahoo.com"
        assert components["From"] == "fromaddress@yahoo.com"
        assert components["Subject"] == "You have mail!"

        payload = email.get_payload()[0].as_string()

        assert "This is a custom message!" in payload
