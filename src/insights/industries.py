from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        industries = list()
        for job in self.jobs_list:
            if job["industry"] != "":
                industries.append(job["industry"])
        return set(industries)
