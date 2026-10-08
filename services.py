from datetime import datetime
from pathlib import Path


class ReportService:
    TIME_FORMAT = "%d.%m.%Y %H:%M:%S"

    @staticmethod
    def save(login: str, time_in: datetime, time_out: datetime):
        line = "+----------------------+---------------------+---------------------+\n"
        header = "| login                | time_in             | time_out            |\n"
        row = (
            f"| {login[:20]:<20} | "
            f"{time_in.strftime(ReportService.TIME_FORMAT):<19} | "
            f"{time_out.strftime(ReportService.TIME_FORMAT):<19} |\n"
        )

        report = line + header + line + row + line + "\n"
        path = Path("report.txt")

        with path.open("a", encoding="utf-8") as file:
            file.write(report)
