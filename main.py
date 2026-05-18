# main.py — entry point and command centre for CodeSense

import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from config import settings
from cli.scanner import scan_file

console = Console()

def show_welcome():
    console.print(Panel(
        f"[bold cyan]{settings.APP_NAME}[/bold cyan] [dim]v{settings.VERSION}[/dim]\n[dim]AI Code Reviewer[/dim]",
        border_style="cyan"
    ))

def show_results(file_path: str):
    console.print(f"\n[dim]Analyzing {file_path} ...[/dim]")
    reports = scan_file(file_path)
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Function", style="cyan", width=25)
    table.add_column("Score", justify="center", width=8)
    table.add_column("Health", width=10)
    for r in reports:
        label = r.health_label()
        color = "green" if label == "good" else "yellow" if label == "warning" else "red"
        table.add_row(
            f"{r.name}()",
            f"[{color}]{r.complexity}[/{color}]",
            f"[{color}]{label}[/{color}]"
        )
    console.print(table)

def main():
    show_welcome()
    if len(sys.argv) == 3 and sys.argv[1] == "analyze":
        show_results(sys.argv[2])
    else:
        console.print("[dim]Usage: python main.py analyze [/dim]")

if __name__ == "__main__":
    main()