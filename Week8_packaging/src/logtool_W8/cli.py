import typer
from . import VERSION
from .parser import parse_log
from .manager import LogManager
from .api_client import upload_log

app = typer.Typer()

@app.command()
def version():
    print(f"LogTool version {VERSION}")

@app.command()
def parse(path: str):
    with open(path, "r") as file:
        for line in file:
            log = parse_log(line)
            print(f"{log.level}: {log.message}"            )

@app.command()
def stats(path: str):
    manager = LogManager()

    with open(path, "r") as file:
        for line in file:
            log = parse_log(line)
            manager.add_log(log)

    frequency = manager.count_frequency()

    for level, count in frequency.items():
        print(f"{level}: {count}")

    upload_log(frequency)


# dumb command for learning
@app.command()
def hello():
    print("Hello World")

@app.command()
def greet(
    name: str = typer.Argument(...),
    upper: bool = typer.Option(False)
):
    if upper:
        print(name.upper())
    else:
        print(name)

@app.command()
def show_config(
    host: str = typer.Option("localhost_default"),
    port: int = typer.Option(0)
):
    print(host)
    print(port)

@app.command()
def add(a: int, b: int):
    print(a+b)

@app.command()
def repeat(number: int):
    for i in range(number):
        print("Hello")

if __name__ == "__main__":
    app()