import json
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Curated reference links and topic-specific learning materials for the 18 topics
CURATED_RESOURCES = {
    "Data Preprocessing & Cleaning": {
        "beginner": [
            {"title": "Handling Missing Values & Imputation in Python", "type": "Article", "url": "https://scikit-learn.org/stable/modules/impute.html"},
            {"title": "Outlier Detection using IQR & Z-score", "type": "Guide", "url": "https://pandas.pydata.org/docs/user_guide/index.html"}
        ],
        "intermediate": [
            {"title": "Robust Scaling & Transformation Pipelines", "type": "Tutorial", "url": "https://scikit-learn.org/stable/modules/preprocessing.html"}
        ],
        "advanced": [
            {"title": "Iterative Imputer (MICE) & Domain-Specific Cleaning at Scale", "type": "Documentation", "url": "https://scikit-learn.org/stable/modules/impute.html#iterative-imputer"}
        ]
    },
    "Pandas DataFrames & Aggregations": {
        "beginner": [
            {"title": "10 Minutes to Pandas Official Guide", "type": "Tutorial", "url": "https://pandas.pydata.org/docs/user_guide/10min.html"},
            {"title": "Indexing and Selecting Data with loc & iloc", "type": "Article", "url": "https://pandas.pydata.org/docs/user_guide/indexing.html"}
        ],
        "intermediate": [
            {"title": "Mastering Pandas GroupBy & Multi-index Aggregations", "type": "Guide", "url": "https://pandas.pydata.org/docs/user_guide/groupby.html"}
        ],
        "advanced": [
            {"title": "High-Performance Vectorization & Memory Optimization in Pandas", "type": "Paper", "url": "https://pandas.pydata.org/docs/user_guide/scale.html"}
        ]
    },
    "Data Visualization with Matplotlib & Seaborn": {
        "beginner": [
            {"title": "Matplotlib Pyplot Basics & Figure Anatomy", "type": "Guide", "url": "https://matplotlib.org/stable/tutorials/introductory/quick_start.html"},
            {"title": "Understanding Boxplots & Histograms", "type": "Article", "url": "https://seaborn.pydata.org/tutorial/distributions.html"}
        ],
        "intermediate": [
            {"title": "Seaborn Correlation Heatmaps & PairPlots", "type": "Tutorial", "url": "https://seaborn.pydata.org/tutorial/relational.html"}
        ],
        "advanced": [
            {"title": "Interactive Multi-axis Dashboards & FacetGrids", "type": "Documentation", "url": "https://seaborn.pydata.org/generated/seaborn.FacetGrid.html"}
        ]
    },
    "Search Algorithms & Heuristics": {
        "beginner": [
            {"title": "BFS & DFS Graph Traversals Explained", "type": "Tutorial", "url": "https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/"},
            {"title": "Introduction to State Space Search in AI", "type": "Article", "url": "https://en.wikipedia.org/wiki/State_space_search"}
        ],
        "intermediate": [
            {"title": "A* Search Algorithm and Admissible Heuristics", "type": "Guide", "url": "https://www.geeksforgeeks.org/a-search-algorithm/"}
        ],
        "advanced": [
            {"title": "Consistent Heuristics & IDA* Memory-Bounded Search", "type": "Paper", "url": "https://en.wikipedia.org/wiki/Iterative_deepening_A*"}
        ]
    },
    "Propositional & First-Order Logic": {
        "beginner": [
            {"title": "Truth Tables & Propositional Connectives", "type": "Article", "url": "https://plato.stanford.edu/entries/logic-classical/"},
            {"title": "Inference Rules: Modus Ponens & Modus Tollens", "type": "Tutorial", "url": "https://www.geeksforgeeks.org/rules-of-inference-in-propositional-logic/"}
        ],
        "intermediate": [
            {"title": "Converting to Conjunctive Normal Form (CNF) & Resolution", "type": "Guide", "url": "https://www.cs.cmu.edu/~avrim/ML09/lectures/lecture_inference.pdf"}
        ],
        "advanced": [
            {"title": "First-Order Logic Resolution Refutation & Unification", "type": "Documentation", "url": "https://en.wikipedia.org/wiki/Unification_(computer_science)"}
        ]
    },
    "Expert Systems & Rule Engines": {
        "beginner": [
            {"title": "Architecture of an Expert System (Inference Engine & KB)", "type": "Article", "url": "https://www.geeksforgeeks.org/expert-systems-in-artificial-intelligence/"},
            {"title": "Forward Chaining vs Backward Chaining", "type": "Guide", "url": "https://www.javatpoint.com/forward-chaining-and-backward-chaining-in-ai"}
        ],
        "intermediate": [
            {"title": "Conflict Resolution Strategies in Production Rules", "type": "Tutorial", "url": "https://en.wikipedia.org/wiki/Conflict_resolution_(logic)"}
        ],
        "advanced": [
            {"title": "Rete Algorithm for Fast Rule Matching", "type": "Paper", "url": "https://en.wikipedia.org/wiki/Rete_algorithm"}
        ]
    },
    "Linear & Logistic Regression": {
        "beginner": [
            {"title": "Linear Regression and Mean Squared Error Loss", "type": "Tutorial", "url": "https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares"},
            {"title": "Sigmoid Activation & Log-Odds Intuition", "type": "Guide", "url": "https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression"}
        ],
        "intermediate": [
            {"title": "Gradient Descent Optimization and Learning Rate Tuning", "type": "Article", "url": "https://ml-cheatsheet.readthedocs.io/en/latest/gradient_descent.html"}
        ],
        "advanced": [
            {"title": "Regularization with Lasso (L1) and Ridge (L2)", "type": "Paper", "url": "https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification"}
        ]
    },
    "Decision Trees & Random Forests": {
        "beginner": [
            {"title": "Decision Tree Splits: Entropy vs Gini Impurity", "type": "Guide", "url": "https://scikit-learn.org/stable/modules/tree.html"},
            {"title": "Understanding Bagging and Ensemble Wisdom", "type": "Tutorial", "url": "https://www.geeksforgeeks.org/bagging-vs-boosting-in-machine-learning/"}
        ],
        "intermediate": [
            {"title": "Random Forest Hyperparameters: n_estimators & max_depth", "type": "Article", "url": "https://scikit-learn.org/stable/modules/ensemble.html#forest"}
        ],
        "advanced": [
            {"title": "Feature Importance Calculation (MDI vs Permutation Importance)", "type": "Documentation", "url": "https://scikit-learn.org/stable/modules/permutation_importance.html"}
        ]
    },
    "Performance Metrics & Cross-Validation": {
        "beginner": [
            {"title": "Confusion Matrix: TP, FP, TN, FN Explained", "type": "Article", "url": "https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix"},
            {"title": "Precision, Recall, and the F1-Score Trade-off", "type": "Guide", "url": "https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics"}
        ],
        "intermediate": [
            {"title": "K-Fold and Stratified Cross-Validation Strategies", "type": "Tutorial", "url": "https://scikit-learn.org/stable/modules/cross_validation.html"}
        ],
        "advanced": [
            {"title": "ROC-AUC Curves and Precision-Recall Curves for Imbalanced Data", "type": "Paper", "url": "https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics"}
        ]
    },
    "Normalization & Functional Dependency": {
        "beginner": [
            {"title": "Relational Schema Design & Anomalies (Insert/Update/Delete)", "type": "Guide", "url": "https://www.geeksforgeeks.org/database-normalization-introduction/"},
            {"title": "First (1NF) and Second (2NF) Normal Forms", "type": "Article", "url": "https://www.geeksforgeeks.org/normal-forms-in-dbms/"}
        ],
        "intermediate": [
            {"title": "Third Normal Form (3NF) vs Boyce-Codd (BCNF)", "type": "Tutorial", "url": "https://www.javatpoint.com/dbms-bcnf"}
        ],
        "advanced": [
            {"title": "Armstrong's Axioms & Minimal Cover Calculation", "type": "Documentation", "url": "https://en.wikipedia.org/wiki/Armstrong%27s_axioms"}
        ]
    },
    "SQL Joins & Subqueries": {
        "beginner": [
            {"title": "Visual SQL Joins: Inner, Left, Right, and Full", "type": "Tutorial", "url": "https://www.w3schools.com/sql/sql_join.asp"},
            {"title": "Aggregations with GROUP BY and HAVING Clauses", "type": "Guide", "url": "https://www.w3schools.com/sql/sql_having.asp"}
        ],
        "intermediate": [
            {"title": "Subqueries vs Correlated Subqueries Explained", "type": "Article", "url": "https://www.geeksforgeeks.org/sql-correlated-subqueries/"}
        ],
        "advanced": [
            {"title": "EXPLAIN Query Execution Plans & B-Tree Indexing Optimization", "type": "Documentation", "url": "https://use-the-index-luke.com/"}
        ]
    },
    "NoSQL & Document Databases": {
        "beginner": [
            {"title": "RDBMS vs NoSQL: When and Why to Choose NoSQL", "type": "Article", "url": "https://www.mongodb.com/nosql-explained"},
            {"title": "JSON & BSON Document Data Model in MongoDB", "type": "Tutorial", "url": "https://www.mongodb.com/basics"}
        ],
        "intermediate": [
            {"title": "Understanding the CAP Theorem (Consistency, Availability, Partition)", "type": "Guide", "url": "https://en.wikipedia.org/wiki/CAP_theorem"}
        ],
        "advanced": [
            {"title": "Sharding, Replication Sets, and Eventual Consistency", "type": "Paper", "url": "https://www.mongodb.com/docs/manual/replication/"}
        ]
    },
    "Perceptrons & Multi-Layer Networks": {
        "beginner": [
            {"title": "The McCulloch-Pitts Neuron & Single Perceptron", "type": "Tutorial", "url": "https://en.wikipedia.org/wiki/Perceptron"},
            {"title": "Why Perceptrons Cannot Solve Non-Linear XOR Problems", "type": "Article", "url": "https://towardsdatascience.com/how-neural-networks-solve-the-xor-problem-59763136bdd7"}
        ],
        "intermediate": [
            {"title": "Multi-Layer Perceptrons (MLP) and Forward Propagation", "type": "Guide", "url": "https://cs231n.github.io/neural-networks-1/"}
        ],
        "advanced": [
            {"title": "Universal Approximation Theorem and Deep Representations", "type": "Paper", "url": "https://en.wikipedia.org/wiki/Universal_approximation_theorem"}
        ]
    },
    "Backpropagation & Gradient Descent": {
        "beginner": [
            {"title": "Calculus Behind Neural Networks: The Chain Rule", "type": "Tutorial", "url": "https://ml-cheatsheet.readthedocs.io/en/latest/backpropagation.html"},
            {"title": "Loss Surfaces and the Vanishing Gradient Problem", "type": "Article", "url": "https://en.wikipedia.org/wiki/Vanishing_gradient_problem"}
        ],
        "intermediate": [
            {"title": "Optimizers Compared: SGD, Momentum, RMSprop, and Adam", "type": "Guide", "url": "https://ruder.io/optimizing-gradient-descent/"}
        ],
        "advanced": [
            {"title": "Computational Graphs and Automatic Differentiation (Autograd)", "type": "Documentation", "url": "https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html"}
        ]
    },
    "Activation Functions & Overfitting": {
        "beginner": [
            {"title": "Activation Functions: Sigmoid, Tanh, ReLU, and Leaky ReLU", "type": "Article", "url": "https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6"},
            {"title": "Softmax Function for Multi-Class Probabilities", "type": "Guide", "url": "https://en.wikipedia.org/wiki/Softmax_function"}
        ],
        "intermediate": [
            {"title": "Dropout Regularization: Training Thinned Networks", "type": "Tutorial", "url": "https://jmlr.org/papers/v15/srivastava14a.html"}
        ],
        "advanced": [
            {"title": "Batch Normalization & Layer Normalization Dynamics", "type": "Paper", "url": "https://arxiv.org/abs/1502.03167"}
        ]
    },
    "Text Normalization & Tokenization": {
        "beginner": [
            {"title": "Word and Sentence Tokenization in Python NLTK", "type": "Tutorial", "url": "https://www.nltk.org/book/ch03.html"},
            {"title": "Stemming vs Lemmatization: Porter Stemmer vs WordNet", "type": "Article", "url": "https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html"}
        ],
        "intermediate": [
            {"title": "Stop Words Removal and Regex Pattern Cleaning", "type": "Guide", "url": "https://www.nltk.org/"}
        ],
        "advanced": [
            {"title": "Subword Tokenization: Byte-Pair Encoding (BPE) & WordPiece", "type": "Paper", "url": "https://huggingface.co/docs/transformers/tokenizer_summary"}
        ]
    },
    "Vector Space Models & TF-IDF": {
        "beginner": [
            {"title": "Bag of Words (BoW) Representation Explained", "type": "Article", "url": "https://scikit-learn.org/stable/modules/feature_extraction.html#the-bag-of-words-representation"},
            {"title": "Term Frequency (TF) and Inverse Document Frequency (IDF)", "type": "Guide", "url": "https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting"}
        ],
        "intermediate": [
            {"title": "Using TfidfVectorizer in Scikit-Learn with N-grams", "type": "Tutorial", "url": "https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html"}
        ],
        "advanced": [
            {"title": "Cosine Similarity and Dense Embeddings (Word2Vec / FastText)", "type": "Paper", "url": "https://radimrehurek.com/gensim/models/word2vec.html"}
        ]
    },
    "Sentiment Analysis & Naive Bayes": {
        "beginner": [
            {"title": "Introduction to Sentiment Polarity Classification", "type": "Tutorial", "url": "https://en.wikipedia.org/wiki/Sentiment_analysis"},
            {"title": "Multinomial Naive Bayes Classifier in NLP", "type": "Article", "url": "https://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes"}
        ],
        "intermediate": [
            {"title": "Laplace Smoothing and Handling Zero Frequencies", "type": "Guide", "url": "https://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html"}
        ],
        "advanced": [
            {"title": "Aspect-Based Sentiment Analysis & Transformer Finetuning", "type": "Paper", "url": "https://huggingface.co/blog/sentiment-analysis-python"}
        ]
    },
    # DBATU AI&DS Semester V Curriculum Resources
    "Linear Regression & Inductive Bias": {
        "beginner": [
            {"title": "Foundations of Supervised Learning & Linear Regression", "type": "Guide", "url": "https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares"},
            {"title": "Gradient Descent Optimization & Cost Surfaces", "type": "Article", "url": "https://ml-cheatsheet.readthedocs.io/en/latest/gradient_descent.html"}
        ],
        "intermediate": [
            {"title": "Inductive Bias, Hypothesis Space & Cross-Validation in ML", "type": "Tutorial", "url": "https://scikit-learn.org/stable/modules/cross_validation.html"}
        ],
        "advanced": [
            {"title": "Regularization Techniques (Lasso, Ridge & ElasticNet)", "type": "Documentation", "url": "https://scikit-learn.org/stable/modules/linear_model.html#elastic-net"}
        ]
    },
    "Bayes Theorem & Logistic Regression": {
        "beginner": [
            {"title": "Bayes Rule & Maximum Likelihood Estimation", "type": "Guide", "url": "https://en.wikipedia.org/wiki/Maximum_likelihood_estimation"},
            {"title": "Logistic Regression & Sigmoid Activation Function", "type": "Tutorial", "url": "https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression"}
        ],
        "intermediate": [
            {"title": "Support Vector Machines (SVM) & Maximum Margin Hyperplanes", "type": "Article", "url": "https://scikit-learn.org/stable/modules/svm.html"}
        ],
        "advanced": [
            {"title": "Mercer Theorem & The Kernel Trick (RBF, Polynomial)", "type": "Paper", "url": "https://en.wikipedia.org/wiki/Kernel_method"}
        ]
    },
    "Artificial Neurons & Perceptron Learning": {
        "beginner": [
            {"title": "McCulloch-Pitts Neuron & Single Layer Perceptrons", "type": "Tutorial", "url": "https://en.wikipedia.org/wiki/Perceptron"},
            {"title": "Linear Separability & The XOR Problem", "type": "Article", "url": "https://towardsdatascience.com/how-neural-networks-solve-the-xor-problem-59763136bdd7"}
        ],
        "intermediate": [
            {"title": "Multilayer Perceptrons & Backpropagation Calculus", "type": "Guide", "url": "https://cs231n.github.io/neural-networks-1/"}
        ],
        "advanced": [
            {"title": "Modern Activation Functions (ReLU, Leaky ReLU, GELU, Swish)", "type": "Documentation", "url": "https://pytorch.org/docs/stable/nn.html#non-linear-activations-weighted-sum-nonlinearity"}
        ]
    },
    "PAC Learning & VC Dimension": {
        "beginner": [
            {"title": "Introduction to Computational Learning Theory", "type": "Article", "url": "https://en.wikipedia.org/wiki/Computational_learning_theory"},
            {"title": "Understanding the Bias-Variance Tradeoff", "type": "Guide", "url": "https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html"}
        ],
        "intermediate": [
            {"title": "Vapnik-Chervonenkis (VC) Dimension & Sample Complexity", "type": "Tutorial", "url": "https://en.wikipedia.org/wiki/VC_dimension"}
        ],
        "advanced": [
            {"title": "Ensemble Methods: AdaBoost, Gradient Boosting & XGBoost", "type": "Paper", "url": "https://scikit-learn.org/stable/modules/ensemble.html"}
        ]
    },
    "K-Means & Hierarchical Clustering": {
        "beginner": [
            {"title": "K-Means Clustering & Voronoi Partitions", "type": "Tutorial", "url": "https://scikit-learn.org/stable/modules/clustering.html#k-means"},
            {"title": "Determining Optimal K with the Elbow Method & Silhouette Score", "type": "Guide", "url": "https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html"}
        ],
        "intermediate": [
            {"title": "Agglomerative Hierarchical Clustering & Dendrograms", "type": "Article", "url": "https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering"}
        ],
        "advanced": [
            {"title": "Gaussian Mixture Models (GMM) & Expectation-Maximization", "type": "Documentation", "url": "https://scikit-learn.org/stable/modules/mixture.html"}
        ]
    },
    "Java Platform & Fundamentals": {
        "beginner": [
            {"title": "Java Virtual Machine (JVM) Architecture & Execution", "type": "Guide", "url": "https://docs.oracle.com/javase/tutorial/getStarted/intro/definition.html"},
            {"title": "Primitive Types, Operators & Control Flow in Java", "type": "Tutorial", "url": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/index.html"}
        ],
        "intermediate": [
            {"title": "Memory Management: Stack vs Heap in Java", "type": "Article", "url": "https://www.baeldung.com/java-stack-heap"}
        ],
        "advanced": [
            {"title": "JVM Garbage Collection Algorithms (G1, ZGC)", "type": "Documentation", "url": "https://docs.oracle.com/en/java/javase/17/gctuning/"}
        ]
    },
    "Encapsulation & Constructors": {
        "beginner": [
            {"title": "Object-Oriented Programming: Classes, Objects & Constructors", "type": "Guide", "url": "https://docs.oracle.com/javase/tutorial/java/javaOO/index.html"},
            {"title": "Inheritance, Polymorphism & Method Overriding", "type": "Tutorial", "url": "https://docs.oracle.com/javase/tutorial/java/IandI/index.html"}
        ],
        "intermediate": [
            {"title": "Abstract Classes vs Interfaces & Default Methods", "type": "Article", "url": "https://www.baeldung.com/java-abstract-class-vs-interface"}
        ],
        "advanced": [
            {"title": "Java Design Patterns: Factory, Singleton & Builder", "type": "Documentation", "url": "https://refactoring.guru/design-patterns/java"}
        ]
    },
    "Exception Handling Mechanism": {
        "beginner": [
            {"title": "Throwable Hierarchy: Checked vs Unchecked Exceptions", "type": "Tutorial", "url": "https://docs.oracle.com/javase/tutorial/essential/exceptions/"},
            {"title": "Try-Catch-Finally Blocks & Exception Propagation", "type": "Guide", "url": "https://www.baeldung.com/java-exceptions"}
        ],
        "intermediate": [
            {"title": "Java Collections Framework: List, Set, Map Implementations", "type": "Article", "url": "https://docs.oracle.com/javase/tutorial/collections/"}
        ],
        "advanced": [
            {"title": "Try-With-Resources (AutoCloseable) & Custom Exceptions", "type": "Documentation", "url": "https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html"}
        ]
    },
    "Functional Programming & Streams API": {
        "beginner": [
            {"title": "Java Lambda Expressions & Functional Interfaces", "type": "Tutorial", "url": "https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html"},
            {"title": "Java Streams API: filter, map, and collect Operations", "type": "Guide", "url": "https://www.baeldung.com/java-8-streams"}
        ],
        "intermediate": [
            {"title": "JDBC Connection & PreparedStatement Best Practices", "type": "Article", "url": "https://docs.oracle.com/javase/tutorial/jdbc/basics/"}
        ],
        "advanced": [
            {"title": "Parallel Streams, ForkJoinPool & Reactive Streams", "type": "Paper", "url": "https://docs.oracle.com/javase/tutorial/collections/streams/parallelism.html"}
        ]
    },
    "Cloud Computing Fundamentals": {
        "beginner": [
            {"title": "NIST Cloud Computing Definitions & Essential Characteristics", "type": "Guide", "url": "https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-145.pdf"},
            {"title": "Hypervisors: Type-1 (Bare Metal) vs Type-2 (Hosted)", "type": "Tutorial", "url": "https://www.vmware.com/topics/glossary/content/hypervisor.html"}
        ],
        "intermediate": [
            {"title": "Containerization Concepts (Docker) vs Traditional VMs", "type": "Article", "url": "https://docs.docker.com/get-started/overview/"}
        ],
        "advanced": [
            {"title": "Hardware-Assisted Virtualization (Intel VT-x, AMD-V, SR-IOV)", "type": "Documentation", "url": "https://en.wikipedia.org/wiki/Hardware-assisted_virtualization"}
        ]
    },
    "Distributed AI Architecture & Compute Infrastructure": {
        "beginner": [
            {"title": "CPU vs GPU Architecture for Parallel Processing", "type": "Article", "url": "https://developer.nvidia.com/blog/cuda-refresher-reviewing-the-origins-of-gpu-computing/"},
            {"title": "CUDA Execution Model: Grids, Blocks, Threads & Warps", "type": "Tutorial", "url": "https://docs.nvidia.com/cuda/cuda-c-programming-guide/"}
        ],
        "intermediate": [
            {"title": "Data Parallelism vs Model Parallelism vs Pipeline Parallelism", "type": "Guide", "url": "https://huggingface.co/docs/transformers/v4.20.1/en/perf_train_gpu_many"}
        ],
        "advanced": [
            {"title": "All-Reduce Communication Primitives (NCCL, Ring All-Reduce)", "type": "Paper", "url": "https://developer.nvidia.com/nccl"}
        ]
    },
    "PyTorch Distributed Data Parallel (DDP)": {
        "beginner": [
            {"title": "Getting Started with Distributed Data Parallel (DDP) in PyTorch", "type": "Tutorial", "url": "https://pytorch.org/tutorials/intermediate/ddp_tutorial.html"},
            {"title": "DistributedSampler & Gradient Synchronization", "type": "Guide", "url": "https://pytorch.org/docs/stable/data.html#torch.utils.data.distributed.DistributedSampler"}
        ],
        "intermediate": [
            {"title": "Automatic Mixed Precision (AMP) & torch.cuda.amp", "type": "Article", "url": "https://pytorch.org/docs/stable/amp.html"}
        ],
        "advanced": [
            {"title": "Fully Sharded Data Parallel (FSDP) & DeepSpeed ZeRO Stages", "type": "Paper", "url": "https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html"}
        ]
    },
    "Big Data Dimensions & Data Engineering Lifecycle": {
        "beginner": [
            {"title": "The 5 V's of Big Data: Volume, Velocity, Variety, Veracity, Value", "type": "Guide", "url": "https://en.wikipedia.org/wiki/Big_data"},
            {"title": "The Data Engineering Lifecycle: Generation, Storage, Ingestion, Transformation, Serving", "type": "Article", "url": "https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/"}
        ],
        "intermediate": [
            {"title": "Batch vs Stream Processing: Lambda & Kappa Architectures", "type": "Tutorial", "url": "https://www.databricks.com/glossary/lambda-architecture"}
        ],
        "advanced": [
            {"title": "Modern Data Stack & Data Mesh Paradigms", "type": "Documentation", "url": "https://martinfowler.com/articles/data-monolith-to-mesh.html"}
        ]
    },
    "Hadoop Ecosystem & HDFS Architecture": {
        "beginner": [
            {"title": "Hadoop Distributed File System (HDFS) Architecture Guide", "type": "Guide", "url": "https://hadoop.apache.org/docs/r3.3.6/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html"},
            {"title": "NameNode, DataNode & Heartbeat Replication Dynamics", "type": "Tutorial", "url": "https://www.geeksforgeeks.org/hdfs-architecture-in-hadoop/"}
        ],
        "intermediate": [
            {"title": "Apache Spark Resilient Distributed Datasets (RDDs) & Lineage", "type": "Article", "url": "https://spark.apache.org/docs/latest/rdd-programming-guide.html"}
        ],
        "advanced": [
            {"title": "Spark Catalyst Query Optimizer & Tungsten Engine", "type": "Paper", "url": "https://databricks.com/blog/2015/04/13/deep-dive-into-spark-sqls-catalyst-optimizer.html"}
        ]
    },
    "Event Streaming Fundamentals & Message Brokers": {
        "beginner": [
            {"title": "Apache Kafka Architecture: Topics, Partitions, Brokers & Offsets", "type": "Tutorial", "url": "https://kafka.apache.org/intro"},
            {"title": "Publish-Subscribe vs Message Queueing Models", "type": "Guide", "url": "https://aws.amazon.com/pub-sub-messaging/"}
        ],
        "intermediate": [
            {"title": "Kafka Consumer Groups, Rebalancing & Partition Assignment", "type": "Article", "url": "https://www.confluent.io/blog/tutorial-getting-started-with-the-new-apache-kafka-0-9-consumer-client/"}
        ],
        "advanced": [
            {"title": "Event-Driven Stream Processing: Windowing (Tumbling, Sliding, Session)", "type": "Documentation", "url": "https://kafka.apache.org/documentation/streams/"}
        ]
    },
    "Apache Airflow & Workflow Orchestration": {
        "beginner": [
            {"title": "Apache Airflow Core Concepts: DAGs, Tasks, Operators, Sensors", "type": "Guide", "url": "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html"},
            {"title": "Creating Your First Airflow DAG in Python", "type": "Tutorial", "url": "https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html"}
        ],
        "intermediate": [
            {"title": "Task Dependencies, XComs & Dynamic Task Mapping", "type": "Article", "url": "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html"}
        ],
        "advanced": [
            {"title": "Data Governance, Lineage (Apache Atlas) & OpenLineage Integration", "type": "Paper", "url": "https://openlineage.io/"}
        ]
    },
    "Vector Representations & Distance Metrics": {
        "beginner": [
            {"title": "Dense Embeddings & Semantic Vector Search Explained", "type": "Guide", "url": "https://www.pinecone.io/learn/vector-embeddings/"},
            {"title": "Vector Distance Metrics: Cosine Similarity, Euclidean & Dot Product", "type": "Tutorial", "url": "https://www.pinecone.io/learn/vector-similarity/"}
        ],
        "intermediate": [
            {"title": "Why Relational DBs Fall Short: The Need for Dedicated Vector DBs", "type": "Article", "url": "https://www.databricks.com/glossary/vector-database"}
        ],
        "advanced": [
            {"title": "High-Dimensional Vector Geometry & The Curse of Dimensionality", "type": "Paper", "url": "https://en.wikipedia.org/wiki/Curse_of_dimensionality"}
        ]
    },
    "Exact vs Approximate Nearest Neighbor Search": {
        "beginner": [
            {"title": "Exact k-NN vs Approximate Nearest Neighbor (ANN) Trade-off", "type": "Tutorial", "url": "https://www.pinecone.io/learn/what-is-similarity-search/"},
            {"title": "Recall@K and Latency Benchmarking in Vector Search", "type": "Guide", "url": "https://github.com/erikbern/ann-benchmarks"}
        ],
        "intermediate": [
            {"title": "Inverted File Index (IVF) & Product Quantization (PQ) Compression", "type": "Article", "url": "https://faiss.ai/cpp_api/struct/structfaiss_1_1IndexIVFPQ.html"}
        ],
        "advanced": [
            {"title": "Hierarchical Navigable Small World (HNSW) Graph Indexing", "type": "Paper", "url": "https://arxiv.org/abs/1603.09320"}
        ]
    },
    "RAG Pipeline Architecture & Context Injection": {
        "beginner": [
            {"title": "Retrieval-Augmented Generation (RAG) Architecture Overview", "type": "Guide", "url": "https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/"},
            {"title": "Document Chunking Strategies & Overlap Window Tuning", "type": "Tutorial", "url": "https://www.pinecone.io/learn/chunking-strategies/"}
        ],
        "intermediate": [
            {"title": "Cross-Encoder Re-rankers for Enhanced Precision in RAG", "type": "Article", "url": "https://www.sbert.net/examples/applications/retrieve_rerank/README.html"}
        ],
        "advanced": [
            {"title": "RAG Evaluation Frameworks: Ragas (Faithfulness & Answer Relevance)", "type": "Paper", "url": "https://docs.ragas.io/en/stable/"}
        ]
    },
    "LLM Fundamentals & Tokenization": {
        "beginner": [
            {"title": "Large Language Models & Tokenization Mechanics", "type": "Guide", "url": "https://platform.openai.com/tokenizer"},
            {"title": "Context Windows, Attention Heads & Temperature/Top-P Parameters", "type": "Tutorial", "url": "https://www.promptingguide.ai/introduction/settings"}
        ],
        "intermediate": [
            {"title": "System, User, and Assistant Message Roles in Conversational Models", "type": "Article", "url": "https://platform.openai.com/docs/guides/text-generation"}
        ],
        "advanced": [
            {"title": "Transformer Attention: Multi-Head Scaled Dot-Product Mechanics", "type": "Paper", "url": "https://arxiv.org/abs/1706.03762"}
        ]
    },
    "Prompt Patterns & Chain-of-Thought": {
        "beginner": [
            {"title": "Prompt Engineering Guide: Zero-Shot and Few-Shot Prompting", "type": "Guide", "url": "https://www.promptingguide.ai/techniques/fewshot"},
            {"title": "Delimiters and Role Prompting Techniques", "type": "Tutorial", "url": "https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/"}
        ],
        "intermediate": [
            {"title": "Chain-of-Thought (CoT) Prompting & Step-by-Step Reasoning", "type": "Article", "url": "https://arxiv.org/abs/2201.11903"}
        ],
        "advanced": [
            {"title": "ReAct Framework: Synergizing Reasoning and Acting in Language Models", "type": "Paper", "url": "https://arxiv.org/abs/2210.03629"}
        ]
    },
    "Prompt Safety, Evaluation & Guardrails": {
        "beginner": [
            {"title": "Hallucinations & Prompt Injection Vulnerabilities in LLMs", "type": "Guide", "url": "https://owasp.org/www-project-top-10-for-large-language-model-applications/"},
            {"title": "Evaluation Metrics: BLEU, ROUGE & BERTScore", "type": "Tutorial", "url": "https://huggingface.co/spaces/evaluate-metric/rouge"}
        ],
        "intermediate": [
            {"title": "NeMo Guardrails & Llama Guard for Input/Output Filtering", "type": "Article", "url": "https://github.com/NVIDIA/NeMo-Guardrails"}
        ],
        "advanced": [
            {"title": "LLM-as-a-Judge Evaluation Frameworks & Function Calling Safety", "type": "Paper", "url": "https://arxiv.org/abs/2306.05685"}
        ]
    }
}


class LearningRequirementClassifier:
    """
    Scikit-learn Decision Tree model for explainable student learning requirement prediction.
    Features:
      0: Topic Accuracy (%) [0 - 100]
      1: Previous Overall Score (%) [0 - 100]
      2: Attempt Number (1, 2, 3...)
      3: Correct Answers Count in Topic
      4: Total Questions in Topic
    
    Classes:
      0: 'Revision'           (Need core foundational study)
      1: 'Practice'           (Need applied drills & exercises)
      2: 'Advanced Learning'  (Ready for higher difficulty & capstones)
    """

    CLASS_NAMES = ['Revision', 'Practice', 'Advanced Learning']
    FEATURE_NAMES = [
        'Topic Accuracy (%)',
        'Previous Overall Score (%)',
        'Attempt Number',
        'Correct Count',
        'Total Questions'
    ]

    def __init__(self):
        self.model = DecisionTreeClassifier(
            max_depth=3,
            criterion='gini',
            random_state=42
        )
        self.is_trained = False
        self._train_initial_model()

    def _train_initial_model(self):
        """
        Trains the Decision Tree on diverse pedagogical student performance vectors.
        """
        training_samples = [
            # Low accuracy (< 40%) -> Revision
            [0.0, 30.0, 1, 0, 3],
            [15.0, 35.0, 1, 0, 3],
            [33.3, 40.0, 1, 1, 3],
            [25.0, 25.0, 2, 1, 4],
            [33.3, 50.0, 2, 1, 3],
            [0.0, 20.0, 1, 0, 4],
            [30.0, 38.0, 1, 1, 3],

            # Moderate accuracy (40% - 70%) -> Practice
            [40.0, 50.0, 1, 2, 5],
            [50.0, 55.0, 1, 2, 4],
            [66.7, 60.0, 1, 2, 3],
            [60.0, 65.0, 1, 3, 5],
            [66.7, 70.0, 2, 2, 3],
            [50.0, 62.0, 2, 2, 4],
            [45.0, 52.0, 1, 2, 4],

            # High accuracy (> 70%) -> Advanced Learning
            [75.0, 75.0, 1, 3, 4],
            [80.0, 80.0, 1, 4, 5],
            [100.0, 85.0, 1, 3, 3],
            [100.0, 92.0, 2, 3, 3],
            [85.0, 78.0, 1, 4, 5],
            [75.0, 82.0, 2, 3, 4],
            [100.0, 100.0, 1, 5, 5]
        ]

        # Labels: 0 = Revision, 1 = Practice, 2 = Advanced Learning
        training_labels = [
            0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2, 2, 2, 2
        ]

        X = np.array(training_samples, dtype=float)
        y = np.array(training_labels, dtype=int)

        self.model.fit(X, y)
        self.is_trained = True

    def predict(self, topic_accuracy: float, previous_score: float, attempt_num: int, correct: int, total: int):
        """
        Returns predicted requirement name ('Revision', 'Practice', 'Advanced Learning')
        and explainable rationale.
        """
        features = np.array([[topic_accuracy, previous_score, attempt_num, correct, total]], dtype=float)
        pred_idx = self.model.predict(features)[0]
        prediction_label = self.CLASS_NAMES[pred_idx]

        # Confidence / Class Probabilities
        proba = self.model.predict_proba(features)[0]
        confidence = round(float(proba[pred_idx]) * 100.0, 1)

        # Transparent explanation string for college viva defense
        if prediction_label == 'Revision':
            explanation = (
                f"Model evaluated Topic Accuracy ({topic_accuracy:.1f}%) below the 40% mastery boundary. "
                f"Feature importance prioritized foundational gaps over attempt count; recommending core concept revision and step-by-step rebuilding."
            )
        elif prediction_label == 'Practice':
            explanation = (
                f"Model evaluated Topic Accuracy ({topic_accuracy:.1f}%) in the 40%-70% competence band with overall score {previous_score:.1f}%. "
                f"Foundational understanding is present, but application drills and intermediate question practice are required to achieve mastery."
            )
        else:
            explanation = (
                f"Model evaluated Topic Accuracy ({topic_accuracy:.1f}%) above the 70% threshold. "
                f"Classified as 'Advanced Learning' — candidate has demonstrated conceptual strength and is ready for higher-order synthesis and challenging edge cases."
            )

        return {
            'prediction': prediction_label,
            'confidence': confidence,
            'explanation': explanation,
            'probabilities': {name: round(float(p) * 100, 1) for name, p in zip(self.CLASS_NAMES, proba)}
        }

    def get_feature_importances(self) -> dict:
        """Returns feature importances for transparency and viva demonstration."""
        importances = self.model.feature_importances_
        return {name: round(float(val) * 100, 2) for name, val in zip(self.FEATURE_NAMES, importances)}


# Singleton instance
_ml_classifier = None

def get_ml_classifier() -> LearningRequirementClassifier:
    global _ml_classifier
    if _ml_classifier is None:
        _ml_classifier = LearningRequirementClassifier()
    return _ml_classifier


def resolve_curated_resources(topic_name: str, subject_name: str = "") -> dict:
    """
    Intelligently resolves learning resources for a syllabus topic.
    Checks exact matches, fuzzy keyword matches, and falls back to tailored domain resources.
    """
    # 1. Exact match in CURATED_RESOURCES
    if topic_name in CURATED_RESOURCES:
        return CURATED_RESOURCES[topic_name]

    # 2. Case-insensitive or substring match
    topic_lower = topic_name.lower()
    for key, res in CURATED_RESOURCES.items():
        if key.lower() in topic_lower or topic_lower in key.lower():
            return res

    # 3. Domain fallback based on subject
    subj_lower = subject_name.lower() if subject_name else ""
    if "vector" in subj_lower or "rag" in topic_lower or "embedding" in topic_lower:
        return {
            "beginner": [{"title": f"Vector Embeddings & Semantic Search in {topic_name}", "type": "Guide", "url": "https://www.pinecone.io/learn/vector-embeddings/"}],
            "intermediate": [{"title": f"ANN Indexing (HNSW/IVF) for {topic_name}", "type": "Tutorial", "url": "https://faiss.ai/"}],
            "advanced": [{"title": f"Production RAG Pipelines & Optimization with {topic_name}", "type": "Documentation", "url": "https://docs.llamaindex.ai/"}]
        }
    elif "cloud" in subj_lower or "distributed" in subj_lower or "gpu" in topic_lower:
        return {
            "beginner": [{"title": f"Fundamentals of Cloud Systems & {topic_name}", "type": "Guide", "url": "https://aws.amazon.com/what-is-cloud-computing/"}],
            "intermediate": [{"title": f"PyTorch Distributed Training (DDP/FSDP) & {topic_name}", "type": "Tutorial", "url": "https://pytorch.org/tutorials/intermediate/ddp_tutorial.html"}],
            "advanced": [{"title": f"GPU Tensor Cores & Large-Scale AI Clusters: {topic_name}", "type": "Paper", "url": "https://developer.nvidia.com/"}]
        }
    elif "big data" in subj_lower or "kafka" in topic_lower or "spark" in topic_lower or "hadoop" in topic_lower or "engineering" in subj_lower:
        return {
            "beginner": [{"title": f"Big Data Architecture & {topic_name} Explained", "type": "Article", "url": "https://spark.apache.org/docs/latest/"}],
            "intermediate": [{"title": f"Event Streaming & Lakehouse Architectures for {topic_name}", "type": "Tutorial", "url": "https://kafka.apache.org/documentation/"}],
            "advanced": [{"title": f"Workflow Orchestration with Airflow & {topic_name}", "type": "Documentation", "url": "https://airflow.apache.org/docs/"}]
        }
    elif "java" in subj_lower or "oop" in subj_lower:
        return {
            "beginner": [{"title": f"Java Core Fundamentals & {topic_name}", "type": "Tutorial", "url": "https://docs.oracle.com/javase/tutorial/"}],
            "intermediate": [{"title": f"Collections, Streams & JDBC in {topic_name}", "type": "Guide", "url": "https://www.baeldung.com/java-tutorial"}],
            "advanced": [{"title": f"Concurrency, Memory Model & JVM Internals for {topic_name}", "type": "Documentation", "url": "https://docs.oracle.com/en/java/"}]
        }
    elif "machine learning" in subj_lower or "deep learning" in subj_lower:
        return {
            "beginner": [{"title": f"Foundations of {topic_name} in Machine Learning", "type": "Guide", "url": "https://scikit-learn.org/stable/user_guide.html"}],
            "intermediate": [{"title": f"Hands-on Implementation of {topic_name}", "type": "Tutorial", "url": "https://pytorch.org/tutorials/"}],
            "advanced": [{"title": f"State-of-the-Art Research & Optimization for {topic_name}", "type": "Paper", "url": "https://arxiv.org/list/cs.LG/recent"}]
        }
    elif "operating" in subj_lower or "os" in subj_lower:
        return {
            "beginner": [{"title": f"Operating System Concepts: {topic_name}", "type": "Article", "url": "https://www.geeksforgeeks.org/operating-systems/"}],
            "intermediate": [{"title": f"Scheduling, Synchronization & Memory: {topic_name}", "type": "Guide", "url": "https://pages.cs.wisc.edu/~remzi/OSTEP/"}],
            "advanced": [{"title": f"Kernel Architecture & Systems Programming in {topic_name}", "type": "Documentation", "url": "https://www.kernel.org/doc/html/latest/"}]
        }
    elif "prompt" in subj_lower or "llm" in subj_lower:
        return {
            "beginner": [{"title": f"Prompt Engineering Guide & {topic_name}", "type": "Guide", "url": "https://www.promptingguide.ai/"}],
            "intermediate": [{"title": f"Chain-of-Thought & LangChain Prompts for {topic_name}", "type": "Tutorial", "url": "https://python.langchain.com/docs/"}],
            "advanced": [{"title": f"Guardrails, Prompt Injection Defense & Evaluation in {topic_name}", "type": "Paper", "url": "https://arxiv.org/abs/2302.11382"}]
        }
    elif "analytics" in subj_lower or "probability" in subj_lower or "math" in subj_lower or "discrete" in subj_lower:
        return {
            "beginner": [{"title": f"Mathematical Foundations of {topic_name}", "type": "Tutorial", "url": "https://www.khanacademy.org/math/statistics-probability"}],
            "intermediate": [{"title": f"Hypothesis Testing & Statistical Inference: {topic_name}", "type": "Guide", "url": "https://docs.scipy.org/doc/scipy/reference/stats.html"}],
            "advanced": [{"title": f"Rigorous Proofs & High-Dimensional Analytics in {topic_name}", "type": "Documentation", "url": "https://stats.stackexchange.com/"}]
        }
    elif "stack" in subj_lower or "web" in subj_lower:
        return {
            "beginner": [{"title": f"Modern Web Development Fundamentals: {topic_name}", "type": "Guide", "url": "https://developer.mozilla.org/"}],
            "intermediate": [{"title": f"Full Stack Integration & APIs for {topic_name}", "type": "Tutorial", "url": "https://laravel.com/docs"}],
            "advanced": [{"title": f"Enterprise Architecture & Performance in {topic_name}", "type": "Documentation", "url": "https://developer.mozilla.org/en-US/docs/Web/Performance"}]
        }
    elif "edge" in subj_lower or "hardware" in topic_lower or "embedded" in topic_lower:
        return {
            "beginner": [{"title": f"Edge AI & Embedded Systems Primer: {topic_name}", "type": "Guide", "url": "https://www.arm.com/technologies/machine-learning"}],
            "intermediate": [{"title": f"Model Quantization & TinyML Deployment for {topic_name}", "type": "Tutorial", "url": "https://www.tensorflow.org/lite/microcontrollers"}],
            "advanced": [{"title": f"Heterogeneous Computing & NPU Acceleration: {topic_name}", "type": "Paper", "url": "https://developer.qualcomm.com/"}]
        }

    # Generic fallback
    return {
        "beginner": [{"title": f"Introductory Guide to {topic_name}", "type": "Documentation", "url": "https://scikit-learn.org"}],
        "intermediate": [{"title": f"Practical Application: {topic_name}", "type": "Tutorial", "url": "https://pandas.pydata.org"}],
        "advanced": [{"title": f"Advanced Mastery & Research in {topic_name}", "type": "Paper", "url": "https://arxiv.org"}]
    }


def generate_topic_recommendations(
    topic_name: str,
    subject_name: str,
    accuracy: float,
    classification: str,
    previous_score: float = 50.0,
    attempt_number: int = 1,
    correct: int = 0,
    total: int = 3,
    subtopics: str = ""
) -> dict:
    """
    Generates rule-based pedagogical recommendations enhanced with Scikit-learn predictions.
    
    Weak topics:
      - Basic concepts
      - Beginner learning material
      - Concrete examples
      - Practice questions
      - Revision quiz
    Average topics:
      - Concept revision
      - Intermediate examples
      - Practice questions
      - Topic quiz
    Strong topics:
      - Advanced questions
      - Higher difficulty problems
      - Additional learning material
    """
    classifier = get_ml_classifier()
    ml_result = classifier.predict(
        topic_accuracy=accuracy,
        previous_score=previous_score,
        attempt_num=attempt_number,
        correct=correct,
        total=total
    )

    resources = resolve_curated_resources(topic_name, subject_name)

    subtopic_list = [s.strip() for s in subtopics.split(';')] if subtopics else [topic_name]

    if classification == 'WEAK':
        title = f"Priority Action Plan: Fundamentals & Revision for {topic_name}"
        steps = [
            {
                "step": 1,
                "title": f"1. Basic Concepts & Fundamentals of {topic_name}",
                "description": f"Focus on understanding the foundational definitions, core principles, and terminology of {topic_name}.",
                "subtopics_to_review": subtopic_list
            },
            {
                "step": 2,
                "title": "2. Beginner Learning Material",
                "description": "Read introductory documentation and conceptual walkthroughs before attempting code exercises.",
                "resources": resources.get('beginner', [])
            },
            {
                "step": 3,
                "title": "3. Step-by-Step Examples",
                "description": f"Trace simple, worked-out examples for {subtopic_list[0] if subtopic_list else topic_name} by hand."
            },
            {
                "step": 4,
                "title": "4. Practice Questions (Easy to Medium)",
                "description": "Attempt 5-10 foundational multiple-choice and conceptual drill questions to verify retention."
            },
            {
                "step": 5,
                "title": "5. Revision Quiz",
                "description": f"Take the 5-minute revision checkpoint for {topic_name} before moving to more advanced subjects."
            }
        ]
        badge_color = "danger"

    elif classification == 'AVERAGE':
        title = f"Skill Enhancement: Concept Revision & Practice for {topic_name}"
        steps = [
            {
                "step": 1,
                "title": f"1. Concept Revision for {topic_name}",
                "description": f"Quickly review key formulas, edge conditions, and execution rules in {topic_name}.",
                "subtopics_to_review": subtopic_list
            },
            {
                "step": 2,
                "title": "2. Intermediate Examples & Problem Solving",
                "description": "Examine case studies and intermediate problems that combine multiple theoretical concepts.",
                "resources": resources.get('intermediate', [])
            },
            {
                "step": 3,
                "title": "3. Practice Questions",
                "description": "Solve medium-difficulty scenario-based questions to solidify analytical instincts."
            },
            {
                "step": 4,
                "title": "4. Topic Mastery Quiz",
                "description": f"Attempt a timed topic assessment to boost your accuracy from {accuracy:.1f}% to > 75%."
            }
        ]
        badge_color = "warning"

    else:  # STRONG
        title = f"Mastery & Extension: Advanced Challenges for {topic_name}"
        steps = [
            {
                "step": 1,
                "title": f"1. Advanced Questions & Edge Cases in {topic_name}",
                "description": f"Tackle non-trivial, analytical questions requiring deep synthesis across {topic_name}.",
                "subtopics_to_review": subtopic_list
            },
            {
                "step": 2,
                "title": "2. Higher Difficulty Problems",
                "description": "Solve algorithmic edge-cases, optimization challenges, and multi-step computational problems."
            },
            {
                "step": 3,
                "title": "3. Additional Learning Material & Research",
                "description": "Explore state-of-the-art documentation, open-source libraries, and academic research papers.",
                "resources": resources.get('advanced', [])
            }
        ]
        badge_color = "success"

    return {
        "topic_name": topic_name,
        "subject_name": subject_name,
        "accuracy": accuracy,
        "classification": classification,
        "predicted_requirement": ml_result['prediction'],
        "ml_confidence": ml_result['confidence'],
        "ml_explanation": ml_result['explanation'],
        "ml_probabilities": ml_result['probabilities'],
        "title": title,
        "badge_color": badge_color,
        "steps": steps,
        "resources": resources.get('beginner', []) + resources.get('intermediate', []) + resources.get('advanced', [])
    }
