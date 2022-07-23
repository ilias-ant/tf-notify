from notifiers import get_notifier

from .base import BaseNotificationCallback


class SlackCallback(BaseNotificationCallback):
    def __init__(self, webhook_url: str):

        self.webhook_url = webhook_url
        self.slack = get_notifier('slack')

    def on_train_end(self, logs=None):

        self.slack.notify(
            message=f"model <{self.model.name}> has completed its training!",
            webhook_url=self.webhook_url,
            username="tf-notify",
            icon_url="https://www.python.org/static/favicon.ico",
        )  # TODO: deprecate Incoming WebHooks integration in favor of the new Slack SDK
