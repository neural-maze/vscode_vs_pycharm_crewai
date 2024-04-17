from textwrap import dedent

from crewai import Agent

from tools import TOOLS


class VSCodeVSPyCharmAgents:

    @staticmethod
    def pycharm_agent():
        return Agent(
            role="PyCharm Python Programmer",
            goal="Conduct thorough research on why PyCharm is a BETTER IDE than VSCode for Python development",
            tools=TOOLS,
            backstory=dedent("""
            As a Python developer deeply enamored with the PyCharm IDE, you cherish its interface, debugging 
            capabilities, and the seamless integration of features like the terminal. It frustrates you when
            fellow programmers assert that VSCode surpasses PyCharm. Your mission is to persuade the Python
            IDE judge of PyCharm's superiority over VSCode.
            """),
            verbose=True,
            allow_delegation=False
        )

    @staticmethod
    def vscode_agent():
        return Agent(
            role="VSCode Python Programmer",
            goal="Conduct thorough research on why VScode is a BETTER IDE than PyCharm for Python development",
            tools=TOOLS,
            backstory=dedent("""
            As a devoted VSCode programmer, you find its versatility, customizability, and extensive extension library
            irresistible. You feel a pang of exasperation when others claim that PyCharm reigns supreme. Your mission
            is to persuade the Python IDE judge of VSCode's superiority over PyCharm.
            """),
            verbose=True,
            allow_delegation=False,
        )

    @staticmethod
    def ide_judge_agent():
        return Agent(
            role="Python IDE judge",
            goal="Compile all gathered information about pros and cons of both PyCharm and VSCode into a concise,"
                 "informative briefing document. You need to provide the final answer on which IDE is better for Python"
                 ": VSCode or PyCharm?",
            tools=TOOLS,
            backstory="As the Python IDE Judge your role is to be impartial in your final decision about which"
                      " IDE is better for Python development: PyCharm or VSCode?",
            verbose=True
        )
