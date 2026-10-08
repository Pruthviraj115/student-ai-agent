from langchain.tools import tool




@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception:
        return "Unable to calculate the expression."


@tool
def check_placement_eligibility(
    tenth_percentage: float,
    twelfth_percentage: float,
    cgpa: float,
) -> str:
    """
    Check whether a student meets basic placement eligibility criteria.

    Criteria:
    - 10th percentage >= 70
    - 12th percentage >= 65
    - CGPA >= 7.5
    """

    requirements = {
        "10th": tenth_percentage >= 70,
        "12th": twelfth_percentage >= 65,
        "CGPA": cgpa >= 7.5,
    }

    if all(requirements.values()):
        return (
            "Eligible. The student meets all three criteria: "
            "10th >= 70%, 12th >= 65%, and CGPA >= 7.5."
        )

    failed = [
        requirement
        for requirement, passed in requirements.items()
        if not passed
    ]

    return (
        f"Not eligible. The student does not meet: {', '.join(failed)}."
    )