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

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
