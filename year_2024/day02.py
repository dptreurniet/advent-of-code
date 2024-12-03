def is_inc(report):
    return sorted(report) == report

def is_dec(report):
    return list(reversed(sorted(report))) == report

def min_dist(report):
    return min([abs(report[i] - report[i-1]) for i in range(1, len(report))])

def max_dist(report):
    return max([abs(report[i] - report[i-1]) for i in range(1, len(report))])

def reports_to_test(report):
    yield report
    for i in range(len(report)):
        r = report.copy()
        del r[i]
        yield r

def is_safe(report):
    return (is_inc(report) or is_dec(report)) and min_dist(report) > 0 and max_dist(report) < 4

def is_safe_with_pops(report):
    for r in reports_to_test(report):
        if (is_inc(r) or is_dec(r)) and min_dist(r) > 0 and max_dist(r) < 4:
            return True
    return False


def solve(data):
    with open(data) as f:
        reports = [list(map(int, line.strip().split(' '))) for line in f.readlines()]

    safe_reports = [report for report in reports if is_safe(report)]
    yield len(safe_reports)

    safe_reports = [report for report in reports if is_safe_with_pops(report)]
    yield len(safe_reports)




