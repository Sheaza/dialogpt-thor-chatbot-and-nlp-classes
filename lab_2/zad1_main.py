import pandas as pd

# employees = [["Jan", "Kowalski", 4500], ["Kasia", "Kowalska", 6000], ["Ari", "Kwiat", 5400]]
# rec_invoices = [['2022-06-05', 30000], ['2022-07-05', 15000], ['2022-03-05', 50000]]
# iss_invoices = [['2022-07-05', 300], ['2022-04-05', 1500], ['2022-02-05', 500]]
#
# employees_df = pd.DataFrame(employees, columns=["name", "surname", "salary"])
# rec_invoices_df = pd.DataFrame(rec_invoices, columns=["date", "amount"])
# iss_invoices_df = pd.DataFrame(iss_invoices, columns=["date", "amount"])
#
# employees_df.to_csv("data/employees.csv", index=False)
# rec_invoices_df.to_csv("data/rec_invoices.csv", index=False)
# iss_invoices_df.to_csv("data/iss_invoices.csv", index=False)


def get_budget_from_invoices(year: int, invoices: pd.DataFrame) -> pd.DataFrame:
    invoices = invoices[pd.DatetimeIndex(invoices["date"]).year == year]
    amount = invoices.groupby(by=pd.DatetimeIndex(invoices["date"]).month).sum().reset_index()
    return amount


def get_employee_salaries(employees: pd.DataFrame) -> int:
    salaries = employees["salary"].sum()
    return salaries


def get_budget(employees_csv: str, rec_invoices_csv: str, iss_invoices_csv: str, year: int = 2022):
    rec_invoices = pd.read_csv(rec_invoices_csv)
    iss_invoices = pd.read_csv(iss_invoices_csv)
    employees = pd.read_csv(employees_csv)
    rec_invoices_sum = get_budget_from_invoices(year, rec_invoices)
    iss_invoices_sum = get_budget_from_invoices(year, iss_invoices)
    for i in range(1, 13):
        sum = rec_invoices_sum[rec_invoices_sum['date'] == i]['amount'].sum() - iss_invoices_sum[iss_invoices_sum['date'] == i]['amount'].sum() - employees["salary"].sum()
        print(f"Budget for {i} month: {sum}")

get_budget("data/employees.csv", "data/rec_invoices.csv", "data/iss_invoices.csv", 2022)

