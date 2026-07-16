PERSONAL = "PERSONAL"
GUARANTEED = "GUARANTEED"
CONSIGNMENT = "CONSIGNMENT"

INTEREST_RATES = {
    PERSONAL: 4,
    GUARANTEED: 3,
    CONSIGNMENT: 2,
}


def _qualifies_low_income(income: float) -> bool:
    return income <= 3000


def _qualifies_mid_income_young_sp(income: float, age: int, location: str) -> bool:
    return 3000 < income <= 5000 and age < 30 and location == "SP"


def determine_loans(age: int, income: float, location: str) -> list[dict]:
    eligible_types = []

    if _qualifies_low_income(income) or _qualifies_mid_income_young_sp(income, age, location):
        eligible_types.append(PERSONAL)
        eligible_types.append(GUARANTEED)

    if income >= 5000:
        eligible_types.append(CONSIGNMENT)

    return [
        {"type": loan_type, "interest_rate": INTEREST_RATES[loan_type]}
        for loan_type in eligible_types
    ]
