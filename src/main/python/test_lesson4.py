from unittest import TestCase

from lesson4 import *


class TestSegments(TestCase):
    def test_to_segment(self):
        self.assertEqual(to_segments('ABCD', 1), ('A', 'B', 'C', 'D'))
        self.assertEqual(to_segments('ABCD', 2), ('AB', 'CD',))
        self.assertEqual(to_segments('0000111100001111', 4), ('0000', '1111', '0000', '1111'))
        self.assertEqual(to_segments('0111100001111', 4, '0'), ('0000', '1111', '0000', '1111'))

    def test_to_octets(self):
        self.assertEqual(to_octets('0000111100001111'), ('00001111', '00001111',))
        self.assertEqual(to_octets('111100001111'), ('00001111', '00001111',))


class TestMask(TestCase):
    def test_mask_to_bin(self):
        self.assertEquals(mask_to_bin(8), '11111111000000000000000000000000')
        self.assertEquals(mask_to_bin(10), '11111111110000000000000000000000')
        self.assertEquals(mask_to_bin(16), '11111111111111110000000000000000')
        self.assertEquals(mask_to_bin(20), '11111111111111111111000000000000')
        self.assertEquals(mask_to_bin(24), '11111111111111111111111100000000')
        self.assertEquals(mask_to_bin(30), '11111111111111111111111111111100')
        self.assertEquals(mask_to_bin(32), '11111111111111111111111111111111')

    def test_mask_to_ip(self):
        self.assertEqual(mask_to_ip(0), (0, 0, 0, 0))
        self.assertEqual(mask_to_ip(8), (255, 0, 0, 0))
        self.assertEqual(mask_to_ip(16), (255, 255, 0, 0))
        self.assertEqual(mask_to_ip(24), (255, 255, 255, 0))
        self.assertEqual(mask_to_ip(32), (255, 255, 255, 255))


class TestIPv4(TestCase):
    def test_ip_to_bin(self):
        self.assertEqual(ip_to_bin((255, 0, 0, 0)), ('11111111', '00000000', '00000000', '00000000'))
        self.assertEqual(ip_to_bin((255, 255, 0, 0)), ('11111111', '11111111', '00000000', '00000000'))
        self.assertEqual(ip_to_bin((255, 255, 255, 0)), ('11111111', '11111111', '11111111', '00000000'))
        self.assertEqual(ip_to_bin((255, 255, 255, 255)), ('11111111', '11111111', '11111111', '11111111'))
        self.assertEqual(ip_to_bin((10, 0, 0, 0)), ('00001010', '00000000', '00000000', '00000000'))
        self.assertEqual(ip_to_bin((172, 16, 0, 0)), ('10101100', '00010000', '00000000', '00000000'))
        self.assertEqual(ip_to_bin((192, 168, 0, 0)), ('11000000', '10101000', '00000000', '00000000'))

    def test_get_ipv4_class(self):
        self.assertEqual(get_ipv4_class((0, 0, 0, 0)), 'A')
        self.assertEqual(get_ipv4_class((10, 0, 0, 0)), 'A')
        self.assertEqual(get_ipv4_class((127, 255, 255, 255)), 'A')
        self.assertEqual(get_ipv4_class((128, 0, 0, 0)), 'B')
        self.assertEqual(get_ipv4_class((128, 16, 0, 0)), 'B')
        self.assertEqual(get_ipv4_class((191, 255, 255, 255)), 'B')
        self.assertEqual(get_ipv4_class((192, 0, 0, 0)), 'C')
        self.assertEqual(get_ipv4_class((192, 168, 0, 0)), 'C')
        self.assertEqual(get_ipv4_class((223, 255, 255, 255)), 'C')
        self.assertEqual(get_ipv4_class((224, 0, 0, 0)), 'D')
        self.assertEqual(get_ipv4_class((239, 255, 255, 255)), 'D')
        self.assertEqual(get_ipv4_class((240, 0, 0, 0)), 'E')
        self.assertEqual(get_ipv4_class((247, 255, 255, 255)), 'E')

    def test_get_network(self):
        self.assertEqual(get_ipv4_network((0, 0, 0, 0)), ((0, 0, 0, 0), 8))
        self.assertEqual(get_ipv4_network((10, 0, 0, 0)), ((10, 0, 0, 0), 8))
        self.assertEqual(get_ipv4_network((127, 0, 0, 0)), ((127, 0, 0, 0), 8))
        self.assertEqual(get_ipv4_network((128, 0, 0, 0)), ((128, 0, 0, 0), 16))
        self.assertEqual(get_ipv4_network((191, 0, 0, 0)), ((191, 0, 0, 0), 16))
        self.assertEqual(get_ipv4_network((192, 0, 0, 0)), ((192, 0, 0, 0), 24))
        self.assertEqual(get_ipv4_network((223, 0, 0, 0)), ((223, 0, 0, 0), 24))

        self.assertEqual(get_ipv4_network((2, 2, 2, 2), 16), ((2, 2, 0, 0), 16))
        self.assertEqual(get_ipv4_network((10, 10, 10, 10), 24), ((10, 10, 10, 0), 24))
        self.assertEqual(get_ipv4_network((127, 127, 127, 127), 8), ((127, 0, 0, 0), 8))
        self.assertEqual(get_ipv4_network((128, 128, 128, 128), 24), ((128, 128, 128, 0), 24))

    def test_get_broadcast(self):
        self.assertEqual(get_ipv4_broadcast((0, 0, 0, 0)), (0, 255, 255, 255))
        self.assertEqual(get_ipv4_broadcast((127, 0, 0, 0)), (127, 255, 255, 255))
        self.assertEqual(get_ipv4_broadcast((128, 0, 0, 0)), (128, 0, 255, 255))
        self.assertEqual(get_ipv4_broadcast((191, 0, 0, 0)), (191, 0, 255, 255))
        self.assertEqual(get_ipv4_broadcast((192, 0, 0, 0)), (192, 0, 0, 255))
        self.assertEqual(get_ipv4_broadcast((223, 0, 0, 0)), (223, 0, 0, 255))

    def test_is_private(self):
        self.assertEqual(is_private((8, 8, 8, 8)), False)

        self.assertEqual(is_private((10, 0, 0, 0)), True)
        self.assertEqual(is_private((10, 255, 255, 255)), True)

        self.assertEqual(is_private((172, 16, 0, 0)), True)
        self.assertEqual(is_private((172, 31, 255, 255)), True)
        self.assertEqual(is_private((172, 32, 0, 0)), False)

        self.assertEqual(is_private((192, 168, 0, 1)), True)
        self.assertEqual(is_private((192, 168, 1, 1)), True)
