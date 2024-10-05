import numpy as np

file = "input.txt"
b = "bin.txt"

hex = {}

bins = [x.strip() for x in open(b).readlines()]

for b in bins:
    l, r = b.split(" = ")
    hex[l] = r

with open(file) as f:
    s = f.read().strip()

packet = ""
for s_ in s:
    packet += hex[s_]


def ver(packet):
    v = packet[:3]
    packet = packet[3:]
    return int(v, 2), packet


def type(packet):
    t = packet[:3]
    packet = packet[3:]
    return int(t, 2), packet


def literal(packet):
    groups = []
    b = packet[:5]
    packet = packet[5:]
    while b[0] != "0":
        groups.append(b)
        b = packet[:5]
        packet = packet[5:]
    else:
        groups.append(b)
    length = 0
    nbr = ""
    for g in groups:
        length += len(g)
        nbr += g[1:]
    return int(nbr, 2), packet, length


def decode(packet):
    version, packet = ver(packet)
    type_id, packet = type(packet)
    packet_length = 6
    version_sum = [version]
    value = []
    if type_id == 4:
        v, packet, l = literal(packet)
        packet_length += l
        packet_value = v
    else:
        length_type_id = packet[0]
        packet = packet[1:]
        packet_length += 1
        if length_type_id == "0":
            length_in_bits = int(packet[:15], 2)
            packet = packet[15:]
            packet_length += 15
            while length_in_bits != 0:
                v, packet, l, val = decode(packet)
                version_sum.append(v)
                value.append(val)
                length_in_bits -= l
                packet_length += l
        else:
            nbr_of_sub_packets = int(packet[:11], 2)
            packet = packet[11:]
            packet_length += 11
            for i in range(nbr_of_sub_packets):
                v, packet, l, val = decode(packet)
                version_sum.append(v)
                packet_length += l
                value.append(val)

        match type_id:
            case 0:
                output = sum(value)
            case 1:
                output = np.prod(value)
            case 2:
                output = min(value)
            case 3:
                output = max(value)
            case 5:
                output = 1 if value[0] > value[1] else 0
            case 6:
                output = 1 if value[0] < value[1] else 0
            case 7:
                output = 1 if value[0] == value[1] else 0

        packet_value = output

    return sum(version_sum), packet, packet_length, packet_value


version_sum, _, _, packet_value = decode(packet)
# part 1
print(version_sum)
# part 2
print(packet_value)
