import schedule

class Scheduler:

    def __init__(self, jobs):
        self._jobs = jobs

    def schedule_jobs(self):
        for job in self._jobs:
            schedule.every.day.at("0:00").do(job)
