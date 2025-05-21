# 🧠 OpenAI Agents SDK 

This README explains core concepts of the OpenAI Agents SDK based on a learning task. It is written in a student-friendly format to help understand how the SDK is structured and why certain design decisions were made.

---

## 📌 What is this SDK?

The OpenAI Agents SDK allows developers to build AI-powered agents that can reason, use tools, and interact with users. It provides helpful abstractions like `Agent`, `Runner`, and context handling to simplify development.

---

## 📚 Questions & Answers

### **1. Why is the `Agent` class defined as a `dataclass`?**

- `@dataclass` automatically creates constructor and utility methods.
- It simplifies code since `Agent` mostly stores configuration and instructions.
- It improves readability and makes it easier to create agent objects.

### **2a. What are `instructions` in the `Agent` class? Why can they be a callable?**

- `instructions` is the **system prompt** used to define how the agent behaves.
- It can be a **string** (static prompt) or a **callable** (dynamic prompt).
- A callable lets you generate prompts based on the current context or input, making agents smarter.

### **2b. Why is the user prompt passed to `Runner.run()`? Why is it a classmethod?**

- The user prompt is what the agent needs to respond to — so it's passed when we **run** the agent.
- `run()` is a `@classmethod` because:
  - It doesn't need an instance of `Runner`.
  - It helps manage the whole lifecycle of an agent task from a class level.
  - It's responsible for executing the agent based on instructions, tools, and context.

---

### **3. What is the purpose of the `Runner` class?**

- `Runner` manages the **execution** of agent tasks.
- It:
  - Accepts the user prompt,
  - Loads tools and context,
  - Calls the agent,
  - Returns the final response.

Think of it like:
- `Agent` = definition and behavior setup
- `Runner` = execution engine that processes input and produces output

---

### **4. What are Generics in Python? Why use them for `TContext`?**

- **Generics** let you write flexible code that works with any type.
- `TContext` is a **TypeVar**, which makes context handling **type-safe and customizable**.
- Each agent can define its own context structure while still getting type hints and autocompletion.

---


## 🧪 Example Structure

```python
from openai import Agent, Runner

def dynamic_prompt(ctx):
    return f"You are assisting with task: {ctx['task_name']}"

agent = Agent(
    name="HelperAgent",
    instructions=dynamic_prompt,
    tools=[],
)

response = Runner.run(agent, input="How do I write a README?", context={"task_name": "Writing Docs"})
print(response.output)
