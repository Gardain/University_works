import unittest

from lab3.main import is_valid_ipv4, find_all_ipv4


class TestIPv4Regex(unittest.TestCase):

    def test_valid_ips(self):
        valid_ips = ["192.168.1.1", "255.255.255.255", "0.0.0.0", "127.0.0.1"]
        for ip in valid_ips:
            self.assertTrue(is_valid_ipv4(ip), f"IP {ip} должен быть корректным")

    def test_invalid_ips(self):
        invalid_ips = ["256.100.100.100", "192.168.1.256", "192.168.1", "192.168..1", "abc.def.gha.bcd",
                       "999.999.999.999"]
        for ip in invalid_ips:
            self.assertFalse(is_valid_ipv4(ip), f"IP {ip} должен быть некорректным")

    def test_find_all_ipv4(self):
        text = "Тестовые IP: 192.168.1.1 и 10.0.0.1, а также 300.1.1.1"
        found_ips = find_all_ipv4(text)
        self.assertEqual(found_ips, ['192.168.1.1', '10.0.0.1'], "Должно находить только корректные IP")


if __name__ == "__main__":
    unittest.main()
