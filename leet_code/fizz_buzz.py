class Solution:

    def fizzBuzz(self, n: int):
        ans = []
        fizz_buzz_dict = {
            3: "Fizz", 5: "Buzz"
        }

        for i in range(1, n + 1):
            fizz_buzz_str = ""
            for val in fizz_buzz_dict:
                if i % val == 0:
                    fizz_buzz_str += fizz_buzz_dict[val]

            if not fizz_buzz_str:
                ans.append(str(i))
            else:
                ans.append(fizz_buzz_str)
        return ans
