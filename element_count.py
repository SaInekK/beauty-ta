from collections import defaultdict

list_version = [
    ['665587', 2],
    ['669532', 1],
    ['669537', 2],
    ['669532', 1],
    ['665587', 1],
]


def group_and_count_versions(versions):
    counts = defaultdict(int)
    for version in versions:
        counts[tuple(version)] += 1

    grouped_versions = [[*version, count] for version, count in counts.items()]
    return grouped_versions


if __name__ == '__main__':
    res = group_and_count_versions(list_version)
    print(res)
