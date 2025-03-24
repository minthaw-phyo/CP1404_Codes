from project import Project
import datetime

FILENAME = "projects.txt"


def main():
    """Main function to manage the project management program."""
    print("Welcome to Pythonic Project Management")

    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

    while True:
        print(menu)
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load projects: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save projects: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save = input("Would you like to save to projects.txt? (y/n): ").lower()
            if save == 'y':
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option. Please try again.")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip header line
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    name = parts[0]
                    start_date = parts[1]
                    priority = int(parts[2])
                    cost_estimate = float(parts[3])  # Now explicitly handled as float
                    completion = int(parts[4])  # Handling as percentage

                    # Create Project object and add to list
                    projects.append(Project(name, start_date, priority, cost_estimate, completion))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list.")
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion}\n")


def display_projects(projects):
    """Display completed and incomplete projects."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("\nIncomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(complete):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects that start after a specific date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date >= date]
    filtered_projects.sort(key=lambda x: x.start_date)
    for project in filtered_projects:
        print(f"  {project}")


def add_new_project(projects):
    """Add a new project."""
    print("\nLet's add a new project:")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(new_project)



def update_project(projects):
    """Update an existing project."""
    # Sort projects by priority and display with index numbers
    sorted_projects = sorted(projects)

    print("\nCurrent Projects:")
    for index, project in enumerate(sorted_projects):
        print(f"{index}. {project}")

    try:
        index = int(input("\nProject choice: "))
        if 0 <= index < len(sorted_projects):
            project = sorted_projects[index]

            print(f"{project}")

            # Get new completion value (skip if blank)
            new_completion = input("New Percentage: ")
            if new_completion:
                new_completion = int(new_completion)
            else:
                new_completion = project.completion

            # Get new priority value (skip if blank)
            new_priority = input("New Percentage: ")
            if new_priority:
                new_priority = int(new_priority)
            else:
                new_priority = project.priority
            project.update(new_completion, new_priority)

        else:
            print("Invalid project number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
