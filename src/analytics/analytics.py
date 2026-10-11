from tabulate import tabulate
import database


def print_table(title, rows, headers):
    print(f"\n{title}")
    print(tabulate(rows, headers=headers, tablefmt="rounded_outline", floatfmt=",.2f"))


def show_analytics():
    print_table("Summary", database.total_and_average(), ["Total", "Average", "Rows"])
    print_table("Spending by category", database.spending_by_category(), ["Category", "Total"])
    print_table("Top 3 expenses", database.top_expenses(), ["Name", "Amount", "Category"])