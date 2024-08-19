from crewai import Task
from textwrap import dedent

class TranslationTasks:

    def translation_task(self, agent, source_text, target_language):
        return Task(
            description=dedent(f"""
                Translate the following text from its original language to {target_language}.
                Ensure that the translation is accurate, contextually appropriate,
                and maintains the original meaning and tone.

                Source Text:
                {source_text}

                The final translation must be a high-quality version of the original text,
                adapted to {target_language} with all nuances preserved.
            """),
            agent=agent,
            expected_output="High-quality translation of the source text"
        )

    def evaluation_task(self, agent, source_text, target_language):
        return Task(
            description=dedent(f"""
                Evaluate the provided translation of the text from its original language to {target_language}.
                Assess the translation for accuracy, fluency, and fidelity to the source text.

                Source Text:
                {source_text}

                The evaluation must include a numeric quality score from 0 to 100 called ADAPT_METRIC (ADM),
                where more than 80 is a good translation that requires no additional edits.
                If the evaluation result is not satisfactory, call the translation agent to redo the translation.
            """),
            agent=agent,
            context=[self.translation_task(agent, source_text, target_language)],
            expected_output="Evaluation result with a quality metric you have created called ADAPT_METRIC (ADM)"
        )

    def retranslation_task_if_needed(self, agent, source_text, target_language):
        return Task(
            description=dedent(f"""
                Based on the evaluation, if ADAPT_METRIC (ADM) is less than 80, then the translation is unsatisfactory
                and needs to be redone. If it's above 80, no further action is required.
                If necessary, please redo the translation of the following text from its original language to {target_language}.

                Source Text:
                {source_text}

                Ensure the new translation is accurate, contextually appropriate,
                and maintains the original meaning and tone.
            """),
            agent=agent,
            context=[
                self.translation_task(agent, source_text, target_language),
                self.evaluation_task(agent, source_text, target_language)
            ],
            expected_output="Only the revised translation."
        )
