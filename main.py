import click

PRIORITIES = {
    "c": "Crucial",
    "h": "High",
    "m": "Medium",
    "l": "Low",
    "o": "Optional",
}

@click.group
def my_commands():
    pass

@click.command()
@click.option("--name", prompt="Enter your name", help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}!")

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todo_file", type=click.Path(exists=False), required=0)
@click.option("-n", "--name", prompt="Enter the task name", help="The name of to-do item")
@click.option("-d", "--description", prompt="Enter the task description", help="The description of to-do item")
def add_items(name, description, priority, todo_file):
    todo_file = todo_file if todo_file is not None else "my-to-do.txt"
    with open(todo_file, "a+") as f:
        f.write(f"{name}: {description} [Priority: {PRIORITIES[priority]}]")


@click.command()
@click.argument("idx", type=int, required=1)
def delete_items(idx):
    with open("my-to-do.txt", "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open("my-to-do.txt", "w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")

@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todo_file", type=click.Path(exists=True), required = 0)
def list_items(priority, todo_file):
    filename = todo_file if todo_file is not None else "my-to-do.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for idx, todo in enumerate(todo_list):
            print(f"({idx}) - {todo}")
    else:
        for idx, todo in enumerate(todo_list):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                print(f"({idx}) - {todo}")



my_commands.add_command(hello)
my_commands.add_command(add_items)
my_commands.add_command(delete_items)
my_commands.add_command(list_items)

if __name__ == "__main__":
    my_commands()