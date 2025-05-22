def findPoisonedDuration(timeSeries, duration):
    if not timeSeries:
        return 0

    total = 0
    end = 0

    for start in timeSeries:
        if start > end:
            total += duration
        else:
            total += start + duration - end
        end = start + duration

    return total
