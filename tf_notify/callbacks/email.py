from typing import Any

from notifiers import get_notifier

from .base import BaseNotificationCallback


class EmailCallback(BaseNotificationCallback):
    """
    A custom tf.callbacks.Callback that enables sending email messages to SMTP servers.

    Keep in mind that in order to authenticate against an SMTP server (e.g. *smtp.mail.yahoo.com*),
    you will have to first generate a one-time password (or equivalent) from the respective email provider.

    Attributes:
        to (Union[str, list]): the email address of the recipient - can be a `str` (single recipient) or a `list` (multiple recipients)
        **kwargs (Any): Arbitrary keyword arguments - supported keys: `subject`, `from`, `host`, `port`, `tls`, `ssl`, `html`, `login`. Sensible defaults are used for `message` and `subject`, bu they can also be overrided accordingly.

    Examples:
        >>> import tensorflow as tf
        >>> from tf_notify import EmailCallback
        >>>
        >>> model = tf.keras.Sequential(name="neural-network")
        >>> model.add(tf.keras.layers.Dense(1, input_dim=784))
        >>> model.compile(
        >>>     optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.1),
        >>>     loss="mean_squared_error",
        >>>     metrics=["mean_absolute_error"],
        >>> )
        >>>
        >>> model.fit(
        >>>     x_train,
        >>>     y_train,
        >>>     batch_size=128,
        >>>     epochs=2,
        >>>     verbose=0,
        >>>     validation_split=0.5,
        >>>     callbacks=[
        >>>         EmailCallback(
        >>>             to="toaddress@yahoo.com",
        >>>             from_="fromaddress@yahoo.com",
        >>>             host="smtp.mail.yahoo.com",
        >>>             port=465,
        >>>             username="my-cool-username",
        >>>             password="my-cool-password",  # one-time app password
        >>>             ssl=True,
        >>>         )
        >>>     ],
        >>> )

    **Note**: Any attributes or methods prefixed with _underscores are forming a so called "private" API, and is
    for internal use only. They may be changed or removed at anytime.
    """

    def __init__(self, to: str, **kwargs: Any):

        self.to = to
        self.additional_properties = kwargs
        self.email = get_notifier("email")

    def on_train_end(self, logs=None):

        message = self.additional_properties.pop(
            "message", f"model <{self.model.name}> has completed its training!"
        )
        subject = self.additional_properties.pop(
            "subject", "New mail from 'tf-notify'!"
        )

        self.email.notify(
            message=message,
            to=self.to,
            subject=subject,
            **self.additional_properties,
        )
