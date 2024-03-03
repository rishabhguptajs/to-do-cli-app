import click
import sys
import codecs
import os

@click.command()
@click.option('--n', type=int, required=True)
def dots(n):
    click.echo('.' * n)

# dots()

@click.command()
@click.option('--form', '-f', 'from_')
@click.option('--to', '-t')
def reserved_param(from_, to):
    click.echo(f"from {from_} to {to}")

# reserved_param()
    
@click.command()
@click.option('--n', default = 1, show_default = True, help="No. of Dots to print ")
@click.option('--gr', default = False, is_flag= True, show_default=True, help="Greet the world! ")
@click.option('--br', default = False, is_flag = True, show_default = True, help="No. of dashes to print ")
def dotsBR(n, gr, br):
    if gr:
        click.echo("Hello People!")
    click.echo('.'*n)
    if br:
        click.echo('-'*n)

# dotsBR()
        
@click.command()
@click.option('--pos', nargs = 3, help="Sides of triangle: ", type=float)
def perimeter(pos):
    global x, y, z
    x , y, z = pos
    click.echo(f"The perimeter of triangle with sides {x}, {y} and {z} is {x+y+z}")

# perimeter()
    

@click.command()
@click.option('--commit', is_flag = True, required=True, help="Initialise the commit operation")
@click.option('-m', required=False, default="", help="Commit message")
def commit(commit, m):
    if not m:
        click.echo(f"Committed changes")
    else:
        click.echo(f"Committed changes with message - {m}")

# commit()
        
@click.command()
@click.option('--shout/--no-shout', default=False)
def info(shout):
    sys_env = sys.platform
    if shout:
        click.echo(sys_env.upper() + "!!!!!")
    else:
        click.echo(sys_env)

# info()

@click.command()
@click.option('--upper', 'transformation', flag_value = 'upper')
@click.option('--lower', 'transformation', flag_value = 'lower', default = True)
def infoTR(transformation):
    click.echo(getattr(sys.platform, transformation)())

# infoTR()
    
@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def encode(password):
    click.echo(f"Encoded: {codecs.encode(password, 'rot13')}")

# encode()
    
@click.command()
@click.option(
    '--username',
    prompt=True,
    default=lambda: os.environ.get("USER", ""),
    show_default = "current user"
)
def helloUser(username):
    click.echo(f"Hello, {username}!!")

# helloUser()
    

