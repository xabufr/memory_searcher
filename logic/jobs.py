import redis


class Jobs():
    def __init__(self):
        self.__client = redis.Redis("127.0.0.1", "6379")

    def add_job(self, job):
        self.__client.rpush("jobs", job)

    def get_next_job(self):
        job = self.__client.lpop("jobs")
        if job is not None:
            self.__client.incr("finished_jobs")
        return job

    def pending_jobs(self):
        return self.__client.llen("jobs")

    def has_next_jobs(self):
        return self.pending_jobs() > 0

    def finished_jobs(self):
        finished = self.__client.get("finished_jobs")
        return int(finished) if finished is not None else 0

    def clear(self):
        self.__client.delete("jobs")
        self.__client.delete("finished_jobs")

    def iterate(self):
        job = self.get_next_job()
        while job is not None:
            yield job
            job = self.get_next_job()
