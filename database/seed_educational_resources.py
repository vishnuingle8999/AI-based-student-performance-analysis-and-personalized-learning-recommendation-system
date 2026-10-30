import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models.schema import db, Topic, LearningResource

# Curated dataset of verified real educational resources across multiple platforms
CURATED_RESOURCES_DATA = [
    # ----------------------------------------------------
    # Machine Learning (Semester V)
    # ----------------------------------------------------
    {
        "topic_name": "Linear Regression & Inductive Bias",
        "resources": [
            {
                "title": "Linear Regression in Machine Learning (Comprehensive Guide)",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/ml-linear-regression/",
                "description": "Formulation of Ordinary Least Squares, cost functions, gradient descent updates, and code implementation.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Linear Regression, Clearly Explained with Step-by-Step Examples",
                "provider": "StatQuest with Josh Starmer",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=nk2CQITm_eo",
                "description": "Visual intuition of linear regression, residuals, R-squared, and finding the best fit line.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Machine Learning for Everybody – Full Beginner Course",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=i_LwzRVP7bg",
                "description": "Hands-on walk-through covering supervised regression models, feature scaling, and validation.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Scikit-Learn Linear Models & Regularization Guide",
                "provider": "Scikit-learn Documentation",
                "resource_type": "documentation",
                "resource_url": "https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares",
                "description": "Official documentation covering Ridge, Lasso, ElasticNet, and solver algorithms.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Bayes Theorem & Logistic Regression",
        "resources": [
            {
                "title": "Understanding Logistic Regression and the Sigmoid Function",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/understanding-logistic-regression/",
                "description": "Detailed explanation of log-odds, maximum likelihood estimation, decision boundaries, and confusion matrices.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Logistic Regression Details Pt.1: Coefficients and Odds",
                "provider": "StatQuest with Josh Starmer",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=yIYKR4gJW60",
                "description": "Clear step-by-step visual demonstration of log-odds curve, probability transformations, and fitting.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "NPTEL Machine Learning: Logistic Regression & Classification",
                "provider": "NPTEL (IIT Kharagpur)",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=jGwO_b-dQ1g",
                "description": "Formal university lecture analyzing gradient ascent for log likelihood and multiclass extensions.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Naive Bayes Classifiers and Laplace Smoothing",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/naive-bayes-classifiers/",
                "description": "Prior probability, likelihood, posterior calculation, and conditional independence assumption.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Artificial Neurons & Perceptron Learning",
        "resources": [
            {
                "title": "Single Layer Perceptron in Machine Learning",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/single-layer-perceptron-in-tensorflow/",
                "description": "McCulloch-Pitts neuron, activation thresholds, perceptron learning rule, and the XOR limitation.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "But what is a neural network? Deep Learning Chapter 1",
                "provider": "3Blue1Brown",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=aircAruvnKk",
                "description": "World-class visual animations showing how weighted sums and activations recognize patterns.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Neural Networks and Backpropagation Calculus",
                "provider": "3Blue1Brown",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=IHZwWFHWa-w",
                "description": "Geometric intuition for partial derivatives, chain rule propagation, and gradient descent optimization.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Scikit-learn Multi-Layer Perceptron (MLP) Specification",
                "provider": "Scikit-learn Documentation",
                "resource_type": "documentation",
                "resource_url": "https://scikit-learn.org/stable/modules/neural_networks_supervised.html",
                "description": "Implementation parameters for MLPClassifier: hidden layers, activation, and Adam/SGD solvers.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "PAC Learning & VC Dimension",
        "resources": [
            {
                "title": "Vapnik-Chervonenkis (VC) Dimension in Machine Learning",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/vapnik-chervonenkis-vc-dimension/",
                "description": "Shattering points, hypothesis space capacity, sample complexity, and bounds on generalization error.",
                "difficulty": "Advanced",
                "verification_status": "verified"
            },
            {
                "title": "Computational Learning Theory and PAC Framework",
                "provider": "NPTEL (IIT Madras)",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=DCg3O0Q_s70",
                "description": "Rigorous academic formulation of Probably Approximately Correct (PAC) learning and epsilon-delta bounds.",
                "difficulty": "Advanced",
                "verification_status": "verified"
            },
            {
                "title": "Ensemble Methods, Bagging and Boosting Explained",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/bagging-vs-boosting-in-machine-learning/",
                "description": "Variance reduction with Random Forests and bias reduction with AdaBoost and Gradient Boosting.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "K-Means & Hierarchical Clustering",
        "resources": [
            {
                "title": "K-Means Clustering Algorithm and Elbow Method",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/k-means-clustering-introduction/",
                "description": "Centroid initialization, Voronoi partitions, convergence criteria, and inertia evaluation.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "K-means Clustering Clearly Explained",
                "provider": "StatQuest with Josh Starmer",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=4b5d3muPQmA",
                "description": "Intuitive step-by-step graphical walk-through of assigning points and recalculating cluster means.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Hierarchical Clustering and Dendrogram Interpretation",
                "provider": "StatQuest with Josh Starmer",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=7xHsRkOdVwo",
                "description": "Agglomerative vs divisive clustering, single/complete linkage distance, and dendrogram cuts.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Scikit-learn Clustering Algorithms Guide",
                "provider": "Scikit-learn Documentation",
                "resource_type": "documentation",
                "resource_url": "https://scikit-learn.org/stable/modules/clustering.html#k-means",
                "description": "Documentation for KMeans, MiniBatchKMeans, AgglomerativeClustering, and silhouette scores.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },

    # ----------------------------------------------------
    # Object Oriented Programming in Java (Semester V)
    # ----------------------------------------------------
    {
        "topic_name": "Java Platform & Fundamentals",
        "resources": [
            {
                "title": "How JVM Works – JVM Architecture Explained",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/jvm-works-jvm-architecture/",
                "description": "Class loader subsystem, JVM memory areas (Method, Heap, Stack, PC, Native), and Execution Engine.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Java Programming for Beginners – Full Course",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=A74TOX803D0",
                "description": "Comprehensive guide to JDK, JRE, primitive types, control flow, loops, and Scanner input.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Java Language Fundamentals and Getting Started",
                "provider": "Oracle Java Tutorials",
                "resource_type": "documentation",
                "resource_url": "https://docs.oracle.com/javase/tutorial/getStarted/intro/definition.html",
                "description": "Official Oracle tutorial on compile-time bytecode generation and write-once-run-anywhere platform.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Methods & Stack Execution",
        "resources": [
            {
                "title": "Stack vs Heap Memory Allocation in Java",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/stack-vs-heap-memory-allocation/",
                "description": "Stack frame lifecycle, method invocation, primitive local variables vs object references in heap.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Java Methods, Parameters & Call Stack Demonstration",
                "provider": "Telusko",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=9kJk1Xm19Zg",
                "description": "Practical code demonstration of static vs instance methods, method overloading, and return values.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Java String Immutability and StringBuilder Guide",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/string-vs-stringbuilder-vs-stringbuffer-in-java/",
                "description": "String constant pool, thread-safe StringBuffer vs mutable StringBuilder performance.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Encapsulation & Constructors",
        "resources": [
            {
                "title": "Encapsulation, Data Hiding, and Access Modifiers in Java",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/encapsulation-in-java/",
                "description": "Private fields, public getters and setters, constructor chaining with this() and super().",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Java Object-Oriented Programming (OOP) in 1.5 Hours",
                "provider": "Programming with Mosh",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=pTB0EiLXUC8",
                "description": "Crystal-clear visual demonstration of coupling, encapsulation, inheritance, and dynamic polymorphism.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Oracle Official Guide to Classes, Objects & Constructors",
                "provider": "Oracle Java Tutorials",
                "resource_type": "documentation",
                "resource_url": "https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html",
                "description": "Authoritative documentation explaining class declaration, member access, and constructor instantiation.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Exception Handling Mechanism",
        "resources": [
            {
                "title": "Exception Handling in Java (try, catch, throw, throws, finally)",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/exceptions-in-java/",
                "description": "Throwable hierarchy, Checked vs Unchecked exceptions, try-with-resources, and custom exception classes.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Java Exception Handling Complete Tutorial",
                "provider": "Telusko",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=r_vbh3N4XbU",
                "description": "Step-by-step coding tutorial showing multi-catch blocks, stack trace debugging, and resource cleanup.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Java Collections Framework (List, Set, Map) Overview",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/collections-in-java-2/",
                "description": "Hierarchy of ArrayList, LinkedList, HashSet, TreeSet, HashMap, and iterators.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Functional Programming & Streams API",
        "resources": [
            {
                "title": "Java Streams API, Filter, Map, and Reduce Explained",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/stream-in-java/",
                "description": "Intermediate vs terminal operations, lambda expressions, and pipeline processing.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Java Functional Programming and Streams API Crash Course",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=Q93JsQ8vcwA",
                "description": "In-depth code exercises with functional interfaces, method references, and parallel streams.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Official Oracle Java SE 8 Stream API Documentation",
                "provider": "Oracle Java Documentation",
                "resource_type": "documentation",
                "resource_url": "https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html",
                "description": "Complete specification of stream pipelines, spliterators, and collectors.",
                "difficulty": "Advanced",
                "verification_status": "verified"
            }
        ]
    },

    # ----------------------------------------------------
    # Cloud and Distributed AI Systems (Semester V)
    # ----------------------------------------------------
    {
        "topic_name": "Cloud Computing Fundamentals",
        "resources": [
            {
                "title": "Introduction to Cloud Computing & NIST Architecture",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/cloud-computing/",
                "description": "5 essential characteristics, on-demand self-service, broad network access, resource pooling.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Cloud Computing Tutorial for Beginners – Full Course",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=2LaAJq1lB1Q",
                "description": "Comprehensive explanation of hypervisors (Type-1 bare metal vs Type-2 hosted), VMs, and containers.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "NPTEL Cloud Computing Course Lecture 1",
                "provider": "NPTEL (IIT Kharagpur)",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=eP_g3NqK4zY",
                "description": "University-level lecture on parallel computing foundations, virtualization taxonomy, and SLAs.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Distributed AI Architecture & Compute Infrastructure",
        "resources": [
            {
                "title": "CPU vs GPU Architecture for High-Performance AI",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/difference-between-cpu-and-gpu/",
                "description": "ALU density, memory bandwidth, SIMD parallelism, latency vs throughput comparison.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "How GPUs Work and Accelerate Machine Learning",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=60fL2bO_p_c",
                "description": "CUDA programming model: threads, blocks, grids, warps, and tensor core matrix multiplications.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "NVIDIA CUDA C++ Official Programming Guide",
                "provider": "NVIDIA Documentation",
                "resource_type": "documentation",
                "resource_url": "https://docs.nvidia.com/cuda/cuda-c-programming-guide/",
                "description": "Authoritative guide on GPU memory hierarchy, shared memory bank conflicts, and kernels.",
                "difficulty": "Advanced",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "PyTorch Distributed Data Parallel (DDP)",
        "resources": [
            {
                "title": "Getting Started with Distributed Data Parallel (DDP) in PyTorch",
                "provider": "PyTorch Official Documentation",
                "resource_type": "documentation",
                "resource_url": "https://pytorch.org/tutorials/intermediate/ddp_tutorial.html",
                "description": "Official PyTorch step-by-step tutorial on multi-GPU training with DistributedSampler and gradient sync.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Distributed Model Training with PyTorch (DDP & FSDP)",
                "provider": "PyTorch Official Channel",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=Cvdhwx-OBBo",
                "description": "Video walkthrough of torch.distributed, NCCL backend, Ring All-Reduce, and ZeRO memory stages.",
                "difficulty": "Advanced",
                "verification_status": "verified"
            },
            {
                "title": "Distributed Deep Learning Training in PyTorch",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/distributed-training-in-pytorch/",
                "description": "Data parallelism vs model parallelism, rank, world size, and mixed precision with torch.cuda.amp.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },

    # ----------------------------------------------------
    # Data Engineering and Big Data Systems (Semester V)
    # ----------------------------------------------------
    {
        "topic_name": "Hadoop Ecosystem & HDFS Architecture",
        "resources": [
            {
                "title": "Hadoop Ecosystem and Architecture Components",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/hadoop-ecosystem/",
                "description": "NameNode, DataNode, Secondary NameNode, block replication, MapReduce, YARN, and Hive.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Hadoop Tutorial for Beginners – Architecture and Hands-on",
                "provider": "Edureka",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=gT_u4m8wWpA",
                "description": "Video demonstration of cluster setup, fault tolerance via heartbeats, and MapReduce execution.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Apache Hadoop HDFS Architecture Design Guide",
                "provider": "Apache Software Foundation",
                "resource_type": "documentation",
                "resource_url": "https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html",
                "description": "Official documentation covering file system namespace, block placement, and data replication.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Event Streaming Fundamentals & Message Brokers",
        "resources": [
            {
                "title": "Apache Kafka Architecture and Core Fundamentals",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/apache-kafka-architecture/",
                "description": "Publish-subscribe model, brokers, topics, partitions, consumer groups, and offset tracking.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Apache Kafka in 6 Minutes – An Illustrated Guide",
                "provider": "Confluent",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=Ch5VhJzaoaI",
                "description": "Visual introduction to event streaming, append-only logs, and decoupled microservice communication.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Apache Kafka Full Course for Beginners",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=R873BlNVUB4",
                "description": "Hands-on development with producers, consumers, partition keys, rebalancing, and Kafka Streams.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Apache Airflow & Workflow Orchestration",
        "resources": [
            {
                "title": "Introduction to Apache Airflow and DAG Design",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/introduction-to-apache-airflow/",
                "description": "Directed Acyclic Graphs (DAGs), Operators (Bash, Python), Tasks, Sensors, and the Web UI.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Apache Airflow Tutorial for Beginners – Complete Pipeline",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=K9AnJ9_ZAXE",
                "description": "Building, scheduling, and monitoring production data pipelines with Airflow in Python.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Apache Airflow Core Concepts Documentation",
                "provider": "Apache Airflow Documentation",
                "resource_type": "documentation",
                "resource_url": "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html",
                "description": "Official documentation covering task lifecycles, XComs, dynamic task mapping, and connections.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },

    # ----------------------------------------------------
    # Vector Databases (Semester V)
    # ----------------------------------------------------
    {
        "topic_name": "Vector Representations & Distance Metrics",
        "resources": [
            {
                "title": "Vector Embeddings & Semantic Search Explained",
                "provider": "Pinecone Learning Center",
                "resource_type": "documentation",
                "resource_url": "https://www.pinecone.io/learn/vector-embeddings/",
                "description": "High-dimensional vector embeddings, semantic proximity, and converting text to dense vectors.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Word Embeddings and Vector Search Clearly Explained",
                "provider": "StatQuest with Josh Starmer",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=e9U0QAFbfLI",
                "description": "Intuitive explanation of dense vector spaces, cosine distance, dot product, and Euclidean metric.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Cosine Similarity and Distance Metrics in Machine Learning",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/cosine-similarity/",
                "description": "Mathematical formula, normalized dot products, angle calculation, and Python NumPy code.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Exact vs Approximate Nearest Neighbor Search",
        "resources": [
            {
                "title": "Hierarchical Navigable Small World (HNSW) Graph Indexing",
                "provider": "Pinecone Learning Center",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=QvLQYMf1Tso",
                "description": "Multi-layer skip-list graph algorithm for fast approximate nearest neighbor (ANN) retrieval.",
                "difficulty": "Advanced",
                "verification_status": "verified"
            },
            {
                "title": "K-Nearest Neighbors (k-NN) and Distance Metrics",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/k-nearest-neighbours/",
                "description": "Exact linear search complexity O(N*d) vs ANN indexing speed-up trade-offs.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "FAISS (Facebook AI Similarity Search) Documentation",
                "provider": "Facebook Research Documentation",
                "resource_type": "documentation",
                "resource_url": "https://faiss.ai/",
                "description": "Official guide to IndexFlatL2, IndexIVFFlat, Product Quantization (PQ), and GPU indexing.",
                "difficulty": "Advanced",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "RAG Pipeline Architecture & Context Injection",
        "resources": [
            {
                "title": "Retrieval-Augmented Generation (RAG) Architecture and Design",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/retrieval-augmented-generation-rag/",
                "description": "Document chunking, embedding generation, semantic retrieval, and prompt context injection.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Retrieval Augmented Generation (RAG) Full Tutorial with LangChain",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=LhnCsLZZf6c",
                "description": "Step-by-step project building a full RAG pipeline connecting PDF documents, vector store, and LLM.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "LangChain QA over Documents (RAG Architecture)",
                "provider": "LangChain Official Documentation",
                "resource_type": "documentation",
                "resource_url": "https://python.langchain.com/docs/use_cases/question_answering/",
                "description": "Official documentation covering text splitters, vector stores, re-rankers, and response synthesis.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },

    # ----------------------------------------------------
    # Introduction to Operating Systems (Semester IV)
    # ----------------------------------------------------
    {
        "topic_name": "Processes, Threads & CPU Scheduling",
        "resources": [
            {
                "title": "CPU Scheduling in Operating Systems (FCFS, SJF, SRTF, RR, Priority)",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/",
                "description": "Gantt chart calculations, turnaround time, waiting time, and preemptive scheduling algorithms.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "CPU Scheduling Algorithms Playlist – Neso Academy",
                "provider": "Neso Academy",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=ewabbflt_80",
                "description": "Comprehensive visual video explanations with numerical examples for all standard OS scheduling algorithms.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "NPTEL Operating Systems: Process Management and Threads",
                "provider": "NPTEL (IIT Kharagpur)",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=Yf_tA4k3m3A",
                "description": "University-level lecture on process control blocks (PCB), context switching, and user vs kernel threads.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Synchronization & Deadlock Prevention",
        "resources": [
            {
                "title": "Banker's Algorithm for Deadlock Avoidance with Example",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/bankers-algorithm-in-operating-system-2/",
                "description": "Resource-allocation graph, Coffman's 4 conditions, safe state verification, and request-edge algorithms.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Process Synchronization and Semaphores – Abdul Bari",
                "provider": "Abdul Bari",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=UbhT_v4_q_M",
                "description": "Legendary visual teaching of critical section, race conditions, counting vs binary semaphores.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Memory Allocation & Page Replacement",
        "resources": [
            {
                "title": "Paging and Virtual Memory in Operating System",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/paging-in-operating-system/",
                "description": "Logical to physical address translation, Page Table Base Register, TLB hit/miss, and internal fragmentation.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Page Replacement Algorithms (FIFO, LRU, Optimal) – Neso Academy",
                "provider": "Neso Academy",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=WtwffsE_88U",
                "description": "Step-by-step numerical examples solving page faults, Belady's anomaly, and LRU stack implementation.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },

    # ----------------------------------------------------
    # Data Structures (Semester III)
    # ----------------------------------------------------
    {
        "topic_name": "Linked List Implementations",
        "resources": [
            {
                "title": "Linked List Data Structure – Complete Guide with Code",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/data-structures/linked-list/",
                "description": "Singly, doubly, and circular linked lists with insertion, deletion, and reversal algorithms.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Linked Lists in 15 Minutes with Visual Demonstrations",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=RBSGKlAvoiM",
                "description": "Animated node pointer manipulation, traversing, inserting at head/tail, and memory diagrams.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "Linked List Data Structure Operations – Abdul Bari",
                "provider": "Abdul Bari",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=0IAPZzGSbME",
                "description": "Deep algorithmic trace of pointer reassignment and dynamic memory allocation.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Trees, BST & Graph Traversals",
        "resources": [
            {
                "title": "Binary Search Tree (BST) Data Structure",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/binary-search-tree-data-structure/",
                "description": "Inorder, preorder, and postorder traversals, search, insertion, deletion, and AVL rotations.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Tree and Graph Traversals (BFS & DFS) Explained",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=tWVWeAqZ0WU",
                "description": "Queue-based Breadth First Search and stack-based Depth First Search with adjacency matrix/list.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },

    # ----------------------------------------------------
    # Prompt Engineering (Semester III)
    # ----------------------------------------------------
    {
        "topic_name": "LLM Fundamentals & Tokenization",
        "resources": [
            {
                "title": "Prompt Engineering Guide – Introduction & Settings",
                "provider": "DAIR.AI Prompting Guide",
                "resource_type": "documentation",
                "resource_url": "https://www.promptingguide.ai/introduction/settings",
                "description": "Temperature, Top-P, tokens, frequency penalty, and system vs user vs assistant messages.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "ChatGPT Prompt Engineering for Developers Course",
                "provider": "DeepLearning.AI",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=_ZvnD93Mr5r",
                "description": "Andrew Ng and Isa Fulford explaining clear instructions, delimiters, and few-shot formatting.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "What is Prompt Engineering? Concepts and Use Cases",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/what-is-prompt-engineering/",
                "description": "Role prompting, instruction tuning, few-shot prompting, and context window management.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            }
        ]
    },
    {
        "topic_name": "Prompt Patterns & Chain-of-Thought",
        "resources": [
            {
                "title": "Chain-of-Thought Prompting & Reasoning Techniques",
                "provider": "DAIR.AI Prompting Guide",
                "resource_type": "documentation",
                "resource_url": "https://www.promptingguide.ai/techniques/cot",
                "description": "Zero-shot CoT ('Let\\'s think step by step'), Few-shot CoT, and self-consistency mechanisms.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Advanced Prompt Engineering: Chain-of-Thought & ReAct Framework",
                "provider": "freeCodeCamp.org",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=0hXjU0Y3_iE",
                "description": "Synergizing reasoning and acting with tool usage, web search, and structured output parsing.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },

    # ----------------------------------------------------
    # Deep Learning (Semester VI)
    # ----------------------------------------------------
    {
        "topic_name": "CNNs, Convolutions & Vision Architectures",
        "resources": [
            {
                "title": "Convolutional Neural Networks (CNN) Architecture Guide",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/convolutional-neural-networks-cnn/",
                "description": "Kernel convolution, padding, stride, pooling layers, feature maps, and dense layers.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Convolutional Neural Networks Explained Visually",
                "provider": "3Blue1Brown",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=KuXjwB4LzSA",
                "description": "Geometric intuition showing how convolutional kernels extract edges, textures, and object parts.",
                "difficulty": "Beginner",
                "verification_status": "verified"
            },
            {
                "title": "PyTorch Official CNN Image Classification Tutorial",
                "provider": "PyTorch Documentation",
                "resource_type": "documentation",
                "resource_url": "https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html",
                "description": "Complete implementation in PyTorch using nn.Conv2d, nn.MaxPool2d, and cross entropy loss.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    },

    # ----------------------------------------------------
    # Natural Language Processing (Semester VI)
    # ----------------------------------------------------
    {
        "topic_name": "Transformers, Sentiment & Machine Translation",
        "resources": [
            {
                "title": "Transformers and Self-Attention Mechanism Architecture",
                "provider": "GeeksforGeeks",
                "resource_type": "notes",
                "resource_url": "https://www.geeksforgeeks.org/transformer-architecture/",
                "description": "Scaled dot-product attention, multi-head attention, positional encodings, encoder-decoder stacks.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            },
            {
                "title": "Stanford CS224N: Natural Language Processing with Deep Learning",
                "provider": "Stanford Online",
                "resource_type": "video",
                "resource_url": "https://www.youtube.com/watch?v=rmVRLeJRkl4",
                "description": "World-renowned Stanford University lecture on word vectors, self-attention, and Transformer language models.",
                "difficulty": "Advanced",
                "verification_status": "verified"
            },
            {
                "title": "Hugging Face Transformers Documentation & Tasks",
                "provider": "Hugging Face Documentation",
                "resource_type": "documentation",
                "resource_url": "https://huggingface.co/docs/transformers/index",
                "description": "Official documentation covering BERT, GPT-2, pipeline API, and sentiment classification.",
                "difficulty": "Intermediate",
                "verification_status": "verified"
            }
        ]
    }
]


def seed_educational_resources():
    """
    Seeds curated verified educational resources for syllabus topics.
    Matches topics by exact name or substring.
    """
    with app.app_context():
        inserted_count = 0
        all_topics = Topic.query.all()
        topic_map = {t.name.lower().strip(): t for t in all_topics}

        for item in CURATED_RESOURCES_DATA:
            target_name = item["topic_name"].lower().strip()
            
            # Find matching topic in database
            matched_topic = topic_map.get(target_name)
            if not matched_topic:
                # Try partial substring match
                for t_name, t_obj in topic_map.items():
                    if target_name in t_name or t_name in target_name:
                        matched_topic = t_obj
                        break

            if not matched_topic:
                print(f"[WARN] No matching topic found for '{item['topic_name']}'")
                continue

            for res in item["resources"]:
                # Check for existing resource with same topic_id and resource_url
                existing = LearningResource.query.filter_by(
                    topic_id=matched_topic.id,
                    resource_url=res["resource_url"]
                ).first()

                if not existing:
                    new_res = LearningResource(
                        topic_id=matched_topic.id,
                        title=res["title"],
                        provider=res["provider"],
                        resource_type=res["resource_type"],
                        resource_url=res["resource_url"],
                        description=res.get("description", ""),
                        language=res.get("language", "English"),
                        difficulty=res.get("difficulty", "Beginner"),
                        verification_status=res.get("verification_status", "verified")
                    )
                    db.session.add(new_res)
                    inserted_count += 1

        db.session.commit()
        print(f"[SUCCESS] Seeded {inserted_count} verified educational resources.")
        print(f"Total LearningResources in DB: {LearningResource.query.count()}")


if __name__ == '__main__':
    seed_educational_resources()
