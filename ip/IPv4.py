import re

from number.numberTuple import NumberSystem
from number.numberTuple import NumberTuple

IPV4_DEC_REGEX = r'^[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
IPV4_BIN_REGEX = r'^[0-1]{8}\.[0-1]{8}\.[0-1]{8}\.[0-1]{8}$'


class Byte:
    def __init__(self, dec_num=None, bin_num=None):
        self.bits = None
        if dec_num is not None and int(dec_num) <= 255:
            self.bits = NumberTuple(int(dec_num), NumberSystem.DECIMAL)
        elif bin_num is not None and len(bin_num) <= 8:
            self.bits = NumberTuple(bin_num, NumberSystem.BINARY)
        else:
            raise ValueError(f"Values {dec_num} and {bin_num} aren't byte conform.")

    def __str__(self):
        return self.get_decimal()

    def get_decimal(self):
        return str(self.bits.decimal_number)

    def add(self, add_byte) -> str:
        if not isinstance(add_byte, Byte):
            raise ValueError('No Byte Object.')
        ret_val = ''

        for i, b in enumerate(add_byte.get_binary()):
            if self.get_binary()[i] is b and b is '1':
                ret_val += '1'
            else:
                ret_val += '0'

        return ret_val

    def get_binary(self):
        return self.bits.binary_number.ljust(8, '0')

    def print_binary(self):
        print(self.get_binary())


class IPAddress:

    @staticmethod
    def is_ipv4_dec(value):
        return isinstance(value, str) and re.match(IPV4_DEC_REGEX, value)

    @staticmethod
    def is_ipv4_bin(value):
        return isinstance(value, str) and re.match(IPV4_BIN_REGEX, value)

    def __init__(self, bytes_value):
        self.bytes = list()
        if isinstance(bytes_value, list) and all(isinstance(e, Byte) for e in bytes_value):
            self.bytes = bytes_value
        elif self.is_ipv4_dec(bytes_value):
            self.bytes = [Byte(dec_num=b) for b in bytes_value.split('.')]
        elif self.is_ipv4_bin(bytes_value):
            self.bytes = [Byte(bin_num=b) for b in bytes_value.split('.')]
        else:
            raise ValueError(f"Input {bytes_value} is no ipv4 address.")

    def __str__(self):
        return ".".join(str(b.get_decimal()) for b in self.bytes)

    def get_binary_ip(self):
        return ".".join(str(b.get_binary()) for b in self.bytes)

    def add(self, ip_address):
        ret_val = '.'.join(ip_address.bytes[i].add(b)
                           for i, b
                           in enumerate(self.bytes))
        return IPAddress(ret_val)


class IPv4Subnet:
    def __init__(self, ip_address, subnet_mask=None, net_address=None, cidr=None, default_gateway=None):
        if not (isinstance(ip_address, IPAddress) and (isinstance(subnet_mask, IPAddress) or cidr is not None)):
            raise ValueError(f"No IP address: {ip_address},{subnet_mask}")
        if subnet_mask is None and cidr is None:
            raise ValueError(f"No subnetmask set")

        self.subnet_mask = subnet_mask
        self.cidr = cidr
        self.ip_address = ip_address
        self.default_gateway = default_gateway
        self.net_address = net_address

        if cidr is None:
            self.set_cidr_from_subnet_mask()

        if subnet_mask is None:
            self.set_subnet_mask_from_cidr()

        if net_address is None:
            self.set_net_address(ip_address, self.subnet_mask, True)

    def set_net_address(self, ip_address, subnet_mask, print_calc=False):
        self.net_address = ip_address.add(subnet_mask)

        if print_calc:
            print(f"IP-Address: {ip_address}, Subnet-Mask: {subnet_mask}")
            print(f"{'':5}", ip_address.get_binary_ip())
            print(f"{'+':5}", subnet_mask.get_binary_ip())
            print("".join('-' for i in range(10)))
            print(self.net_address.get_binary_ip())
            print(f"Network-Mask {self.net_address}")

    def set_cidr_from_subnet_mask(self):
        self.cidr = self.subnet_mask.get_binary_ip().count('1')

    def set_subnet_mask_from_cidr(self):
        bits = ''.join('1' if i <= int(self.cidr) else '0' for i in range(32))
        assert len(bits) == 32
        ip_bytes = [Byte(bin_num=bits[0:8]), Byte(bin_num=bits[8:16]), Byte(bin_num=bits[16:24]),
                    Byte(bin_num=bits[24:32])]

        self.subnet_mask = IPAddress(ip_bytes)


# ip = IPAddress("159.99.23.0")
# print(ip)
# subnet = IPv4Subnet(ip, cidr='27')
# print(subnet)
