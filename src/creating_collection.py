from typing import List


def create_collection(data: List[str]) -> tuple:

    collection = []

    for record in data:
        split_record = record.split(',')
        for address in split_record:
            _, port = address.rsplit(':', 1)
            ip_type, ip = _.split('@') if '@' in _ else (None, _)
            ip_type = 'ipv4' if '.' in ip else 'ipv6' if ':' in ip else ip_type
            ip = '0.0.0.0' if ip_type == 'ipv4' and ip == '' else '::' if ip_type == 'ipv6' and ip == '' else ip
            collection.append({'IP': ip, 'Type': ip_type, 'Port': port})

    return tuple(collection)
