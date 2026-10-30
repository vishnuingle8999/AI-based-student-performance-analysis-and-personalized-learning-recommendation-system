# -*- coding: utf-8 -*-
"""
Builds the complete updated DBATU Syllabus CSV and Questions CSV.
Contains all 17 core DBATU AI&DS subjects across Semesters III, IV, V, VI,
with exactly 60 distinct questions per subject (1,020 total questions).
"""

import os
import sys
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database.questions_bank_sem3 import get_all_sem3_questions
from database.questions_bank_sem4 import get_all_sem4_questions
from database.questions_bank_sem5 import get_all_sem5_questions
from database.questions_bank_sem6 import get_all_sem6_questions

def build_syllabus_data():
    branch = "Artificial Intelligence & Data Science"
    rows = []

    # ==========================
    # SEMESTER III (Second Year)
    # ==========================
    y2 = "Second Year"
    sem3 = "Semester III"

    # 1. Engineering Mathematics-III
    s = "Engineering Mathematics-III"
    rows.append((branch, y2, sem3, s, "Unit 1: Laplace Transform", "Laplace Transforms & Properties", "Conditions for existence; Elementary transforms; Shifting properties; Transform of derivatives and integrals; Periodic functions; Dirac delta"))
    rows.append((branch, y2, sem3, s, "Unit 2: Inverse Laplace Transform", "Inverse Laplace & Differential Equations", "Partial fractions; Convolution theorem; Solving linear differential equations with constant coefficients"))
    rows.append((branch, y2, sem3, s, "Unit 3: Fourier Transform", "Fourier Integrals & Transforms", "Fourier integral theorem; Sine and Cosine integrals; Complex Fourier transform; Parseval's identity"))
    rows.append((branch, y2, sem3, s, "Unit 4: Partial Differential Equations and Their Applications", "PDEs, Wave Equation & Heat Equation", "Formation of PDEs; Lagrange's linear equations; Separation of variables; One-dimensional wave equation; One-dimensional heat flow equation"))
    rows.append((branch, y2, sem3, s, "Unit 5: Functions of Complex Variables", "Analytic Functions, Cauchy-Riemann & Residues", "Analytic functions; Cauchy-Riemann equations; Harmonic functions; Cauchy's integral theorem; Cauchy's integral formula; Residues and Residue theorem"))

    # 2. Discrete Mathematics
    s = "Discrete Mathematics"
    rows.append((branch, y2, sem3, s, "Unit 1: Propositional Logic and Predicates", "Propositional Logic & Quantifiers", "Propositions; Truth tables; Logical equivalences; Normal forms; Quantifiers; Rules of inference; Resolution; Fallacies"))
    rows.append((branch, y2, sem3, s, "Unit 2: Set Theory, Functions and Relations", "Sets, Functions, Relations & Posets", "Sets; Cartesian products; Injective/Surjective/Bijective functions; Relations; Equivalence classes; Partial ordering; Hasse diagrams; Topological sort"))
    rows.append((branch, y2, sem3, s, "Unit 3: Combinatorics and Recurrence Relations", "Permutations, Combinations & Recurrence", "Pigeonhole principle; Permutations & combinations; Inclusion-exclusion; Recurrence relations; Generating functions"))
    rows.append((branch, y2, sem3, s, "Unit 4: Graph Theory and Trees", "Graphs, Eulerian Paths & Spanning Trees", "Simple & bipartite graphs; Euler and Hamiltonian paths; Planar graphs; Trees; Spanning trees; Kruskal and Prim algorithms; Huffman coding"))
    rows.append((branch, y2, sem3, s, "Unit 5: Algebraic Structures and Morphism", "Groups, Rings, Fields & Lattices", "Binary operations; Semigroups; Monoids; Groups; Subgroups; Lagrange's theorem; Rings; Integral domains; Fields; Boolean algebra"))

    # 3. Data Structures
    s = "Data Structures"
    rows.append((branch, y2, sem3, s, "Unit 1: Data Types, Arrays and Hash Tables", "Arrays & Hash Tables", "ADT; Time and space complexity; Sparse matrices; Hash tables; Hash functions; Collision resolution; Chaining; Open addressing"))
    rows.append((branch, y2, sem3, s, "Unit 2: Stacks and Queues", "Stack & Queue Data Structures", "Stack and queue ADTs; Array & linked implementation; Circular queue; Infix to postfix conversion; Postfix evaluation; Recursion; Priority queue"))
    rows.append((branch, y2, sem3, s, "Unit 3: Linked Lists", "Linked List Implementations", "Singly linked list; Doubly linked list; Circular linked list; Insert/delete/reverse operations; Dynamic memory management; Garbage collection"))
    rows.append((branch, y2, sem3, s, "Unit 4: Trees and Graphs", "Trees, BST & Graph Traversals", "Binary trees; Binary Search Tree (BST); Inorder/Preorder/Postorder traversals; Heaps; AVL balanced trees; Graph representations; Dijkstra; Warshall"))
    rows.append((branch, y2, sem3, s, "Unit 5: Searching and Sorting", "Search Algorithms & Sorting Techniques", "Linear search; Binary search; Skip lists; Insertion sort; Selection sort; Merge sort; Quick sort; Radix sort; Heap sort"))

    # 4. Artificial Intelligence
    s = "Artificial Intelligence"
    rows.append((branch, y2, sem3, s, "Unit 1: Introduction to AI and Intelligent Agents", "AI Foundations & Intelligent Agents", "AI definitions and history; Rationality; PEAS environments; Agent architectures: reflex, model-based, goal-based, utility-based, learning agents"))
    rows.append((branch, y2, sem3, s, "Unit 2: Problem Solving by Searching and CSP", "Search Algorithms & Constraint Satisfaction", "Problem formulation; BFS; DFS; Uniform Cost Search; A* search; Admissible heuristics; Minimax; Alpha-Beta pruning; CSP; AC-3"))
    rows.append((branch, y2, sem3, s, "Unit 3: Knowledge Representation and Reasoning", "Logic & First-Order Inference", "Propositional logic; First-Order Logic; Unification; Forward chaining; Backward chaining; Resolution refutation; Ontologies; Semantic networks"))
    rows.append((branch, y2, sem3, s, "Unit 4: Probabilistic Reasoning and Planning", "Bayesian Networks & AI Planning", "Uncertainty; Bayesian networks; Conditional probability tables; Dempster-Shafer theory; Fuzzy logic; STRIPS/PDDL planning; Goal stack planning"))

    # 5. Prompt Engineering
    s = "Prompt Engineering"
    rows.append((branch, y2, sem3, s, "Unit 1: Introduction to Prompt Engineering & LLMs", "LLM Fundamentals & Tokenization", "Evolution of NLP to LLMs; Tokens & embeddings; Context windows; Prompting vs fine-tuning; Temperature and Top-P; System/User/Assistant roles"))
    rows.append((branch, y2, sem3, s, "Unit 2: Foundations of Prompt Design & Advanced Prompting", "Prompt Patterns & Chain-of-Thought", "Zero-shot and few-shot; Delimiters; Role prompting; Chain-of-Thought (CoT); ReAct framework; Multimodal prompts; LangChain prompt templates"))
    rows.append((branch, y2, sem3, s, "Unit 3: Prompt Engineering for Domain-Specific Tasks", "Domain-Specific Prompts & Code Generation", "Code generation and debugging; Conversational agents; Legal and medical prompts; Structured JSON outputs; Low-resource languages"))
    rows.append((branch, y2, sem3, s, "Unit 4: Prompt Safety, Bias, and Ethics", "Prompt Safety, Evaluation & Guardrails", "Hallucinations; Prompt injection; Jailbreak attacks; System prompt leakage; Evaluation: BLEU, ROUGE, BERTScore, LLM-as-a-judge; Function calling"))

    # ==========================
    # SEMESTER IV (Second Year)
    # ==========================
    sem4 = "Semester IV"

    # 1. Introduction to Operating Systems
    s = "Introduction to Operating Systems"
    rows.append((branch, y2, sem4, s, "Unit 1: Introduction and Operating System Structures", "Operating System Structures & System Calls", "OS definitions; Real-Time OS; Kernel vs user mode; System calls (fork, exec, wait); Monolithic vs Microkernel; PCB structure"))
    rows.append((branch, y2, sem4, s, "Unit 2: Processes and CPU Scheduling", "Processes, Threads & CPU Scheduling", "Process states; Context switching; Threads; CPU scheduling: FCFS, SJF/SRTF, Priority, Round Robin, Multilevel Feedback Queues; Zombie/orphan processes"))
    rows.append((branch, y2, sem4, s, "Unit 3: Process Synchronization and Deadlocks", "Synchronization & Deadlock Prevention", "Critical section problem; Race conditions; Semaphores; Mutex; Producer-consumer problem; Coffman deadlock conditions; Banker's algorithm"))
    rows.append((branch, y2, sem4, s, "Unit 4: Memory Management and Virtual Memory", "Memory Allocation & Page Replacement", "Logical vs physical addresses; MMU; Fragmentation; Paging; TLB; Page faults; Page replacement: FIFO, LRU, Optimal; Belady's anomaly; Thrashing"))
    rows.append((branch, y2, sem4, s, "Unit 5: File Management and Mass-Storage Structure", "File Systems & Disk Scheduling", "File concepts; Inodes; Contiguous/linked/indexed allocation; Disk scheduling: FCFS, SSTF, SCAN, C-SCAN; RAID levels; Swap space"))

    # 2. Data Analytics
    s = "Data Analytics"
    rows.append((branch, y2, sem4, s, "Unit 1: Statistical Data and Concepts", "Statistical Methods & Sampling", "Statistical methods and bias; Sampling methods; Data cleaning and imputation; Missing data; Outlier detection; Hypothesis testing; P-value; Type I/II errors"))
    rows.append((branch, y2, sem4, s, "Unit 2: Descriptive Statistics", "Measures of Central Tendency & Dispersion", "Mean; Median; Mode; Standard deviation; Variance; Skewness; Kurtosis; Quartiles; IQR; Coefficient of variation"))
    rows.append((branch, y2, sem4, s, "Unit 3: Data Transformation and Standardization", "Data Normalization & Transforms", "Box-Cox transformation; Yeo-Johnson; Min-Max scaling; Z-score standardization; Log transform; Logit transform; Discretization and binning"))
    rows.append((branch, y2, sem4, s, "Unit 4: Classical Tests and Contingency Tables", "Hypothesis Tests & Goodness of Fit", "Z-test; Student's t-test; Paired t-test; Welch's t-test; Goodness of fit: Shapiro-Wilk, Kolmogorov-Smirnov, Chi-square; Contingency tables; Fisher's exact test"))
    rows.append((branch, y2, sem4, s, "Unit 5: Analysis of Variance and Covariance", "ANOVA & Non-Parametric Variance Tests", "One-Way ANOVA; F-statistic; Homogeneity of variance (Levene's test); Two-Way ANOVA; Kruskal-Wallis non-parametric test; ANCOVA; MANOVA"))

    # 3. Probability and Statistics
    s = "Probability and Statistics"
    rows.append((branch, y2, sem4, s, "Unit 1: Probability Theory", "Probability Axioms & Bayes Theorem", "Axiomatic probability; Addition theorem; Conditional probability; Independence; Multiplication rule; Bayes theorem of inverse probability"))
    rows.append((branch, y2, sem4, s, "Unit 2: Random Variable and Mathematical Expectation", "Random Variables, PMF, PDF & Expectation", "Discrete & continuous random variables; PMF; PDF; CDF; Mathematical expectation E[X]; Variance Var(X); Joint distributions; Covariance"))
    rows.append((branch, y2, sem4, s, "Unit 3: Theoretical Probability Distributions", "Binomial, Poisson & Normal Distributions", "Binomial distribution; Poisson distribution; Normal distribution; Standard normal Z-score; Empirical 68-95-99.7 rule; Central Limit Theorem"))
    rows.append((branch, y2, sem4, s, "Unit 4: Correlation", "Correlation Coefficients & Probable Error", "Karl Pearson's correlation coefficient r; Monotonic relationships; Spearman's rank correlation rho; Probable error; Coefficient of determination"))
    rows.append((branch, y2, sem4, s, "Unit 5: Linear Regression Analysis", "Regression Lines & Properties", "Lines of regression Y on X and X on Y; Regression coefficients b_yx and b_xy; Intersection at means; Properties of regression lines; Ordinary least squares"))

    # 4. Full Stack Development
    s = "Full Stack Development"
    rows.append((branch, y2, sem4, s, "Unit 1: Bootstrap and Responsive Layouts", "Bootstrap Grids & Components", "Bootstrap 12-column grid; Breakpoints; Typography; Buttons; Alerts; Cards; Modals; Navigation bars; Mobile-first responsive design"))
    rows.append((branch, y2, sem4, s, "Unit 2: JavaScript Fundamentals and DOM", "JavaScript Language & DOM Manipulation", "Variables var/let/const; Scopes; Hoisting; Strict equality; DOM selection querySelector; Event listeners; Event bubbling; Form validation; JSON"))
    rows.append((branch, y2, sem4, s, "Unit 3: jQuery Events and AJAX", "jQuery Library & Asynchronous AJAX", "jQuery syntax $(selector); Document ready; Effects and animations; DOM traversal; Asynchronous AJAX $.ajax(); REST GET/POST requests"))
    rows.append((branch, y2, sem4, s, "Unit 4: PHP and MySQL Integration", "Server-Side PHP & Database Operations", "PHP syntax; Superglobals $_POST/$_GET; PDO database connection; Prepared statements; SQL injection prevention; Sessions and cookies"))
    rows.append((branch, y2, sem4, s, "Unit 5: MVC with Laravel Framework", "MVC Pattern & Laravel Architecture", "Model-View-Controller architecture; Artisan CLI; Composer; Routing routes/web.php; Blade templates; Eloquent ORM; Migrations; CSRF"))

    # ==========================
    # SEMESTER V (Third Year)
    # ==========================
    y3 = "Third Year"
    sem5 = "Semester V"

    # 1. Machine Learning
    s = "Machine Learning"
    rows.append((branch, y3, sem5, s, "Unit 1: Foundations of Machine Learning & Supervised Learning", "Linear Regression & Inductive Bias", "Hypothesis space; Inductive bias; Cost functions; Gradient descent; Cross-validation; Decision trees; Pruning; k-NN; PCA"))
    rows.append((branch, y3, sem5, s, "Unit 2: Probabilistic Learning, Bayes & Support Vector Machines", "Bayes Theorem & Logistic Regression", "Bayes rule; Maximum Likelihood; Naive Bayes; Log-odds; Sigmoid activation; SVM; Margin maximization; Support vectors; Kernel trick"))
    rows.append((branch, y3, sem5, s, "Unit 3: Perceptrons, Neural Networks & Backpropagation", "Artificial Neurons & Perceptron Learning", "McCulloch-Pitts neuron; Perceptron convergence; Linear separability; XOR limitation; Multilayer networks; Backpropagation; Activation functions"))
    rows.append((branch, y3, sem5, s, "Unit 4: Computational Learning Theory & Ensembles", "PAC Learning & VC Dimension", "PAC learnability; Sample complexity; VC dimension; Bagging; Random Forests; AdaBoost; Gradient Boosting; Bias-variance tradeoff"))
    rows.append((branch, y3, sem5, s, "Unit 5: Clustering & Unsupervised Learning", "K-Means & Hierarchical Clustering", "K-means algorithm; K-means++; Elbow method; Silhouette score; Agglomerative clustering; Dendrograms; GMM; EM algorithm"))

    # 2. Object Oriented Programming in Java
    s = "Object Oriented Programming in Java"
    rows.append((branch, y3, sem5, s, "Unit 1: Introduction to Object Technology & Java Basics", "Java Platform & Fundamentals", "JVM; JDK; JRE; Primitive data types; Scanner input; Type casting; Control structures; Loops: while, for, do-while; Sentinel iteration"))
    rows.append((branch, y3, sem5, s, "Unit 2: Methods, Arrays and Strings", "Methods & Stack Execution", "Static vs instance methods; Method call stack; Method overloading; Arrays 1D/2D; ArrayList; String immutability; StringBuilder; Regular expressions"))
    rows.append((branch, y3, sem5, s, "Unit 3: Classes, Objects & OOP Principles", "Encapsulation & Constructors", "Classes & objects; Constructors; this keyword; Access modifiers; Composition; Inheritance; super keyword; Polymorphism; Dynamic dispatch; Interfaces"))
    rows.append((branch, y3, sem5, s, "Unit 4: Exception Handling, Collections & File Processing", "Exception Handling Mechanism", "Throwable hierarchy; Checked vs unchecked exceptions; try-catch-finally; try-with-resources; Collections framework: List, Set, Map; File I/O; NIO"))
    rows.append((branch, y3, sem5, s, "Unit 5: Advanced Java Concepts & JDBC", "Functional Programming & Streams API", "Lambda expressions; Functional interfaces; Streams API filter/map/reduce; Generics; Wildcards; JDBC drivers; PreparedStatement; Transactions"))

    # 3. Cloud and Distributed AI Systems
    s = "Cloud and Distributed AI Systems"
    rows.append((branch, y3, sem5, s, "Unit 1: Introduction to Cloud & Virtualization", "Cloud Computing Fundamentals", "NIST cloud definition; Essential characteristics; Virtualization taxonomy; Type-1 vs Type-2 hypervisors; Full vs para-virtualization; Containers"))
    rows.append((branch, y3, sem5, s, "Unit 2: Cloud Architecture & Enterprise Services", "Cloud Service & Deployment Models", "IaaS; PaaS; SaaS; Public/Private/Hybrid clouds; SLAs; Cloud economics; Storage-as-a-Service (S3); DBaaS; Auto-scaling; Capacity planning"))
    rows.append((branch, y3, sem5, s, "Unit 3: Aneka Cloud Platform Framework", "Aneka Container Architecture & Platform Abstraction", "Aneka framework; PAL layer; Fabric & Foundation services; Application services; Programming models: Task, Thread, MapReduce; Hybrid cloud"))
    rows.append((branch, y3, sem5, s, "Unit 4: Distributed AI Systems & GPU Computing", "Distributed AI Architecture & Compute Infrastructure", "Need for Distributed AI; CPU vs GPU architecture; CUDA execution model; Tensor cores; Data/Model/Pipeline parallelism; Ring All-Reduce"))
    rows.append((branch, y3, sem5, s, "Unit 5: Distributed Training of AI Models (DDP & FSDP)", "PyTorch Distributed Data Parallel (DDP)", "torch.distributed; DDP workflow; DistributedSampler; GPU memory constraints; Mixed precision (AMP); ZeRO memory stages; PyTorch FSDP"))

    # 4. Data Engineering and Big Data Systems
    s = "Data Engineering and Big Data Systems"
    rows.append((branch, y3, sem5, s, "Unit 1: Fundamentals of Data Engineering & Big Data", "Big Data Dimensions & Data Engineering Lifecycle", "5 Vs of Big Data; Data engineering lifecycle; Modern data stack; Batch vs stream processing; Lambda and Kappa architectures; Data engineer role"))
    rows.append((branch, y3, sem5, s, "Unit 2: Distributed Storage & Processing Frameworks (Hadoop & Spark)", "Hadoop Ecosystem & HDFS Architecture", "Hadoop HDFS; NameNode and DataNodes; Block replication; MapReduce Map/Shuffle/Reduce; Apache Spark RDDs; Lazy evaluation; Catalyst optimizer"))
    rows.append((branch, y3, sem5, s, "Unit 3: Data Warehousing, Data Integration & Lakehouse", "Dimensional Modeling & Data Warehousing", "OLTP vs OLAP; Fact & dimension tables; Star vs snowflake schema; SCD Type 2; Data Marts; ETL vs ELT; Data Lake vs Lakehouse; Delta Lake"))
    rows.append((branch, y3, sem5, s, "Unit 4: Real-Time Data Engineering & Kafka Streaming", "Event Streaming Fundamentals & Message Brokers", "Event-driven architecture; Pub-sub messaging; Apache Kafka brokers, topics, partitions, offsets; Consumer groups; Tumbling/sliding windows"))
    rows.append((branch, y3, sem5, s, "Unit 5: Data Governance, Security & Workflow Orchestration", "Apache Airflow & Workflow Orchestration", "Airflow DAGs, operators, tasks, sensors; Data lineage (Apache Atlas); Data security & RBAC; Data masking; Data Mesh; Data observability"))

    # 5. Vector Databases
    s = "Vector Databases"
    rows.append((branch, y3, sem5, s, "Unit 1: Fundamentals of Vector Databases & Embeddings", "Vector Representations & Distance Metrics", "Dense vector embeddings; Semantic search; Distance metrics: Cosine similarity, Euclidean distance, Dot product; Relational vs vector DBs"))
    rows.append((branch, y3, sem5, s, "Unit 2: Vector Embeddings & Data Preparation", "Embedding Generation & Transformer Models", "Word2Vec; Sentence-BERT; CLIP multimodal embeddings; Dimensionality reduction (PCA, UMAP); Text chunking strategies; Metadata payloads"))
    rows.append((branch, y3, sem5, s, "Unit 3: Vector Indexing & Approximate Nearest Neighbor (ANN)", "Exact vs Approximate Nearest Neighbor Search", "Exact k-NN vs ANN trade-off; Recall@K; Inverted File Index (IVF); Product Quantization (PQ); HNSW graphs; Hybrid search; Pre/post filtering"))
    rows.append((branch, y3, sem5, s, "Unit 4: Vector Database Systems & Architecture", "Vector Database Ecosystem (Milvus, Pinecone, FAISS)", "FAISS library; Milvus distributed architecture; Pinecone SaaS; Chroma; Data ingestion pipelines; Sharding and high availability; pgvector"))
    rows.append((branch, y3, sem5, s, "Unit 5: Retrieval-Augmented Generation (RAG) & Emerging Trends", "RAG Pipeline Architecture & Context Injection", "RAG motivation and workflow; Document chunking & overlap; Cross-encoder rerankers; Ragas evaluation (Faithfulness); Prompt injection; GraphRAG"))

    # ==========================
    # SEMESTER VI (Third Year)
    # ==========================
    sem6 = "Semester VI"

    # 1. Deep Learning
    s = "Deep Learning"
    rows.append((branch, y3, sem6, s, "Unit 1: Traditional Machine Learning and Artificial Neural Networks", "ANN Architectures & Gradient Descent", "Biological vs artificial neuron; Perceptron; XOR limitation; Backpropagation; Vanishing gradients; ReLU; Leaky ReLU; Softmax; Adam optimizer"))
    rows.append((branch, y3, sem6, s, "Unit 2: Deep Architecture and Convolutional Neural Networks (CNN)", "CNNs, Convolutions & Vision Architectures", "Local receptive fields; Weight sharing; 2D Convolutions; Pooling; AlexNet; VGG-16; ResNet skip connections; Batch normalization; Dropout; YOLO; U-Net"))
    rows.append((branch, y3, sem6, s, "Unit 3: Deep Sequence Models (RNN, GRU, LSTM)", "RNNs, LSTMs & Sequence Modeling", "Recurrent feedback; BPTT; Vanishing gradients in RNNs; LSTM Forget/Input/Output gates; Cell state; GRU; BiLSTM; Seq2Seq; Attention mechanism"))
    rows.append((branch, y3, sem6, s, "Unit 4: Deep Unsupervised Learning, GANs & Transfer Learning", "Autoencoders, GANs & Transfer Learning", "Autoencoders; VAEs; Latent space; GAN Generator and Discriminator; Mode collapse; Transfer learning; Fine-tuning; Data augmentation; Diffusion models"))
    rows.append((branch, y3, sem6, s, "Unit 5: Responsible AI, MLOps and Industrial Applications", "Explainable AI, MLOps & Model Deployment", "Explainable AI (LIME, SHAP); Algorithmic bias; Concept drift; MLflow; Model quantization (FP32 to INT8); ONNX Runtime; Canary deployment; Feature stores"))

    # 2. Natural Language Processing
    s = "Natural Language Processing"
    rows.append((branch, y3, sem6, s, "Unit 1: Lexical Analysis and Morphology", "Morphology & Language Modeling", "Morphology fundamentals; Stemming vs lemmatization; Finite State Transducers; POS tagging; N-gram language models; Perplexity; HMMs; Viterbi algorithm"))
    rows.append((branch, y3, sem6, s, "Unit 2: Speech Processing & Acoustic Models", "Speech Processing & Audio Recognition", "Vocal articulation; Phonemes; MFCC acoustic features; Mel scale; Speech segmentation; Text-to-Speech (TTS); WaveNet; Acoustic and Language models"))
    rows.append((branch, y3, sem6, s, "Unit 3: Parsing Algorithms & Named Entity Recognition", "Syntactic Parsing & Sequence Labeling", "Context-Free Grammars; CYK chart parser; Earley parser; Dependency parsing; Named Entity Recognition (NER); BIO tagging; Conditional Random Fields (CRF)"))
    rows.append((branch, y3, sem6, s, "Unit 4: Lexical Knowledge Networks & Word Sense Disambiguation", "WordNet, WSD & Coreference", "WordNet synsets; Hypernymy/Hyponymy; Meronymy; Word Sense Disambiguation (WSD); Lesk algorithm; Coreference resolution; Anaphora; Semantic roles"))
    rows.append((branch, y3, sem6, s, "Unit 5: NLP Applications & Modern Architectures", "Transformers, Sentiment & Machine Translation", "Transformer architecture; Scaled dot-product self-attention; Multi-head attention; BERT masked language modeling; Sentiment analysis; Neural Machine Translation; BLEU"))

    # 3. Fundamental Edge AI
    s = "Fundamental Edge AI"
    rows.append((branch, y3, sem6, s, "Unit 1: Fundamentals of Heterogeneous Systems & SoC", "SoC Architecture & Inter-Processor Communication", "System-on-Chip (SoC); Application processors vs Microcontrollers; Heterogeneous systems; Inter-Processor Communication (IPC); OpenAMP; Zero-copy frame buffers"))
    rows.append((branch, y3, sem6, s, "Unit 2: Hardware Abstraction Layers (HAL) & Power Management", "HAL, MMIO & Power-Aware Scheduling", "Hardware Abstraction Layer (HAL); Memory-Mapped I/O (MMIO); Pin multiplexing; Power gating; DVFS; Wake-on-interrupt; Watchdog timers; Deep sleep; DMA; I2C/SPI"))
    rows.append((branch, y3, sem6, s, "Unit 3: Basics of Neural Hardware Acceleration & Vision Processing", "SIMD Acceleration & MIPI-CSI Vision", "SIMD parallelism; Vectorization; ARM NEON; MIPI-CSI camera interface; Image Signal Processor (ISP); YUV color formats; OpenCV; Fused Multiply-Accumulate (FMA)"))
    rows.append((branch, y3, sem6, s, "Unit 4: Specialized Accelerators (DSPs and NPUs)", "DSPs, NPUs & Edge Acceleration", "Neural Processing Units (NPUs); TOPS and TOPS/Watt efficiency; Digital Signal Processors (DSPs); Google Edge TPU; NVIDIA Jetson; Neural graph compilers; Kernel fusion"))
    rows.append((branch, y3, sem6, s, "Unit 5: Model Compression & Quantization (FP32 to INT8)", "Quantization, Pruning & TinyML Deployment", "Model compression; INT8 Post-Training Quantization (PTQ); Quantization-Aware Training (QAT); Structured and unstructured pruning; Knowledge distillation; TensorFlow Lite Micro; TinyML"))

    return rows


