class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        def DP4(count):
            if count == 1:
                return 1
            if count == 2:
                return 2
            if count == 3:
                return 4
            all_counts = [0] * (count + 1)
            all_counts[0] = 1
            all_counts[1] = 1
            all_counts[2] = 2
            all_counts[3] = 4

            for i in range(4, count + 1):
                all_counts[i] = all_counts[i - 1] + all_counts[i - 2] + all_counts[i - 3] + all_counts[i - 4]

            return all_counts[count]

        def DP3(count):
            if count == 1:
                return 1
            if count == 2:
                return 2
            all_counts = [0] * (count + 1)
            all_counts[0] = 1
            all_counts[1] = 1
            all_counts[2] = 2
            if count < 3:
                return all_counts[count]
            for i in range(3, count + 1):
                all_counts[i] = all_counts[i - 1] + all_counts[i - 2] + all_counts[i - 3]

            return all_counts[count]

        total_press = []
        current_char = pressedKeys[0]
        count = 1
        for i in range(1, len(pressedKeys)):
            if pressedKeys[i] == current_char:
                count += 1
            else:
                pressed_info = (current_char, count)
                count = 1
                current_char = pressedKeys[i]
                total_press.append(pressed_info)

        pressed_info = (current_char, count)
        total_press.append(pressed_info)

        S = 1
        for press_tuple in total_press:
            if press_tuple[0] == '7' or press_tuple[0] == '9':
                S *= DP4(press_tuple[1])
            else:
                S *= DP3(press_tuple[1])

        return S % (10**9 + 7)
