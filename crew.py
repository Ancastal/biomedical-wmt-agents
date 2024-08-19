from crewai import Crew

from translation_agents import TranslationAgents
from translation_tasks import TranslationTasks

class TranslationCrew:

  def __init__(self, source_text, target_language):
    self.source_text = source_text
    self.target_language = target_language

  def run(self):
    agents = TranslationAgents()
    tasks = TranslationTasks()

    translator_agent = agents.translator_agent()
    evaluator_agent = agents.evaluator_agent()
    reviewer_agent = agents.reviewer_agent()


    translation_task = tasks.translation_task(
        translator_agent,
        self.source_text,
        self.target_language
        )

    evaluation_task = tasks.evaluation_task(
      evaluator_agent,
      self.source_text,
      self.target_language
    )

    with open('evaluation_task_result.txt', 'w') as f:
        f.write(str(evaluation_task))
        f.write(evaluation_task.description)
        f.write('\n')
        f.write(evaluation_task.expected_output)
        f.write('\n')

    retranslation_task = tasks.retranslation_task_if_needed(
      reviewer_agent,
      self.source_text,
      self.target_language
    )

    crew = Crew(
      agents=[translator_agent, evaluator_agent],
      tasks=[translation_task, evaluation_task, retranslation_task],
      verbose=True
    )

    result = crew.kickoff()
    return result
