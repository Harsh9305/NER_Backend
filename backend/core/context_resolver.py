def resolve_context(entities):
    resolved = entities.copy()
    if 'FORWARDER' not in resolved:
        resolved['FORWARDER'] = 'N:1'
    if 'LINE' not in resolved:
        resolved['LINE'] = 'Line7'
    return resolved