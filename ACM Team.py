def acm_team(topic: list[str]) -> list[int]:
    n = len(topic)
    max_topics = 0
    team_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            topics_known = 0
            for k in range(len(topic[i])):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    topics_known += 1
            if topics_known > max_topics:
                max_topics = topics_known
                team_count = 1
            elif topics_known == max_topics:
                team_count += 1

    return [max_topics, team_count]
