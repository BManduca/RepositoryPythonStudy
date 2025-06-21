import time
from plyer import notification


if __name__ == '__main__':
  while True:
    notification.notify(
      title = "Reminder",
      message = "Take your Medicine!",
      timeout = 10
    )
    time.sleep(90)