def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    for checkin, checkout in permanence_period:
        if (
            isinstance(checkin, int) is False
            or isinstance(checkout, int) is False
        ):
            return None
        if checkin <= target_time <= checkout:
            counter += 1
    return counter
