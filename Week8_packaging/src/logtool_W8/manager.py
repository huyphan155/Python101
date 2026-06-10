class LogManager:
    def __init__(self):
        self.logs = []
        frequency = {}

    def add_log(self, log):
        self.logs.append(log)

    def get_logs(self):
        return self.logs

    def count_frequency(self):
        frequency = {}
        for line in self.logs:
            level = line.level
            if level not in frequency:
                frequency[level] = 1
            else:
                frequency[level] += 1
        return frequency

