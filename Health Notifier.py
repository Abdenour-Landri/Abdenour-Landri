from win10toast_click import ToastNotifier
import time

toaster = ToastNotifier()
interval = 20 * 60


def health():
    toaster.show_toast(
        title="Health Notifier",
        msg="Drink water and straighten your back",
        duration=10,
        threaded=True)
    time.sleep(interval)


def rest():
    toaster.show_toast(
        title="Take a break",
        msg="You worked hard take a break",
        duration=10,
        threaded=True)
    time.sleep(interval)


# every 20 minutes we drink water and every 40 min we take a break

while True:
    for i in range(2):
        health()
    rest()
