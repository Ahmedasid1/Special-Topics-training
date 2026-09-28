# Special Topics Training

A Python environment for hands-on training in modern data science and large language model workflows. The included dependencies support exploratory notebooks, Hugging Face models and datasets, embeddings, fine-tuning, retrieval-augmented generation (RAG), and Modal-based cloud execution.

## Topics

- Data science with NumPy, pandas, matplotlib, and scikit-learn
- Interactive notebook development with Jupyter and IPython kernels
- Model and dataset workflows with PyTorch and Hugging Face
- Sentence embeddings with Sentence Transformers
- Parameter-efficient fine-tuning with PEFT and TRL
- RAG applications with LangChain, ChromaDB, and PDF ingestion
- Cloud execution with Modal

## Setup

Prerequisites: Python 3.10 or later and `pip`.

```powershell
git clone https://github.com/Ahmedasid1/Special-Topics-training.git
Set-Location "Special-Topics-training"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On macOS or Linux, activate the virtual environment with:

```bash
source .venv/bin/activate
```

## Use Jupyter

After activating the environment, launch Jupyter Lab:

```powershell
jupyter lab
```

When creating a notebook, select the Python kernel associated with this project's `.venv` environment.

## Dependencies

The full dependency list is maintained in [requirements.txt](requirements.txt). Install or update the environment whenever that file changes:

```powershell
python -m pip install -r requirements.txt
```

## Optional Services

Some workflows require their own authentication before use:

- Hugging Face: authenticate with `huggingface-cli login` when accessing gated models or publishing assets.
- Modal: authenticate with `modal setup` before running cloud functions.

## Prompt Engineering Experiment

Use the same model and user question for all three runs. Change only the system prompt so the comparison is fair.

**Test question:** Explain REST APIs. Explain recursion. What is dependency injection? Show me an example.

**A — Minimal system prompt:**

```text
You are a programming assistant.

```

**B — Detailed system prompt:**

```text
You are DevMentor helping beginner programmers.
Explain concepts clearly with examples.

```

**C — Constrained system prompt:**

```text
You are DevMentor.
Explain before code.
Keep answers concise.
Use beginner-friendly examples.
Mention uncertainty when unsure.

```

### Reflection

1. **Which prompt was most useful, and why?** B was the most beginner-friendly: the restaurant analogy for REST APIs and nesting-doll analogy for recursion make the ideas approachable. However, its dependency-injection example is inconsistent: the factory constructs `DatabaseConnector` with too few arguments, so the example would not run as shown.
2. **What differences did you see?** A gave formal definitions, a numbered explanation of recursion, and several HTTP examples, but expanded REST incorrectly as “Representational State of Resource.” B used more analogies and a warmer, step-by-step tone. C was more concise in its REST section, but still gave a long dependency-injection explanation and repeated the inconsistent example. All three covered the same topics and included code examples.
3. **Did more instructions always help?** No. Beginner-focused instructions led to useful analogies, but the responses still contained a faulty dependency-injection example. The request to mention uncertainty in C produced an irrelevant question (“Are you sure you understand recursion?”) rather than a useful statement of uncertainty.
4. **Which rules changed behaviour the most?** The beginner-friendly instruction changed the explanations most by adding the restaurant and nesting-doll analogies. “Keep answers concise” shortened parts of C, especially its REST section, but did not keep the whole response concise. The uncertainty instruction also changed the answer, though not helpfully.

### Conclusion

With the same multi-part question, changing the system prompt changed the tone and presentation: A was more formal, B used beginner-friendly analogies, and C attempted a concise style but remained lengthy and added an unhelpful uncertainty question. B was the most approachable, but the responses also contained factual and code-example problems. The experiment shows that prompt instructions can guide style and emphasis, but do not guarantee correctness or concision; definitions and examples still need to be checked.

### MEMORY INVESTIGATION
After running the scripted chats the model was able to remember the information about my favourite language. Below is the response: 

>>> My favorite programming langauge is python. 
Python is an excellent choice for a programming language. 
It's known for its simplicity, readability, and 
versatility. Here are some reasons why Python is a popular 
choice among programmers:

1. **Easy to learn**: Python has a simple syntax and is 
relatively easy to learn, making it a great language for 
beginners.
2. **Versatile**: Python can be used for a wide range of 
applications, including web development, data analysis, 
machine learning, and more.
3. **Large community**: Python has a massive and active 
community, which means there are many resources available 
for learning and troubleshooting.
4. **Cross-platform**: Python can run on multiple 
operating systems, including Windows, macOS, and Linux.
5. **Extensive libraries**: Python has a vast collection 
of libraries and frameworks that make it easy to perform 
various tasks, such as data analysis, web development, and 
more.

Some popular uses of Python include:

1. **Data analysis**: Python is widely used for data 
analysis, machine learning, and data visualization.
2. **Web development**: Python is used in web development 
frameworks such as Django and Flask.
3. **Automation**: Python is often used for automating 
tasks, such as data scraping, file management, and more.
4. **Scientific computing**: Python is used in scientific 
computing for tasks such as numerical analysis, signal 
processing, and more.

What do you like most about Python? Is there a specific 
area where you'd like to learn more?

>>> Explain interfaces.
**Interfaces**

In programming, an interface is a contract between a 
client and a server that specifies the methods and data 
that can be used to interact with the server.

Think of an interface as a blueprint or a set of 
instructions that says what can be done with a particular 
service or system.

**Example:**

Let's say we have a bank account interface that allows us 
to perform the following actions:

1. Deposit money
2. Withdraw money
3. Check balance

The interface would specify the methods and data that can 
be used to interact with the account, such as:

* `deposit(amount)`: deposit a certain amount of money 
into the account
* `withdraw(amount)`: withdraw a certain amount of money 
from the account
* `get_balance()`: retrieve the current balance of the 
account

**Key aspects of interfaces:**

1. **Abstraction**: Interfaces abstract away the 
implementation details of a system or service, allowing 
clients to interact with it without knowing the underlying 
details.
2. **Contract**: Interfaces define a contract between the 
client and the server, specifying the methods and data 
that can be used to interact with the server.
3. **Standardization**: Interfaces provide a standard way 
for clients to interact with a server or system, making it 
easier to develop and maintain applications.

**Types of interfaces:**

1. **Abstract interface**: An abstract interface is a 
class that cannot be instantiated and provides a set of 
abstract methods that must be implemented by any class 
that inherits from it.
2. **Concrete interface**: A concrete interface is a class 
that implements a set of methods and provides a specific 
implementation for those methods.

**Importance of interfaces:**

1. **Flexibility**: Interfaces allow clients to switch 
between different implementations of a service or system 
without changing the client code.
2. **Reusability**: Interfaces enable the reusability of 
code by providing a standard way for clients to interact 
with a server or system.
3. **Maintainability**: Interfaces make it easier to 
maintain applications by providing a clear and 
standardized way of interacting with a server or system.

I hope this explanation helps! Do you have any specific 
questions about interfaces or would you like me to 
elaborate on any of the points I mentioned?

>>> what is my favorite programming language?
Your favorite programming language is Python