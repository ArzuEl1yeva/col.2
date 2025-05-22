def acm_team(topic):
    max_topics = 0
    team_count = 0

    n = len(topic)
    for i in range(n):
        for j in range(i + 1, n):
            combined = int(topic[i], 2) | int(topic[j], 2)
            topics_known = bin(combined).count('1')

            if topics_known > max_topics:
                max_topics = topics_known
                team_count = 1
            elif topics_known == max_topics:
                team_count += 1

    return [max_topics, team_count]
print(acm_team(["000", "000", "000"]))