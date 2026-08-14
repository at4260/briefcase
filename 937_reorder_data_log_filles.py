class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
        # a1 9 2 3 1 => numbers, numbers append
        # g1 act car => letters, letters append
        # ab1 off key dog
        # cd1 off key dog

        # O(m*n log n) time, O(m*n) space
            # other option is to hand implement sort
            # but would not do it while iterating through logs - becomes O(m* n2) for constantly reshifting digit_logs
            # would put all in digit_logs, then sort for O(m* n log n) time 

        letter_logs, digit_logs = [], []
        for log in logs:
            split_log = log.split(" ")
            digit_logs.append(log) if split_log[1].isdigit() else letter_logs.append(log)

        # first key is to sort by contents, then sort by identifier if contents same
        return sorted(letter_logs, key=lambda x: (x.split(" ")[1:], x.split(" ")[0])) + digit_logs
    