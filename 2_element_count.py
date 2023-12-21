from collections import defaultdict


def group_and_count_versions(versions):
    counts = defaultdict(int)
    for version in versions:
        counts[tuple(version)] += 1

    grouped_versions = [[*version, count] for version, count in counts.items()]
    return grouped_versions


def main():
    list_version = [
        ['665587', 2],
        ['669532', 1],
        ['669537', 2],
        ['669532', 1],
        ['665587', 1],
    ]
    result = group_and_count_versions(list_version)
    print(result)


if __name__ == '__main__':
    main()
