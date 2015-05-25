#
# Filters for using in when statements.

PORTS = [80, 443, 488, 8008, 8009, 8443]

def has_restricted_port(backends):
    for backend in backends:
        if 'servers' in backend:
            for server in backend['servers']:
                if 'port' in server and server['port'] not in PORTS:
                    return True
    return False

class FilterModule(object):
    def filters(self):
        return {
            'has_restricted_port': has_restricted_port
        }

