class Result:
    def __init__(self, total_time, line_count):
        self.total_time = total_time
        self.line_count = line_count

    def success_count(self, success):
        return len(success)

    def failure_count(self, failure):
        return len(failure)
