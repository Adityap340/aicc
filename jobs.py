class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def get_max_deadline(jobs):
    max_deadline = 0
    for job in jobs:
        max_deadline = max(max_deadline, job.deadline)
    return max_deadline

def schedule_jobs(jobs, scheduled_jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    for job in jobs:
        for j in range(job.deadline - 1, -1, -1):
            if scheduled_jobs[j] is None:
                scheduled_jobs[j] = job
                break

def calculate_total_profit(jobs):
    total_profit = 0
    for job in jobs:
        if job is not None:
            total_profit += job.profit
    return total_profit

def main():
    n = int(input("Enter the number of jobs: "))
    jobs = []

    for i in range(n):
        print(f"Enter details for job {i + 1}:")
        id = int(input("ID: "))
        deadline = int(input("Deadline: "))
        profit = int(input("Profit: "))
        jobs.append(Job(id, deadline, profit))

    max_deadline = get_max_deadline(jobs)
    scheduled_jobs = [None] * max_deadline

    schedule_jobs(jobs, scheduled_jobs)

    total_profit = calculate_total_profit(scheduled_jobs)

    print("Scheduled Jobs: ")
    for job in scheduled_jobs:
        if job is not None:
            print(f"Job ID: {job.id}, Deadline: {job.deadline}, Profit: {job.profit}")
    print("Total Profit:", total_profit)

if __name__ == "__main__":
    main()
