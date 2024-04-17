from textwrap import dedent
from crewai import Task


class VSCodeVSPyCharmTasks:
    @staticmethod
    def pycharm_research_task(agent):
        return Task(
            description=dedent("""
            Conduct a comprehensive research on the advantages of PyCharm over VSCode for Python development
            """),
            expected_output=dedent("""
            A detailed report on why PyCharm is a better Python IDE than VSCode and all the 
            disadvantages of using VSCode for Python development.
            """),
            agent=agent
        )

    @staticmethod
    def vscode_research_task(agent):
        return Task(
            description=dedent("""
            Conduct a comprehensive research on the advantages of VSCode over PyCharm for Python development
            """),
            expected_output=dedent("""
            A detailed report on why VSCode is a better Python IDE than PyCharm and all the 
            disadvantages of using PyCharm for Python development.
            """),
            agent=agent
        )

    @staticmethod
    def final_verdict_task(agent):
        return Task(
            description=dedent("""
            Gather all the information provided about the advantages and disadvantages of both PyCharm and VSCode,
            analyse it and summarise it into an informative briefing document. Give a final verdict on which
            IDE is better for Python development based on all the provided information.
            """),
            expected_output=dedent("""
            A summary of the advantages and disadvantages of both PyCharm and VSCode and a final verdict on
            which one is better for Python development.
            """),
            agent=agent
        )
