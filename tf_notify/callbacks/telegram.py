from notifiers import get_notifier

from .base import BaseNotificationCallback


class TelegramCallback(BaseNotificationCallback):
    """
    A custom tf.callbacks.Callback that provides instant integration with Telegram messaging app.

    For more on Telegram bots (and how to create one yourself) see: <https://core.telegram.org/bots> \n
    For an example how to retrieve the `chat_id` for your bot, see: <https://stackoverflow.com/a/32572159/10251805>

    Examples:
        >>> import tensorflow as tf
        >>> from tf_notify import TelegramCallback
        >>>
        >>> model = tf.keras.Sequential(name='neural-network')
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
        >>>         TelegramCallback(token='XXXX:YYYY', chat_id=-1234)
        >>>     ],
        >>> )

    **Note**: Any attributes or methods prefixed with _underscores are forming a so called "private" API, and is
    for internal use only. They may be changed or removed at anytime.
    """

    def __init__(self, token: str, chat_id: int):

        self.token = token
        self.chat_id = chat_id
        self.telegram = get_notifier('telegram')

    def on_train_end(self, logs=None):

        self.telegram.notify(
            message=f"model <{self.model.name}> has completed its training!",
            token=self.token,
            chat_id=self.chat_id,
        )
