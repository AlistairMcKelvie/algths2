from __future__ import division
def read_file(file):
    with open(file, 'r') as f:
        job_count = int(f.readline())
        jobs = []
        for i in range(job_count):
            w, l = f.readline().split()
            jobs.append({'weight': int(w), 'length': int(l)})
    return jobs

def order_jobs_diff(jobs):
    for job in jobs:
        job['priority'] = job['weight'] - job['length']
    jobs.sort(key = lambda x: (-x['priority'], -x['weight']))
    return jobs

def order_jobs_ratio(jobs):
    for job in jobs:
        job['priority'] = job['weight'] / job['length']
    jobs.sort(key = lambda x: (-x['priority']))
    return jobs


def calc_sum_of_weighted_completion_times(jobs):
    cum_time = 0
    sum = 0
    for job in jobs:
        cum_time += job['length']
        sum += job['weight'] * cum_time
    return sum
