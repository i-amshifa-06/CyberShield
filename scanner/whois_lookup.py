import whois


def clean_value(value):

    # If value is list
    if isinstance(value, list):

        cleaned = []

        for item in value:

            if item not in cleaned:
                cleaned.append(str(item))

        return ", ".join(cleaned)

    # If normal value
    return str(value)


def get_whois_info(domain):

    try:

        data = whois.whois(domain)

        result = {

            "domain_name":
                clean_value(data.domain_name),

            "registrar":
                clean_value(data.registrar),

            "creation_date":
                clean_value(data.creation_date),

            "expiration_date":
                clean_value(data.expiration_date),

            "name_servers":
                clean_value(data.name_servers),

            "emails":
                clean_value(data.emails),

            "country":
                clean_value(data.country)

        }

        return result

    except Exception as e:

        return {
            "error": str(e)
        }
