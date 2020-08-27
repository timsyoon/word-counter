# Author: Timothy Yoon
# Date: August 27, 2020
# Description: This test file contains unit tests that use various assert
# functions to test the HashMap class from hash_map.py.

import unittest
from hash_map import SLNode
from hash_map import LinkedList
from hash_map import hash_function_1
from hash_map import hash_function_2
from hash_map import HashMap
from test_student_hashmap import create_random_tuple
from test_student_hashmap import get_keys_from_map
from test_student_hashmap import check_lists_are_equals


class HashMapTester(unittest.TestCase):
    """
    Contain unit tests for the HashMap class.
    """
    def test_generate_hash_index_1(self):
        """
        Test generate_hash_index.
        :passed: yes
        """
        hash_m = HashMap(6, hash_function_1)
        print(hash_m.generate_hash_index("dog"))
        self.assertEqual(2, hash_m.generate_hash_index("dog"))

    def test_contains_key_1(self):
        """
        Test contains_key with a hash map of 2 buckets.
        :passed: yes
        """
        # Create some linked lists

        # First linked list
        ll_1 = LinkedList()
        ll_1.add_front("cat", 3)
        ll_1.add_front("bin", 2)
        ll_1.add_front("ape", 1)
        # print("ll_1:", ll_1)

        # Second linked list
        ll_2 = LinkedList()
        ll_2.add_front("fin", 3)
        ll_2.add_front("ewe", 2)
        ll_2.add_front("dim", 1)
        # print("ll_2:", ll_2)

        # Create hash map
        hash_m = HashMap(4, hash_function_1)
        hash_m._buckets[0] = ll_1
        hash_m._buckets[1] = ll_2

        print(hash_m)
        print(hash_m.contains_key("ape"))
        self.assertTrue(hash_m.contains_key("ape"))
        self.assertTrue(hash_m.contains_key("bin"))
        self.assertTrue(hash_m.contains_key("cat"))
        self.assertTrue(hash_m.contains_key("dim"))
        self.assertTrue(hash_m.contains_key("ewe"))
        self.assertTrue(hash_m.contains_key("fin"))

        self.assertFalse(hash_m.contains_key("aqe"))
        self.assertFalse(hash_m.contains_key("Bin"))
        self.assertFalse(hash_m.contains_key("BIN"))
        self.assertFalse(hash_m.contains_key("bat"))
        self.assertFalse(hash_m.contains_key("diM"))
        self.assertFalse(hash_m.contains_key("ew"))
        self.assertFalse(hash_m.contains_key("fIn"))
        self.assertFalse(hash_m.contains_key("blue"))
        self.assertFalse(hash_m.contains_key("mop"))

    def test_contains_key_2(self):
        """
        Test contains_key with a hash map of 1 bucket.
        :passed: yes
        """
        # Make a linked list
        ll_1 = LinkedList()
        ll_1.add_front("cot", 3)
        ll_1.add_front("box", 2)
        ll_1.add_front("axe", 1)
        # print("ll_1:", ll_1)

        # Make a hash map
        hash_m = HashMap(7, hash_function_2)
        hash_m._buckets[6] = ll_1

        # Make calls to contains_key
        self.assertTrue(hash_m.contains_key("axe"))
        self.assertTrue(hash_m.contains_key("box"))
        self.assertTrue(hash_m.contains_key("cot"))

        self.assertFalse(hash_m.contains_key("Axe"))
        self.assertFalse(hash_m.contains_key("aXe"))
        self.assertFalse(hash_m.contains_key("axE"))
        self.assertFalse(hash_m.contains_key("AXE"))
        self.assertFalse(hash_m.contains_key("boxx"))
        self.assertFalse(hash_m.contains_key("cat"))
        self.assertFalse(hash_m.contains_key("verb"))

        # print(hash_m.contains_key("AXE"))

    def test_contains_key_3(self):
        """
        Test contains_key with an empty hash map.
        :passed: yes
        """
        # Make an empty hash map
        hash_m = HashMap(3, hash_function_2)
        print(hash_m)

        self.assertFalse(hash_m.contains_key("cat"))
        self.assertFalse(hash_m.contains_key(" "))

    def test_contains_key_4(self):
        """
        Test contains_key with an empty hash map.
        :passed: yes
        """
        # Make an empty hash map
        hash_m = HashMap(0, hash_function_2)
        print("hash_m:", hash_m)

        self.assertFalse(hash_m.contains_key("blue"))
        self.assertFalse(hash_m.contains_key("a"))
        self.assertFalse(hash_m.contains_key(" "))

        print(hash_m.contains_key("a"))

    def test_contains_key_5(self):
        """
        Test contains_key with Example #1 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 1 ---")
        m = HashMap(50, hash_function_1)
        print(m.contains_key('key1'))
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key3', 30)
        print(m.contains_key('key1'))
        print(m.contains_key('key4'))
        print(m.contains_key('key2'))
        print(m.contains_key('key3'))
        m.remove('key3')
        print(m.contains_key('key3'))

    def test_contains_key_6(self):
        """
        Test contains_key with Example #2 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 2 ---")
        m = HashMap(75, hash_function_2)
        keys = [i for i in range(1, 1000, 20)]
        for key in keys:
            m.put(str(key), key * 42)
        print(m.size, m.capacity)
        result = True
        for key in keys:
            # all inserted keys must be present
            result = result and m.contains_key(str(key))
            # all NOT inserted keys must be absent
            result = result and not m.contains_key(str(key + 1))
        print(result)

    def test_put_1(self):
        """
        Test put() on a hash map of capacity 0.
        :passed: yes
        """
        hash_m = HashMap(0, hash_function_1)
        print("map before put():", hash_m)

        hash_m.put("key1", 10)
        print("put('key1', 10):", hash_m)

        print(hash_m.put("key1", 10))

    def test_put_2(self):
        """
        Test put() on a hash map of capacity 1.
        :passed: yes
        """
        hash_m = HashMap(1, hash_function_1)
        print("map before put():", hash_m)

        hash_m.put("key1", 10)
        print("put('key1', 10): ", hash_m)

        hash_m.put("key1", 11)
        print("put('key1', 11): ", hash_m)

        hash_m.put("key2", 20)
        print("put('key2', 20): ", hash_m)

        hash_m.put("key3", 30)
        print("put('key3', 30): ", hash_m)

        # Update key3
        hash_m.put("key3", 31)
        print("put('key3', 31): ", hash_m)

        # Update key2
        hash_m.put("key2", 21)
        print("put('key2', 21): ", hash_m)

        # Update key1
        hash_m.put("key1", 12)
        print("put('key1', 12): ", hash_m)

    def test_put_3(self):
        """
        Test put() on a hash map of capacity 6.
        :passed: yes
        """
        hash_m = HashMap(6, hash_function_1)
        print("map before put():")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key1", 10))
        print("put('key1', 10):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("box", 20))
        print("put('box', 20):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key2", 30))
        print("put('key2', 30):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key3", 40))
        print("put('key3', 40):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key4", 50))
        print("put('key4', 50):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key5", 60))
        print("put('key5', 60):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key2", 22))
        print("put('key2', 22):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key5", 55))
        print("put('key5', 55):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key6", 66))
        print("put('key6', 66):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key1", 100))
        print("put('key1', 100):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key3", 300))
        print("put('key3', 300):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("key6", 600))
        print("put('key6', 600):")
        print(hash_m)

        self.assertEqual(None, hash_m.put("box", 1000))
        print("put('box', 1000):")
        print(hash_m)

    def test_put_4(self):
        """
        Test put() with Example #1 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 1 ---")
        m = HashMap(50, hash_function_1)
        for i in range(150):
            m.put('str' + str(i), i * 100)
            if i % 25 == 24:
                print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    def test_put_5(self):
        """
        Test put() with Example #2 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 2 ---")
        m = HashMap(40, hash_function_2)
        for i in range(50):
            m.put('str' + str(i // 3), i * 100)
            if i % 10 == 9:
                print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    def test_get_1(self):
        """
        Test get() with Example #1 and #2 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 1 ---")
        m = HashMap(30, hash_function_1)
        print(m.get('key'))
        m.put('key1', 10)
        print(m.get('key1'))

        print("--- EXAMPLE 2 ---")
        m = HashMap(150, hash_function_2)
        for i in range(200, 300, 7):
            m.put(str(i), i * 10)
        print(m.size, m.capacity)
        for i in range(200, 300, 21):
            print(i, m.get(str(i)), m.get(str(i)) == i * 10)
            print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    def test_remove_1(self):
        """
        Test remove() with Example #1 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 1 ---")
        m = HashMap(50, hash_function_1)
        print(m.get('key1'))
        m.put('key1', 10)
        print(m.get('key1'))
        m.remove('key1')
        print(m.get('key1'))
        m.remove('key4')

    def test_remove_2(self):
        """
        Test remove() on a HashMap of capacity 0.
        :passed: yes
        """
        hash_m = HashMap(0, hash_function_1)
        print(hash_m.remove("key1"))

    def test_remove_3(self):
        """
        Test remove() on an empty HashMap.
        :passed: yes
        """
        hash_m = HashMap(6, hash_function_1)
        print(hash_m.remove("cat"))

    def test_empty_buckets_1(self):
        """
        Test empty_buckets() with Example #1 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 1 ---")
        m = HashMap(100, hash_function_1)
        print(m.empty_buckets(), m.size, m.capacity)
        m.put('key1', 10)
        print(m.empty_buckets(), m.size, m.capacity)
        m.put('key2', 20)
        print(m.empty_buckets(), m.size, m.capacity)
        m.put('key1', 30)
        print(m.empty_buckets(), m.size, m.capacity)
        m.put('key4', 40)
        print(m.empty_buckets(), m.size, m.capacity)

    def test_empty_buckets_2(self):
        """
        Test empty_buckets() with Example #2 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 2 ---")
        m = HashMap(50, hash_function_1)
        for i in range(150):
            m.put('key' + str(i), i * 100)
            if i % 30 == 0:
                print(m.empty_buckets(), m.size, m.capacity)

    def test_table_load_1(self):
        """
        Test table_load() with Example #1 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 1 ---")
        m = HashMap(100, hash_function_1)
        print(m.table_load())
        m.put('key1', 10)
        print(m.table_load())
        m.put('key2', 20)
        print(m.table_load())
        m.put('key1', 30)
        print(m.table_load())

    def test_table_load_2(self):
        """
        Test table_load() with Example #2 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 2 ---")
        m = HashMap(50, hash_function_1)
        for i in range(50):
            m.put('key' + str(i), i * 100)
            if i % 10 == 0:
                print(m.table_load(), m.size, m.capacity)

    def test_clear_1(self):
        """
        Test clear() with Example #1 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 1 ---")
        m = HashMap(100, hash_function_1)
        print(m.size, m.capacity)
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key1', 30)
        print(m.size, m.capacity)
        m.clear()
        print(m.size, m.capacity)

    def test_clear_2(self):
        """
        Test clear() with Example #2 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 2 ---")
        m = HashMap(50, hash_function_1)
        print(m.size, m.capacity)
        m.put('key1', 10)
        print(m.size, m.capacity)
        m.put('key2', 20)
        print(m.size, m.capacity)
        m.resize_table(100)
        print(m.size, m.capacity)
        m.clear()
        print(m.size, m.capacity)

    def test_resize_table_1(self):
        """
        Test resize_table() with Example #1 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 1 ---")
        m = HashMap(20, hash_function_1)
        m.put('key1', 10)
        print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
        m.resize_table(30)
        print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

    def test_resize_table_2(self):
        """
        Test resize_table() with Example #2 from the guidelines.
        :passed: yes
        """
        print("--- EXAMPLE 2 ---")
        m = HashMap(75, hash_function_2)
        keys = [i for i in range(1, 1000, 13)]
        for key in keys:
            m.put(str(key), key * 42)
        print(m.size, m.capacity)
        for capacity in range(111, 1000, 117):
            m.resize_table(capacity)
            result = True
            for key in keys:
                result = result and m.contains_key(str(key))
                result = result and not m.contains_key(str(key + 1))
            print(capacity, result, m.size, m.capacity,
                  round(m.table_load(), 2))
