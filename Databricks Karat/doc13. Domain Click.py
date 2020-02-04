def count_click(array):
    results = {}

    for item in array:
        domains, counts = item

        sub_domain = ''
        sub_domains = domains.split('.')
        for i in range(len(sub_domains) - 1, -1, -1):
            domain = sub_domains[i]
            if sub_domain == '':
                sub_domain = domain
            else:
                sub_domain = domain + '.' + sub_domain

            results[sub_domain] = results.get(sub_domain, 0) + int(counts)

    return results


array = [
    ["google.com", "60"],
    ["yahoo.com", "50"],
    ["sports.yahoo.com", "80"]
]
print(count_click(array))


def count_click(array):
    results = {}

    for item in array:
        domain, counts = item
        sub_domains = domain.split('.')

        sub_domain = ''
        for i in range(len(sub_domains) - 1, -1, -1):
            if sub_domain == '':
                sub_domain = sub_domains[i]
            else:
                sub_domain = sub_domains[i] + '.' + sub_domain

            if sub_domain not in results:
                results[sub_domain] = 0
            results[sub_domain] += int(counts)
    return results

array = [
    ["google.com", "60"],
    ["yahoo.com", "50"],
    ["sports.yahoo.com", "80"]
]
print(count_click(array))
