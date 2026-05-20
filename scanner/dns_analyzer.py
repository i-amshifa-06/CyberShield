import dns.resolver


def clean_record(value):

    value = str(value)

    value = value.replace('\"', '')

    return value


def get_dns_records(domain):

    records = {
        "A": [],
        "MX": [],
        "NS": [],
        "TXT": [],
        "CNAME": []
    }

    record_types = ["A", "MX", "NS", "TXT", "CNAME"]

    for record_type in record_types:

        try:

            answers = dns.resolver.resolve(domain, record_type)

            for answer in answers:

                cleaned = clean_record(answer)

                records[record_type].append(cleaned)

        except:
            pass

    return records
