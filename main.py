from time import sleep
from psutil import sensors_battery
from plyer import notification


def seconds_to_hms(seconds) -> str:
    """
    Converts seconds into Hour(s), Minute(s) and Second(s).
    :param seconds: Number of seconds as a mandatory parameter
    :return: int
    """

    _minutes, _seconds = divmod(seconds, 60)
    _hours, _minutes = divmod(_minutes, 60)
    return "%d Hrs %02d Mins %02d Secs" % (_hours, _minutes, _seconds)


def power_notify(ttl: str, per: int, rem: str, msg: str, sec: int = 5):
    notification.notify(
        title=ttl,
        message=f"● {per}% battery currently\n"
                f"● {rem} left\n"
                f"{msg}.",
        app_name="System POWER",
        timeout=sec
    )


if __name__ == '__main__':
    while True:
        _battery_info = sensors_battery().power_plugged, sensors_battery().percent, \
            seconds_to_hms(sensors_battery().secsleft)

        # If running on battery power
        if not _battery_info[0]:
            if _battery_info[1] <= 20:
                pass
            elif _battery_info[1] <= 30:
                pass
            elif _battery_info[1] <= 40:
                pass
            elif _battery_info[1] <= 60:
                power_notify(ttl="Power Half", msg="Make sure the AC power is available",
                             per=_battery_info[1], rem=_battery_info[2])

        # If running on AC power
        else:
            if _battery_info[1] >= 80:
                pass
            elif _battery_info[1] >= 90:
                pass
            elif _battery_info[1] >= 95:
                pass
            elif _battery_info[1] >= 100:
                pass

        sleep(10)
