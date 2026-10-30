# -*- coding: utf-8 -*-
"""
Generate 300 DBATU Questions for Semester III (60 questions for each of the 5 subjects)
Subjects:
  1. Artificial Intelligence (25AFAIPC304) - 60 Qs (15 per unit x 4 units)
  2. Prompt Engineering (25AFAIPC307) - 60 Qs (15 per unit x 4 units)
  3. Data Structures (25AF1245PC302) - 60 Qs (12 per unit x 5 units)
  4. Discrete Mathematics (25AF1245PC303) - 60 Qs (12 per unit x 5 units)
  5. Engineering Mathematics-III (25AF1000BS301) - 60 Qs (12 per unit x 5 units)
"""

def get_ai_questions():
    questions = []
    sub = "Artificial Intelligence"
    branch = "Artificial Intelligence & Data Science"
    year = "Second Year"
    sem = "Semester III"

    u1 = "Unit 1: Introduction to AI and Intelligent Agents"
    t1 = "AI Foundations & Intelligent Agents"
    ai_u1 = [
        (t1, "What benchmark test was proposed by Alan Turing in 1950 to evaluate whether a machine can exhibit human-equivalent intelligence?",
         "Turing Test (Imitation Game)", "Voight-Kampff Test", "Lovelace Test", "Chinese Room Test", "A", "Easy"),
        (t1, "What defines a 'Rational Agent' in modern artificial intelligence (Russell & Norvig)?",
         "An agent that always selects an action expected to maximize its performance measure given its percept history and built-in knowledge",
         "An agent with human feelings and empathy", "An agent that never makes computational errors", "An agent that executes in O(1) time", "A", "Easy"),
        (t1, "What does the acronym PEAS stand for in specifying task environments for intelligent agents?",
         "Performance measure, Environment, Actuators, Sensors", "Program, Execution, Architecture, Storage",
         "Process, Entity, Attribute, Schema", "Perception, Evaluation, Action, State", "A", "Easy"),
        (t1, "An environment where an agent's sensors give complete and accurate access to the entire state of the world at each point is classified as:",
         "Fully Observable", "Partially Observable", "Continuous", "Stochastic", "A", "Easy"),
        (t1, "A chess game with an opponent is classified under which task environment taxonomy?",
         "Fully observable, deterministic (strategic), discrete, multi-agent (competitive)",
         "Partially observable, stochastic, continuous, single-agent",
         "Episodic, dynamic, unobservable, cooperative", "Continuous, chaotic, non-deterministic", "A", "Medium"),
        (t1, "An environment where the next state of the environment is completely determined by the current state and the agent's action is:",
         "Deterministic", "Stochastic", "Static", "Episodic", "A", "Easy"),
        (t1, "An environment that can change while the agent is deliberating or calculating its next action is classified as:",
         "Dynamic", "Static", "Semidynamic", "Discrete", "A", "Easy"),
        (t1, "What type of agent selects actions based solely on the current percept, ignoring the history of past percepts?",
         "Simple Reflex Agent", "Model-based Reflex Agent", "Goal-based Agent", "Utility-based Agent", "A", "Easy"),
        (t1, "What internal component does a Model-Based Reflex Agent maintain to handle partially observable environments?",
         "An internal state reflecting unobserved aspects of the current environment based on percept history",
         "A complete database of all world facts", "A random number generator", "A neural network with 100 layers", "A", "Medium"),
        (t1, "Which agent architecture explicitly evaluates different world states using a continuous real-valued trade-off happiness metric?",
         "Utility-Based Agent", "Simple Reflex Agent", "Table-Driven Agent", "Goal-Based Agent", "A", "Medium"),
        (t1, "In the Learning Agent framework, which component is responsible for suggesting exploratory actions leading to new experiences?",
         "Learning Element", "Performance Element", "Problem Generator", "Critic", "C", "Hard"),
        (t1, "In the Learning Agent framework, what does the 'Critic' evaluate?",
         "How well the agent is doing with respect to an external performance standard", "The speed of the CPU",
         "The syntax of input queries", "The memory bus bandwidth", "A", "Medium"),
        (t1, "What was the landmark 1956 workshop that officially coined the term 'Artificial Intelligence' and founded the field?",
         "Dartmouth Summer Research Project on Artificial Intelligence", "Turing Conference London",
         "MIT Cybernetics Symposium", "Stanford AI Workshop", "A", "Easy"),
        (t1, "What philosophical thought experiment formulated by John Searle (1980) challenged Strong AI and functional symbol manipulation?",
         "The Chinese Room Argument", "Ship of Theseus", "Brain in a Vat", "Maxwell's Demon", "A", "Medium"),
        (t1, "What historical periods in AI history were characterized by severe funding cutbacks and disillusionment following unmet promises?",
         "AI Winters", "AI Dark Ages", "Silicon Depressions", "Algorithmic Recessions", "A", "Easy")
    ]

    u2 = "Unit 2: Problem Solving by Searching and CSP"
    t2 = "Search Algorithms & Constraint Satisfaction"
    ai_u2 = [
        (t2, "Which data structure is utilized to maintain the frontier (fringe) nodes in Breadth-First Search (BFS)?",
         "Queue (First-In, First-Out)", "Stack (Last-In, First-Out)", "Priority Queue / Min-Heap", "Hash Table", "A", "Easy"),
        (t2, "What is the time complexity of Breadth-First Search on a tree with branching factor b and solution depth d?",
         "O(b^d)", "O(d^b)", "O(b * d)", "O(log d)", "A", "Medium"),
        (t2, "Which uninformed search algorithm is space-efficient like DFS (O(b*d) memory) yet complete and optimal like BFS?",
         "Iterative Deepening Depth-First Search (IDDFS)", "Depth-Limited Search with limit 1", "Uniform Cost Search", "Bidirectional Greedy Search", "A", "Medium"),
        (t2, "In Uniform-Cost Search (Dijkstra's algorithm), what node from the frontier is always expanded first?",
         "The node with the lowest path cost g(n) from the start node", "The node with the highest heuristic value h(n)",
         "The deepest node in the tree", "The node with the most child branches", "A", "Easy"),
        (t2, "In A* search with evaluation function f(n) = g(n) + h(n), what does an 'Admissible Heuristic' guarantee?",
         "h(n) never overestimates the true minimal cost to reach the goal node from n (i.e. h(n) <= h*(n))",
         "h(n) is strictly greater than the true cost", "h(n) is always 0", "h(n) is equal to g(n)", "A", "Easy"),
        (t2, "What property ensures that A* graph search is optimal without needing to reopen closed nodes (monotonicity)?",
         "Consistency (Triangle Inequality: h(n) <= c(n, a, n') + h(n'))", "Linear independence", "Commutativity", "Transitivity", "A", "Hard"),
        (t2, "What is the primary evaluation function f(n) minimized in Greedy Best-First Search?",
         "f(n) = h(n)", "f(n) = g(n)", "f(n) = g(n) + h(n)", "f(n) = g(n) - h(n)", "A", "Easy"),
        (t2, "In adversarial two-player zero-sum games (like Chess or Tic-Tac-Toe), what algorithm computes optimal moves?",
         "Minimax Algorithm", "Kruskal's Algorithm", "Apriori Algorithm", "Bellman-Ford Algorithm", "A", "Easy"),
        (t2, "What optimization technique prunes branches in the Minimax game tree without affecting the final evaluation decision?",
         "Alpha-Beta Pruning", "Decision Tree Pruning", "Laplace Smoothing", "Forward Checking", "A", "Easy"),
        (t2, "In Alpha-Beta pruning, what does the alpha parameter mathematically track?",
         "The highest-value choice (best lower bound) found so far along the path for the MAX player",
         "The lowest-value choice for MIN", "The total number of explored nodes", "The branching factor", "A", "Medium"),
        (t2, "What three components define a Constraint Satisfaction Problem (CSP)?",
         "Variables (X), Domains (D), and Constraints (C)", "Weights, Biases, and Activations",
         "Inputs, Hidden layers, and Outputs", "Premises, Inference rules, and Conclusions", "A", "Easy"),
        (t2, "Which heuristic in backtracking search for CSPs selects the variable with the fewest remaining legal values in its domain?",
         "Minimum Remaining Values (MRV) / Most Constrained Variable Heuristic",
         "Degree Heuristic", "Least Constraining Value Heuristic", "Forward Pruning", "A", "Medium"),
        (t2, "Which CSP heuristic chooses the value that leaves the maximum number of choices open for neighboring variables?",
         "Least Constraining Value (LCV) Heuristic", "MRV Heuristic", "Max-Min Heuristic", "Alpha-Beta Heuristic", "A", "Medium"),
        (t2, "What constraint propagation algorithm enforces Arc Consistency across all directed pairs of variables (X_i, X_j) in a CSP?",
         "AC-3 Algorithm", "Dijkstra Algorithm", "K-Means Algorithm", "Viterbi Algorithm", "A", "Hard"),
        (t2, "What classic 8-puzzle and 8-queens problems represent benchmark domains for testing?",
         "State space search and Constraint Satisfaction Problem algorithms",
         "Text-to-speech synthesis", "Hardware bus protocol arbitration", "Relational database indexing", "A", "Easy")
    ]

    u3 = "Unit 3: Knowledge Representation and Reasoning"
    t3 = "Logic & First-Order Inference"
    ai_u3 = [
        (t3, "What inference rule of propositional logic states that if 'P' is true and 'P -> Q' is true, then 'Q' can be inferred?",
         "Modus Ponens", "Modus Tollens", "Resolution Rule", "Hypothetical Syllogism", "A", "Easy"),
        (t3, "What inference rule states that given 'not Q' and 'P -> Q', one can validly deduce 'not P'?",
         "Modus Tollens", "Modus Ponens", "Disjunctive Syllogism", "Conjunction Introduction", "A", "Easy"),
        (t3, "Which logic representation overcomes propositional logic limitations by supporting objects, relations, and quantifiers (forall, exists)?",
         "First-Order Logic (FOL) / Predicate Calculus", "Propositional Logic", "Boolean Algebra", "Fuzzy Logic", "A", "Easy"),
        (t3, "What does the existential quantifier (exists x) express in First-Order Logic?",
         "There exists at least one object x in the domain satisfying the predicate", "The statement is true for every possible object x",
         "The predicate is always false", "Object x does not exist in memory", "A", "Easy"),
        (t3, "What does the universal quantifier (forall x) express in First-Order Logic?",
         "The predicate is true for every object x in the domain of discourse", "Only one specific object satisfies the predicate",
         "No objects satisfy the formula", "The truth value is unknown", "A", "Easy"),
        (t3, "What is Conjunctive Normal Form (CNF) required for automated theorem proving via resolution?",
         "A conjunction (AND) of one or more clauses, where each clause is a disjunction (OR) of literals",
         "A disjunction of conjunctions", "A formula with no negation operators", "A binary truth table", "A", "Medium"),
        (t3, "What algorithmic process in First-Order Logic resolution finds substitutions (theta) that make two logical expressions identical?",
         "Unification", "Skolemization", "Discretization", "Tokenization", "A", "Hard"),
        (t3, "What is 'Skolemization' in converting First-Order Logic formulas to clausal form?",
         "The elimination of existential quantifiers by replacing existentially quantified variables with Skolem constants or Skolem functions",
         "The removal of implication arrows", "Negation normal form conversion", "Truth table verification", "A", "Hard"),
        (t3, "How does automated Resolution Refutation prove that a knowledge base KB entails a query alpha (KB |= alpha)?",
         "By adding the negation of the query (not alpha) to KB and deriving a logical contradiction (the empty clause)",
         "By generating all 2^N truth assignments", "By running forward simulation", "By randomly checking 5 cases", "A", "Medium"),
        (t3, "What reasoning strategy begins with known facts in working memory and fires production rules whose IF-conditions are satisfied?",
         "Forward Chaining (Data-driven reasoning)", "Backward Chaining (Goal-driven reasoning)", "Bidirectional A*", "Adversarial Minimax", "A", "Easy"),
        (t3, "What reasoning strategy begins with a goal hypothesis and works backward to see if supporting premises are present in memory?",
         "Backward Chaining (Goal-driven reasoning)", "Forward Chaining", "Breadth-First Generation", "Greedy Search", "A", "Easy"),
        (t3, "Which logic programming language uses backward chaining over definite Horn clauses and unification for AI problem solving?",
         "Prolog", "C++", "JavaScript", "HTML", "A", "Easy"),
        (t3, "What is a 'Horn Clause' in computational logic?",
         "A logical clause containing at most one positive (unnegated) literal", "A formula with infinite variables",
         "A clause with no variables", "A contradiction", "A", "Medium"),
        (t3, "What is 'Ontology' in artificial intelligence knowledge engineering?",
         "A formal, explicit specification of a shared conceptualization (entities, categories, properties, and relationships in a domain)",
         "The study of CPU architectures", "A network routing protocol", "A data encryption cipher", "A", "Medium"),
        (t3, "What knowledge representation structure represents concepts as nodes interconnected by labeled relational edges (such as 'is-a', 'part-of')?",
         "Semantic Network", "Decision Table", "Truth Table", "Bytecode Array", "A", "Easy")
    ]

    u4 = "Unit 4: Probabilistic Reasoning and Planning"
    t4 = "Bayesian Networks & AI Planning"
    ai_u4 = [
        (t4, "What graphical model represents a joint probability distribution over a set of random variables using a Directed Acyclic Graph (DAG)?",
         "Bayesian Network (Belief Network)", "Markov Decision Process", "Finite State Machine", "Dendrogram", "A", "Easy"),
        (t4, "In a Bayesian Network, what conditional independence property holds for each node X_i?",
         "Each node is conditionally independent of its non-descendants given its parents: P(X_1...X_n) = prod P(X_i | Parents(X_i))",
         "Every variable is independent of all other variables unconditionally", "Variables must be linearly correlated",
         "Parents are independent of their children", "A", "Hard"),
        (t4, "What is a Conditional Probability Table (CPT) in a discrete Bayesian Network?",
         "A table specifying the conditional probability distribution of a node for each possible combination of values of its parent nodes",
         "A lookup table for mathematical square roots", "A table of encryption keys", "A routing table for internet gateways", "A", "Medium"),
        (t4, "What graph property determines whether variable X is conditionally independent of Y given evidence Z in a Bayesian Network?",
         "d-Separation (Directional Separation)", "Eulerian Path existence", "Hamiltonian Cycle", "Max-Flow Min-Cut", "A", "Hard"),
        (t4, "Which exact inference algorithm computes marginal probabilities in tree-structured Bayesian Networks?",
         "Variable Elimination (or Belief Propagation)", "Gradient Descent", "QuickSort", "Backtracking search", "A", "Medium"),
        (t4, "Which mathematical theory generalizes Bayesian probability by using belief and plausibility functions to represent epistemic uncertainty?",
         "Dempster-Shafer Theory of Evidence", "Fuzzy Set Theory", "Linear Programming", "Calculus of Variations", "A", "Medium"),
        (t4, "In Lotfi Zadeh's Fuzzy Set Theory, how is the membership of an element in a fuzzy set characterized?",
         "By a continuous membership degree value between 0.0 and 1.0 (indicating degree of truth)",
         "By a strict binary 0 or 1 indicator only", "By complex imaginary numbers", "By an integer from 1 to 100", "A", "Easy"),
        (t4, "In classical AI planning, what standard domain definition language specifies actions via Preconditions and Effects?",
         "Planning Domain Definition Language (PDDL) / STRIPS", "HTML5", "SQL DDL", "YAML", "A", "Easy"),
        (t4, "In STRIPS planning representation, what are the two components of an Action's Effect?",
         "Add List (literals that become true) and Delete List (literals that become false)",
         "Input List and Output List", "Success List and Failure List", "Local List and Global List", "A", "Medium"),
        (t4, "What classical planning algorithm plans by attempting to satisfy sub-goals on a goal stack, backtracking when sub-goal interactions conflict?",
         "Goal Stack Planning", "A* Graph Search", "Breadth First Search", "Reinforcement Q-Learning", "A", "Medium"),
        (t4, "What planning approach decomposes high-level abstract tasks into progressively detailed sub-tasks until primitive actions are reached?",
         "Hierarchical Task Network (HTN) Planning", "Linear Regression", "Brute Force Enumeration", "Monte Carlo Tree Search", "A", "Medium"),
        (t4, "What is the 'Frame Problem' in classical artificial intelligence planning?",
         "The computational challenge of representing what remains UNCHANGED in the world state after an action is executed",
         "Fitting computer monitors into plastic frames", "Video frame dropping during transmission", "HTML iframe security flaws", "A", "Hard"),
        (t4, "What is a Markov Decision Process (MDP) characterized by in reinforcement learning and sequential decision problems?",
         "States (S), Actions (A), Transition Model P(s'|s, a), Reward Function R(s, a, s'), and Discount Factor gamma",
         "Nodes, Edges, Weights, and Biases", "Registers, ALU, Program Counter, and Accumulator", "Tables, Views, Triggers, and Indexes", "A", "Medium"),
        (t4, "What equation expresses the optimal state-value function V*(s) in dynamic programming and reinforcement learning?",
         "Bellman Optimality Equation", "Euler-Lagrange Equation", "Navier-Stokes Equation", "Schrodinger Wave Equation", "A", "Hard"),
        (t4, "What sampling-based approximate inference method generates sample states in Bayesian Networks proportional to likelihood weights?",
         "Likelihood Weighting (or Gibbs Sampling / MCMC)", "Exact Variable Elimination", "Resolution Refutation", "Breadth First Traversal", "A", "Medium")
    ]

    for q in ai_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ai_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ai_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ai_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_prompt_eng_questions():
    questions = []
    sub = "Prompt Engineering"
    branch = "Artificial Intelligence & Data Science"
    year = "Second Year"
    sem = "Semester III"

    u1 = "Unit 1: Introduction to Prompt Engineering & LLMs"
    t1 = "LLM Fundamentals & Tokenization"
    pe_u1 = [
        (t1, "What is 'Prompt Engineering' in generative artificial intelligence?",
         "The practice of designing, structuring, and optimizing natural language inputs (prompts) to guide Large Language Models toward accurate and desired outputs",
         "Writing compiler code in C++", "Manufacturing GPU chips", "Configuring network switches", "A", "Easy"),
        (t1, "What are 'Tokens' in Large Language Models (LLMs)?",
         "The basic atomic fragments (sub-words, words, or characters) into which text is decomposed by tokenizers (such as BPE or WordPiece)",
         "Cryptocurrency digital coins", "Database primary keys", "HTML tags", "A", "Easy"),
        (t1, "On average across English text, roughly how many words does 1,000 tokens represent in OpenAI GPT models?",
         "Approximately 750 words", "Exactly 1,000 words", "10,000 words", "50 words", "A", "Easy"),
        (t1, "What is the 'Context Window' of a Large Language Model?",
         "The maximum total number of tokens (prompt + generated completion) the model can process and attend to in a single forward pass",
         "The physical dimensions of the monitor window", "The operating system RAM limit", "The browser tab size", "A", "Easy"),
        (t1, "What is the primary difference between 'Prompt Engineering' and 'Fine-Tuning'?",
         "Prompt engineering adapts model behavior via in-context instructions without updating model weights; fine-tuning updates neural weights via gradient descent on training datasets",
         "Prompt engineering requires 100 GPUs", "Fine-tuning does not change weights", "There is no difference", "A", "Medium"),
        (t1, "Which parameter controls the randomness and creativity of an LLM's token generation?",
         "Temperature (where 0.0 is deterministic and 1.0+ is highly creative/random)", "Batch Size", "Learning Rate", "Weight Decay", "A", "Easy"),
        (t1, "What does the 'Top-P' (Nucleus Sampling) parameter do during LLM decoding?",
         "It dynamically samples only from the smallest set of tokens whose cumulative probability exceeds the threshold p",
         "It picks the top-P layers of the neural network", "It limits output to P paragraphs", "It stops generation after P seconds", "A", "Medium"),
        (t1, "In the Chat Completion API format, what role is typically assigned to define the model's persona, operational rules, and behavioral guardrails?",
         "System role ('system')", "User role ('user')", "Assistant role ('assistant')", "Function role ('tool')", "A", "Easy"),
        (t1, "What role represents the historical model responses generated in a conversational session?",
         "Assistant role ('assistant')", "System role", "Admin role", "Root role", "A", "Easy"),
        (t1, "Which of the following is an open-weights foundation LLM released by Mistral AI?",
         "Mistral 7B / Mixtral 8x7B", "GPT-4", "Claude 3.5 Sonnet", "Google Gemini Pro", "A", "Easy"),
        (t1, "What architectural transformer innovation enabled LLMs to process distant token relationships in parallel?",
         "Self-Attention Mechanism (Transformer Attention is All You Need)", "Recurrent Hidden Markov Gates", "Convolutional Max-Pooling", "FIFO Queue Stacks", "A", "Medium"),
        (t1, "What happens when input text exceeds the maximum context window of an LLM?",
         "The model truncates earlier tokens or rejects the API request with a context length exceeded error",
         "The model runs in half-speed mode", "The computer restarts", "The model switches to offline mode", "A", "Easy"),
        (t1, "What parameter in LLM generation sets a maximum boundary on the length of the returned response?",
         "max_tokens (max_completion_tokens)", "min_epochs", "temperature", "top_k", "A", "Easy"),
        (t1, "What is 'Frequency Penalty' in LLM generation parameters?",
         "A setting that discourages the model from repeating the exact same words based on their frequency in the generated text so far",
         "A penalty for slow network requests", "A CPU clock throttling setting", "A billing fee per API query", "A", "Medium"),
        (t1, "What is 'In-Context Learning' (ICL) in foundation language models?",
         "The ability of an LLM to adapt to new tasks during inference solely based on examples and instructions provided in the prompt, without updating weights",
         "Learning by compiling Python scripts", "Reading files from disk", "Running gradient backpropagation", "A", "Medium")
    ]

    u2 = "Unit 2: Foundations of Prompt Design & Advanced Prompting"
    t2 = "Prompt Patterns & Chain-of-Thought"
    pe_u2 = [
        (t2, "What is 'Zero-Shot Prompting'?",
         "Prompting an LLM to perform a task with instructions only, providing zero prior demonstration examples",
         "Prompting a model with zero tokens", "Prompting without an internet connection", "Using an un-trained model", "A", "Easy"),
        (t2, "What is 'Few-Shot Prompting' (In-Context Demonstration)?",
         "Providing a few high-quality input-output example pairs in the prompt before the target query to guide the model's reasoning format and style",
         "Prompting a model three times sequentially", "Fine-tuning a model on five rows of data", "Generating only three words", "A", "Easy"),
        (t2, "Why are Delimiters (such as triple backticks ``` or XML tags <context></context>) recommended in prompt design?",
         "They clearly demarcate sections of the prompt (instructions, context, query) preventing prompt injection and formatting confusion",
         "They speed up GPU floating point calculations", "They reduce API token costs to zero", "They are required by JSON parsers", "A", "Easy"),
        (t2, "What is 'Role Prompting' (Persona Adoption)?",
         "Instructing the model to adopt a specific professional persona (e.g., 'Act as an expert DBATU Computer Science Professor')",
         "Assigning Linux user permissions to the model", "Creating a login role in SQL", "Simulating an actor in video games", "A", "Easy"),
        (t2, "What landmark prompting technique formulated by Wei et al. (2022) dramatically improves LLM complex mathematical and logical reasoning?",
         "Chain-of-Thought (CoT) Prompting ('Let us think step by step')", "Random Guess Prompting", "Greedy Decoding", "One-Word Output Prompting", "A", "Easy"),
        (t2, "What is 'Zero-Shot Chain-of-Thought' popularized by Kojima et al. (2022)?",
         "Appending the simple phrase 'Let's think step by step' to prompt the model to generate intermediate reasoning steps before the final answer",
         "Training a new model from scratch", "Running 100 parallel prompts", "Using zero-shot classification in scikit-learn", "A", "Easy"),
        (t2, "What is 'Self-Consistency' prompting in advanced reasoning workflows?",
         "Sampling multiple diverse reasoning paths from an LLM and selecting the most consistent final answer via majority voting",
         "Checking if the prompt has no syntax errors", "Verifying database ACID properties", "Running prompt regression tests", "A", "Medium"),
        (t2, "What is the core premise of the 'ReAct' (Reason + Act) prompting framework (Yao et al., 2022)?",
         "Interleaving thought reasoning steps with external tool execution actions and environment observation feedback in a loop",
         "Compiling React.js frontend code with LLMs", "Reacting to network packet loss", "Disabling model hallucinations", "A", "Medium"),
        (t2, "What is 'Multimodal Prompting'?",
         "Providing prompts that combine multiple sensory modalities (such as images, diagrams, audio, and text) to vision-language models",
         "Using multiple monitors to type prompts", "Running prompts across multiple operating systems", "Using both mouse and keyboard", "A", "Easy"),
        (t2, "In Python, which popular open-source framework provides abstractions for prompt templates, chains, and LLM agent orchestration?",
         "LangChain (or LlamaIndex)", "NumPy", "Matplotlib", "Flask alone", "A", "Easy"),
        (t2, "In LangChain, what does a PromptTemplate provide?",
         "A reproducible, parameterized prompt string with named input variables that can be dynamically populated at runtime",
         "A graphical web editor", "A database connection pool", "An encryption cipher", "A", "Easy"),
        (t2, "How do you enforce structured JSON output reliably from modern OpenAI models?",
         "Setting response_format={'type': 'json_object'} (or Structured Outputs with Pydantic JSON schemas) and requesting JSON in the prompt",
         "Asking the model politely to write code", "Using regex on text output", "Renaming the API key", "A", "Medium"),
        (t2, "What is 'Step-Back Prompting' in advanced problem solving?",
         "Asking the model to first identify high-level principles or general concepts before answering a specific challenging instance",
         "Deleting the last character of a prompt", "Reverting to previous model versions", "Canceling an API request", "A", "Hard"),
        (t2, "What is 'Socratic Prompting'?",
         "Guiding the user or model through a sequence of probing questions that reveal underlying assumptions and contradictions rather than giving direct answers",
         "Translating text to ancient Greek", "Writing philosophical essays", "Compiling philosophical truth tables", "A", "Medium"),
        (t2, "What is the purpose of 'Few-Shot Chain-of-Thought' over standard Few-Shot?",
         "Providing worked-out step-by-step reasoning solutions inside the demonstration examples, not just the final answers",
         "Using fewer than 2 examples", "Speeding up network response times", "Reducing model memory footprint", "A", "Medium")
    ]

    u3 = "Unit 3: Prompt Engineering for Domain-Specific Tasks"
    t3 = "Domain-Specific Prompts & Code Generation"
    pe_u3 = [
        (t3, "How can you prompt an LLM to generate production-ready code with minimal bugs?",
         "Specify the programming language, framework version, input/output types, edge cases, error handling, and test requirements explicitly",
         "Type 'write code' with no details", "Ask the model to write code in one second", "Disable system instructions", "A", "Easy"),
        (t3, "What prompting pattern is most effective for automated code debugging?",
         "Provide the original code snippet, the exact error traceback/message, expected vs actual behavior, and request step-by-step root cause analysis",
         "Paste the entire repository without error logs", "Ask the model if it likes Python", "Send empty messages", "A", "Easy"),
        (t3, "In conversational dialogue design, what is 'Few-Shot Persona Inoculation'?",
         "Giving 2-3 sample conversational turns showing how the bot handles difficult, angry, or ambiguous user queries while maintaining character",
         "Vaccinating the computer against malware", "Installing antivirus on cloud servers", "Restarting the chat session", "A", "Medium"),
        (t3, "When prompting for medical or legal domain summaries, what essential guardrail should be embedded in the system prompt?",
         "A strict instruction to state that the output is for informational purposes only and not a substitute for certified medical or legal advice",
         "A guarantee that the LLM's diagnosis is 100% legally binding", "A requirement to invent clinical trials", "Instructions to prescribe medication", "A", "Easy"),
        (t3, "How do you prompt an LLM for robust data extraction from messy semi-structured text (e.g. invoices)?",
         "Define an exact JSON schema or Pydantic model with strict field types and instruct the model to return ONLY valid JSON matching the schema",
         "Ask for a free-form essay", "Tell the model to guess if missing", "Send the text as an image only", "A", "Easy"),
        (t3, "What is 'Prompt Chaining' in complex multi-step domain workflows?",
         "Decomposing a complex task into discrete sequential sub-tasks where the verified output of one prompt becomes the input context of the next",
         "Typing 50 questions in a single sentence", "Running prompts in an infinite loop", "Connecting two computers with a chain", "A", "Medium"),
        (t3, "What challenge arises when prompting Large Language Models in low-resource regional Indian languages (e.g. Marathi, Sanskrit)?",
         "Higher token fragmentation per word (sub-optimal tokenization) and lower training representation, often addressed by cross-lingual prompting or English instructions with vernacular context",
         "LLMs cannot process UTF-8 characters", "Regional scripts are illegal in AI", "Computers cannot display non-Latin fonts", "A", "Hard"),
        (t3, "What is 'Meta-Prompting'?",
         "Using an LLM to automatically generate, critique, and refine prompts for another LLM or downstream task",
         "Writing prompts about social media companies", "Creating meta tags for HTML websites", "Changing Facebook settings", "A", "Medium"),
        (t3, "In educational tutoring applications, how should a prompt be designed to prevent students from simply copying answers?",
         "Instruct the tutor model to act as a supportive mentor that provides hints and conceptual explanations rather than direct final answers",
         "Instruct the model to give the complete answer immediately", "Disable student chat", "Grade the student F automatically", "A", "Easy"),
        (t3, "What prompting strategy helps extract balanced pro/con arguments for controversial or multi-faceted policy questions?",
         "'Perspective Taking' / Multi-persona prompting instructing the model to synthesize arguments from distinct stakeholder perspectives",
         "Asking for only one extreme opinion", "Randomly flipping a coin", "Refusing to discuss the topic", "A", "Easy"),
        (t3, "How do you prompt an LLM to generate comprehensive Unit Tests for a Python function?",
         "Provide the function implementation and instruct the model to write pytest test cases covering happy paths, boundary values, null inputs, and exceptions",
         "Ask for a poem about testing", "Tell the model to run pytest on its own server", "Type 'test it'", "A", "Easy"),
        (t3, "What is 'Self-Refinement' (Iterative Critique) prompting?",
         "Prompting the model to generate a draft solution, critique its own draft against given criteria, and produce an improved final version",
         "A manual git commit command", "Training weights on a GPU", "A compiler optimization flag", "A", "Medium"),
        (t3, "What is 'Least-to-Most Prompting'?",
         "Decomposing a challenging problem into a series of simpler sequential sub-problems and solving them incrementally",
         "Sorting numbers in ascending order", "Minimizing token usage to 1 token", "Running the cheapest model first", "A", "Medium"),
        (t3, "How does 'Few-Shot Example Diversity' impact in-context classification performance?",
         "Diverse examples covering various classes, edge cases, and sentence lengths yield much higher accuracy than repetitive, uniform examples",
         "Diversity degrades performance", "All examples must have identical words", "Only 1 example should ever be used", "A", "Medium"),
        (t3, "What is 'Prompt Formatting Consistency'?",
         "Ensuring identical structural patterns (e.g., 'Input: ... Output: ...') across all demonstration examples so the model easily follows the pattern",
         "Changing fonts in Microsoft Word", "Using colorful terminal text", "Writing prompts in all uppercase", "A", "Easy")
    ]

    u4 = "Unit 4: Prompt Safety, Bias, and Ethics"
    t4 = "Prompt Safety, Evaluation & Guardrails"
    pe_u4 = [
        (t4, "What is an 'LLM Hallucination'?",
         "A confident, syntactically convincing response generated by an LLM that is factually false, ungrounded, or fabricated",
         "An optical illusion on computer screens", "A hardware glitch in GPU memory", "A slow network response", "A", "Easy"),
        (t4, "What is a 'Direct Prompt Injection' attack?",
         "An adversarial attack where a user crafts an input designed to override or ignore the developer's system instructions and guardrails",
         "Injecting SQL into a MySQL table", "A physical hardware short-circuit", "A virus transmitted via USB", "A", "Easy"),
        (t4, "What is an 'Indirect Prompt Injection' attack?",
         "When an LLM ingests external untrusted data (e.g. a poisoned webpage or email) that contains hidden instructions that hijack the model's behavior during RAG",
         "Hacking a Wi-Fi router", "Stealing physical server racks", "Corrupting CPU firmware", "A", "Medium"),
        (t4, "What is 'Jailbreaking' in LLM safety terminology?",
         "Using sophisticated roleplay, hypothetical scenarios, or encoded prompts (e.g. DAN prompts) to bypass safety alignment and generate restricted/harmful content",
         "Rooting an Android smartphone", "Unlocking an iPhone operating system", "Running Linux on a PlayStation", "A", "Easy"),
        (t4, "What is 'System Prompt Leakage'?",
         "A vulnerability where an adversarial user tricks an LLM into revealing its private, confidential system instructions and internal guidelines",
         "Coolant leaking from GPU radiators", "Memory leaks in C++ code", "A Wi-Fi password leak", "A", "Medium"),
        (t4, "Which metric commonly used in NLP evaluation measures n-gram overlap between machine-generated text and reference human translations?",
         "BLEU (Bilingual Evaluation Understudy) Score", "Silhouette Score", "F-statistic", "Gini Coefficient", "A", "Easy"),
        (t4, "Which evaluation metric evaluates text summarization by calculating n-gram recall against gold standard reference summaries?",
         "ROUGE (Recall-Oriented Understudy for Gisting Evaluation)", "BLEU", "Perplexity", "Accuracy", "A", "Easy"),
        (t4, "What semantic similarity evaluation metric uses contextual embeddings from pre-trained BERT to compute cosine similarity between candidate and reference texts?",
         "BERTScore", "Levenshtein Edit Distance", "Jaccard Index", "Euclidean Distance", "A", "Medium"),
        (t4, "What is 'LLM-as-a-Judge' in automated prompt evaluation pipelines?",
         "Using a capable foundation model (like GPT-4) with detailed rubrics to score and critique the outputs of other models on criteria like relevance and accuracy",
         "A court software for legal trials", "A compiler that checks syntax errors", "A unit test framework in C", "A", "Medium"),
        (t4, "What is 'Function Calling' (Tool Use) in modern LLM API architectures?",
         "The model's ability to recognize when an external function should be called, and return a structured JSON object with the appropriate arguments to execute",
         "The model executing Python code directly inside the GPU kernel", "Calling a phone number via VoIP", "A recursion stack overflow", "A", "Medium"),
        (t4, "What open-source guardrail library allows developers to enforce output structures, validate Pydantic types, and prevent hallucinations in LLM outputs?",
         "Guardrails AI (or NeMo Guardrails)", "Pandas", "Scikit-Learn", "PyTorch", "A", "Easy"),
        (t4, "What is 'Constitutional AI' developed by Anthropic?",
         "A training and alignment methodology where models critique and revise their own responses according to a set of written constitutional principles and values",
         "An AI that passes the bar exam", "A government computer system", "An algorithm written into national law", "A", "Hard"),
        (t4, "What is 'Toxicity Filtering' in prompt and response safety moderation?",
         "Scanning user inputs and model outputs using dedicated classification models to block hate speech, harassment, self-harm, and violent content",
         "Filtering physical dust from computers", "Removing spam emails from inboxes", "Deleting broken URLs", "A", "Easy"),
        (t4, "Why should sensitive personal data (PII) never be included in prompts sent to public third-party commercial LLM APIs without enterprise data agreements?",
         "Because data may be retained for future model retraining, creating severe privacy violations and compliance breaches (GDPR, HIPAA, DPDP Act)",
         "Because the model will crash", "Because the API will charge double fees", "Because models cannot process names", "A", "Easy"),
        (t4, "What is 'Red Teaming' in LLM safety evaluation?",
         "Systematically attempting to probe, attack, and exploit vulnerabilities, biases, and safety bypasses in an LLM before public deployment",
         "Painting server cases red", "Testing network cable throughput", "A competition between graphic designers", "A", "Medium")
    ]

    for q in pe_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in pe_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in pe_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in pe_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_ds_questions():
    questions = []
    sub = "Data Structures"
    branch = "Artificial Intelligence & Data Science"
    year = "Second Year"
    sem = "Semester III"

    u1 = "Unit 1: Data Types, Arrays and Hash Tables"
    t1 = "Arrays & Hash Tables"
    ds_u1 = [
        (t1, "What is an Abstract Data Type (ADT)?",
         "A mathematical model for data types where the data type is defined by its behavior (operations) from the point of view of a user, independent of implementation",
         "A physical RAM circuit", "A programming language syntax rule", "A compiler optimization phase", "A", "Easy"),
        (t1, "What is the worst-case time complexity of accessing an array element by its index in memory?",
         "O(1)", "O(n)", "O(log n)", "O(n^2)", "A", "Easy"),
        (t1, "What defines a 'Sparse Matrix' in numerical computing?",
         "A matrix in which the vast majority of elements have a value of zero", "A matrix with only complex numbers",
         "A matrix that cannot be inverted", "A matrix with negative dimensions", "A", "Easy"),
        (t1, "What triplet representation is typically used to store a sparse matrix in memory efficiently?",
         "<Row, Column, Value>", "<Index, Pointer, Size>", "<Key, Hash, Bucket>", "<Start, End, Weight>", "A", "Easy"),
        (t1, "What is a 'Hash Collision' in hash table data structures?",
         "When two distinct keys produce the exact same hash index via the hash function: h(k1) == h(k2)",
         "When the computer runs out of disk storage", "When an integer overflows 32 bits", "When a network packet is lost", "A", "Easy"),
        (t1, "Which collision resolution technique stores all colliding elements in a linked list at the hashed bucket index?",
         "Separate Chaining", "Linear Probing", "Quadratic Probing", "Double Hashing", "A", "Easy"),
        (t1, "What is 'Primary Clustering' in open addressing hash tables using linear probing?",
         "The tendency for occupied hash slots to form continuous long blocks, significantly increasing average search times",
         "Creating database clusters in the cloud", "Grouping files into directories", "Sorting array elements", "A", "Medium"),
        (t1, "In open addressing with Quadratic Probing, how is the i-th probe index calculated for key k?",
         "hash(k, i) = (h(k) + c1*i + c2*i^2) mod m", "hash(k, i) = (h(k) + i) mod m", "hash(k, i) = h(k) * i", "hash(k, i) = (h(k) + 2^i)", "A", "Medium"),
        (t1, "What is the 'Load Factor' (alpha) of a hash table with n elements and m total slots?",
         "alpha = n / m", "alpha = m / n", "alpha = n * m", "alpha = n - m", "A", "Easy"),
        (t1, "What is a 'Perfect Hash Function'?",
         "A hash function that maps a static set of keys to integers with zero collisions",
         "A hash function that never uses CPU cycles", "A function that generates random strings", "A cryptographic SHA-256 hash", "A", "Medium"),
        (t1, "In the division method of hashing h(k) = k mod m, what is the best choice for table size m?",
         "A prime number not close to a power of 2", "A power of 2 (e.g. 2^p)", "An even composite number", "A multiple of 10", "A", "Medium"),
        (t1, "What is the expected average-case time complexity of search, insert, and delete operations in a well-distributed Hash Table?",
         "O(1)", "O(log n)", "O(n)", "O(n log n)", "A", "Easy")
    ]

    u2 = "Unit 2: Stacks and Queues"
    t2 = "Stack & Queue Data Structures"
    ds_u2 = [
        (t2, "What operational principle governs the insertion and deletion of elements in a Stack?",
         "Last-In, First-Out (LIFO)", "First-In, First-Out (FIFO)", "Highest-Value First", "Random Access", "A", "Easy"),
        (t2, "What error occurs when a push() operation is attempted on a stack that is already completely full?",
         "Stack Overflow", "Stack Underflow", "Null Pointer Dereference", "Deadlock", "A", "Easy"),
        (t2, "What error occurs when a pop() operation is attempted on an empty stack?",
         "Stack Underflow", "Stack Overflow", "Segmentation Fault", "Memory Leak", "A", "Easy"),
        (t2, "What operational principle governs a standard Queue data structure?",
         "First-In, First-Out (FIFO)", "Last-In, First-Out (LIFO)", "Priority Inversion", "Double-Ended Access", "A", "Easy"),
        (t2, "Why is a Circular Queue preferred over a standard linear array-based queue?",
         "It reuses empty positions created by dequeues at the front of the array using modulo arithmetic ((rear + 1) % capacity), preventing false overflow",
         "It executes in O(log n) time instead of O(1)", "It has infinite memory capacity", "It sorts elements automatically", "A", "Medium"),
        (t2, "What is the postfix (Reverse Polish) equivalent of the infix expression: (A + B) * C?",
         "A B + C *", "A B C + *", "* + A B C", "+ A B * C", "A", "Easy"),
        (t2, "What data structure is utilized by compilers to evaluate postfix arithmetic expressions and check matching parentheses?",
         "Stack", "Queue", "Binary Search Tree", "Adjacency Matrix", "A", "Easy"),
        (t2, "What is the value of the postfix expression: 5 3 + 2 *?",
         "16", "11", "25", "10", "A", "Easy"),
        (t2, "What queue variant allows insertion and deletion operations at both the front and rear ends?",
         "Double-Ended Queue (Deque)", "Circular Queue", "Priority Queue", "Monotonic Queue", "A", "Easy"),
        (t2, "In a Priority Queue, how are elements dequeued?",
         "The element with the highest (or lowest) priority is removed first, regardless of insertion order",
         "In strict arrival order (FIFO)", "In strict reverse arrival order (LIFO)", "Randomly", "A", "Easy"),
        (t2, "How can a Queue be implemented using two Stacks (S1 and S2)?",
         "Enqueue pushes onto S1; Dequeue pops from S2 (if S2 is empty, transfer all elements from S1 to S2)",
         "Push onto both stacks simultaneously", "Pop from both stacks alternately", "It is impossible to build a queue with stacks", "A", "Medium"),
        (t2, "What internal data structure in the operating system runtime environment manages recursive function calls?",
         "Call Stack (Execution Stack)", "Kernel Queue", "Binary Search Tree", "Hash Table", "A", "Easy")
    ]

    u3 = "Unit 3: Linked Lists"
    t3 = "Linked List Implementations"
    ds_u3 = [
        (t3, "What are the two basic components stored inside each node of a Singly Linked List?",
         "Data value and a Next pointer referencing the subsequent node", "Data value and previous pointer",
         "Left child and right child pointers", "Row index and column index", "A", "Easy"),
        (t3, "What is the primary advantage of a Linked List over a static contiguous Array?",
         "Dynamic size allocation at runtime and efficient insertion/deletion without shifting subsequent elements",
         "O(1) random access by index", "Lower memory usage per element", "Cache locality", "A", "Easy"),
        (t3, "What is the time complexity to insert a new node at the head (beginning) of a Singly Linked List?",
         "O(1)", "O(n)", "O(log n)", "O(n^2)", "A", "Easy"),
        (t3, "What does each node in a Doubly Linked List contain compared to a singly linked list?",
         "Data value, a Next pointer, and a Prev pointer pointing to the predecessor node",
         "Two data values", "A pointer to the middle node", "An array of 10 pointers", "A", "Easy"),
        (t3, "In a Circular Singly Linked List, where does the 'next' pointer of the last node point to?",
         "The first node (Head) of the list", "NULL / nullptr", "Itself exclusively", "The middle node", "A", "Easy"),
        (t3, "What is the time complexity to find the N-th element in a standard Singly Linked List of length N?",
         "O(N)", "O(1)", "O(log N)", "O(N log N)", "A", "Easy"),
        (t3, "What algorithm detects a cycle or loop in a linked list using two pointers moving at different speeds (Slow and Fast)?",
         "Floyd's Cycle-Finding Algorithm (Tortoise and Hare)", "Dijkstra's Algorithm", "Binary Search", "Kadane's Algorithm", "A", "Medium"),
        (t3, "What happens if dynamic memory allocated with malloc() in C or new in C++ is never freed when pointers are lost?",
         "Memory Leak", "Stack Overflow", "Bus Error", "Arithmetic Overflow", "A", "Easy"),
        (t3, "What is the role of automated 'Garbage Collection' in modern runtime environments (like Java and Python)?",
         "To automatically identify and reclaim heap memory occupied by objects that are no longer reachable by any live reference",
         "To empty the operating system recycle bin", "To delete temporary files from disk", "To defragment physical RAM chips", "A", "Easy"),
        (t3, "What is the time complexity to reverse a Singly Linked List of length N in-place iteratively?",
         "O(N) time and O(1) auxiliary space", "O(N^2) time", "O(log N) time", "O(N) space", "A", "Medium"),
        (t3, "In a doubly linked list, what is the time complexity to delete a given node if a pointer directly to that node is already provided?",
         "O(1)", "O(n)", "O(log n)", "O(n^2)", "A", "Medium"),
        (t3, "What is a 'Header Linked List'?",
         "A linked list that contains a special dummy node (header node) at the beginning to simplify boundary insertion/deletion operations",
         "A linked list stored in ROM", "A list containing only header files (.h)", "A list without pointers", "A", "Easy")
    ]

    u4 = "Unit 4: Trees and Graphs"
    t4 = "Trees, BST & Graph Traversals"
    ds_u4 = [
        (t4, "What is a 'Binary Tree'?",
         "A hierarchical tree data structure in which each parent node has at most two child nodes (left child and right child)",
         "A tree with exactly 2 nodes in total", "A tree where all nodes have identical values", "A directed graph with cycles", "A", "Easy"),
        (t4, "What property uniquely characterizes a Binary Search Tree (BST)?",
         "For every node, all values in its left subtree are strictly less than the node's value, and all values in its right subtree are greater",
         "All leaves are at the exact same depth", "Every node has exactly two children", "The root node always contains the maximum value", "A", "Easy"),
        (t4, "Which depth-first tree traversal visits nodes in the order: Left Subtree -> Root Node -> Right Subtree?",
         "Inorder Traversal (which outputs BST values in sorted ascending order)", "Preorder Traversal", "Postorder Traversal", "Level-order Traversal", "A", "Easy"),
        (t4, "What is the worst-case time complexity of searching for an element in an unbalanced (skewed) Binary Search Tree of N nodes?",
         "O(N)", "O(log N)", "O(1)", "O(N log N)", "A", "Easy"),
        (t4, "What self-balancing binary search tree maintains balance by ensuring that the heights of the two child subtrees of any node differ by at most one (Balance Factor in {-1, 0, +1})?",
         "AVL Tree", "Binary Heap", "B-Tree", "Trie", "A", "Medium"),
        (t4, "What is a 'Max-Heap' property in a complete binary tree?",
         "The value of each parent node is greater than or equal to the values of its children, with the maximum element at the root",
         "All leaves have value 0", "Left child is always greater than right child", "The root is the minimum element", "A", "Easy"),
        (t4, "What is the space complexity to represent a graph with V vertices and E edges using an Adjacency Matrix?",
         "O(V^2)", "O(V + E)", "O(E^2)", "O(V * E)", "A", "Easy"),
        (t4, "What algorithm finds the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights?",
         "Dijkstra's Algorithm", "Warshall's Algorithm", "Kruskal's Algorithm", "Depth First Search", "A", "Easy"),
        (t4, "What algorithm computes the Transitive Closure (reachability matrix) of a directed graph?",
         "Warshall's Algorithm", "Prim's Algorithm", "Huffman Algorithm", "KMP Algorithm", "A", "Medium"),
        (t4, "What is the difference between a Tree and a Graph in computer science?",
         "A tree is a connected, undirected acyclic graph with exactly V - 1 edges; a general graph may contain cycles and disconnected components",
         "A graph has no vertices", "A tree cannot store numbers", "There is no difference", "A", "Easy"),
        (t4, "What is a 'Threaded Binary Tree'?",
         "A binary tree variant where null child pointers are repurposed to point to the in-order predecessor or successor nodes, enabling fast stack-less traversals",
         "A tree that runs on multiple CPU threads", "A tree stored in a JSON file", "A tree with colored nodes", "A", "Hard"),
        (t4, "What graph traversal uses a queue to visit vertices layer-by-layer in order of increasing distance from the start vertex?",
         "Breadth-First Search (BFS)", "Depth-First Search (DFS)", "Topological Sort", "Preorder Traversal", "A", "Easy")
    ]

    u5 = "Unit 5: Searching and Sorting"
    t5 = "Search Algorithms & Sorting Techniques"
    ds_u5 = [
        (t5, "What precondition must be satisfied before Binary Search can be applied to an array?",
         "The array elements must be sorted in order", "The array must contain only positive integers",
         "The array size must be a power of 2", "The array must be stored on SSD", "A", "Easy"),
        (t5, "What is the time complexity of Binary Search on a sorted array of N elements?",
         "O(log N)", "O(1)", "O(N)", "O(N^2)", "A", "Easy"),
        (t5, "What is a 'Stable' sorting algorithm?",
         "A sort that preserves the relative order of equal keys (records with identical sort keys appear in the same order in the output as in the input)",
         "A sort that never crashes the computer", "A sort with O(1) space complexity", "A sort that runs in linear time", "A", "Easy"),
        (t5, "What is the average and worst-case time complexity of Merge Sort?",
         "O(N log N) in both average and worst case", "O(N^2) worst case, O(N) best case", "O(N) worst case", "O(log N)", "A", "Easy"),
        (t5, "What is the worst-case time complexity of QuickSort (occurring when the chosen pivot is repeatedly the smallest or largest element)?",
         "O(N^2)", "O(N log N)", "O(N)", "O(log N)", "A", "Easy"),
        (t5, "What sorting algorithm builds the final sorted array one item at a time by repeatedly taking the next element and inserting it into its correct position among previously sorted elements?",
         "Insertion Sort", "Selection Sort", "Bubble Sort", "Radix Sort", "A", "Easy"),
        (t5, "What non-comparative integer sorting algorithm sorts numbers digit-by-digit starting from least significant digit (LSD) using a stable subroutine like Counting Sort?",
         "Radix Sort", "QuickSort", "HeapSort", "MergeSort", "A", "Medium"),
        (t5, "What is the time complexity of Heap Sort on an array of N elements?",
         "O(N log N)", "O(N^2)", "O(N)", "O(log N)", "A", "Easy"),
        (t5, "What is a 'Skip List' data structure?",
         "A probabilistic data structure that layers multiple linked lists with forward shortcuts to achieve O(log n) search, insert, and delete operations",
         "An array that skips even indices", "A queue that drops packets", "A binary search tree with array storage", "A", "Hard"),
        (t5, "In an external sorting context (sorting massive data files that exceed available RAM), which algorithm is standardly used?",
         "External Multi-Way Merge Sort", "In-place QuickSort", "Bubble Sort", "Selection Sort", "A", "Medium"),
        (t5, "What is the time complexity of Selection Sort on an array of N elements?",
         "O(N^2) in all cases (best, average, worst)", "O(N log N)", "O(N)", "O(1)", "A", "Easy"),
        (t5, "What is the theoretical lower bound on comparison-based sorting algorithms in the worst case?",
         "Omega(N log N)", "Omega(N)", "Omega(log N)", "Omega(N^2)", "A", "Hard")
    ]

    for q in ds_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ds_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ds_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ds_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ds_u5: questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_discrete_maths_questions():
    questions = []
    sub = "Discrete Mathematics"
    branch = "Artificial Intelligence & Data Science"
    year = "Second Year"
    sem = "Semester III"

    u1 = "Unit 1: Propositional Logic and Predicates"
    t1 = "Propositional Logic & Quantifiers"
    dm_u1 = [
        (t1, "What is a 'Proposition' in mathematical logic?",
         "A declarative statement that is either strictly True or False, but not both",
         "A question ending with a question mark", "An algebraic equation with unknown variables", "A command instructing the CPU", "A", "Easy"),
        (t1, "What is the truth value of the logical implication P -> Q when P is False and Q is False?",
         "True (vacuously true)", "False", "Undefined", "Neither True nor False", "A", "Easy"),
        (t1, "Which logical equivalence represents De Morgan's Law for conjunction: not(P and Q)?",
         "not P or not Q", "not P and not Q", "P or Q", "not P -> not Q", "A", "Easy"),
        (t1, "What is a 'Tautology' in propositional logic?",
         "A compound proposition that is always True regardless of the truth values of its individual propositional variables",
         "A proposition that is always False (Contradiction)", "A proposition that depends on empirical data", "A formula with no negation", "A", "Easy"),
        (t1, "What is the Contrapositive of the conditional statement 'If it rains, then the ground is wet' (P -> Q)?",
         "If the ground is not wet, then it does not rain (not Q -> not P)",
         "If it does not rain, then the ground is not wet", "If the ground is wet, then it rains",
         "It rains and the ground is not wet", "A", "Easy"),
        (t1, "What is the negation of the quantified predicate statement: forall x P(x)?",
         "exists x (not P(x))", "forall x (not P(x))", "exists x P(x)", "not (exists x P(x))", "A", "Medium"),
        (t1, "What is the negation of: exists x P(x)?",
         "forall x (not P(x))", "exists x (not P(x))", "forall x P(x)", "not (forall x P(x))", "A", "Medium"),
        (t1, "What rule of inference states that if (P or Q) is true and (not P) is true, then Q must be true?",
         "Disjunctive Syllogism", "Modus Ponens", "Modus Tollens", "Hypothetical Syllogism", "A", "Easy"),
        (t1, "What rule of inference states that if (P -> Q) and (Q -> R) are both true, then (P -> R) is true?",
         "Hypothetical Syllogism (Transitivity of Implication)", "Conjunction Elimination", "Modus Ponens", "Resolution", "A", "Easy"),
        (t1, "In the Resolution rule for propositional logic, what resolvent is derived from clauses (P or Q) and (not P or R)?",
         "Q or R", "P or R", "not Q or R", "P and not P", "A", "Medium"),
        (t1, "What is the 'Fallacy of Affirming the Consequent'?",
         "Invalidly concluding P from (P -> Q) and Q", "Concluding Q from (P -> Q) and P",
         "Concluding not P from (P -> Q) and not Q", "Assuming a tautology is false", "A", "Medium"),
        (t1, "What is a 'Well-Formed Formula' (WFF) in predicate logic?",
         "A syntactically valid string of symbols generated according to the formal grammar rules of the logic system",
         "A formula with only 2 variables", "A formula that has been compiled into C code", "A true statement about integers", "A", "Easy")
    ]

    u2 = "Unit 2: Set Theory, Functions and Relations"
    t2 = "Sets, Functions, Relations & Posets"
    dm_u2 = [
        (t2, "If set A has N elements (|A| = N), how many elements are in its Power Set P(A)?",
         "2^N", "N^2", "2*N", "N!", "A", "Easy"),
        (t2, "What is the Cartesian Product A x B of two sets A = {1, 2} and B = {x, y}?",
         "{(1, x), (1, y), (2, x), (2, y)}", "{1, 2, x, y}", "{(1, 2), (x, y)}", "{1x, 2y}", "A", "Easy"),
        (t2, "What property characterizes an 'Injective' (One-to-One) function f: A -> B?",
         "Distinct domain elements map to distinct codomain elements: f(a1) = f(a2) implies a1 = a2",
         "Every element of codomain B is an image of at least one element of A", "The domain and codomain have equal size",
         "The function has an inverse only if it is constant", "A", "Easy"),
        (t2, "What property characterizes a 'Surjective' (Onto) function f: A -> B?",
         "The range of f equals its codomain B (for every b in B, there exists a in A such that f(a) = b)",
         "No two elements map to the same image", "The function is linear", "The function is symmetric", "A", "Easy"),
        (t2, "A function that is both Injective and Surjective is classified as:",
         "Bijective (One-to-One Correspondence) and possesses a unique inverse function",
         "Reflexive", "Transitive", "Homomorphic", "A", "Easy"),
        (t2, "What three mathematical properties must a binary relation R on set A satisfy to be an 'Equivalence Relation'?",
         "Reflexive, Symmetric, and Transitive", "Reflexive, Antisymmetric, and Transitive",
         "Irreflexive, Symmetric, and Dense", "Total, Transitive, and Commutative", "A", "Easy"),
        (t2, "What fundamental theorem states that an equivalence relation on set A partitions A into a collection of disjoint equivalence classes?",
         "Fundamental Theorem of Equivalence Relations (Equivalence Partition Theorem)",
         "Lagrange's Theorem", "Pigeonhole Principle", "Euler's Totient Theorem", "A", "Medium"),
        (t2, "What three properties must a relation R on set A satisfy to be a 'Partial Order Relation' (POSET)?",
         "Reflexive, Antisymmetric, and Transitive", "Reflexive, Symmetric, and Transitive",
         "Irreflexive, Asymmetric, and Intransitive", "Symmetric, Associative, and Commutative", "A", "Easy"),
        (t2, "What visual diagram represents a finite partially ordered set (poset) by omitting transitive and reflexive edges?",
         "Hasse Diagram", "Venn Diagram", "State Transition Diagram", "Dendrogram", "A", "Easy"),
        (t2, "What algorithm computes a linear extension / ordering of vertices in a Directed Acyclic Graph (DAG) consistent with its partial order?",
         "Topological Sort", "Kruskal's Algorithm", "Binary Search", "Warshall's Closure", "A", "Easy"),
        (t2, "In a poset, what is an element m such that no other element x satisfies x < m?",
         "Minimal Element", "Maximal Element", "Greatest Lower Bound", "Least Upper Bound", "A", "Medium"),
        (t2, "What is a 'Lattice' in order theory?",
         "A partially ordered set in which every pair of elements has a unique Least Upper Bound (join / sup) and Greatest Lower Bound (meet / inf)",
         "A grid of integer pixels", "A set with no relations", "A graph with no vertices", "A", "Medium")
    ]

    u3 = "Unit 3: Combinatorics and Recurrence Relations"
    t3 = "Permutations, Combinations & Recurrence"
    dm_u3 = [
        (t3, "What principle states that if n items are put into m containers and n > m, then at least one container must contain more than one item?",
         "Pigeonhole Principle (Dirichlet's Box Principle)", "Inclusion-Exclusion Principle",
         "Well-Ordering Principle", "Mathematical Induction", "A", "Easy"),
        (t3, "How many ways can r objects be chosen from n distinct objects without regard to order, C(n, r)?",
         "n! / (r! * (n - r)!)", "n! / (n - r)!", "n^r", "r! / n!", "A", "Easy"),
        (t3, "How many distinct permutations can be formed using all letters of the word 'SUCCESS'?",
         "7! / (3! * 2!) = 420 (accounting for 3 S's and 2 C's)", "7! = 5040", "7! / 3! = 840", "7^2 = 49", "A", "Medium"),
        (t3, "What is the Principle of Inclusion-Exclusion for two finite sets A and B?",
         "|A union B| = |A| + |B| - |A intersect B|", "|A union B| = |A| + |B|", "|A union B| = |A| * |B|", "|A union B| = |A| - |B|", "A", "Easy"),
        (t3, "What is the characteristic equation for the second-order linear homogeneous recurrence relation: a_n = 5*a_{n-1} - 6*a_{n-2}?",
         "r^2 - 5*r + 6 = 0 (roots r = 2, r = 3)", "r^2 + 5*r - 6 = 0", "r^2 - 6*r + 5 = 0", "5*r - 6 = 0", "A", "Medium"),
        (t3, "What is the general solution of a_n = 5*a_{n-1} - 6*a_{n-2} with characteristic roots r1 = 2 and r2 = 3?",
         "a_n = C1 * (2)^n + C2 * (3)^n", "a_n = C1 * 2 + C2 * 3", "a_n = (2 * 3)^n", "a_n = C1 + C2 * n", "A", "Medium"),
        (t3, "What is the famous recurrence relation for the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13...?",
         "F_n = F_{n-1} + F_{n-2} with F_0 = 0, F_1 = 1", "F_n = 2 * F_{n-1}", "F_n = F_{n-1} * F_{n-2}", "F_n = F_{n-1} + 1", "A", "Easy"),
        (t3, "What is the generating function for the constant sequence 1, 1, 1, 1, ...?",
         "1 / (1 - x) for |x| < 1", "1 / (1 + x)", "e^x", "ln(1 - x)", "A", "Hard"),
        (t3, "What is a 'Derangement' in combinatorics?",
         "A permutation of elements of a set such that no element appears in its original position (zero fixed points)",
         "A sorting algorithm error", "An infinite set", "A matrix without diagonals", "A", "Hard"),
        (t3, "How many edges are in a complete graph K_n with n vertices?",
         "n * (n - 1) / 2", "n", "n^2", "2^n", "A", "Easy"),
        (t3, "In how many ways can 5 people be seated around a circular table (circular permutations)?",
         "(5 - 1)! = 4! = 24", "5! = 120", "5^2 = 25", "2^5 = 32", "A", "Easy"),
        (t3, "What method of mathematical proof establishes a base case P(1) and proves that P(k) implies P(k+1) for all positive integers?",
         "Principle of Mathematical Induction", "Proof by Contradiction", "Direct Constructive Proof", "Proof by Counterexample", "A", "Easy")
    ]

    u4 = "Unit 4: Graph Theory and Trees"
    t4 = "Graphs, Eulerian Paths & Spanning Trees"
    dm_u4 = [
        (t4, "What is the Handshaking Lemma in graph theory?",
         "The sum of degrees of all vertices in any graph G equals twice the number of edges: sum deg(v) = 2 * |E|",
         "The number of vertices always equals edges", "Every graph has an even number of vertices", "Edges cannot cross", "A", "Easy"),
        (t4, "As a direct corollary of the Handshaking Lemma, every undirected graph must have an even number of vertices of:",
         "Odd degree", "Even degree", "Degree 0", "Degree 2", "A", "Medium"),
        (t4, "What is an 'Eulerian Circuit' in a connected graph G?",
         "A closed trail that visits every edge of G exactly once and returns to the starting vertex",
         "A path that visits every vertex exactly once", "A cycle with minimum weight", "A spanning tree", "A", "Easy"),
        (t4, "According to Euler's Theorem, when does a connected graph G contain an Eulerian Circuit?",
         "If and only if every vertex in G has an even degree",
         "If and only if exactly two vertices have odd degree", "If G is a tree", "If G has no cycles", "A", "Easy"),
        (t4, "What is a 'Hamiltonian Cycle' in graph theory?",
         "A closed cycle that visits every VERTEX of the graph exactly once (except starting/ending vertex)",
         "A path that visits every edge once", "A cycle of length 3", "A disconnected subgraph", "A", "Easy"),
        (t4, "What is a 'Bipartite Graph'?",
         "A graph whose vertices can be partitioned into two disjoint sets V1 and V2 such that every edge connects a vertex in V1 to one in V2",
         "A graph with exactly two edges", "A graph with two cycles", "A graph where all degrees are 2", "A", "Easy"),
        (t4, "A graph is bipartite if and only if it contains no cycles of:",
         "Odd length", "Even length", "Length greater than 4", "Any length (must be a tree)", "A", "Medium"),
        (t4, "What is Euler's Formula for any connected planar graph with V vertices, E edges, and F faces (regions)?",
         "V - E + F = 2", "V + E - F = 2", "V * E = F", "V - E = F + 1", "A", "Easy"),
        (t4, "What greedy algorithm finds a Minimum Spanning Tree (MST) by sorting all edges by weight and adding the smallest edge that does not form a cycle?",
         "Kruskal's Algorithm", "Prim's Algorithm", "Dijkstra's Algorithm", "Floyd-Warshall", "A", "Easy"),
        (t4, "What algorithm builds a Minimum Spanning Tree by growing a single tree from an arbitrary root vertex, adding the cheapest edge connecting tree to non-tree vertices?",
         "Prim's Algorithm", "Kruskal's Algorithm", "Bellman-Ford", "Huffman Algorithm", "A", "Easy"),
        (t4, "What prefix coding algorithm builds an optimal binary tree based on character frequencies to achieve lossless data compression?",
         "Huffman Coding", "Hamming Error Coding", "Run-Length Encoding", "Caesar Cipher", "A", "Easy"),
        (t4, "How many edges does any Tree with N vertices contain?",
         "N - 1 edges", "N edges", "N + 1 edges", "N * (N - 1) / 2 edges", "A", "Easy")
    ]

    u5 = "Unit 5: Algebraic Structures and Morphism"
    t5 = "Groups, Rings, Fields & Lattices"
    dm_u5 = [
        (t5, "What four axioms must an algebraic structure (G, *) satisfy to be classified as a 'Group'?",
         "Closure, Associativity, Identity element existence, and Inverse element existence for every element",
         "Commutativity, Distributivity, Linearity, and Orthogonality",
         "Idempotence, Absorption, Involution, and Boundedness", "Transitivity, Reflexivity, Symmetry, and Antisymmetry", "A", "Easy"),
        (t5, "What additional axiom must a group satisfy to be called an 'Abelian Group'?",
         "Commutativity: a * b = b * a for all a, b in G", "Associativity only", "Must be finite", "Elements must be integers", "A", "Easy"),
        (t5, "What algebraic structure (S, *) satisfies only Closure and Associativity (without necessarily having identity or inverses)?",
         "Semigroup", "Monoid", "Group", "Field", "A", "Easy"),
        (t5, "What algebraic structure is a Semigroup that also possesses an Identity element?",
         "Monoid", "Group", "Ring", "Field", "A", "Easy"),
        (t5, "What is Lagrange's Theorem in finite group theory?",
         "The order (size) of any subgroup H divides the order of the finite group G: |G| / |H| is an integer",
         "Every group has prime order", "All subgroups are normal", "The order of a group is infinite", "A", "Medium"),
        (t5, "What is a 'Cyclic Group'?",
         "A group that can be generated by a single element g in G such that every element can be written as a power g^k",
         "A group with periodic table properties", "A group that contains no subgroups", "A non-abelian group", "A", "Easy"),
        (t5, "What algebraic structure (R, +, *) is an abelian group under addition (+), a semigroup under multiplication (*), and multiplication distributes over addition?",
         "Ring", "Field", "Vector Space", "Monoid", "A", "Medium"),
        (t5, "What is an 'Integral Domain'?",
         "A commutative ring with identity and no zero divisors (if a * b = 0, then a = 0 or b = 0)",
         "A field with complex numbers", "A group of matrices", "A domain of continuous functions", "A", "Hard"),
        (t5, "What is a 'Field' (F, +, *) in modern algebra?",
         "A commutative ring with non-zero identity in which every non-zero element has a multiplicative inverse",
         "A set of grass in geometry", "A group with no addition", "A finite set of strings", "A", "Medium"),
        (t5, "Which of the following number systems forms a Field under standard addition and multiplication?",
         "Real Numbers (R) and Rational Numbers (Q)", "Integers (Z) [non-zero integers lack multiplicative inverses in Z]",
         "Natural Numbers (N)", "Even integers", "A", "Medium"),
        (t5, "What is a 'Homomorphism' between two algebraic groups (G, *) and (H, o)?",
         "A function f: G -> H preserving operations: f(a * b) = f(a) o f(b) for all a, b in G",
         "A bijective mapping between sets with no operation rules", "An identity permutation", "A matrix determinant", "A", "Hard"),
        (t5, "In Boolean Algebra, what does the Absorption Law state?",
         "x and (x or y) = x, and x or (x and y) = x", "x and y = y and x", "x or 0 = x", "x and not x = 0", "A", "Easy")
    ]

    for q in dm_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in dm_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in dm_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in dm_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in dm_u5: questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_engg_maths3_questions():
    questions = []
    sub = "Engineering Mathematics-III"
    branch = "Artificial Intelligence & Data Science"
    year = "Second Year"
    sem = "Semester III"

    u1 = "Unit 1: Laplace Transform"
    t1 = "Laplace Transforms & Properties"
    em_u1 = [
        (t1, "What is the formal integral definition of the Laplace Transform L{f(t)} = F(s)?",
         "integral_0^infinity e^(-s*t) * f(t) dt", "integral_-infinity^infinity e^(-i*w*t) * f(t) dt",
         "integral_0^1 f(t) dt", "d/dt [f(t)]", "A", "Easy"),
        (t1, "What is the Laplace transform of the constant function f(t) = 1 for s > 0?",
         "1 / s", "s", "1 / s^2", "1", "A", "Easy"),
        (t1, "What is the Laplace transform of f(t) = t^n for a positive integer n?",
         "n! / s^(n+1)", "1 / s^n", "n! / s^n", "s / (s^2 + n^2)", "A", "Easy"),
        (t1, "What is the Laplace transform of f(t) = e^(a*t) for s > a?",
         "1 / (s - a)", "1 / (s + a)", "a / s", "s / (s - a)", "A", "Easy"),
        (t1, "What is the Laplace transform of f(t) = sin(a*t)?",
         "a / (s^2 + a^2)", "s / (s^2 + a^2)", "a / (s^2 - a^2)", "1 / (s^2 + a^2)", "A", "Easy"),
        (t1, "What is the Laplace transform of f(t) = cos(a*t)?",
         "s / (s^2 + a^2)", "a / (s^2 + a^2)", "s / (s^2 - a^2)", "1 / s", "A", "Easy"),
        (t1, "What does the First Shifting Property of Laplace transforms state: L{e^(a*t) * f(t)}?",
         "F(s - a)", "F(s + a)", "e^(-a*s) * F(s)", "a * F(s)", "A", "Medium"),
        (t1, "What is the Laplace transform of the derivative of a function: L{f'(t)}?",
         "s * F(s) - f(0)", "s * F(s)", "F(s) / s", "s^2 * F(s) - f'(0)", "A", "Medium"),
        (t1, "What property gives the transform of an integral: L{integral_0^t f(u) du}?",
         "F(s) / s", "s * F(s)", "F(s) - f(0)", "F'(s)", "A", "Medium"),
        (t1, "What is the Laplace transform of t * f(t) (Multiplication by t)?",
         "- d/ds [F(s)]", "s * F(s)", "F(s) / s", "integral F(s) ds", "A", "Medium"),
        (t1, "What is the Laplace transform of the Dirac Delta function delta(t - a) for a >= 0?",
         "e^(-a*s)", "1 / s", "s", "0", "A", "Medium"),
        (t1, "What is the Laplace transform of the Heaviside Unit Step function u(t - a)?",
         "e^(-a*s) / s", "1 / s", "e^(a*s)", "s * e^(-a*s)", "A", "Easy")
    ]

    u2 = "Unit 2: Inverse Laplace Transform"
    t2 = "Inverse Laplace & Differential Equations"
    em_u2 = [
        (t2, "What is the Inverse Laplace transform L^(-1){1 / (s - 3)}?",
         "e^(3*t)", "e^(-3*t)", "cos(3*t)", "sin(3*t)", "A", "Easy"),
        (t2, "What is the Inverse Laplace transform L^(-1){s / (s^2 + 16)}?",
         "cos(4*t)", "sin(4*t)", "e^(4*t)", "4 * cos(4*t)", "A", "Easy"),
        (t2, "What is the Inverse Laplace transform L^(-1){1 / (s^2 + 9)}?",
         "(1/3) * sin(3*t)", "sin(3*t)", "cos(3*t)", "3 * sin(3*t)", "A", "Easy"),
        (t2, "What does the Convolution Theorem for Laplace transforms state: L^(-1){F(s) * G(s)}?",
         "integral_0^t f(u) * g(t - u) du (the convolution f(t) * g(t))", "f(t) * g(t) (simple point-wise product)",
         "f(t) + g(t)", "f'(t) * g'(t)", "A", "Medium"),
        (t2, "What algebraic method decomposes rational functions P(s)/Q(s) into simpler terms to find inverse transforms?",
         "Partial Fraction Decomposition", "Integration by parts", "Gaussian Elimination", "Synthetic Division", "A", "Easy"),
        (t2, "What is L^(-1){1 / (s^2 - 4)}?",
         "(1/2) * sinh(2*t)", "cosh(2*t)", "sin(2*t)", "e^(2*t)", "A", "Medium"),
        (t2, "What is L^(-1){s / (s^2 - 4)}?",
         "cosh(2*t)", "sinh(2*t)", "cos(2*t)", "e^(-2*t)", "A", "Medium"),
        (t2, "How are initial value differential equations (e.g., y'' + a*y' + b*y = f(t)) solved using Laplace transforms?",
         "By transforming the differential equation into an algebraic equation in s, solving for Y(s), and taking the inverse transform",
         "By numerical Euler approximation", "By guessing polynomial roots", "By converting to polar coordinates", "A", "Medium"),
        (t2, "What is L^(-1){1 / (s + 2)^3} using the shifting theorem?",
         "(1/2) * t^2 * e^(-2*t)", "t^3 * e^(-2*t)", "e^(-2*t) / 3", "2 * t * e^(-2*t)", "A", "Hard"),
        (t2, "What is L^(-1){e^(-3*s) / s^2} using the second shifting theorem?",
         "(t - 3) * u(t - 3)", "t^2 * u(t - 3)", "e^(-3*t)", "u(t - 3) / 2", "A", "Hard"),
        (t2, "What initial values does the Laplace transform method natively incorporate into the algebraic solution?",
         "Initial conditions at t = 0 (e.g. y(0) and y'(0))", "Boundary conditions at infinity",
         "Eigenvalues at t = 1", "No initial conditions can be used", "A", "Easy"),
        (t2, "What is L^(-1){s / (s^2 + 25)^2} using the derivative property?",
         "(t/10) * sin(5*t)", "(t/5) * cos(5*t)", "sin(5*t)", "t * cos(5*t)", "A", "Hard")
    ]

    u3 = "Unit 3: Fourier Transform"
    t3 = "Fourier Integrals & Transforms"
    em_u3 = [
        (t3, "What is the Fourier Transform F(w) of a continuous function f(t) defined on (-infinity, +infinity)?",
         "integral_-infinity^infinity f(t) * e^(-i*w*t) dt", "integral_0^infinity f(t) * e^(-s*t) dt",
         "sum f(n) * e^(i*n*w)", "integral f(t) * sin(w*t) dt", "A", "Easy"),
        (t3, "What is the Inverse Fourier Transform formula to reconstruct f(t) from F(w)?",
         "(1 / (2*pi)) * integral_-infinity^infinity F(w) * e^(i*w*t) dw", "integral F(w) dw",
         "(1 / pi) * integral F(w) * cos(w*t) dw", "e^(-i*w*t) * F(w)", "A", "Medium"),
        (t3, "What is the Fourier Sine Transform of f(t) on (0, infinity)?",
         "integral_0^infinity f(t) * sin(w*t) dt", "integral f(t) * cos(w*t) dt", "integral f(t) * e^(-w*t) dt", "f(0) * sin(w)", "A", "Easy"),
        (t3, "What is the Fourier Cosine Transform of f(t) on (0, infinity)?",
         "integral_0^infinity f(t) * cos(w*t) dt", "integral f(t) * sin(w*t) dt", "integral f(t) * e^(-i*w*t) dt", "f(0) * cos(w)", "A", "Easy"),
        (t3, "If f(t) is an even function (f(-t) = f(t)), what happens to its Fourier Transform?",
         "The sine component vanishes, and the transform becomes purely real and cosine-based",
         "The transform becomes purely imaginary", "The transform equals zero", "The transform is undefined", "A", "Medium"),
        (t3, "If f(t) is an odd function (f(-t) = -f(t)), what is the nature of its Fourier Transform?",
         "The transform is purely imaginary and odd", "The transform is purely real", "The transform is 1", "The transform diverges", "A", "Medium"),
        (t3, "What does Parseval's Identity state for Fourier Transforms (Conservation of Energy)?",
         "integral_-infinity^infinity |f(t)|^2 dt = (1 / (2*pi)) * integral_-infinity^infinity |F(w)|^2 dw",
         "integral f(t) dt = integral F(w) dw", "F(0) = 1", "|f(t)| = |F(w)|", "A", "Hard"),
        (t3, "What is the Fourier Transform of the shifted function f(t - a)?",
         "e^(-i*w*a) * F(w)", "F(w - a)", "a * F(w)", "e^(a*w) * F(w)", "A", "Medium"),
        (t3, "What is the Fourier Transform of the derivative f'(t)?",
         "i * w * F(w)", "F(w) / (i * w)", "-w^2 * F(w)", "d/dw [F(w)]", "A", "Medium"),
        (t3, "What is the Fourier Transform of the Gaussian function f(t) = e^(-a*t^2)?",
         "Another Gaussian function: sqrt(pi/a) * e^(-w^2 / (4*a))", "A rectangular pulse", "A delta function", "A sine wave", "A", "Hard"),
        (t3, "What condition must a function f(t) satisfy for its Fourier Transform to exist (Dirichlet Conditions)?",
         "f(t) is absolutely integrable: integral_-infinity^infinity |f(t)| dt < infinity, with finite extrema and discontinuities in any interval",
         "f(t) must be a polynomial", "f(t) must be positive everywhere", "f(t) must be constant", "A", "Medium"),
        (t3, "What is the Convolution Theorem for Fourier Transforms: F{f(t) * g(t)}?",
         "F(w) * G(w) (convolution in time corresponds to point-wise multiplication in frequency)",
         "F(w) + G(w)", "F(w) / G(w)", "d/dw [F(w) * G(w)]", "A", "Easy")
    ]

    u4 = "Unit 4: Partial Differential Equations and Their Applications"
    t4 = "PDEs, Wave Equation & Heat Equation"
    em_u4 = [
        (t4, "What is the order of the partial differential equation: d^2 u / dt^2 = c^2 * (d^2 u / dx^2)?",
         "Second Order", "First Order", "Third Order", "Zero Order", "A", "Easy"),
        (t4, "What famous physical phenomenon is modeled by the one-dimensional partial differential equation: d^2 u / dt^2 = c^2 * (d^2 u / dx^2)?",
         "One-Dimensional Wave Equation (e.g. vibrating string)", "One-Dimensional Heat Conduction",
         "Steady-State Laplace Potential", "Poisson Electrostatics", "A", "Easy"),
        (t4, "What physical phenomenon is modeled by the one-dimensional heat equation: du / dt = c^2 * (d^2 u / dx^2)?",
         "Transient Heat Conduction / Diffusion in a rod", "Vibrating membrane", "Fluid turbulence", "Sound propagation", "A", "Easy"),
        (t4, "What standard analytical technique solves linear boundary value PDEs by assuming u(x, t) = X(x) * T(t)?",
         "Method of Separation of Variables", "Newton-Raphson Method", "Runge-Kutta Method", "Laplace Expansion", "A", "Easy"),
        (t4, "What form does Lagrange's Linear Partial Differential Equation of first order take?",
         "P * p + Q * q = R where p = dz/dx, q = dz/dy", "p^2 + q^2 = 1", "z = p*x + q*y + f(p, q)", "p * q = z", "A", "Medium"),
        (t4, "What auxiliary equations are used to solve Lagrange's linear equation P*p + Q*q = R?",
         "dx / P = dy / Q = dz / R", "P*dx + Q*dy = R*dz", "dx/dy = P/Q", "d^2 x / dt^2 = R", "A", "Medium"),
        (t4, "What type of PDE is the two-dimensional Laplace Equation: d^2 u / dx^2 + d^2 u / dy^2 = 0?",
         "Elliptic PDE", "Hyperbolic PDE", "Parabolic PDE", "Ultra-hyperbolic PDE", "A", "Medium"),
        (t4, "How is a PDE formed from a relation z = f(x^2 + y^2) by eliminating arbitrary functions?",
         "By differentiating partially with respect to x and y (obtaining p and q) and eliminating f and f'",
         "By integrating from 0 to 1", "By setting z = 0", "By taking the Fourier transform", "A", "Medium"),
        (t4, "In the separation of variables for the wave equation X''(x)/X(x) = T''(t)/(c^2 * T(t)) = -p^2, what type of solutions for X(x) emerge?",
         "Trigonometric sinusoidal functions: C1 * cos(p*x) + C2 * sin(p*x)",
         "Exponential runaway functions", "Logarithmic curves", "Constant values only", "A", "Hard"),
        (t4, "In the one-dimensional heat equation du/dt = c^2 * d^2 u / dx^2, how does temperature behave over time t as t -> infinity?",
         "Temperatures decay exponentially toward a steady-state equilibrium",
         "Temperatures oscillate with increasing amplitude", "Temperatures become infinite", "Temperatures drop to absolute zero instantly", "A", "Medium"),
        (t4, "What boundary conditions describe a string of length L tightly clamped at both endpoints x = 0 and x = L?",
         "u(0, t) = 0 and u(L, t) = 0 for all t >= 0", "du/dx = 0 at both ends", "u(x, 0) = 0", "u(0, 0) = L", "A", "Easy"),
        (t4, "What classification applies to the 1D Heat Equation (B^2 - 4*A*C = 0)?",
         "Parabolic PDE", "Hyperbolic PDE", "Elliptic PDE", "Circular PDE", "A", "Medium")
    ]

    u5 = "Unit 5: Functions of Complex Variables"
    t5 = "Analytic Functions, Cauchy-Riemann & Residues"
    em_u5 = [
        (t5, "What conditions must a complex function f(z) = u(x, y) + i*v(x, y) satisfy to be Analytic (holomorphic)?",
         "u and v must satisfy the Cauchy-Riemann equations: du/dx = dv/dy and du/dy = -dv/dx with continuous first partial derivatives",
         "u must equal v everywhere", "The function must have no imaginary part", "The integral must be zero", "A", "Easy"),
        (t5, "What are the Cauchy-Riemann equations in Polar coordinates (r, theta) for f(z) = u(r, theta) + i*v(r, theta)?",
         "du/dr = (1/r) * dv/dtheta and dv/dr = -(1/r) * du/dtheta", "du/dr = dv/dtheta", "r * du/dr = dv/dtheta", "du/dtheta = dv/dr", "A", "Hard"),
        (t5, "What equation do the real part u(x, y) and imaginary part v(x, y) of an analytic function both satisfy (Harmonic functions)?",
         "Laplace's Equation: d^2 phi / dx^2 + d^2 phi / dy^2 = 0", "Wave Equation", "Heat Equation", "Poisson Equation", "A", "Medium"),
        (t5, "What is a 'Harmonic Conjugate' of a real harmonic function u(x, y)?",
         "A real function v(x, y) such that f(z) = u + i*v is an analytic function", "The negative of u", "The reciprocal 1/u", "The derivative du/dx", "A", "Medium"),
        (t5, "What does Cauchy's Integral Theorem state for a function f(z) analytic inside and on a simple closed contour C?",
         "contour_integral_C f(z) dz = 0", "contour_integral_C f(z) dz = 2*pi*i", "contour_integral_C f(z) dz = 1", "The integral is undefined", "A", "Easy"),
        (t5, "What does Cauchy's Integral Formula state for the value of an analytic function at an interior point z_0: f(z_0)?",
         "f(z_0) = (1 / (2*pi*i)) * contour_integral_C [f(z) / (z - z_0)] dz", "f(z_0) = 0", "f(z_0) = 2*pi*i * f'(z_0)", "f(z_0) = integral f(z) dz", "A", "Medium"),
        (t5, "What is the value of the contour integral contour_integral_C [1 / (z - a)] dz around a closed circle enclosing point a?",
         "2 * pi * i", "0", "pi * i", "1", "A", "Easy"),
        (t5, "What is a 'Singular Point' (singularity) of a complex function f(z)?",
         "A point z at which f(z) fails to be analytic", "A point where f(z) = 0", "A point on the real axis", "A point with zero derivative", "A", "Easy"),
        (t5, "What type of singularity does f(z) = e^(1/z) have at z = 0?",
         "Essential Singularity", "Simple Pole", "Removable Singularity", "Pole of order 2", "A", "Medium"),
        (t5, "What is the Residue of f(z) = 1 / (z - 2) at its simple pole z = 2?",
         "1", "0", "2", "-1", "A", "Easy"),
        (t5, "What does Cauchy's Residue Theorem state for evaluating contour integrals enclosing isolated singularities z_1, ..., z_k?",
         "contour_integral_C f(z) dz = 2 * pi * i * sum_{j=1}^k Res(f, z_j)", "contour_integral_C f(z) dz = 0",
         "contour_integral_C f(z) dz = sum Res(f, z_j)", "contour_integral_C f(z) dz = pi * i", "A", "Medium"),
        (t5, "What is the formula to compute the residue of f(z) at a simple pole z = z_0?",
         "Res(f, z_0) = lim_{z -> z_0} (z - z_0) * f(z)", "Res(f, z_0) = f(z_0)", "Res(f, z_0) = f'(z_0)", "Res(f, z_0) = 1 / f(z_0)", "A", "Easy")
    ]

    for q in em_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in em_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in em_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in em_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in em_u5: questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_all_sem3_questions():
    all_q = []
    all_q.extend(get_ai_questions())
    all_q.extend(get_prompt_eng_questions())
    all_q.extend(get_ds_questions())
    all_q.extend(get_discrete_maths_questions())
    all_q.extend(get_engg_maths3_questions())
    return all_q
