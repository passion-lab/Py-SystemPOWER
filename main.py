from time import sleep
from psutil import sensors_battery
from plyer import notification


def seconds_to_hms(seconds):
    """
    Converts seconds into Hour(s), Minute(s) and Second(s).
    :param seconds: Number of seconds as a mandatory parameter
    :return: int
    """

    _minutes, _seconds = divmod(seconds, 60)
    _hours, _minutes = divmod(_minutes, 60)
    return "%d:%02d:%02d" % (_hours, _minutes, _seconds)


def notify():
    pass


if __name__ == '__main__':
    while True:
        if not sensors_battery().power_plugged:
            match sensors_battery().percent:
                case 50:
                    pass
        sleep(10)
