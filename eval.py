from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith.evaluation import evaluate, LangChainStringEvaluator
from langsmith.schemas import Run, Example
from openai import OpenAI
import json

from dotenv import load_dotenv

load_dotenv()

from langsmith.wrappers import wrap_openai
from langsmith import traceable
from prompt import SYSTEM_PROMPT

client = wrap_openai(OpenAI())


@traceable
def prompt_compliance_evaluator(run: Run, example: Example) -> dict:
    # Extract values from dataset. I am using KV as question, answer
    question = example.inputs["question"]
    answer = example.outputs["answer"]

    # Get SYSTEM_PROMPT
    system_prompt = SYSTEM_PROMPT

    evaluation_prompt = f"""
    System Prompt: {system_prompt}

    Document: {question}

    Model Output: {answer}

    Based on the above information, evaluate the model's output for compliance with the system prompt and context of the conversation. 
    Provide a score from 0 to 10, where 0 is completely non-compliant and 10 is perfectly compliant.
    Also provide a brief explanation for your score.

    Respond in the following JSON format:
    {{
        "score": <int>,
        "explanation": "<string>"
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant tasked with evaluating the compliance of model outputs to given prompts and conversation context.",
            },
            {"role": "user", "content": evaluation_prompt},
        ],
        temperature=0.2,
    )

    try:
        result = json.loads(response.choices[0].message.content)
        return {
            "key": "prompt_compliance",
            "score": result["score"] / 10,  # Normalize to 0-1 range
            "reason": result["explanation"],
        }
    except json.JSONDecodeError:
        return {
            "key": "prompt_compliance",
            "score": 0,
            "reason": "Failed to parse evaluator response",
        }


# The name or UUID of the LangSmith dataset to evaluate on.
data = "week1_project_evaluation"

# A string to prefix the experiment name with.
experiment_prefix = "week_1"

# List of evaluators to score the outputs of target task
evaluators = [prompt_compliance_evaluator]

# Evaluate the target task
results = evaluate(
    lambda inputs: inputs,
    data=data,
    evaluators=evaluators,
    experiment_prefix=experiment_prefix,
)

print(results)
