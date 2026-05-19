#main.py — entry point and CLI for CodeSense

import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from config import settings
from cli.scanner import scan_file

console = Console()

def show_banner():
    console.print(Panel(
        f"[bold cyan]{settings.APP_NAME}[/bold cyan] [dim]v{settings.VERSION}[/dim]\n[dim]AI Code Reviewer[/dim]",
        border_style="cyan"
    ))

def show_results(file_path: str):
    console.print(f"\n[dim]Analyzing [cyan]{file_path}[/cyan]...[/dim]")
    reports = scan_file(file_path)

    if not reports:
        console.print("[yellow]No functions found in this file.[/yellow]")
        return

    table = Table(title=f"Results for {file_path}")
    table.add_column("Function", style="cyan")
    table.add_column("Line", style="dim")
    table.add_column("Score", justify="center")
    table.add_column("Health", justify="center")

    for r in reports:
        label = r.health_label()
        if label == "good":
            colour = "green"
        elif label == "warning":
            colour = "yellow"
        else:
            colour = "red"
        table.add_row(
            f"{r.name}()",
            f"{r.line}",
            f"{r.complexity}",
            f"[{colour}]{label}[/{colour}]"
        )
    console.print(table)

def main():
    show_banner()
    if len(sys.argv) == 3 and sys.argv[1] == "analyze":
        show_results(sys.argv[2])
    else:
        console.print("[dim]Usage: python main.py analyze <file.py>[/dim]")

if __name__ == "__main__":
    main()