def generate_all_files():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)

    syllabus_csv_path = os.path.join(data_dir, 'syllabus.csv')
    questions_csv_path = os.path.join(data_dir, 'questions.csv')

    # 1. Write syllabus.csv
    syllabus_rows = build_syllabus_data()
    print(f"Writing {len(syllabus_rows)} syllabus rows to {syllabus_csv_path}...")
    with open(syllabus_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['branch', 'year', 'semester', 'subject', 'unit', 'topic', 'subtopic'])
        for r in syllabus_rows:
            writer.writerow(r)

    # 2. Collect all 1020 questions
    all_questions = []
    print("Collecting Semester III questions...")
    all_questions.extend(get_all_sem3_questions())
    print("Collecting Semester IV questions...")
    all_questions.extend(get_all_sem4_questions())
    print("Collecting Semester V questions...")
    all_questions.extend(get_all_sem5_questions())
    print("Collecting Semester VI questions...")
    all_questions.extend(get_all_sem6_questions())

    print(f"Total questions collected: {len(all_questions)}")

    # 3. Write questions.csv
    print(f"Writing {len(all_questions)} questions to {questions_csv_path}...")
    with open(questions_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['student_id', 'branch', 'year', 'semester', 'subject', 'unit', 'topic', 'question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'difficulty'])
        for idx, q in enumerate(all_questions, start=1):
            # q: (branch, year, sem, sub, unit, topic, question_text, opt_a, opt_b, opt_c, opt_d, correct, diff)
            student_id = "S001"
            writer.writerow([student_id, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11], q[12]])

    print("Generation complete! All syllabus and question records generated successfully.")

if __name__ == '__main__':
    generate_all_files()
