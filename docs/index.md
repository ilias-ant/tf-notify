# tf-notify

[![PyPI](https://img.shields.io/pypi/v/tf-notify?color=blue&label=PyPI&logo=PyPI&logoColor=white)](https://pypi.org/project/tf-notify/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tf-notify?logo=python&logoColor=white)](https://www.python.org/) [![Tensorflow version](https://shields.io/badge/tensorflow-2.7%20%7C%202.8%20%7C%202.9%20-simple?logo=tensorflow&style=flat)](https://www.tensorflow.org/)
[![codecov](https://codecov.io/gh/ilias-ant/tf-notify/branch/main/graph/badge.svg?token=2H0VB8I8IH)](https://codecov.io/gh/ilias-ant/tf-notify) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ilias-ant/tf-notify/CI)](https://github.com/ilias-ant/tf-notify/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/tf-notify/badge/?version=latest)](https://tf-notify.readthedocs.io/en/latest/?badge=latest)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/tf-notify?color=orange)](https://www.python.org/dev/peps/pep-0427/)

> Want to get notified on the progress of your Tensorflow model training?

This package provides a [tf.keras](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback) callback to send notifications to a messaging app of your choice.

## Supported Apps

The following apps are currently supported. But, do check the project frequently, as many more will soon be supported!

<table>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/ilias-ant/tf-notify/main/static/logos/slack.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://tf-notify.readthedocs.io/en/latest/api/#tf_notify.callbacks.slack.SlackCallback">Slack</a>
    </td>
   <td>
      <img src="https://raw.githubusercontent.com/ilias-ant/tf-notify/main/static/logos/telegram.png" height="128" width="128" style="max-height: 128px; max-width: 128px;"><a href="https://tf-notify.readthedocs.io/en/latest/api/#tf_notify.callbacks.telegram.TelegramCallback">Telegram</a>
    </td>
  </tr>
</table>

