import tensorflow as tf

from tfnotify import SlackCallback

# define the tf.keras model to add callbacks to
model = tf.keras.Sequential(name='neural-network')
model.add(tf.keras.layers.Dense(1, input_dim=784))
model.compile(
    optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.1),
    loss="mean_squared_error",
    metrics=["mean_absolute_error"],
)

model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=2,
    verbose=0,
    validation_split=0.5,
    callbacks=[
        SlackCallback(webhook_url='https://url.to/webhook')
    ],  # send a Slack notification when training ends!
)
