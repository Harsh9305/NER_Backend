def generate_output(entities):
    output = []
    output.append("Entity1 = DUT")
    output.append("Entity1 Keywords =")
    output.append(f"UserVSI-1 = VLAN={entities.get('VLAN', 'N/A')}, PBIT={entities.get('PBIT', '0')}")
    output.append(f"UserVSI-1 Parent = {entities.get('LINE', 'Line7')}")
    output.append(f"Forwarder = {entities.get('FORWARDER', 'N:1')}")
    return "\n".join(output)