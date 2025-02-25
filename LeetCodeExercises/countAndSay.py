class Solution:

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        i = 1
        string = "1"
        while i < n:
            str_len = 1
            current_char = string[0]
            string_keys = []
            string_values = []
            for j in range(1, len(string)):
                if string[j] != current_char:
                    string_keys.append(current_char)
                    string_values.append(str_len)
                    current_char = string[j]
                    str_len = 1
                else:
                    str_len += 1

            string_keys.append(current_char)
            string_values.append(str_len)

            new_string = ""

            for k in range(len(string_keys)):
                new_string += str(string_values[k])
                new_string += string_keys[k]

            string = new_string
            i += 1

        return string


solution = Solution()
print(solution.countAndSay(5))
