from Jobs import Jobs
import unittest


class tests(unittest.TestCase):
    def setUp(self):
        self.jobs = Jobs()
        self.jobs.clear()

    def test_can_retrieve_one_inserted(self):
        job = "hello"
        self.jobs.add_job(job)
        assert self.jobs.get_next_job() == job

    def test_finished_jobs(self):
        assert self.jobs.finished_jobs() == 0
        job = "hello"
        self.jobs.add_job(job)
        self.jobs.get_next_job()
        assert 1 == self.jobs.finished_jobs()

    def test_jobs_order(self):
        jobs = range(10, 0, -1) + range(1, 1100)
        jobs = ["job-"+str(job) for job in jobs]
        for job in jobs:
            self.jobs.add_job(job)

        for job in jobs:
            assert self.jobs.get_next_job() == job

    def test_pending_jobs(self):
        assert self.jobs.pending_jobs() == 0
        self.jobs.add_job("coucou")
        assert 1 == self.jobs.pending_jobs()
        assert self.jobs.has_next_jobs()
        self.jobs.get_next_job()