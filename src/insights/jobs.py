from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        self.jobs_list = list()
        with open(path, "r", encoding="utf-8") as file:
            open_file = csv.DictReader(file, delimiter=",", quotechar='"')
            self.jobs_list = [row for row in open_file]
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = list()
        for job in self.jobs_list:
            job_types.append(job["job_type"])
        return set(job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict
    ) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria tem que ser um dicionário")
        filtered_jobs = jobs
        for key, value in filter_criteria.items():
            filtered_jobs = [
                job for job in filtered_jobs if job.get(key) == value
            ]

        return filtered_jobs
