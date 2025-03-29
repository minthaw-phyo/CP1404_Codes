import datetime

class Project:


    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Initialise a Project object."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """Return a string representation of a object."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Compare projects by name for sorting."""
        return self.name.lower() < other.name.lower()

    def is_complete(self):
        """Return True if the project is complete."""
        return self.completion == 100

    def update(self, new_completion=None, new_priority=None):
        """Update the project's completion"""
        if new_completion is not None:
            self.completion = new_completion
        if new_priority is not None:
            self.priority = new_priority
