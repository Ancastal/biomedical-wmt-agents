from textwrap import dedent
from crew import TranslationCrew
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
  print('--------------------------------------------')
  print("Welcome to Translation and Evaluation Crew")
  print('--------------------------------------------')

  source_text = input(
    dedent("""
      Please enter the text you need to translate:
    """))

  target_language = input(
    dedent("""
      What is the target language for the translation?
    """))
  print()

  translation_crew = TranslationCrew(source_text, target_language)
  result = translation_crew.run()
  print("\n\n--------------------------------------------")
  print(" Here is your Translation and Evaluation Result")
  print("--------------------------------------------")
  print(result)
