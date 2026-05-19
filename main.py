# main.py — entry point and CLI for CodeSense

import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from config import settings
from cli.scanner import scan_file
from storage.database import init_db, save_run, get_history

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

    warnings = 0
    for r in reports:
        label = r.health_label()
        if label == "good":
            colour = "green"
        elif label == "warning":
            colour = "yellow"
            warnings += 1
        else:
            colour = "red"
            warnings += 1
        table.add_row(
            f"{r.name}()",
            f"{r.line}",
            f"{r.complexity}",
            f"[{colour}]{label}[/{colour}]"
        )
    console.print(table)

    save_run(file_path, len(reports), warnings)
    console.print(f"[dim]✓ Saved to history — {len(reports)} functions, {warnings} warnings[/dim]")

def show_history():
    runs = get_history()
    if not runs:
        console.print("[yellow]No history yet. Run an analysis first.[/yellow]")
        return
    table = Table(title="Analysis History")
    table.add_column("ID", style="dim")
    table.add_column("File", style="cyan")
    table.add_column("Date", style="dim")
    table.add_column("Functions", justify="center")
    table.add_column("Warnings", justify="center")
    for r in runs:
        w_colour = "red" if r.warnings > 0 else "green"
        table.add_row(
            str(r.id),
            r.file_path,
            r.run_date.strftime("%Y-%m-%d %H:%M"),
            str(r.total),
            f"[{w_colour}]{r.warnings}[/{w_colour}]"
        )
    console.print(table)

def main():
    init_db()
    show_banner()
    if len(sys.argv) == 3 and sys.argv[1] == "analyze":
        show_results(sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == "history":
        show_history()
    else:
        console.print("[dim]Usage:[/dim]")
        console.print("[dim]  python main.py analyze <file.py>[/dim]")
        console.print("[dim]  python main.py history[/dim]")

if __name__ == "__main__":
    main()