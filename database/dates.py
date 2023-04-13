from dateutil import tz
from datetime import datetime, timedelta


def datetime_now(tzone):
    return datetime.now(tz=tz.gettz(tzone))