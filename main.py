from dotenv import load_dotenv
from langchain.agents import create_agent

from tools import calculator, check_placement_eligibility

load_dotenv()

agent = create_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[
        calculator,
        check_placement_eligibility,
    ],
    system_prompt="""
    You are a helpful AI student and placement assistant.

    Use the calculator tool whenever a mathematical calculation is required.

    Use the placement eligibility tool whenever the user
    asks whether their academic scores satisfy the placement criteria.

    Explain the result clearly to the user.
    """
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": """
                I scored 72% in 10th, 68% in 12th,
                and have a CGPA of 7.8.
                Am I eligible for the placement?
                """
            }
        ]
    }
)

print(result["messages"][-1].content)