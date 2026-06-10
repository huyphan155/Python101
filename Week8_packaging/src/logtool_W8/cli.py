import typer

app = typer.Typer()

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