from datetime import datetime, time
import unittest

def get_current_time():
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M:%S")
    return formatted_time

class Greeter:
    def greet(self, name):
        trimmed_name = name.strip()
        capitalized_name = trimmed_name.capitalize()
        current_time = datetime.strptime(get_current_time(), "%H:%M:%S").time()

        if time(6, 0) <= current_time < time(12, 0):
            greeting = f"Buenos días {capitalized_name}"
        elif time(18, 0) <= current_time < time(22, 0):
            greeting = f"Buenas tardes {capitalized_name}"
        else:
            greeting = f"Buenas noches {capitalized_name}"

        print(f"Se llamó a greet con el nombre '{trimmed_name}' a las {current_time}: {greeting}")
        return greeting
    
class TestGreeter(unittest.TestCase):
    current_time = datetime.strptime(get_current_time(), "%H:%M:%S").time()
    if time(6, 0) <= current_time < time(12, 0):
        def test_greet_morning(self):
            greeter = Greeter()
            result = greeter.greet("john")
    
            expected = f"Buenos días john"
            self.assertEqual(result, expected)
    elif time(18, 0) <= current_time < time(22, 0):
        def test_greet_afternoon(self):
            greeter = Greeter()
            result = greeter.greet("alice")

            expected = f"Buenas tardes Alice"
            self.assertEqual(result, expected)
    else:        
        def test_greet_night(self):
            greeter = Greeter()
            result = greeter.greet("bob")

            expected = f"Buenas noches Bob"
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

