from datetime import datetime, timedelta

class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_timeout=20):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.last_failure_time = None

    def record_failure(self):
        self.failures += 1
        self.last_failure_time = datetime.now()

    def is_open(self):
        if self.failures >= self.failure_threshold:
            if datetime.now() > self.last_failure_time + timedelta(seconds=self.recovery_timeout):
                self.reset()
                return False
            return True
        return False

    def reset(self):
        self.failures = 0
        self.last_failure_time = None
