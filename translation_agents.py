from crewai import Agent
from langchain_community.llms import OpenAI

class TranslationAgents():
    def translator_agent(self):
        return Agent(
            role='Translator Expert',
            goal='Provide accurate and contextually appropriate translations',
            backstory=
            'An expert in multiple languages and proficient in translating complex texts',
            verbose=True)

    def evaluator_agent(self):
        return Agent(
            role='Translation Evaluator',
            goal='Evaluate and ensure the quality of translations',
            backstory="""A professional with extensive experience in assessing
            translation accuracy, fluency, and fidelity to the source text""",
            verbose=True)

    def reviewer_agent(self):
        return Agent(
            role='Translation Reviewer',
            goal='Review and provide feedback on translations',
            backstory="""A language expert with a keen eye for detail and a passion for improving translation quality""",
            verbose=True)
