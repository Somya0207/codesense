# main.py — the entry point of CodeSense

from rich.console import Console
from rich.panel import Panel
from config import settings

console = Console()

def main():
    console.print(
        Panel(
            f"[bold red]{settings.APP_NAME}[/bold red] [dim]v{settings.VERSION}[/dim]\n[dim]AI Code Reviewer[/dim]",
            border_style="red"
        )
    )
    console.print("[magenta]Project is ready![/magenta]")
    console.print(f"[dim]Debug mode: {settings.DEBUG}[/dim]")

if __name__ == "__main__":
    main()