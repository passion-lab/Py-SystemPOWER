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
                f"{msg}",
        app_name="System POWER",
        timeout=sec
    )


if __name__ == '__main__':

    # Will be true once notification is shown
    is_notified = False

    while True:
        _battery_info = sensors_battery().power_plugged, sensors_battery().percent, \
            seconds_to_hms(sensors_battery().secsleft)

        # If running on battery power
        if not _battery_info[0]:

            if _battery_info[1] < (50 or 40 or 30 or 24):
                is_notified = False

            if _battery_info[1] == 25:
                if not is_notified:
                    power_notify(ttl="Power Critical | URGENT", msg="Immediately plug-in the power adapter.",
                                 per=_battery_info[1], rem=_battery_info[2], sec=10)
                    is_notified = True
            elif _battery_info[1] == 30:
                if not is_notified:
                    power_notify(ttl="Power Emergency | PLUG-IN",
                                 msg="Device is running in emergency battery power. Connect the device with AC power "
                                     "adapter. Shut down the system if AC not available.",
                                 per=_battery_info[1], rem=_battery_info[2], sec=10)
                    is_notified = True
            elif _battery_info[1] == 40:
                if not is_notified:
                    power_notify(ttl="Power Down | READY", msg="Get ready to power up the battery of your device soon.",
                                 per=_battery_info[1], rem=_battery_info[2])
                    is_notified = True
            elif _battery_info[1] == 50:
                if not is_notified:
                    power_notify(ttl="Power Half | ALERT", msg="Make sure the adapter and AC power is available.",
                                 per=_battery_info[1], rem=_battery_info[2])
                    is_notified = True

        # If running on AC power
        else:

            if _battery_info[1] > (80 or 90 or 95):
                is_notified = False

            if _battery_info[1] == 80:
                if not is_notified:
                    power_notify(ttl="Power Enough | ALERT", msg="Now the battery power is enough to work with.",
                                 per=_battery_info[1], rem=_battery_info[2])
                    is_notified = True
            elif _battery_info[1] == 90:
                if not is_notified:
                    power_notify(ttl="Power Limit | PLUG-OUT", msg="Release the AC adapter. Upper limit reached.",
                                 per=_battery_info[1], rem=_battery_info[2])
                    is_notified = True
            elif _battery_info[1] == 95:
                if not is_notified:
                    power_notify(ttl="Power Over | WARNING", msg="Quickly turn off the AC power supply or"
                                                                 " plug-out the adapter cord from the device.",
                                 per=_battery_info[1], rem=_battery_info[2], sec=10)
                    is_notified = True
            elif _battery_info[1] == 100:
                power_notify(ttl="Power Full | URGENT", msg="Battery power is full now. Switch of the AC"
                                                            " power Immediately.",
                             per=_battery_info[1], rem=_battery_info[2], sec=10)

        sleep(60)
