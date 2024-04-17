from crewai import Crew

from tasks import VSCodeVSPyCharmTasks
from agents import VSCodeVSPyCharmAgents

tasks = VSCodeVSPyCharmTasks()
agents = VSCodeVSPyCharmAgents()

pycharm_agent = agents.pycharm_agent()
vscode_agent = agents.vscode_agent()
ide_judge_agent = agents.ide_judge_agent()

pycharm_research_task = tasks.pycharm_research_task(pycharm_agent)
vscode_research_task = tasks.vscode_research_task(vscode_agent)
final_verdict_task = tasks.final_verdict_task(ide_judge_agent)

final_verdict_task.context = [pycharm_research_task, vscode_research_task]

crew = Crew(
    agents=[
        pycharm_agent,
        vscode_agent,
        ide_judge_agent
    ],
    tasks=[
        pycharm_research_task,
        vscode_research_task,
        final_verdict_task
    ]
)

result = crew.kickoff()


print("Here is the result: ")
print(result)
