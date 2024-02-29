import click


PRIORITIES = {
    "c": "Crucial",
    "h": "High",
    "m": "Medium",
    "l": "Low",
    "o": "Optional",
}

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todo_file", type=click.Path(exists=False), required=0)
@click.option("-n", "--name", prompt="Enter the task name", help="The name of to-do item")
@click.option("-d", "--description", prompt="Enter the task description", help="The description of to-do item")
def add_items(name, description, priority, todo_file):
    todo_file = todo_file if todo_file is not None else "my-to-do.txt"
    with open(todo_file, "a+") as f:
        f.write(f"{name}: {description} [Priority: {PRIORITIES[priority]}]")




if __name__ == "__main__":
    add_items()