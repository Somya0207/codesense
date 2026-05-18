# core/models.py — data shapes for CodeSense results


from dataclasses import dataclass, field


@dataclass

class Issue:

    kind:    str

    message: str

    line:    int


@dataclass

class FunctionReport:
    
    name:       str

    line:       int

    complexity: int

    issues: list[Issue] = field(default_factory=list)


    def health_label(self) -> str:

        if self.complexity <= 7:

            return "good"

        elif self.complexity <= 10:

            return "warning"

        else:

            return "critical"