from notifiers import get_notifier

from .base import BaseNotificationCallback


class SlackCallback(BaseNotificationCallback):
    """
    A custom tf.callbacks.Callback that provides instant integration with Slack messaging app.

    Attributes:
        webhook_url (str): an Incoming Webhook URL for a given workspace and channel. You can generate one over at: <https://my.slack.com/services/new/incoming-webhook/>

    Examples:
        >>> import tensorflow as tf
        >>> from tf_notify import SlackCallback
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
        >>>         SlackCallback(webhook_url="https://url.to/webhook")
        >>>     ],
        >>> )

    **Note**: Any attributes or methods prefixed with _underscores are forming a so called "private" API, and is
    for internal use only. They may be changed or removed at anytime.
    """

    def __init__(self, webhook_url: str):

        self.webhook_url = webhook_url
        self.slack = get_notifier("slack")

    def on_train_end(self, logs=None):

        self.slack.notify(
            message=f"model <{self.model.name}> has completed its training!",
            webhook_url=self.webhook_url,
            username="tf-notify",
            icon_url="https://www.python.org/static/favicon.ico",
        )  # TODO: deprecate Incoming WebHooks integration in favor of the new Slack SDK
