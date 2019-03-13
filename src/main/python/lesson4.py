import math
import re
from typing import Iterable
from typing import NewType
from typing import Tuple
from typing import TypeVar
from typing import Union

IPv4 = NewType('IPv4', Tuple[int, int, int, int])
IPv4Network = NewType('IPv4Network', Tuple[IPv4, int])
BinIPv4 = NewType('BinIPv4', Tuple[str, str, str, str])

E = TypeVar('E')


def to_segments(array: Iterable[E], segment_size: int, fill_item: E = None) -> Tuple[Tuple[E]]:
    total_segments = math.ceil(len(array) / float(segment_size))
    total_missing = total_segments * segment_size - len(array)
    missing = [fill_item] * total_missing
    if isinstance(array, (str,)):
        missing = ''.join(missing)
    array = missing + array
    return tuple(array[index:index + segment_size] for index in range(0, len(array), segment_size))


def to_octets(bin_text: str) -> Tuple[str]:
    return to_segments(bin_text, 8, '0')


IP_REGEX = re.compile(r'(?P<address>[0-9]+(?:\.[0-9]+){3})/(?P<mask>[0-9]+)?')


def str_to_ipv4(text: str) -> Tuple[IPv4, int]:
    match = IP_REGEX.match(text)
    if not match:
        raise Exception('{} is not a valid ipv4'.format(text))
    str_address, str_mask = match.groups()
    ipv4 = tuple(map(int, str_address.split('.')))
    mask = int(str_mask)
    return ipv4, mask


def ip_to_bin(ip: IPv4, zfill=8) -> BinIPv4:
    return tuple(map(lambda octet: bin(octet)[2:].zfill(zfill), ip))


def ip_to_hex(ip: IPv4, zfill=2) -> BinIPv4:
    return tuple(map(lambda octet: hex(octet)[2:].zfill(zfill), ip))


def mask_to_bin(mask: int, max_size=32) -> str:
    return ('1' * mask) + ('0' * (max_size - mask))


def mask_to_ip(mask: Union[str, int]) -> IPv4:
    if isinstance(mask, (int,)):
        mask = mask_to_bin(mask)
    return tuple(map(lambda it: int(it, 2), to_octets(mask)))


def lazy_logic_and(a: Iterable[E], b: Iterable[E]) -> Iterable[E]:
    return map(lambda t: t[0] & t[1], zip(a, b))


def logic_and(a: Iterable[E], b: Iterable[E]) -> Tuple[E]:
    return tuple(lazy_logic_and(a, b))


def lazy_logic_not(a: Iterable[E], bits_size) -> Iterable[E]:
    max_value = 1 << bits_size
    all_ones = max_value - 1
    return map(lambda it: it ^ all_ones, a)


def logic_not(a: Iterable[E], bits_size) -> Tuple[E]:
    return tuple(lazy_logic_not(a), bits_size)


def lazy_logic_or(a: Iterable[E], b: Iterable[E]) -> Iterable[E]:
    return map(lambda t: t[0] | t[1], zip(a, b))


def logic_or(a: Iterable[E], b: Iterable[E]) -> Iterable[E]:
    return tuple(lazy_logic_or(a, b))


ipv4_classes = (
    ('A', '0'),
    ('B', '10'),
    ('C', '110'),
    ('D', '1110'),
    ('E', '1111'),
)

ipv4_default_masks = {
    'A': 8,
    'B': 16,
    'C': 24,
}


def get_ipv4_class(ip: IPv4):
    first_octet = bin(ip[0])[2:].zfill(8)
    for class_name, prefix in ipv4_classes:
        if first_octet.startswith(prefix):
            return class_name
    return None


def get_ipv4_network(ip: IPv4, mask=None) -> IPv4Network:
    if mask is None:
        ipv4_class = get_ipv4_class(ip)
        mask = ipv4_default_masks.get(ipv4_class, 0)
    ip_mask = mask_to_ip(mask)
    return logic_and(ip, ip_mask), mask


def get_ipv4_broadcast(ip: IPv4, mask=None) -> IPv4:
    if mask is None:
        ipv4_class = get_ipv4_class(ip)
        mask = ipv4_default_masks.get(ipv4_class, 0)
    ipv4_mask = lazy_logic_not(mask_to_ip(mask), 8)
    return logic_or(ip, ipv4_mask)


ipv4_private_networks = (
    ((10, 0, 0, 0), 8),
    ((172, 16, 0, 0), 12),
    ((192, 168, 0, 0), 16),
    ((169, 254, 0, 0), 16),
)


def is_private(ip: IPv4):
    for private_address, mask in ipv4_private_networks:
        network, _ = get_ipv4_network(ip, mask)
        if private_address == network:
            return True
    return False


class IPv4NetworkInfo(object):
    address: IPv4
    binary_address: str
    hex_address: str
    mask: int
    binary_mask: str
    broadcast: IPv4
    hex_broadcast: str
    binary_broadcast: str

    @classmethod
    def from_network(cls, network: IPv4Network):
        address, mask = network
        broadcast = get_ipv4_broadcast(*network)
        return cls(
            address=address,
            binary_address=ip_to_bin(address),
            hex_address=ip_to_hex(address),
            mask=mask,
            binary_mask=mask_to_bin(mask),
            broadcast=broadcast,
            hex_broadcast=ip_to_hex(broadcast),
            binary_broadcast=ip_to_bin(broadcast)
        )

    def __init__(self,
                 address: IPv4,
                 binary_address: str,
                 hex_address: str,
                 mask: int,
                 binary_mask: str,
                 broadcast: IPv4,
                 hex_broadcast: str,
                 binary_broadcast: str):
        self.address = address
        self.binary_address = binary_address
        self.hex_address = hex_address
        self.mask = mask
        self.binary_mask = binary_mask
        self.broadcast = broadcast
        self.hex_broadcast = hex_broadcast
        self.binary_broadcast = binary_broadcast

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(self.__dict__))


class IPv4AddressInfo(object):
    address: IPv4
    binary_address: str
    hex_address: str
    network: IPv4NetworkInfo

    @classmethod
    def from_address(cls, address: IPv4, mask=None):
        return cls(
            address=address,
            binary_address=ip_to_bin(address),
            hex_address=ip_to_hex(address),
            network=IPv4NetworkInfo.from_network(get_ipv4_network(address, mask))
        )

    def __init__(self, address: IPv4, binary_address: str, hex_address: str, network: IPv4NetworkInfo):
        self.address = address
        self.binary_address = binary_address
        self.hex_address = hex_address
        self.network = network

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(self.__dict__))


if __name__ == '__main__':
    ip, mask = str_to_ipv4('192.168.0.1/28')
    print(IPv4AddressInfo.from_address(ip, mask))
