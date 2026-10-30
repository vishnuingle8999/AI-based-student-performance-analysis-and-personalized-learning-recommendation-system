# -*- coding: utf-8 -*-
"""
Generate 300 DBATU Questions for Semester V (60 questions for each of the 5 subjects)
Units are strictly mapped to the updated DBATU AI&DS Syllabus.
"""

def get_sem5_questions():
    questions = []

    # =========================================================================
    # SUBJECT 1: Machine Learning (60 Questions: 12 per Unit)
    # =========================================================================
    sub = "Machine Learning"
    branch = "Artificial Intelligence & Data Science"
    year = "Third Year"
    sem = "Semester V"

    # --- Unit 1: Foundations of Machine Learning & Supervised Learning (12 Qs) ---
    u1 = "Unit 1: Foundations of Machine Learning & Supervised Learning"
    t1_1 = "Linear Regression & Inductive Bias"
    t1_2 = "Decision Trees & Instance-Based Learning"

    ml_u1 = [
        (t1_1, "What is the primary objective of the cost function (Mean Squared Error) in Linear Regression?",
         "Maximize the distance between predicted and actual data points",
         "Minimize the sum of squared differences between observed and predicted values",
         "Maximize the variance of the explanatory variables",
         "Convert continuous outputs into discrete binary classes", "B", "Easy"),

        (t1_1, "Which concept describes the set of all assumptions a learning algorithm makes to predict outputs for unseen data?",
         "Sample complexity", "Inductive bias", "Hypothesis variance", "Occam margin", "B", "Medium"),

        (t1_1, "In Linear Regression with multiple features, what matrix equation computes the analytical closed-form weights (Normal Equation)?",
         "theta = (X^T * X)^(-1) * X^T * y",
         "theta = X * (X^T * X) * y",
         "theta = (X * X^T)^(-1) * y",
         "theta = X^T * (y - X)", "A", "Hard"),

        (t1_1, "What is the primary purpose of applying k-fold cross-validation during model training?",
         "To guarantee zero training error on the entire dataset",
         "To assess model generalizability and prevent overly optimistic performance estimates",
         "To reduce computational complexity of gradient descent to O(1)",
         "To convert unsupervised algorithms into supervised ones", "B", "Easy"),

        (t1_1, "If a machine learning model achieves 99.8% accuracy on training data but drops to 52% on test data, the model is suffering from:",
         "High bias (Underfitting)", "High variance (Overfitting)", "Zero sample complexity", "Gradient explosion", "B", "Easy"),

        (t1_1, "Which technique introduces an L2 penalty on regression coefficients to shrink weights and mitigate multicollinearity?",
         "Lasso Regression", "Ridge Regression", "Elastic Net L1 exclusively", "Polynomial expansion", "B", "Medium"),

        (t1_2, "In decision tree learning algorithms like ID3, which metric measures the expected reduction in entropy after partitioning by an attribute?",
         "Gini Impurity", "Information Gain", "Residual Sum of Squares", "Silhouette Coefficient", "B", "Easy"),

        (t1_2, "What is the theoretical maximum value of binary entropy for a classification node with two equally likely classes (p = 0.5)?",
         "0.0", "0.5", "1.0", "Infinity", "C", "Medium"),

        (t1_2, "How does post-pruning a decision tree improve generalization performance on unseen test data?",
         "By converting continuous attributes into categorical strings",
         "By removing lower branches that capture random noise and overfitting artifacts",
         "By expanding leaves until every sample is purely isolated",
         "By replacing the tree with a linear regression line", "B", "Medium"),

        (t1_2, "Which characteristic distinguishes k-Nearest Neighbors (k-NN) as an 'instance-based' or 'lazy' learner?",
         "It constructs an explicit global decision boundary during the training phase",
         "It defers computation until query time, storing training instances in memory without prior model building",
         "It requires extensive backpropagation epochs to learn weights",
         "It is strictly restricted to binary classification tasks", "B", "Medium"),

        (t1_2, "In Principal Component Analysis (PCA) for feature reduction, principal components are chosen such that they are:",
         "Orthogonal to each other and maximize the captured data variance",
         "Linearly dependent and minimize the covariance matrix determinant",
         "Strictly parallel to the original coordinate axes",
         "Non-invertible and normalized between 0 and 1", "A", "Hard"),

        (t1_2, "Which collaborative filtering approach computes user ratings based on similarity between item interaction vectors?",
         "User-based collaborative filtering", "Item-based collaborative filtering",
         "Content-based keyword matching", "Decision forest ranking", "B", "Easy")
    ]

    # --- Unit 2: Probabilistic Learning, Bayes & Support Vector Machines (12 Qs) ---
    u2 = "Unit 2: Probabilistic Learning, Bayes & Support Vector Machines"
    t2_1 = "Bayes Theorem & Logistic Regression"
    t2_2 = "Support Vector Machines & Kernel Methods"

    ml_u2 = [
        (t2_1, "What fundamental 'naive' assumption does the Naive Bayes classifier make regarding input features?",
         "All features follow a strict uniform distribution",
         "Features are conditionally independent given the class label",
         "Features must be strictly orthogonal in Euclidean space",
         "Feature values must always be continuous real numbers", "B", "Easy"),

        (t2_1, "Why is Laplace (additive) smoothing applied when calculating probabilities in Naive Bayes text classification?",
         "To prevent division by zero or zero probability when a word does not occur in training data",
         "To convert words into lower-dimensional dense vectors",
         "To remove punctuation and stop words automatically",
         "To accelerate matrix inversion in high-dimensional datasets", "A", "Medium"),

        (t2_1, "In Logistic Regression, which link function maps linear combination z = w^T * x + b into a probability range (0, 1)?",
         "Rectified Linear Unit (ReLU)", "Hyperbolic Tangent (Tanh)", "Standard Sigmoid (Logistic) Function", "Softmax Function", "C", "Easy"),

        (t2_1, "What is the standard loss function optimized in binary Logistic Regression via gradient descent?",
         "Mean Squared Error (MSE)", "Binary Cross-Entropy (Log Loss)", "Hinge Loss", "Kullback-Leibler Divergence", "B", "Medium"),

        (t2_1, "If the odds of an event occurring are 3:1, what is the corresponding predicted probability of the event?",
         "0.25", "0.33", "0.75", "0.90", "C", "Medium"),

        (t2_1, "Maximum Likelihood Estimation (MLE) in probabilistic models seeks parameter values that:",
         "Minimize the prior probability distribution",
         "Maximize the probability of observing the given training data",
         "Force all model weights to be strictly zero",
         "Eliminate all outlier records from the dataset", "B", "Hard"),

        (t2_2, "In Support Vector Machines (SVM), what are 'support vectors'?",
         "All data points located in the interior of the class cluster",
         "The critical training points that lie closest to the decision boundary and define the margin",
         "Hyperplane normal vectors that do not touch any training samples",
         "Synthetic samples generated via SMOTE oversampling", "B", "Easy"),

        (t2_2, "What type of optimization problem is formulated when deriving the maximum margin hyperplane for a linear SVM?",
         "Unconstrained linear programming problem",
         "Convex quadratic programming problem with linear inequality constraints",
         "Non-convex combinatorial integer optimization",
         "Eigenvalue decomposition of an asymmetric matrix", "B", "Hard"),

        (t2_2, "In soft-margin SVM, what is the operational effect of choosing a very large regularization penalty parameter C?",
         "The optimizer permits wide margins with numerous misclassified points",
         "The optimizer heavily penalizes margin violations, leading to narrower margins and potential overfitting",
         "The margin width becomes infinite",
         "The kernel function is automatically disabled", "B", "Hard"),

        (t2_2, "What is the primary advantage of the 'Kernel Trick' in Support Vector Machines?",
         "It projects data into higher-dimensional space implicitly by computing inner products without explicit coordinate mapping",
         "It simplifies quadratic programming to a linear regression closed-form solution",
         "It guarantees zero validation error on all non-linear datasets",
         "It reduces training time complexity to O(log n)", "A", "Medium"),

        (t2_2, "Which popular SVM kernel function is defined as K(x, z) = exp(-gamma * ||x - z||^2)?",
         "Linear Kernel", "Polynomial Kernel", "Radial Basis Function (RBF / Gaussian) Kernel", "Sigmoid Hyperbolic Kernel", "C", "Easy"),

        (t2_2, "Which loss function is utilized natively in the primal formulation of Support Vector Machines?",
         "Cross-entropy loss", "Hinge loss: max(0, 1 - y * f(x))", "Mean Absolute Error", "Huber loss", "B", "Medium")
    ]

    # --- Unit 3: Perceptrons, Neural Networks & Backpropagation (12 Qs) ---
    u3 = "Unit 3: Perceptrons, Neural Networks & Backpropagation"
    t3_1 = "Artificial Neurons & Perceptron Learning"
    t3_2 = "Multilayer Networks & Backpropagation"

    ml_u3 = [
        (t3_1, "What was the historic mathematical limitation of the single-layer Rosenblatt Perceptron proven by Minsky and Papert (1969)?",
         "It could not compute basic logical AND functions",
         "It was incapable of learning non-linearly separable logic functions like XOR",
         "It could only accept binary inputs, not continuous numbers",
         "It required infinite training iterations to converge on linearly separable data", "B", "Easy"),

        (t3_1, "According to the Perceptron Convergence Theorem, what condition guarantees the perceptron will find a separating hyperplane in finite steps?",
         "The learning rate must decay exponentially to zero",
         "The training dataset must be linearly separable",
         "All input features must be normalized between -1 and +1",
         "The activation function must be continuously differentiable", "B", "Medium"),

        (t3_1, "In the McCulloch-Pitts neuron model, what determines whether the neuron produces an output of 1?",
         "The weighted sum of inputs must exceed a predefined threshold without active inhibitory inputs",
         "The backpropagated error must equal zero",
         "The softmax distribution must sum to exactly 1.0",
         "The derivative of the loss must be negative", "A", "Medium"),

        (t3_1, "What type of decision boundary is produced by a single artificial neuron with a linear combination of two inputs?",
         "A parabolic curve", "A straight line in 2D space", "A closed circular contour", "A discontinuous step curve", "B", "Easy"),

        (t3_2, "Which mathematical principle provides the foundation for computing gradient updates layer-by-layer in Backpropagation?",
         "L'Hopital's Rule", "Cauchy-Schwarz Inequality", "Multivariate Calculus Chain Rule", "Euler's Totient Theorem", "C", "Easy"),

        (t3_2, "What computational issue occurs when deep networks use Sigmoid or Tanh activations across many hidden layers?",
         "Dying ReLU explosion", "Vanishing Gradient Problem where gradients diminish exponentially toward early layers",
         "Weight matrix inversion singularity", "Underflow of the learning rate", "B", "Medium"),

        (t3_2, "Why is the Rectified Linear Unit (ReLU), f(x) = max(0, x), predominantly used in deep neural network hidden layers?",
         "It outputs bounded probabilities between 0 and 1",
         "Its derivative is 1 for positive inputs, mitigating vanishing gradients and enabling fast sparse computation",
         "It prevents dead neurons completely under all negative weight updates",
         "It is continuously differentiable across all real numbers including x = 0", "B", "Medium"),

        (t3_2, "What distinguishes Stochastic Gradient Descent (SGD) with mini-batches from standard Batch Gradient Descent?",
         "Mini-batch SGD updates weights using a small random subset of samples per step rather than the entire dataset",
         "Mini-batch SGD evaluates the analytical Hessian matrix at every step",
         "Batch Gradient Descent updates weights after every single individual training sample",
         "Mini-batch SGD guarantees exact global minimum convergence without oscillations", "A", "Easy"),

        (t3_2, "In neural network optimization, what is the role of the 'Momentum' parameter?",
         "To randomly drop neuron connections during forward propagation",
         "To accelerate gradient vectors in the relevant direction and dampen high-frequency oscillations across ravines",
         "To scale training inputs to zero mean and unit variance",
         "To clamp weights between -1.0 and +1.0", "B", "Medium"),

        (t3_2, "In a feedforward neural network with 10 input neurons, 1 hidden layer of 20 neurons, and 3 output neurons (all with bias), how many total trainable weights exist?",
         "200 weights", "283 weights (20*10 + 20 biases + 3*20 + 3 biases)", "300 weights", "240 weights", "B", "Hard"),

        (t3_2, "Which activation function is most appropriate for the final layer of a multi-class classification neural network with mutually exclusive classes?",
         "Sigmoid", "Softmax", "ReLU", "Tanh", "B", "Easy"),

        (t3_2, "Why is Xavier (Glorot) weight initialization preferred over initializing all neural network weights to identical constants (e.g., zero)?",
         "Identical weights cause symmetric neurons to compute identical gradients and fail to learn distinct features",
         "Zero initialization causes immediate numeric overflow in floating point registers",
         "Xavier initialization guarantees zero loss after the first epoch",
         "It eliminates the need for activation functions in hidden layers", "A", "Hard")
    ]

    # --- Unit 4: Computational Learning Theory & Ensembles (12 Qs) ---
    u4 = "Unit 4: Computational Learning Theory & Ensembles"
    t4_1 = "PAC Learning & VC Dimension"
    t4_2 = "Ensemble Methods & Tree Bagging/Boosting"

    ml_u4 = [
        (t4_1, "In Leslie Valiant's Probably Approximately Correct (PAC) learning framework, what does 'Approximately' formally represent?",
         "The probability of the learning algorithm terminating in polynomial time is at least 1 - delta",
         "The error of the learned hypothesis on unseen instances is bounded by epsilon: error(h) <= epsilon",
         "The training error must equal zero on all samples",
         "The hypothesis space must be infinitely countable", "B", "Medium"),

        (t4_1, "In PAC learning, what does 'Probably' formally represent?",
         "The probability that the hypothesis error exceeds epsilon is bounded by confidence parameter delta: Pr[error(h) <= epsilon] >= 1 - delta",
         "The algorithm executes probabilistic Monte Carlo sampling",
         "Features are assumed to follow a Gaussian normal distribution",
         "The number of training samples is strictly finite", "A", "Medium"),

        (t4_1, "What does the Vapnik-Chervonenkis (VC) dimension of a hypothesis space H measure?",
         "The number of floating point parameters required to store H",
         "The maximum cardinality of a set of points that can be shattered (assigned all possible binary labels) by H",
         "The computational time complexity required to fit H using gradient descent",
         "The ratio of training samples to testing samples", "B", "Hard"),

        (t4_1, "What is the VC dimension of linear classifiers (hyperplanes) in 2-dimensional space?",
         "2", "3", "4", "Infinite", "B", "Medium"),

        (t4_1, "Sample complexity in computational learning theory defines:",
         "The maximum memory occupied by the dataset during training",
         "The minimum number of training examples required to guarantee PAC learnability within (epsilon, delta) bounds",
         "The total number of floating point multiplications per training epoch",
         "The ratio of positive to negative examples in the ground truth distribution", "B", "Medium"),

        (t4_1, "According to Occam's Razor in machine learning, given two hypotheses with similar training error, one should prefer:",
         "The hypothesis with the maximum number of parameters and highest VC dimension",
         "The simpler hypothesis with lower complexity and fewer arbitrary assumptions",
         "The hypothesis trained over the greatest number of iterations",
         "The hypothesis utilizing non-linear polynomial kernels", "B", "Easy"),

        (t4_2, "What ensemble technique trains multiple base estimators on random bootstrap samples drawn with replacement from the training set?",
         "Boosting", "Bagging (Bootstrap Aggregating)", "Stacking with a meta-learner", "Gradient Ascent", "B", "Easy"),

        (t4_2, "How does a Random Forest introduce additional decorrelation among trees compared to standard bagging?",
         "By selecting a random subset of features at each candidate split point",
         "By assigning higher weights to misclassified instances after each tree is built",
         "By constraining all trees to have a maximum depth of 1",
         "By converting continuous features into one-hot binary matrices", "A", "Medium"),

        (t4_2, "In the AdaBoost algorithm, what happens to training samples that are misclassified by the current weak classifier?",
         "They are permanently removed from subsequent training rounds",
         "Their weights are increased so subsequent classifiers focus more on difficult instances",
         "Their features are normalized to zero mean",
         "They are assigned to the validation holdout split", "B", "Easy"),

        (t4_2, "What is the key algorithmic difference between Bagging and Boosting?",
         "Bagging builds models sequentially to reduce bias, whereas Boosting builds models in parallel to reduce variance",
         "Bagging builds models in parallel to reduce variance, whereas Boosting builds models sequentially to reduce bias",
         "Bagging only works on neural networks while Boosting only works on decision trees",
         "There is no operational difference; both names are interchangeable", "B", "Medium"),

        (t4_2, "Which prominent gradient boosted tree library optimizes loss via second-order Taylor expansion and incorporates tree-depth regularization?",
         "Scikit-learn Perceptron", "XGBoost (Extreme Gradient Boosting)", "Weka J48", "Pandas Rolling Aggregate", "B", "Medium"),

        (t4_2, "What components comprise the expected generalization error under the Bias-Variance Decomposition?",
         "Bias^2 + Variance + Irreducible Noise",
         "Precision + Recall + F1 Score",
         "Entropy - Information Gain",
         "Training Error + Test Error", "A", "Hard")
    ]

    # --- Unit 5: Clustering & Unsupervised Learning (12 Qs) ---
    u5 = "Unit 5: Clustering & Unsupervised Learning"
    t5_1 = "K-Means & Hierarchical Clustering"
    t5_2 = "Gaussian Mixture Models & Expectation Maximization"

    ml_u5 = [
        (t5_1, "What objective function does the standard K-Means clustering algorithm attempt to minimize?",
         "Within-Cluster Sum of Squares (Inertia)",
         "Between-cluster maximum margin distance",
         "Log-likelihood of a uniform distribution",
         "Total number of leaf nodes in the dendrogram", "A", "Easy"),

        (t5_1, "How does the K-Means++ initialization algorithm improve upon standard random centroid selection?",
         "It sets all centroids to the global dataset origin (0, 0)",
         "It chooses initial cluster centers with probability proportional to the squared distance from nearest existing center",
         "It runs PCA first and places centroids on the main eigenvector",
         "It assigns every data point its own individual centroid", "B", "Medium"),

        (t5_1, "When evaluating clustering performance without ground truth labels, what does a Silhouette Score of +0.85 indicate?",
         "Points are assigned to overlapping clusters with high ambiguity",
         "Points are well-matched to their own cluster and poorly matched to neighboring clusters (strong separation)",
         "Points are completely misclassified and should be assigned to adjacent clusters",
         "The dataset has zero variance across all dimensions", "B", "Medium"),

        (t5_1, "In the Elbow Method for determining optimal K in K-Means, what is plotted on the Y-axis against the number of clusters K?",
         "Classification accuracy percentage", "Sum of Squared Errors (Inertia)", "Receiver Operating Characteristic area", "F1 score", "B", "Easy"),

        (t5_1, "Which hierarchical clustering approach starts with all data points in a single giant cluster and iteratively splits them into smaller clusters?",
         "Agglomerative (Bottom-up) approach", "Divisive (Top-down) approach", "K-Means Lloyd partitioning", "DBSCAN density expansion", "B", "Easy"),

        (t5_1, "In agglomerative hierarchical clustering, what does 'Complete Linkage' define as the distance between two clusters?",
         "The minimum distance between any single pair of points in the two clusters",
         "The maximum distance between any single pair of points in the two clusters",
         "The distance between the centroids of the two clusters",
         "The average variance of all points in both clusters combined", "B", "Medium"),

        (t5_1, "What visual tree-like diagram illustrates the sequence of merges or splits in hierarchical clustering?",
         "Scatter plot matrix", "Dendrogram", "Voronoi tessellation", "Residual plot", "B", "Easy"),

        (t5_2, "Why are Gaussian Mixture Models (GMM) referred to as 'soft clustering' compared to K-Means?",
         "GMM requires integer coordinate values for all observations",
         "GMM assigns each observation a probability of belonging to each cluster rather than a rigid hard assignment",
         "GMM only works on 2-dimensional image data",
         "GMM does not compute distance metrics between data points", "B", "Easy"),

        (t5_2, "Which iterative algorithm is employed to estimate parameters (means, covariances, mixing coefficients) in Gaussian Mixture Models?",
         "Backpropagation with Adam optimizer", "Expectation-Maximization (EM) Algorithm", "Nelder-Mead Simplex method", "QuickSort Partitioning", "B", "Medium"),

        (t5_2, "During the Expectation (E-step) of the EM algorithm for GMMs, what is computed?",
         "Model parameters are re-estimated using maximum likelihood updates",
         "Posterior probabilities (responsibilities) of each latent Gaussian component generating each data point are evaluated",
         "Cluster centroids are discarded and randomly reinitialized",
         "The covariance matrix is constrained to be strictly spherical", "B", "Hard"),

        (t5_2, "During the Maximization (M-step) of the EM algorithm for GMMs, what occurs?",
         "The responsibilities from the E-step are used to update component means, covariances, and mixing proportions",
         "New data points are generated via Markov Chain Monte Carlo sampling",
         "Eigenvectors of the dataset are rotated by 90 degrees",
         "Outlier points are clipped to 3 standard deviations", "A", "Hard"),

        (t5_2, "What geometric cluster shapes can Gaussian Mixture Models accommodate that standard K-Means cannot effectively capture?",
         "Only strictly spherical clusters of equal radius",
         "Ellipsoidal clusters of arbitrary orientation, size, and varying variance across dimensions",
         "Only rectilinear diamond-shaped clusters",
         "Clusters constrained to 1-dimensional lines only", "B", "Medium")
    ]

    for q in ml_u1:
        questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ml_u2:
        questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ml_u3:
        questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ml_u4:
        questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in ml_u5:
        questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))

    return questions


def get_java_questions():
    questions = []
    sub = "Object Oriented Programming in Java"
    branch = "Artificial Intelligence & Data Science"
    year = "Third Year"
    sem = "Semester V"

    # --- Unit 1: Introduction to Object Technology & Java Basics (12 Qs) ---
    u1 = "Unit 1: Introduction to Object Technology & Java Basics"
    t1_1 = "Java Platform & Fundamentals"
    t1_2 = "Control Structures & Iteration"

    java_u1 = [
        (t1_1, "What component of the Java execution architecture is responsible for converting Java bytecode (.class) into native machine code at runtime?",
         "Java Development Kit (JDK)", "Java Virtual Machine (JVM) Just-In-Time (JIT) Compiler",
         "Java Source Compiler (javac)", "Java Archive Tool (jar)", "B", "Easy"),

        (t1_1, "Which of the following is NOT a primitive data type in the core Java language specification?",
         "boolean", "int", "String", "float", "C", "Easy"),

        (t1_1, "In Java, what is the default value assigned to an uninitialized instance variable of type boolean?",
         "true", "false", "null", "0", "B", "Easy"),

        (t1_1, "Which class in the java.util package is used to parse primitive types and strings from console input streams?",
         "BufferedReader", "Scanner", "System.in.parser", "ConsoleReader", "B", "Easy"),

        (t1_1, "What happens when an expression combines an int variable and a double variable in Java?",
         "A compile-time type mismatch error occurs",
         "The int value is implicitly widened (promoted) to double before the operation executes",
         "The double is truncated into an integer",
         "An ArithmeticException is thrown at runtime", "B", "Medium"),

        (t1_1, "What is the result of the integer division expression 7 / 2 in Java?",
         "3.5", "3", "4", "3.0", "B", "Easy"),

        (t1_2, "Which loop structure in Java is guaranteed to execute its code body at least once regardless of the condition test?",
         "for loop", "while loop", "do-while loop", "enhanced for-each loop", "C", "Easy"),

        (t1_2, "What is the primary operational distinction between 'break' and 'continue' statements inside a Java loop?",
         "'break' terminates the entire enclosing loop; 'continue' skips the remainder of current iteration and proceeds to next",
         "'continue' terminates the loop; 'break' restarts from iteration zero",
         "'break' can only be used in switch statements, never in loops",
         "Both statements execute the exact same operation in bytecode", "A", "Easy"),

        (t1_2, "What occurs if a 'break' statement is omitted from a non-empty case branch inside a standard Java switch construct?",
         "A compiler error is raised immediately",
         "Execution falls through into the subsequent case statements until a break or end of switch is reached",
         "The switch statement restarts from the beginning",
         "The JVM throws a NullPointerException", "B", "Medium"),

        (t1_2, "Which iteration pattern uses a distinct, predetermined sentinel value (such as -1) to terminate user input collection?",
         "Counter-controlled repetition", "Sentinel-controlled repetition", "Infinite recursion", "For-each array traversal", "B", "Medium"),

        (t1_2, "In Java, what evaluates the short-circuit logical AND operator (&&)?",
         "Both operands are always evaluated regardless of the left operand's truth value",
         "If the left operand evaluates to false, the right operand is never evaluated and the result is false",
         "If the left operand evaluates to true, the right operand is skipped",
         "It performs a bitwise conjunction on binary integer representations", "B", "Medium"),

        (t1_2, "What is the output of the Java expression: int x = 5; System.out.println(x++ + ++x);?",
         "10", "11", "12", "13", "C", "Hard")
    ]

    # --- Unit 2: Methods, Arrays and Strings (12 Qs) ---
    u2 = "Unit 2: Methods, Arrays and Strings"
    t2_1 = "Methods & Stack Execution"
    t2_2 = "Arrays & String Manipulation"

    java_u2 = [
        (t2_1, "Which keyword denotes that a Java method belongs to the class itself rather than to specific object instances?",
         "abstract", "static", "final", "transient", "B", "Easy"),

        (t2_1, "How are method arguments passed in Java?",
         "Primitive types are passed by reference; objects are passed by value",
         "Java is strictly pass-by-value for all arguments (where the value of an object variable is the reference/pointer)",
         "Java is pass-by-reference for all objects and primitives",
         "Argument passing mechanism depends on the operating system architecture", "B", "Medium"),

        (t2_1, "What determines method overloading in Java?",
         "Methods sharing identical names but differing in parameter types, number, or order of parameters within the same class",
         "Methods with different access modifiers only",
         "Methods differing exclusively by return type",
         "Methods declared in subclasses with identical signatures", "A", "Medium"),

        (t2_1, "What memory structure manages method call frames, local variables, and return addresses during Java execution?",
         "Java Heap Space", "Call Stack (Thread Stack)", "Metaspace / Method Area", "Permanent Generation", "B", "Easy"),

        (t2_1, "Which Java syntax defines a variable-length argument list (varargs) in a method signature?",
         "public void display(int... numbers)", "public void display(int[]... numbers)",
         "public void display(vararg int numbers)", "public void display(params int numbers)", "A", "Easy"),

        (t2_1, "What runtime error occurs if a recursive Java method lacks a terminating base case?",
         "OutOfMemoryError: Java heap space", "StackOverflowError", "IllegalStateException", "ConcurrentModificationException", "B", "Medium"),

        (t2_2, "What is the index of the last element in a Java array declared as: int[] arr = new int[10];?",
         "10", "9", "0", "-1", "B", "Easy"),

        (t2_2, "Why are java.lang.String objects described as 'immutable' in Java?",
         "String objects cannot be inherited by subclasses",
         "Once a String object is created in memory, its character contents cannot be altered; modifications create new objects",
         "Strings can only hold fixed-size ASCII characters",
         "Strings are automatically deleted after the enclosing method terminates", "B", "Medium"),

        (t2_2, "Where are literal String values (e.g. \"hello\") stored inside the JVM to optimize memory consumption?",
         "Thread Stack Frame", "String Constant Pool (interned strings in Heap)", "Direct Native Byte Buffer", "Register Cache", "B", "Medium"),

        (t2_2, "What is the key functional difference between String and StringBuilder in Java?",
         "String is mutable whereas StringBuilder is immutable",
         "StringBuilder is mutable and designed for efficient string concatenation without creating intermediate objects",
         "StringBuilder is synchronized and thread-safe whereas StringBuffer is unsynchronized",
         "StringBuilder cannot append numerical values", "B", "Easy"),

        (t2_2, "What method checks for structural character-sequence equality between two String objects in Java?",
         "s1 == s2", "s1.equals(s2)", "s1.compareTo(s2) == 1", "s1 = s2", "B", "Easy"),

        (t2_2, "Which method in the java.lang.String class splits a string around matches of a given regular expression?",
         "tokenize()", "split(String regex)", "substring()", "slice()", "B", "Easy")
    ]

    # --- Unit 3: Classes, Objects & OOP Principles (12 Qs) ---
    u3 = "Unit 3: Classes, Objects & OOP Principles"
    t3_1 = "Encapsulation & Constructors"
    t3_2 = "Inheritance & Polymorphism"

    java_u3 = [
        (t3_1, "Which OOP concept bundles data (instance variables) and methods together while restricting direct external access?",
         "Polymorphism", "Encapsulation", "Dynamic Binding", "Multiple Inheritance", "B", "Easy"),

        (t3_1, "What is the default constructor in a Java class?",
         "A constructor that takes all fields as parameters",
         "A compiler-generated zero-argument constructor inserted only if no explicit constructor is defined by the developer",
         "A private constructor that prevents object instantiation",
         "A constructor defined inside an interface", "B", "Medium"),

        (t3_1, "What is the purpose of the 'this' keyword in Java instance methods?",
         "It references the current instance of the class executing the method",
         "It calls methods from the superclass",
         "It creates a new thread in the JVM",
         "It releases memory directly to garbage collection", "A", "Easy"),

        (t3_1, "Which access modifier restricts member visibility strictly to the declaring class itself?",
         "protected", "default (package-private)", "private", "public", "C", "Easy"),

        (t3_1, "What is the effect of applying the 'final' keyword to a class declaration in Java?",
         "The class cannot be instantiated",
         "The class cannot be subclassed (inherited from)",
         "All methods in the class must be declared static",
         "The class is automatically made immutable and serialized", "B", "Medium"),

        (t3_1, "What relationship does 'Composition' represent between two classes in object-oriented design?",
         "IS-A relationship", "HAS-A (part-whole) relationship", "USES-A dependency injection", "EXTENDS relationship", "B", "Easy"),

        (t3_2, "Which keyword is used in Java to establish class inheritance (subclassing)?",
         "implements", "extends", "inherits", "instanceof", "B", "Easy"),

        (t3_2, "Why does Java NOT support multiple inheritance of classes (i.e., a class extending multiple classes)?",
         "To prevent the Diamond Problem and ambiguities in method inheritance",
         "Because the JVM stack size is limited to one class per thread",
         "Because garbage collection cannot resolve multiple parent pointers",
         "Multiple inheritance is deprecated by the IEEE standard", "A", "Medium"),

        (t3_2, "In method overriding, what is the significance of the @Override annotation in Java?",
         "It changes the method visibility to public",
         "It instructs the compiler to verify that the annotated method correctly overrides a method in a superclass or interface",
         "It forces the method to execute synchronously across all threads",
         "It makes the method execute in native C code", "B", "Easy"),

        (t3_2, "Which mechanism determines which overridden method implementation to execute at runtime based on the actual object instance?",
         "Static Early Binding", "Dynamic Method Dispatch (Late Binding)", "Preprocessor Linking", "Bytecode Inlining", "B", "Medium"),

        (t3_2, "Which of the following statements about Java Interfaces is TRUE (since Java 8)?",
         "Interfaces can contain instance variable fields with different values per object",
         "Interfaces can contain default methods with concrete implementations and static utility methods",
         "A class can implement at most one single interface",
         "Interfaces must have private constructors", "B", "Medium"),

        (t3_2, "What is a 'Functional Interface' in Java?",
         "An interface with no methods at all (Marker Interface)",
         "An interface containing exactly one abstract method (annotated with @FunctionalInterface)",
         "An interface that extends java.lang.Runnable and java.lang.Callable simultaneously",
         "An interface containing only private static helper methods", "B", "Easy")
    ]

    # --- Unit 4: Exception Handling, Collections & File Processing (12 Qs) ---
    u4 = "Unit 4: Exception Handling, Collections & File Processing"
    t4_1 = "Exception Handling Mechanism"
    t4_2 = "Java Collections Framework & I/O"

    java_u4 = [
        (t4_1, "Which class sits at the top of the entire Java exception and error class hierarchy?",
         "java.lang.Exception", "java.lang.Throwable", "java.lang.Error", "java.lang.RuntimeException", "B", "Easy"),

        (t4_1, "Which of the following is categorized as an 'Unchecked Exception' (inheriting from RuntimeException)?",
         "java.io.IOException", "java.sql.SQLException", "java.lang.NullPointerException", "java.lang.ClassNotFoundException", "C", "Easy"),

        (t4_1, "When does a 'finally' block execute in a Java try-catch-finally construct?",
         "Only when an exception is thrown and caught",
         "Only when no exception occurs in the try block",
         "Always, regardless of whether an exception is raised or caught (unless JVM exits abruptly via System.exit())",
         "Only if the catch block throws a secondary exception", "C", "Easy"),

        (t4_1, "What interface must an I/O resource class implement to be used within a Java 'try-with-resources' statement?",
         "java.io.Serializable", "java.lang.AutoCloseable", "java.lang.Cloneable", "java.util.EventListener", "B", "Medium"),

        (t4_1, "What is the difference between the 'throw' and 'throws' keywords in Java?",
         "'throw' is used to explicitly instantiate and raise an exception; 'throws' is declared in a method signature to specify exceptions it may propagate",
         "'throws' is used inside method bodies to raise errors; 'throw' is placed in class declarations",
         "'throw' handles unchecked exceptions while 'throws' handles errors only",
         "There is no difference; both are interchangeable in modern Java", "A", "Medium"),

        (t4_1, "What happens when an unhandled checked exception is present in a method body without a try-catch block or a throws clause?",
         "The code compiles but crashes silently at runtime",
         "The Java compiler flags a compilation error: unreported exception must be caught or declared to be thrown",
         "The exception is automatically routed to System.err",
         "The JVM automatically retries the method three times", "B", "Easy"),

        (t4_2, "Which Collection interface represents an ordered sequence of elements that allows duplicate values and positional access?",
         "java.util.Set", "java.util.List", "java.util.Map", "java.util.Queue", "B", "Easy"),

        (t4_2, "What is the average time complexity for basic operations (get, put, containsKey) in a well-distributed java.util.HashMap?",
         "O(1)", "O(log n)", "O(n)", "O(n^2)", "A", "Easy"),

        (t4_2, "Which Set implementation in Java maintains elements sorted in ascending natural order (or according to a Comparator)?",
         "HashSet", "LinkedHashSet", "TreeSet", "CopyOnWriteArraySet", "C", "Medium"),

        (t4_2, "What is 'Autoboxing' in Java?",
         "The automatic conversion that the Java compiler makes between primitive types and their corresponding object wrapper classes",
         "Converting bytecode into native machine instructions",
         "Serializing an entire object graph into an XML file",
         "Packaging multiple .class files into an executable JAR file", "A", "Easy"),

        (t4_2, "What exception is thrown when iterating through a Collection using an Iterator and modifying the collection structurally without using iterator methods?",
         "IndexOutOfBoundsException", "ConcurrentModificationException", "IllegalStateException", "UnsupportedOperationException", "B", "Medium"),

        (t4_2, "Which classes in java.io provide buffered character-based input and output for efficient text file processing?",
         "FileInputStream and FileOutputStream", "BufferedReader and BufferedWriter", "DataInputStream and DataOutputStream", "ObjectInputStream and ObjectOutputStream", "B", "Easy")
    ]

    # --- Unit 5: Advanced Java Concepts & JDBC (12 Qs) ---
    u5 = "Unit 5: Advanced Java Concepts & JDBC"
    t5_1 = "Functional Programming & Streams API"
    t5_2 = "Generics & Database Connectivity (JDBC)"

    java_u5 = [
        (t5_1, "Which lambda expression syntax in Java 8 correctly takes two integers (a, b) and returns their sum?",
         "(a, b) -> a + b", "lambda(a, b) => { return a + b; }", "def add(a, b): a + b", "(int a, int b) :: a + b", "A", "Easy"),

        (t5_1, "Which built-in functional interface in java.util.function accepts a single argument of type T and returns a boolean result?",
         "Consumer<T>", "Function<T, R>", "Predicate<T>", "Supplier<T>", "C", "Easy"),

        (t5_1, "What does the method reference syntax 'String::toUpperCase' represent in Java?",
         "A call to an overridden operator",
         "A shorthand lambda syntax referencing the toUpperCase method of the String class",
         "A direct memory pointer to the C++ runtime",
         "An import statement for package java.lang.String", "B", "Easy"),

        (t5_1, "In the Java Streams API, what distinguishes 'Intermediate operations' from 'Terminal operations'?",
         "Intermediate operations (like filter, map) return a new stream and are executed lazily; terminal operations (like collect, forEach) trigger pipeline execution and produce a result",
         "Intermediate operations close the stream; terminal operations keep the stream open indefinitely",
         "Intermediate operations can only process numeric streams",
         "Terminal operations cannot be chained together", "A", "Medium"),

        (t5_1, "Which Java Stream operation collapses all elements into a single accumulated result using an associative accumulation function?",
         "distinct()", "reduce()", "peek()", "flatMap()", "B", "Medium"),

        (t5_1, "What command-line Read-Eval-Print Loop (REPL) tool was introduced in Java 9 to evaluate snippets of Java code interactively?",
         "jdb", "javadoc", "JShell", "javap", "C", "Easy"),

        (t5_2, "What is the primary benefit of using Generics in Java collections (e.g. List<String>)?",
         "Faster JVM startup times",
         "Compile-time type safety and the elimination of explicit type casting and runtime ClassCastExceptions",
         "Allowing collections to store primitive types without autoboxing",
         "Automatic database table generation", "B", "Easy"),

        (t5_2, "In Java Generics, what does the wildcard syntax 'List<? extends Number>' represent?",
         "A list that accepts any Object whatsoever",
         "A covariant bounded wildcard representing a list of Number or any subclass of Number (read-only safe)",
         "A contravariant wildcard that accepts only superclasses of Number",
         "A compilation error in Java syntax", "B", "Hard"),

        (t5_2, "Why is java.sql.PreparedStatement preferred over java.sql.Statement when executing parameterized queries in JDBC?",
         "PreparedStatement compiles queries in advance and protects against SQL Injection vulnerabilities by safely parameterizing inputs",
         "PreparedStatement can only execute SELECT queries whereas Statement executes UPDATEs",
         "Statement requires an open socket while PreparedStatement works offline",
         "PreparedStatement is non-relational and works with NoSQL", "A", "Medium"),

        (t5_2, "Which method of java.sql.Connection disables automatic commit mode to enable explicit multi-statement transaction management?",
         "conn.setReadOnly(true)", "conn.setAutoCommit(false)", "conn.beginTransaction()", "conn.commitAll(false)", "B", "Easy"),

        (t5_2, "Which JDBC object is returned by executeQuery() and functions as a cursor pointing to rows in a relational database table?",
         "java.sql.ResultSet", "java.sql.RowSetManager", "java.sql.DatabaseMetaData", "java.sql.SQLCursor", "A", "Easy"),

        (t5_2, "In Big-O complexity analysis, what is the worst-case search time complexity for a binary search algorithm on a sorted array of N elements?",
         "O(1)", "O(log N)", "O(N)", "O(N log N)", "B", "Easy")
    ]

    for q in java_u1:
        questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in java_u2:
        questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in java_u3:
        questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in java_u4:
        questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in java_u5:
        questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))

    return questions


def get_cloud_ai_questions():
    questions = []
    sub = "Cloud and Distributed AI Systems"
    branch = "Artificial Intelligence & Data Science"
    year = "Third Year"
    sem = "Semester V"

    # --- Unit 1: Introduction to Cloud & Virtualization (12 Qs) ---
    u1 = "Unit 1: Introduction to Cloud & Virtualization"
    t1_1 = "Cloud Computing Fundamentals"
    t1_2 = "Virtualization Technologies"

    cloud_u1 = [
        (t1_1, "According to the NIST definition, which essential cloud characteristic allows compute capabilities to be provisioned automatically without human interaction with service providers?",
         "Broad network access", "On-demand self-service", "Resource pooling", "Rapid elasticity", "B", "Easy"),

        (t1_1, "Which essential cloud characteristic allows computational resources to be elastically provisioned and released to scale rapidly outward and inward with demand?",
         "Measured service", "Resource pooling", "Rapid elasticity", "Multi-tenancy", "C", "Easy"),

        (t1_1, "In the NIST cloud reference model, what pricing and metering characteristic enables automatic control and optimization of resource usage?",
         "Pay-as-you-go / Measured service", "High availability guarantee", "Symmetric encryption", "Static resource allocation", "A", "Easy"),

        (t1_1, "What is a primary technological challenge in public multi-tenant cloud environments?",
         "Compiling bytecode into machine code",
         "Ensuring strong data isolation, tenant privacy, and mitigating side-channel attacks",
         "Inability to run Linux operating systems",
         "Lack of TCP/IP network protocol support", "B", "Medium"),

        (t1_1, "Which historical technology paradigm directly preceded and laid the algorithmic foundation for modern cloud computing?",
         "Vacuum tube mainframes", "Grid computing and Utility computing", "Punch card batch systems", "Client-server local loops", "B", "Medium"),

        (t1_1, "How does resource pooling achieve economies of scale in multi-tenant cloud data centers?",
         "By dedicating separate physical motherboard servers permanently to each customer",
         "By dynamically serving multiple consumers using a multi-tenant model with shared physical and virtual resources",
         "By disabling virtualization layers completely",
         "By restricting network connectivity to local intranets", "B", "Easy"),

        (t1_2, "What is a Type-1 (Bare-Metal) Hypervisor?",
         "A hypervisor that runs as an application process inside a host operating system (e.g., VirtualBox)",
         "A hypervisor that runs directly on physical server hardware without an underlying host OS (e.g., VMware ESXi, Xen)",
         "A container engine that shares the host OS kernel",
         "A browser plugin for cloud gaming", "B", "Easy"),

        (t1_2, "What is the key characteristic of 'Para-virtualization' compared to 'Full Virtualization'?",
         "The guest operating system is modified with hypercalls to be aware of the underlying hypervisor for higher performance",
         "The guest OS runs completely unmodified using binary translation or hardware CPU extensions",
         "It virtualizes only user-level applications without kernel support",
         "It runs exclusively on ARM architecture chips", "A", "Medium"),

        (t1_2, "Which virtualization technology provides lightweight process-level isolation by sharing the host OS kernel rather than emulating full virtual hardware?",
         "Virtual Machine on ESXi", "OS-Level Containerization (e.g., Docker)", "Type-2 Hypervisor VM", "Firmware ROM flashing", "B", "Easy"),

        (t1_2, "What hardware feature introduced in Intel (VT-x) and AMD (AMD-V) processors enabled efficient hardware-assisted full virtualization?",
         "Root and Non-Root CPU execution modes (Ring -1 operations)",
         "Direct memory access for peripheral sound cards",
         "Hardwired single-instruction matrix multipliers",
         "Hardware-level garbage collectors", "A", "Hard"),

        (t1_2, "Which Microsoft hypervisor technology is built directly into Windows Server for enterprise server virtualization?",
         "Hyper-V", "VMware Workstation", "QEMU", "VirtualBox", "A", "Easy"),

        (t1_2, "What is 'Live Migration' in a virtualized cloud cluster?",
         "Moving a powered-off VM disk image between hard drives",
         "Transferring a running virtual machine from one physical host to another with negligible downtime and without interrupting service",
         "Migrating a database from MySQL to PostgreSQL",
         "Rebooting a hypervisor to apply kernel security patches", "B", "Medium")
    ]

    # --- Unit 2: Cloud Architecture & Enterprise Services (12 Qs) ---
    u2 = "Unit 2: Cloud Architecture & Enterprise Services"
    t2_1 = "Cloud Service & Deployment Models"
    t2_2 = "Enterprise Cloud Storage & Scaling"

    cloud_u2 = [
        (t2_1, "In which cloud service delivery model does the cloud vendor provide fundamental compute, networking, and storage while the customer manages the OS, runtime, and apps?",
         "Software as a Service (SaaS)", "Platform as a Service (PaaS)", "Infrastructure as a Service (IaaS)", "Function as a Service (FaaS)", "C", "Easy"),

        (t2_1, "In the Platform as a Service (PaaS) model, which of the following is managed by the cloud customer?",
         "Physical hardware virtualization", "Operating system patches and kernel updates", "Application source code and data", "Data center cooling and power", "C", "Easy"),

        (t2_1, "Which cloud deployment model combines on-premises private cloud infrastructure with public cloud capacity for data burstability and compliance?",
         "Community Cloud", "Hybrid Cloud", "Distributed P2P Cloud", "Edge Mesh Cloud", "B", "Easy"),

        (t2_1, "What metric in a Cloud Service Level Agreement (SLA) measures the percentage of time a service remains operational and accessible?",
         "Mean Time to Repair (MTTR)", "Service Availability / Uptime percentage (e.g. 99.99%)", "Bandwidth consumption", "Packet jitter", "B", "Easy"),

        (t2_1, "What economic transition is achieved when migrating from on-premises enterprise data centers to public cloud infrastructure?",
         "Shifting heavy upfront Capital Expenditure (CapEx) to flexible operational utility billing (OpEx)",
         "Eliminating all networking costs",
         "Increasing physical hardware depreciation costs",
         "Transitioning to fixed 10-year hardware procurement contracts", "A", "Medium"),

        (t2_1, "What is 'Cloud Interoperability'?",
         "The ability of customer applications and services to run across and exchange data seamlessly between multiple heterogeneous cloud providers",
         "The physical connection of fiber optic cables between data centers",
         "The installation of multi-lingual compilers on cloud nodes",
         "Restricting application deployment to a single proprietary cloud API", "A", "Medium"),

        (t2_2, "Which cloud storage type organizes data as discrete units paired with unique identifiers and customizable metadata, accessible via HTTP/REST APIs (e.g. Amazon S3)?",
         "Block Storage (SAN)", "Object Storage", "Network File System (NFS)", "Raw SCSI LUNs", "B", "Easy"),

        (t2_2, "What is the key advantage of Object Storage for storing massive multi-terabyte AI datasets and model checkpoints?",
         "Low latency seek times for transactional random file writes",
         "Massive horizontal scalability, cost efficiency, and rich metadata tagging without rigid directory tree limits",
         "Direct execution of assembly code inside storage blocks",
         "Zero requirement for IP network routing", "B", "Medium"),

        (t2_2, "What is the primary difference between Horizontal Scaling (Scaling Out) and Vertical Scaling (Scaling Up)?",
         "Horizontal scaling adds more physical/virtual machine instances to a pool; Vertical scaling adds more CPU/RAM capacity to an existing single instance",
         "Horizontal scaling increases CPU clock speeds; Vertical scaling adds hard drives",
         "Horizontal scaling is only used for relational databases; Vertical scaling is for web servers",
         "There is no difference in cloud terminology", "A", "Easy"),

        (t2_2, "Which cloud service provides managed relational and NoSQL databases with automated patching, backup, replication, and high-availability (e.g. Amazon RDS)?",
         "Storage-as-a-Service (STaaS)", "Database-as-a-Service (DBaaS)", "Testing-as-a-Service (TaaS)", "Information-as-a-Service (INaaS)", "B", "Easy"),

        (t2_2, "In cloud architecture, what is a 'Reverse Proxy / Load Balancer' used for?",
         "To compile user source code into bytecode",
         "To evenly distribute incoming client traffic across multiple backend server instances to prevent overload and ensure high availability",
         "To encrypt physical storage hard drives",
         "To translate SQL queries into GraphQL", "B", "Easy"),

        (t2_2, "What mechanism allows a cloud infrastructure to dynamically adjust the number of active server instances based on real-time CPU or memory utilization thresholds?",
         "Static Provisioning", "Auto-Scaling", "Firmware Overclocking", "Manual Re-imaging", "B", "Easy")
    ]

    # --- Unit 3: Aneka Cloud Platform Framework (12 Qs) ---
    u3 = "Unit 3: Aneka Cloud Platform Framework"
    t3_1 = "Aneka Container Architecture & Platform Abstraction"
    t3_2 = "Aneka Programming Models & Cloud Deployment"

    cloud_u3 = [
        (t3_1, "What is the fundamental architectural role of the Aneka framework developed by Manjrasoft and Dr. Rajkumar Buyya?",
         "A desktop video player application",
         "A service-oriented cloud application platform for building, scheduling, and managing enterprise distributed computing applications",
         "A relational database query optimizer",
         "A firmware BIOS replacement for ARM processors", "B", "Easy"),

        (t3_1, "What represents the basic deployment and runtime unit in the Aneka enterprise cloud architecture?",
         "Aneka Container", "Aneka Hypervisor", "Aneka Docker Image", "Aneka BIOS", "A", "Easy"),

        (t3_1, "What is the primary responsibility of the Platform Abstraction Layer (PAL) in the Aneka Container?",
         "To isolate the container's core services from the underlying operating system and hardware specifics",
         "To perform audio and video encoding",
         "To bill customers credit cards directly",
         "To generate synthetic deep learning datasets", "A", "Medium"),

        (t3_1, "In the Aneka container service stack, what category of services manages node membership, dynamic resource provisioning, and inter-node communication?",
         "Application Services", "Fabric Services", "Presentation Services", "Graphics Services", "B", "Medium"),

        (t3_1, "Which Aneka services manage accounting, resource reservation, licensing, security, and billing?",
         "Fabric Services", "Foundation Services", "Execution Services", "Hardware Services", "B", "Medium"),

        (t3_1, "What role do Application Services perform within the Aneka platform framework?",
         "Manage the execution of user applications, job scheduling, and task lifecycle according to chosen programming models",
         "Format physical hard drive partitions",
         "Provide cooling control for data center racks",
         "Compile Java code into C++ binaries", "A", "Medium"),

        (t3_2, "Which programming model supported by Aneka executes independent units of computation that take inputs and produce outputs without inter-task communication?",
         "Task Programming Model (Bag of Tasks / Parameter Sweeps)",
         "Shared Memory Thread Model",
         "Actor Concurrency Model",
         "Event Loop Model", "A", "Medium"),

        (t3_2, "How does the Aneka Distributed Thread Model extend standard Windows/Java multithreading across cloud nodes?",
         "By compiling threads into WebAssembly",
         "By allowing threads to execute transparently on remote distributed cloud nodes while maintaining thread synchronization abstractions",
         "By restricting threads to a single core",
         "By converting multi-threaded programs into sequential single-core scripts", "B", "Hard"),

        (t3_2, "Does the Aneka SDK provide support for developing distributed Big Data analytics applications using the MapReduce paradigm?",
         "No, Aneka only supports single-thread programs",
         "Yes, Aneka includes a native MapReduce programming model implementation and runtime",
         "No, Aneka was deprecated before MapReduce was invented",
         "Only when running on mobile devices", "B", "Medium"),

        (t3_2, "Which Aneka deployment mode leverages local enterprise servers and seamlessly bursts additional workload onto public cloud instances (like Amazon EC2) during peak demands?",
         "Private Cloud Deployment Mode", "Public Cloud Deployment Mode", "Hybrid Cloud Deployment Mode", "Air-gapped Mode", "C", "Easy"),

        (t3_2, "What administrative tool does Aneka provide for cloud system administrators to monitor node states, active containers, and job queues in real time?",
         "Aneka Management Console / Administrative Tools", "Windows Task Manager exclusively", "Linux top command", "Docker Desktop CLI", "A", "Easy"),

        (t3_2, "Which programming language and framework was Aneka primarily developed in for enterprise extensibility?",
         "Microsoft .NET / C# and Java", "PHP 5.4", "Assembly 8086", "Fortran 77", "A", "Medium")
    ]

    # --- Unit 4: Distributed AI Systems & GPU Computing (12 Qs) ---
    u4 = "Unit 4: Distributed AI Systems & GPU Computing"
    t4_1 = "Distributed AI Architecture & Compute Infrastructure"
    t4_2 = "GPU Architecture, CUDA & Parallelism Models"

    cloud_u4 = [
        (t4_1, "Why have modern Deep Learning models (such as GPT-4, LLaMA) necessitated the shift from single-node training to Distributed AI Systems?",
         "Modern models contain billions of parameters requiring petabytes of compute and memory far exceeding the capacity of a single GPU/node",
         "Distributed systems run without power supplies",
         "Single GPUs cannot perform floating point operations",
         "Python code cannot run on single GPUs", "A", "Easy"),

        (t4_1, "Which high-speed networking technology is essential in multi-node AI clusters to provide microsecond latency and Remote Direct Memory Access (RDMA)?",
         "Standard 100Mbps Ethernet", "InfiniBand / RoCE (RDMA over Converged Ethernet)", "Bluetooth 5.0", "Dial-up PPP", "B", "Medium"),

        (t4_1, "In distributed AI clusters, what storage characteristic is critical to prevent GPU idle stalls during training data ingestion?",
         "High sequential read throughput and distributed caching (e.g. GPUDirect Storage, Lustre, Ceph)",
         "Single USB 2.0 thumb drive attachment",
         "Magnetic tape storage exclusively",
         "Optical CD-ROM drives", "A", "Medium"),

        (t4_1, "What primary challenge arises in distributed training when scaling across hundreds of worker nodes?",
         "Overfitting disappears completely",
         "Inter-node network communication overhead during gradient synchronization becomes the dominant bottleneck",
         "Batch size becomes negative",
         "All model weights reset to zero", "B", "Medium"),

        (t4_2, "What is the architectural difference between a modern CPU and an enterprise AI GPU (e.g. NVIDIA H100)?",
         "CPUs optimize for low-latency sequential single-thread execution; GPUs optimize for massive throughput via thousands of parallel arithmetic cores",
         "CPUs have thousands of cores; GPUs have only 2 large cores",
         "GPUs cannot perform matrix multiplication",
         "CPUs are designed exclusively for graphics rendering", "A", "Easy"),

        (t4_2, "In NVIDIA's CUDA execution hierarchy, what is the basic execution unit of 32 parallel threads executed synchronously on a Streaming Multiprocessor (SM)?",
         "Thread Block", "Grid", "Warp", "Fiber", "C", "Medium"),

        (t4_2, "Which specialized hardware execution units inside NVIDIA GPUs accelerate deep learning by computing 4x4 or 16x16 mixed-precision matrix multiply-accumulate operations in a single cycle?",
         "Ray Tracing Cores", "Tensor Cores", "DirectX Shader Units", "Rasterizers", "B", "Easy"),

        (t4_2, "What proprietary interconnect provides high-bandwidth, direct GPU-to-GPU communication bypassing the host PCIe bus (up to 900 GB/s on Hopper)?",
         "SATA Express", "NVLink / NVSwitch", "Thunderbolt 3", "RS-232 Serial", "B", "Easy"),

        (t4_2, "In 'Data Parallelism' for distributed neural network training, how is the workload partitioned across GPUs?",
         "The full model replica resides on every GPU, while each GPU receives a distinct partition (mini-batch) of the training dataset",
         "Different layers of the neural network are placed on different GPUs",
         "Individual matrix columns are split across GPUs",
         "One GPU computes forward passes and all other GPUs remain idle", "A", "Easy"),

        (t4_2, "In 'Model Parallelism' (Tensor Parallelism), what happens when a neural network model is too large to fit in a single GPU's VRAM?",
         "The model layers or weight matrices are partitioned across multiple GPUs so that each GPU holds only a shard of the weights",
         "Training is aborted and replaced with a linear regression model",
         "The batch size is multiplied by 10,000",
         "The training data is deleted", "A", "Medium"),

        (t4_2, "How does 'Pipeline Parallelism' (e.g. GPipe) optimize multi-layer deep network training across sequential GPU stages?",
         "By partitioning consecutive layers across sequential GPUs and pipelining micro-batches to keep stages concurrently utilized",
         "By training only the final classification layer and discarding all prior layers",
         "By routing all data through a single CPU core",
         "By disabling backpropagation passes", "A", "Hard"),

        (t4_2, "Which distributed collective communication algorithm synchronizes gradients across N GPUs in 2*(N-1) communication steps with optimal network bandwidth utilization?",
         "Centralized Parameter Server bottleneck", "Ring All-Reduce", "Single-threaded Broadcast", "Random Gossip protocol", "B", "Hard")
    ]

    # --- Unit 5: Distributed Training of AI Models (DDP & FSDP) (12 Qs) ---
    u5 = "Unit 5: Distributed Training of AI Models (DDP & FSDP)"
    t5_1 = "PyTorch Distributed Data Parallel (DDP)"
    t5_2 = "Fully Sharded Data Parallel (FSDP) & Memory Optimization"

    cloud_u5 = [
        (t5_1, "Which core PyTorch package provides distributed communication primitives and collective operations across multiple GPUs and nodes?",
         "torch.autograd", "torch.distributed", "torch.jit", "torchvision", "B", "Easy"),

        (t5_1, "In PyTorch DistributedDataParallel (DDP), how does process management differ from the older single-process multi-threaded DataParallel (DP)?",
         "DDP spawns a separate dedicated operating system process for each GPU, bypassing Python GIL bottlenecks and enabling multi-node scaling",
         "DDP runs all GPUs in a single master thread with a global lock",
         "DDP can only run on CPU cores, not GPUs",
         "DDP does not synchronize gradients between devices", "A", "Medium"),

        (t5_1, "What utility in PyTorch DataLoader ensures that each GPU process receives a unique, non-overlapping subset of the dataset during DDP training?",
         "RandomSampler", "torch.utils.data.distributed.DistributedSampler", "SequentialSampler", "BatchBatcher", "B", "Easy"),

        (t5_1, "When does PyTorch DDP initiate gradient synchronization across GPUs to maximize compute-communication overlap?",
         "It waits until all backward calculations across all layers are 100% finished before sending any data",
         "It asynchronously fires bucketed All-Reduce communications as soon as individual layer gradients finish during the backward pass",
         "It only synchronizes gradients once every 10 epochs",
         "It transmits gradients before the forward pass executes", "B", "Hard"),

        (t5_1, "What environment variables are typically set by torchrun to initialize a distributed process group in PyTorch?",
         "RANK, LOCAL_RANK, WORLD_SIZE, MASTER_ADDR, MASTER_PORT",
         "GPU_NAME, CUDA_CORES, TEMP_DIR",
         "DATABASE_URL, SECRET_KEY, DEBUG",
         "JAVA_HOME, CLASSPATH, PATH", "A", "Medium"),

        (t5_1, "In distributed training, what is the 'World Size'?",
         "The total number of processes participating in the distributed job across all nodes",
         "The total number of training images in the dataset",
         "The floating-point precision of weight tensors",
         "The latency of the physical network switch in milliseconds", "A", "Easy"),

        (t5_2, "What four major memory components consume GPU VRAM during deep learning model training?",
         "Model Parameters (Weights), Gradients, Optimizer States (e.g. Adam moments), and Activations",
         "Source code files, compiler logs, system BIOS, monitor buffers",
         "Screen resolution pixels, HDMI audio buffers, mouse cursors, keyboard keys",
         "CSV header strings, SQLite tables, HTML templates, CSS files", "A", "Medium"),

        (t5_2, "Why does the standard Adam optimizer consume substantial GPU memory (typically 8 bytes per parameter in FP32)?",
         "Because it saves all past training images in memory",
         "Because it maintains running first momentum (mean) and second momentum (uncentered variance) states for every trainable parameter",
         "Because it generates a new decision tree for every weight",
         "Because it duplicates the entire operating system kernel", "B", "Medium"),

        (t5_2, "What technique reduces GPU memory footprint by using FP16 or BF16 for matrix calculations while maintaining FP32 master weights for stability?",
         "Double Precision Training (FP64)", "Automatic Mixed Precision (AMP)", "Integer Quantization exclusively", "Single Core Emulation", "B", "Easy"),

        (t5_2, "What does the Zero Redundancy Optimizer (ZeRO) Stage 1 partition across distributed training nodes?",
         "Optimizer States (Adam first and second moments)", "Gradients only", "Model Parameters only", "Training Data files exclusively", "A", "Hard"),

        (t5_2, "What does PyTorch Fully Sharded Data Parallel (FSDP) shard across data-parallel ranks to train models that exceed single GPU VRAM?",
         "Optimizer states, gradients, and model parameters (equivalent to ZeRO Stage 3)",
         "Only input images, leaving all weights duplicated",
         "Only the final loss function calculation",
         "Only CPU RAM", "A", "Hard"),

        (t5_2, "How does PyTorch FSDP differ fundamentally from standard DDP when training massive 70B+ parameter LLMs?",
         "Standard DDP duplicates full model parameters and optimizer states on every single GPU leading to Out-Of-Memory (OOM); FSDP shards weights and dynamically gathers them on-demand",
         "Standard DDP is faster for multi-trillion parameter models",
         "FSDP does not support PyTorch models",
         "DDP requires no network communication whereas FSDP runs without GPUs", "A", "Hard")
    ]

    for q in cloud_u1:
        questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in cloud_u2:
        questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in cloud_u3:
        questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in cloud_u4:
        questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in cloud_u5:
        questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))

    return questions


def get_data_eng_questions():
    questions = []
    sub = "Data Engineering and Big Data Systems"
    branch = "Artificial Intelligence & Data Science"
    year = "Third Year"
    sem = "Semester V"

    # --- Unit 1: Fundamentals of Data Engineering & Big Data (12 Qs) ---
    u1 = "Unit 1: Fundamentals of Data Engineering & Big Data"
    t1_1 = "Big Data Dimensions & Data Engineering Lifecycle"
    t1_2 = "Batch vs Stream Processing Architectures"

    de_u1 = [
        (t1_1, "Which of the '5 Vs' of Big Data addresses the trustworthiness, authenticity, and data quality/noise of raw ingested data?",
         "Volume", "Velocity", "Veracity", "Variety", "C", "Easy"),

        (t1_1, "Which 'V' describes the explosive diversity of data formats including structured (SQL), semi-structured (JSON, XML), and unstructured (video, audio, text)?",
         "Variety", "Velocity", "Value", "Veracity", "A", "Easy"),

        (t1_1, "What are the core chronological phases of the Data Engineering Lifecycle?",
         "Generation, Storage, Ingestion, Transformation, Serving",
         "Hyperparameter Tuning, Overfitting, Pruning, Deployment",
         "Syntax Parsing, Lexical Scanning, Compilation, Linking",
         "Encryption, Decryption, Hashing, Key Exchange", "A", "Medium"),

        (t1_1, "What is the primary role difference between a Data Engineer and a Data Scientist?",
         "Data Engineers build, optimize, and maintain scalable data pipelines and storage; Data Scientists analyze data and build predictive ML models",
         "Data Engineers write marketing copy; Data Scientists configure network routers",
         "Data Scientists manage physical data center cabling; Data Engineers only design UI graphics",
         "There is no difference; the titles are completely identical", "A", "Easy"),

        (t1_1, "What technology category forms the foundation of the Modern Data Stack (MDS) for cloud-native data warehousing and processing?",
         "Local Excel spreadsheets", "Cloud Data Warehouses (e.g. Snowflake, BigQuery, Databricks)", "Punch card sorting machines", "Single-threaded Perl scripts", "B", "Easy"),

        (t1_1, "Why did traditional monolithic Relational Database Management Systems (RDBMS) fail to scale for Big Data workloads?",
         "They are strictly non-relational and lack SQL syntax",
         "They rely on single-node vertical scaling and cannot handle petabyte-scale distributed horizontal sharding with flexible schemas",
         "They cannot store integer numbers",
         "They do not support network connections", "B", "Medium"),

        (t1_2, "What characterizes 'Batch Processing' compared to 'Stream Processing'?",
         "Batch processing executes on bounded, static datasets collected over time at scheduled intervals; Stream processing processes unbounded events in near real-time",
         "Batch processing processes events within microseconds",
         "Stream processing can only process data once per month",
         "Batch processing only runs on mobile devices", "A", "Easy"),

        (t1_2, "In Big Data architectural design, what is the 'Lambda Architecture'?",
         "An architecture combining a batch layer for comprehensive accuracy and a speed (streaming) layer for low-latency views",
         "An architecture that runs exclusively on serverless AWS Lambda functions",
         "A neural network architecture with recurrent connections",
         "A relational schema design with triangular joins", "A", "Medium"),

        (t1_2, "What simplification does the 'Kappa Architecture' introduce over the Lambda Architecture?",
         "It eliminates the batch processing layer entirely, handling all data processing through a single stream-first processing engine",
         "It eliminates the streaming layer and only uses overnight tape backups",
         "It replaces SQL with assembly language",
         "It requires all data to be stored on floppy disks", "A", "Hard"),

        (t1_2, "What is a 'Distributed File System' (DFS)?",
         "A file system that transparently stores and manages files across a cluster of networked physical nodes, providing fault tolerance and high throughput",
         "A file system that compresses files into ZIP archives on a local C: drive",
         "A file system without file permissions or folder structures",
         "A proprietary software running exclusively on Apple iPhones", "A", "Easy"),

        (t1_2, "What is 'Data Drift' in production machine learning pipelines managed by data engineers?",
         "The physical movement of hard drives between data centers",
         "Statistical changes in the input data distribution over time that degrade model predictive accuracy",
         "Corrupted binary headers in CSV files",
         "The deletion of obsolete git branches", "B", "Medium"),

        (t1_2, "In distributed data systems, what does 'Data Locality' refer to?",
         "Moving computational tasks close to the physical node where the data is stored, rather than transmitting massive data across the network",
         "Assigning geographic street addresses to server racks",
         "Restricting database access to a single local IP subnet",
         "Translating data into regional languages", "A", "Medium")
    ]

    # --- Unit 2: Distributed Storage & Processing Frameworks (12 Qs) ---
    u2 = "Unit 2: Distributed Storage & Processing Frameworks"
    t2_1 = "Hadoop Ecosystem & HDFS Architecture"
    t2_2 = "Apache Spark Architecture & RDD Computing"

    de_u2 = [
        (t2_1, "In the Hadoop Distributed File System (HDFS), what is the primary role of the NameNode?",
         "It executes user-written Map and Reduce tasks",
         "It manages file system namespace, directory trees, and maps file blocks to DataNodes as the central master metadata server",
         "It physically stores raw data block chunks on local disk",
         "It acts as a hardware network firewall", "B", "Easy"),

        (t2_1, "What is the default block size in modern HDFS installations (Hadoop 3.x)?",
         "4 KB", "64 KB", "128 MB (or 256 MB)", "1 GB", "C", "Easy"),

        (t2_1, "What is the standard default replication factor for data blocks in HDFS to ensure fault tolerance across commodity hardware?",
         "1 replica", "3 replicas (stored across distinct racks/nodes)", "5 replicas", "10 replicas", "B", "Easy"),

        (t2_1, "How does the HDFS NameNode determine if a DataNode has crashed or failed?",
         "By receiving periodic Heartbeat signals; if no heartbeat arrives within a timeout window, the node is marked dead and blocks are re-replicated",
         "By sending a physical electrical pulse through the rack",
         "By polling the customer's web browser",
         "By verifying the operating system serial number", "A", "Medium"),

        (t2_1, "In the classic Hadoop MapReduce programming model, what phase groups and sorts intermediate key-value pairs between the Map and Reduce steps?",
         "InputFormat parsing", "Shuffle and Sort phase", "Combiner cleanup", "RecordWriter flush", "B", "Easy"),

        (t2_1, "What is the function of a 'Combiner' in a Hadoop MapReduce job?",
         "To merge multiple HDFS clusters into a single logical cluster",
         "To act as a 'mini-reducer' on the Map node, performing local aggregation to reduce network bandwidth consumption during shuffle",
         "To combine Java and Python code into one binary",
         "To execute SQL queries directly on HDFS", "B", "Medium"),

        (t2_2, "Why is Apache Spark significantly faster (up to 100x) than traditional Hadoop MapReduce for iterative and machine learning workloads?",
         "Spark uses in-memory (RAM) distributed data processing and avoids continuous read/write spilling to disk between stages",
         "Spark only works on single-core computers",
         "Spark does not perform fault tolerance checks",
         "Spark eliminates the need for RAM and uses CPU cache exclusively", "A", "Easy"),

        (t2_2, "What is a Resilient Distributed Dataset (RDD) in Apache Spark?",
         "A relational SQL table stored on a local SSD",
         "A fault-tolerant, immutable, lazily evaluated distributed collection of objects partitioned across cluster worker nodes",
         "A neural network weight tensor stored in GPU memory",
         "A synchronized Java Vector collection", "B", "Medium"),

        (t2_2, "What is meant by 'Lazy Evaluation' in Apache Spark?",
         "Spark executes all transformations instantly as soon as they are called in code",
         "Spark does not compute execution graphs immediately; transformations build a logical execution plan (DAG) and computation only executes when an Action is called",
         "Spark threads sleep for 10 seconds between tasks",
         "Spark defers error reporting until system shutdown", "B", "Medium"),

        (t2_2, "Which of the following is categorized as a Spark 'Action' rather than a 'Transformation'?",
         "map()", "filter()", "flatMap()", "collect() / count()", "D", "Easy"),

        (t2_2, "In Apache Spark, which internal engine optimizes Structured Queries and DataFrame expressions by generating optimized physical execution plans?",
         "Tungsten Execution Engine & Catalyst Optimizer", "MapReduce JobTracker", "YARN Resource Manager", "Zookeeper Election Engine", "A", "Hard"),

        (t2_2, "What Spark abstraction provides schema enforcement, columnar storage in memory, and native SQL query capabilities over RDDs?",
         "Spark GraphX", "Spark DataFrame / Dataset", "Spark Broadcast Variable", "Spark Accumulator", "B", "Easy")
    ]

    # --- Unit 3: Data Warehousing, Data Integration & Lakehouse (12 Qs) ---
    u3 = "Unit 3: Data Warehousing, Data Integration & Lakehouse"
    t3_1 = "Dimensional Modeling & Data Warehousing"
    t3_2 = "ETL/ELT Pipelines & Modern Lakehouse Architecture"

    de_u3 = [
        (t3_1, "What is the primary difference between OLTP (Online Transaction Processing) and OLAP (Online Analytical Processing) systems?",
         "OLTP is optimized for fast, transactional read/write operations (normalized 3NF); OLAP is optimized for complex aggregation queries across historical data (denormalized)",
         "OLTP only runs in the cloud; OLAP runs only on mainframes",
         "OLTP does not use primary keys; OLAP cannot execute SELECT statements",
         "Both systems are identical in structure and query performance", "A", "Easy"),

        (t3_1, "In dimensional modeling, what characterizes a 'Fact Table'?",
         "It stores descriptive contextual attributes about business entities (e.g. customer address)",
         "It contains quantitative numerical measures/metrics (e.g. sales amount, quantity) and foreign keys referencing dimension tables",
         "It only stores binary image files",
         "It stores database user credentials", "B", "Easy"),

        (t3_1, "How does a 'Snowflake Schema' differ from a 'Star Schema' in a Data Warehouse design?",
         "A Star schema normalizes dimension tables into multiple related tables; Snowflake does not",
         "A Snowflake schema normalizes its dimension tables into sub-dimensions (resembling a snowflake), whereas a Star schema keeps dimensions denormalized",
         "A Snowflake schema contains no fact tables",
         "A Star schema requires NoSQL databases", "B", "Medium"),

        (t3_1, "What is a 'Slowly Changing Dimension Type 2' (SCD Type 2) approach for handling historical changes in dimension records?",
         "Overwriting the existing record directly without tracking history",
         "Creating a new record with a new surrogate key and validity date ranges (start_date, end_date, is_current) to preserve full history",
         "Adding an extra column for the previous value only (preserving only 1 previous state)",
         "Deleting the entire table when a change occurs", "B", "Hard"),

        (t3_1, "What is a 'Data Mart'?",
         "An online retail store selling physical hard drives",
         "A specialized, departmental subset of a Data Warehouse focused on a single business domain (e.g. Marketing, Finance)",
         "A public cloud subscription plan",
         "An open-source Apache web server", "B", "Easy"),

        (t3_1, "What is a 'Surrogate Key' in Data Warehouse dimensional tables?",
         "A business key generated by source operational ERP systems (e.g. Social Security Number)",
         "An artificial, system-assigned sequential integer key used as a primary key independent of source system business keys",
         "A cryptographic private key used for TLS handshake",
         "A foreign key that points to an external web API", "B", "Medium"),

        (t3_2, "What is the fundamental shift between traditional ETL and modern cloud-native ELT architectures?",
         "In ELT, raw data is loaded directly into the scalable cloud data warehouse/lake first, leveraging the warehouse's MPP compute engine to execute transformations",
         "In ELT, data is transformed before being extracted from sources",
         "In ETL, data is never loaded into a database",
         "ELT completely eliminates SQL transformations", "A", "Medium"),

        (t3_2, "What is a 'Data Lake'?",
         "A centralized repository designed to store vast amounts of raw structured, semi-structured, and unstructured data at scale in native format",
         "A swimming pool cooled computer rack",
         "A strictly normalized 3NF MySQL database",
         "A high-speed RAM disk cache", "A", "Easy"),

        (t3_2, "What is the primary architectural advantage of a 'Data Lakehouse' (e.g. Databricks Delta Lake, Apache Iceberg) over a traditional Data Lake?",
         "It combines the low-cost scalable storage of a Data Lake with the ACID transaction guarantees, schema enforcement, and SQL performance of a Data Warehouse",
         "It eliminates the need for cloud object storage",
         "It runs without microprocessors",
         "It only accepts data stored in CSV format", "A", "Medium"),

        (t3_2, "What open-source storage layer brings ACID transactions, scalable metadata handling, and time-travel versioning to Apache Spark Data Lakes?",
         "Delta Lake (or Apache Iceberg / Apache Hudi)", "FTP Server", "NFS v3", "SQLite3", "A", "Medium"),

        (t3_2, "In data pipeline engineering, what does 'Idempotence' mean?",
         "A pipeline run crashes if executed more than once",
         "A pipeline operation produces the exact same end-state result regardless of how many times it is executed with the same inputs",
         "A pipeline that runs only on alternating business days",
         "A pipeline that deletes half of the incoming data records randomly", "B", "Medium"),

        (t3_2, "What open-source tool is widely used to define, version, and orchestrate SQL transformation pipelines inside cloud data warehouses using Jinja and SQL?",
         "dbt (data build tool)", "Adobe Photoshop", "Docker Compose", "VLC Media Player", "A", "Easy")
    ]

    # --- Unit 4: Real-Time Data Engineering & Kafka Streaming (12 Qs) ---
    u4 = "Unit 4: Real-Time Data Engineering & Kafka Streaming"
    t4_1 = "Event Streaming Fundamentals & Message Brokers"
    t4_2 = "Apache Kafka Architecture & Stream Pipelines"

    de_u4 = [
        (t4_1, "In the Publish-Subscribe messaging paradigm, how are publishers and consumers decoupled?",
         "Publishers send messages to designated topics/channels without knowing who or how many consumers will read them",
         "Publishers must open a direct synchronous TCP connection to every single consumer device",
         "Consumers must compile the publisher's source code before receiving data",
         "Publishers and consumers must run in the exact same JVM process", "A", "Easy"),

        (t4_1, "What is an 'Event-Driven Architecture' (EDA)?",
         "A software architecture where decoupled components capture, communicate, and react to significant state changes (events) asynchronously",
         "An architecture where functions are triggered only when calendar events expire",
         "An architecture restricted to single-threaded desktop applications",
         "A relational schema that does not allow updates", "A", "Easy"),

        (t4_1, "How does Apache Kafka's log-centric storage differ fundamentally from traditional message brokers like RabbitMQ or ActiveMQ?",
         "Kafka stores messages in an immutable, append-only, ordered commit log partitioned across disks, allowing messages to be replayed by multiple consumers",
         "Kafka deletes messages immediately as soon as a single consumer acknowledges receipt",
         "Kafka stores messages entirely in CPU L1 cache",
         "Kafka requires all messages to be sorted alphabetically before arrival", "A", "Medium"),

        (t4_1, "What consumer delivery guarantee ensures that every incoming event is processed without loss, but may occasionally be re-processed during network failures?",
         "At-most-once delivery", "At-least-once delivery", "Zero-loss guarantee without network", "Random delivery", "B", "Easy"),

        (t4_2, "In Apache Kafka architecture, what is a 'Partition'?",
         "A physical hard drive formatting utility",
         "The fundamental unit of parallelism and ordered message storage within a Kafka Topic",
         "A firewall rule that blocks external IP addresses",
         "A consumer group coordinator thread", "B", "Medium"),

        (t4_2, "What is an 'Offset' in Apache Kafka?",
         "A sequential integer assigned to each message within a partition that uniquely identifies its position in the append-only log",
         "The difference in time between server clocks",
         "The memory address of the Kafka broker process",
         "The number of dropped network packets", "A", "Easy"),

        (t4_2, "What happens when multiple Kafka consumers join the same 'Consumer Group' subscribing to a multi-partition topic?",
         "Every consumer receives a complete copy of every single message in all partitions",
         "Kafka automatically assigns subsets of topic partitions to distinct consumers in the group, achieving horizontal scale and parallel consumption",
         "All consumers are immediately disconnected due to concurrency conflicts",
         "The topic is automatically deleted", "B", "Medium"),

        (t4_2, "What modern consensus protocol was introduced in Apache Kafka (KIP-500 / KRaft) to eliminate the external dependency on Apache ZooKeeper?",
         "Raft consensus protocol (Kafka Raft Metadata mode - KRaft)", "Paxos algorithm exclusively", "Proof of Work blockchain", "Two-phase commit", "A", "Medium"),

        (t4_2, "In stream processing, what type of window groups streaming events into fixed-size, non-overlapping, contiguous time intervals (e.g. every 5 minutes)?",
         "Sliding Window", "Tumbling Window", "Session Window", "Global Dynamic Window", "B", "Easy"),

        (t4_2, "What type of window groups streaming events based on periods of activity separated by predefined gaps of inactivity (e.g. user web sessions)?",
         "Tumbling Window", "Hopping Window", "Session Window", "Fixed Count Window", "C", "Easy"),

        (t4_2, "In Kafka monitoring, what critical metric represents the difference between the latest produced offset in a partition and the offset currently processed by a consumer?",
         "Consumer Lag", "Replication Jitter", "JVM Garbage Heap", "Producer Latency Factor", "A", "Easy"),

        (t4_2, "Which high-throughput distributed stream processing framework developed by the Apache Software Foundation supports event-time semantics, stateful computation, and exactly-once processing?",
         "Apache Flink (and Apache Spark Streaming)", "Apache HTTP Server", "GNU Wget", "Postfix Mail Server", "A", "Medium")
    ]

    # --- Unit 5: Data Governance, Security & Workflow Orchestration (12 Qs) ---
    u5 = "Unit 5: Data Governance, Security & Workflow Orchestration"
    t5_1 = "Apache Airflow & Workflow Orchestration"
    t5_2 = "Data Governance, Lineage & Emerging Paradigms"

    de_u5 = [
        (t5_1, "In Apache Airflow, what fundamental mathematical structure represents a workflow as a collection of organized tasks with directional execution dependencies?",
         "Directed Acyclic Graph (DAG)", "B-Tree Index", "Cyclic Finite Automaton", "Complete Bipartite Graph", "A", "Easy"),

        (t5_1, "How are DAG workflows defined and authored in Apache Airflow?",
         "Through drag-and-drop XML configuration files exclusively",
         "As standard Python code (configuration as code), allowing programmatic dynamic task generation and version control",
         "By compiling C++ shared libraries",
         "Through manual command-line prompts executed each morning", "B", "Easy"),

        (t5_1, "In Apache Airflow, what is the role of an 'Operator' (e.g. PythonOperator, BashOperator, SQLExecuteQueryOperator)?",
         "It acts as a template for a single atomic task to be executed within a DAG",
         "It operates physical cooling fans in the data center",
         "It provides user authentication for Airflow web UI",
         "It assigns IP addresses to Kubernetes pods", "A", "Easy"),

        (t5_1, "What specialized Airflow operator pauses task execution and repeatedly checks for an external condition (such as file arrival in S3) before allowing downstream tasks to proceed?",
         "BranchPythonOperator", "Sensor (e.g. S3KeySensor, FileSensor)", "DummyOperator", "SubDagOperator", "B", "Medium"),

        (t5_1, "What is 'Backfilling' in Apache Airflow?",
         "Restoring deleted database rows from tape backup",
         "Running DAG instances for historical date intervals in the past after deploying a new or updated pipeline",
         "Filling empty disk sectors with random zeros",
         "Overwriting output data with test data", "B", "Medium"),

        (t5_1, "Which core component of Apache Airflow monitors DAG files, checks task dependencies, and queues runnable task instances for workers?",
         "Airflow Webserver", "Airflow Scheduler", "Airflow Metadata Database", "Airflow Celery Worker", "B", "Easy"),

        (t5_2, "What is 'Data Lineage' in enterprise data governance?",
         "The complete life cycle and historical audit trail documenting where data originated, how it was transformed, and where it moves across systems",
         "The family tree of the engineering development team",
         "The chronological list of git commit author names",
         "The physical network route taken by IP packets", "A", "Easy"),

        (t5_2, "Which open-source metadata management and data governance tool provides automated data lineage tracking and metadata search across Hadoop and cloud systems?",
         "Apache Atlas (and tools like Amundsen / OpenMetadata)", "Apache Maven", "Apache Ant", "Apache Tomcat", "A", "Medium"),

        (t5_2, "Which security mechanism limits data access by granting permissions based strictly on an employee's organizational function and responsibilities?",
         "Role-Based Access Control (RBAC)", "Discretionary Port Knocking", "Symmetric XOR obfuscation", "Single User Sudo mode", "A", "Easy"),

        (t5_2, "What technique replaces sensitive personal data (e.g. Credit Card numbers, SSNs) with realistic fictitious characters while preserving data format for development testing?",
         "Data Masking / Pseudonymization", "Disk Defragmentation", "Data Normalization (3NF)", "Run-Length Encoding", "A", "Easy"),

        (t5_2, "What architectural concept proposed by Zhamak Dehghani shifts data architecture from centralized data lakes to decentralized, domain-oriented ownership where 'Data is treated as a Product'?",
         "Monolithic Enterprise Data Warehouse", "Data Mesh", "Centralized Data Swamp", "Relational Client-Server Loop", "B", "Medium"),

        (t5_2, "What is the primary objective of modern 'Data Observability' platforms (such as Monte Carlo or Great Expectations)?",
         "To monitor data pipeline health, detect schema anomalies, track freshness, and prevent data downtime before it impacts business analytics",
         "To broadcast live video streams of server rooms",
         "To record audio keystrokes of data engineers",
         "To count lines of Python code committed per day", "A", "Medium")
    ]

    for q in de_u1:
        questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in de_u2:
        questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in de_u3:
        questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in de_u4:
        questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in de_u5:
        questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))

    return questions


def get_vector_db_questions():
    questions = []
    sub = "Vector Databases"
    branch = "Artificial Intelligence & Data Science"
    year = "Third Year"
    sem = "Semester V"

    # --- Unit 1: Fundamentals of Vector Databases & Embeddings (12 Qs) ---
    u1 = "Unit 1: Fundamentals of Vector Databases & Embeddings"
    t1_1 = "Vector Representations & Distance Metrics"
    t1_2 = "Relational vs Vector Database Architecture"

    vdb_u1 = [
        (t1_1, "What does an 'Embedding' mathematically represent in modern machine learning and vector search?",
         "A low-dimensional or high-dimensional dense vector of floating-point numbers that captures the semantic meaning of an unstructured data entity",
         "A compressed zip archive of text files",
         "A unique primary key integer in an auto-increment column",
         "A foreign key constraint defined in SQL DDL", "A", "Easy"),

        (t1_1, "Which distance metric measures the cosine of the angle between two multi-dimensional vectors, evaluating orientation regardless of magnitude?",
         "Euclidean Distance (L2 norm)", "Cosine Similarity", "Manhattan Distance (L1 norm)", "Hamming Distance", "B", "Easy"),

        (t1_1, "What is the formula for the Euclidean distance (L2 norm) between two vectors u and v of dimension d?",
         "sqrt( sum_{i=1}^d (u_i - v_i)^2 )",
         "sum_{i=1}^d |u_i - v_i|",
         "(u . v) / (||u|| * ||v||)",
         "max(|u_i - v_i|)", "A", "Easy"),

        (t1_1, "If two non-zero vectors in an embedding space point in the exact same direction, what is their Cosine Similarity value?",
         "0.0", "1.0", "-1.0", "0.5", "B", "Easy"),

        (t1_1, "When two embedding vectors are normalized to unit length (magnitude = 1), their Dot Product is mathematically equal to their:",
         "Manhattan distance", "Cosine similarity", "Euclidean norm squared", "Hamming weight", "B", "Medium"),

        (t1_1, "Which distance metric calculates the sum of absolute coordinate differences between points across grid dimensions (City Block distance)?",
         "Euclidean Distance", "Manhattan Distance (L1 norm)", "Chebyshev Distance", "Minkowski Distance with p=infinity", "B", "Easy"),

        (t1_2, "What fundamental computational limitation prevents traditional relational databases (B-Tree indexes) from performing efficient vector similarity search?",
         "Relational databases cannot store decimal numbers",
         "B-Tree indexes only order 1-dimensional scalar data and degrade to full sequential table scans in high-dimensional vector spaces (Curse of Dimensionality)",
         "SQL syntax cannot execute SELECT queries with WHERE clauses",
         "Relational databases cannot connect to Python scripts", "B", "Medium"),

        (t1_2, "What is the 'Curse of Dimensionality' in the context of high-dimensional vector similarity search?",
         "As dimensionality increases, the volume of the space grows exponentially, causing all pairwise distances to become nearly equidistant and rendering traditional spatial partitioning ineffective",
         "Vectors cannot exceed 3 dimensions in computer memory",
         "Floating point numbers lose precision below zero",
         "GPU compute cores overheat when calculating dot products", "A", "Hard"),

        (t1_2, "Which search paradigm finds documents containing concepts with matching intent rather than exact literal keyword matches?",
         "Lexical / Keyword Search (BM25)", "Semantic Search", "Regular Expression Grep", "Fuzzy Levenshtein Edit Search", "B", "Easy"),

        (t1_2, "In a vector-based product recommendation system, how is an item recommended to a user?",
         "By finding product embedding vectors that are closest to the user's preference embedding vector in the latent embedding space",
         "By sorting products alphabetically by name",
         "By randomly picking products from the relational database",
         "By displaying the product with the smallest integer ID", "A", "Easy"),

        (t1_2, "How do Vector Databases handle 'Unstructured Data' (such as images, video clips, and audio recordings)?",
         "By converting media into raw SQL strings using base64 encoding without indexing",
         "By using deep neural feature extractors to generate dense embeddings of the media, which are indexed and searched via vector similarity",
         "By deleting the media after 24 hours",
         "By transcribing all videos manually into CSV files", "B", "Medium"),

        (t1_2, "Which query operation is the core primitive provided by all specialized Vector Databases?",
         "K-Nearest Neighbor (k-NN) similarity search", "Distributed Two-Phase Commit", "B-Tree Range Scan", "Recursive Common Table Expression", "A", "Easy")
    ]

    # --- Unit 2: Vector Embeddings & Data Preparation (12 Qs) ---
    u2 = "Unit 2: Vector Embeddings & Data Preparation"
    t2_1 = "Embedding Generation & Transformer Models"
    t2_2 = "Chunking Strategies & Vector Storage"

    vdb_u2 = [
        (t2_1, "Which pioneering neural embedding model introduced Word2Vec with Continuous Bag-of-Words (CBOW) and Skip-gram architectures in 2013?",
         "Tomas Mikolov et al. (Google)", "Geoffrey Hinton", "Yann LeCun", "John Hopfield", "A", "Medium"),

        (t2_1, "How does Sentence-BERT (SBERT) improve over standard BERT for generating sentence-level vector embeddings?",
         "It replaces transformers with decision trees",
         "It uses siamese and triplet network structures to generate semantically meaningful sentence embeddings that can be compared quickly via cosine similarity",
         "It restricts embeddings to 2 dimensions",
         "It only accepts single-word tokens", "B", "Medium"),

        (t2_1, "Which multimodal embedding model trained by OpenAI maps both images and natural language text into a shared joint embedding space?",
         "ResNet-50", "CLIP (Contrastive Language-Image Pre-training)", "VGG-16", "Word2Vec", "B", "Easy"),

        (t2_1, "What is the typical dimensionality of dense embeddings generated by modern language models (e.g. text-embedding-3-small, BAAI/bge-large)?",
         "3 to 10 dimensions", "128 to 1536 (or 3072) dimensions", "1 million dimensions", "Exactly 1 dimension", "B", "Medium"),

        (t2_1, "What occurs when the semantic meaning of words depends on their sentence context (e.g., 'bank' of a river vs financial 'bank')?",
         "Static embeddings (Word2Vec) assign fixed vectors, whereas contextual transformer models (BERT) generate different embeddings based on context",
         "All vector databases crash immediately",
         "The dot product becomes zero",
         "The words must be deleted from the corpus", "A", "Medium"),

        (t2_1, "Which non-linear dimensionality reduction technique is predominantly used to visualize high-dimensional embedding clusters in 2D or 3D scatter plots?",
         "t-SNE (t-Distributed Stochastic Neighbor Embedding) or UMAP", "Linear Normal Equation", "Bubble Sort", "Forward Chaining", "A", "Easy"),

        (t2_2, "Why is text 'Chunking' necessary before generating vector embeddings for large documents in RAG applications?",
         "Embedding models and LLMs have fixed maximum token context windows (e.g. 512 or 8192 tokens) and smaller focused chunks retain specific semantic relevance",
         "Because vector databases cannot store text longer than 10 characters",
         "Chunking encrypts the document for cybersecurity compliance",
         "Chunking is only required for PDF files, not plain text", "A", "Easy"),

        (t2_2, "What chunking strategy splits text recursively using a list of separators (e.g. double newlines, single newlines, spaces) to preserve semantic paragraph boundaries?",
         "Fixed character splitting without overlap", "Recursive Character Text Splitting", "Random word sampling", "Binary tree splitting", "B", "Medium"),

        (t2_2, "What is the purpose of including a 'Chunk Overlap' (e.g. 10-20% token overlap) between consecutive document chunks?",
         "To double the size of the database on disk",
         "To ensure critical contextual information at sentence and phrase boundaries is not lost between adjacent chunks",
         "To prevent duplicate vectors in the index",
         "To force the embedding model to run faster", "B", "Medium"),

        (t2_2, "In vector data modeling, what is a 'Metadata Payload' attached to a vector record?",
         "A set of key-value attributes (e.g. document_id, author, category, timestamp, raw text snippet) stored alongside the vector for filtering and display",
         "The binary machine code of the GPU driver",
         "The physical MAC address of the vector database server",
         "The salary of the database administrator", "A", "Easy"),

        (t2_2, "What is 'Semantic Chunking' in advanced data preparation pipelines?",
         "Splitting text strictly every 100 characters",
         "Splitting text dynamically at points where the cosine similarity between consecutive sentence embeddings drops below a predefined threshold (topic shifts)",
         "Deleting all vowels from sentences",
         "Converting paragraphs into SQL schemas", "B", "Hard"),

        (t2_2, "Why are embeddings typically normalized (unit length ||v|| = 1) prior to indexing in vector databases?",
         "Because it simplifies cosine similarity calculation to a fast single dot product operation",
         "Because non-normalized vectors cannot be stored in RAM",
         "Because it converts float numbers into integer booleans",
         "Because it eliminates the need for vector databases", "A", "Medium")
    ]

    # --- Unit 3: Vector Indexing & Approximate Nearest Neighbor (ANN) (12 Qs) ---
    u3 = "Unit 3: Vector Indexing & Approximate Nearest Neighbor (ANN)"
    t3_1 = "Exact vs Approximate Nearest Neighbor Search"
    t3_2 = "ANN Indexing Algorithms (HNSW, IVF, PQ)"

    vdb_u3 = [
        (t3_1, "What is the time complexity of an Exact Nearest Neighbor (Flat/Brute-force) search over a database of N vectors of dimension D?",
         "O(1)", "O(log N)", "O(N * D)", "O(D^2)", "C", "Easy"),

        (t3_1, "What fundamental engineering trade-off is accepted by Approximate Nearest Neighbor (ANN) search algorithms?",
         "Sacrificing 100% recall precision in exchange for dramatic orders-of-magnitude reductions in search latency and query throughput",
         "Sacrificing data security for lower storage costs",
         "Accepting corrupted database tables to increase GPU clock speed",
         "Deleting old vectors to speed up write operations", "A", "Medium"),

        (t3_1, "Which evaluation metric measures the proportion of true top-K nearest neighbors successfully retrieved by an ANN algorithm compared to brute-force exact search?",
         "Recall@K", "Perplexity", "BLEU score", "Mean Squared Error", "A", "Easy"),

        (t3_1, "What does QPS stand for in vector database benchmarking?",
         "Quantum Processor Speed", "Queries Per Second (throughput measure)", "Queue Processing Slot", "Quick Partition Scheme", "B", "Easy"),

        (t3_2, "How does the Inverted File Index (IVF) algorithm speed up vector similarity search?",
         "By sorting all vectors alphabetically",
         "By partitioning the vector space into Voronoi cells using k-means clustering and only searching vectors in the centroids closest to the query vector (nprobe)",
         "By compressing all vectors into 1-bit flags",
         "By storing vectors on tape storage", "B", "Medium"),

        (t3_2, "In IVF indexing, what does the parameter 'nprobe' specify during a query search?",
         "The total number of GPUs allocated to the query",
         "The number of nearest centroid Voronoi cells to inspect during candidate search (trading search time for recall)",
         "The number of threads in the thread pool",
         "The dimension of the output vector", "B", "Hard"),

        (t3_2, "What is Product Quantization (PQ) in vector indexing?",
         "A lossy vector compression technique that decomposes high-dimensional vectors into smaller sub-vectors and quantizes each using a codebook of centroids",
         "An e-commerce algorithm for pricing retail goods",
         "A method for multiplying matrices without floating point units",
         "A query language for NoSQL databases", "A", "Hard"),

        (t3_2, "What popular graph-based ANN indexing algorithm constructs a multi-layer graph where upper layers have longer links (skip-list concept) and lower layers provide fine-grained routing?",
         "KD-Tree", "Hierarchical Navigable Small World (HNSW)", "Locality Sensitive Hashing (LSH)", "R-Tree Index", "B", "Medium"),

        (t3_2, "What are the two primary construction parameters that govern the index quality and memory overhead of an HNSW graph?",
         "M (maximum number of bidirectional links per node) and efConstruction (size of dynamic candidate list during build)",
         "alpha and beta", "K and N", "n_estimators and max_depth", "A", "Hard"),

        (t3_2, "What is 'Hybrid Search' in modern vector search engines?",
         "Searching on both Android and iOS devices simultaneously",
         "Combining dense vector semantic similarity search with sparse lexical keyword search (e.g. BM25 / SPLADE) using Reciprocal Rank Fusion (RRF)",
         "Searching across both relational databases and Excel files",
         "Running queries on CPU and hard disk together", "B", "Medium"),

        (t3_2, "What is the difference between 'Pre-Filtering' and 'Post-Filtering' when executing metadata-filtered vector searches?",
         "Pre-filtering filters the candidate vectors based on metadata before performing the vector similarity search; post-filtering performs vector search first and discards non-matching metadata after",
         "Pre-filtering deletes vectors permanently; post-filtering restores them",
         "Pre-filtering is only for text; post-filtering is only for images",
         "There is no difference in search results or recall", "A", "Hard"),

        (t3_2, "Which algorithmic challenge can cause Post-Filtering to return fewer than the requested K results (or zero results)?",
         "If the top-K nearest neighbors retrieved in the vector space do not meet the strict metadata criteria, they are discarded leaving insufficient results",
         "The vector database runs out of RAM",
         "The metadata becomes unreadable",
         "The GPU encounters a division by zero", "A", "Hard")
    ]

    # --- Unit 4: Vector Database Systems & Architecture (12 Qs) ---
    u4 = "Unit 4: Vector Database Systems & Architecture"
    t4_1 = "Vector Database Ecosystem (Milvus, Pinecone, FAISS)"
    t4_2 = "Query Execution Pipeline & Metadata Filtering"

    vdb_u4 = [
        (t4_1, "Which widely used open-source library developed by Meta (Facebook) AI Research provides highly efficient implementations of similarity search and clustering for dense vectors?",
         "TensorFlow", "FAISS (Facebook AI Similarity Search)", "PyTorch Lightning", "Scikit-Learn", "B", "Easy"),

        (t4_1, "Which leading cloud-native, open-source distributed vector database decouples compute and storage and provides scalable multi-tenant vector indexing on Kubernetes?",
         "Milvus", "SQLite", "Redis single-thread", "Microsoft Access", "A", "Easy"),

        (t4_1, "What distinguishes Pinecone in the vector database ecosystem?",
         "It is an on-premises C++ compiler",
         "It is a fully managed, serverless, cloud-native vector database SaaS requiring zero infrastructure maintenance",
         "It is an open-source relational database that replaced PostgreSQL",
         "It is a mobile app for drawing vector graphics", "B", "Easy"),

        (t4_1, "Which lightweight, open-source embedding database is widely popular for local AI application prototyping and LangChain integration with minimal setup?",
         "Chroma (ChromaDB)", "Oracle RAC", "IBM DB2", "Apache Cassandra", "A", "Easy"),

        (t4_1, "Which open-source vector search engine written in Go is known for its modular architecture, GraphQL API, and built-in vectorization modules?",
         "Weaviate", "MySQL 5.7", "SQLite3", "Hadoop NameNode", "A", "Medium"),

        (t4_1, "Which vector database written in Rust provides high-performance vector search with rich payload-based filtering and geo-spatial query capabilities?",
         "Qdrant", "PostgreSQL 8.0", "MongoDB 2.4", "Memcached", "A", "Medium"),

        (t4_2, "What are the core chronological stages of a Vector Database Ingestion Pipeline?",
         "Raw Document Ingestion -> Preprocessing/Chunking -> Embedding Model Generation -> Vector & Payload Indexing -> Persistent Storage",
         "Compilation -> Bytecode Verification -> Assembly -> Linking",
         "Tokenization -> Hashing -> XOR Encryption -> Decryption",
         "Query Parsing -> Plan Optimization -> Table Lock -> Unlock", "A", "Medium"),

        (t4_2, "In distributed vector databases like Milvus, what is a 'Shard'?",
         "A broken hard drive sector",
         "A horizontal partition of data collections distributed across multiple query/data worker nodes for parallel indexing and searching",
         "A cryptographic hash collision",
         "A user interface theme component", "B", "Medium"),

        (t4_2, "How do modern vector databases ensure high availability and disaster recovery for vector collections?",
         "By maintaining replicated data segments across multiple independent worker nodes and syncing write-ahead logs (WAL) to distributed object storage",
         "By printing hard copies of vector matrices on paper",
         "By storing all data in a single volatile CPU cache register",
         "By restricting access to one user at a time", "A", "Medium"),

        (t4_2, "What is 'Single-Stage Filtered Search' in modern vector database query execution?",
         "Iterating through an HNSW graph while dynamically evaluating metadata predicates during graph traversal to guarantee exact K results with low latency",
         "Filtering out negative numbers from vectors",
         "Executing a SQL query after shutting down the vector engine",
         "Restricting searches to single-character strings", "A", "Hard"),

        (t4_2, "In enterprise fraud detection, how are vector databases utilized effectively?",
         "By computing embeddings of user transaction patterns and detecting anomalous behaviors via cosine distance against historical fraud vector clusters",
         "By blocking all user transactions automatically",
         "By converting transaction amounts into roman numerals",
         "By sorting transactions by credit card expiration date", "A", "Medium"),

        (t4_2, "Which relational database extension adds native vector data types, vector distance operators (<->, <=>), and HNSW/IVFFlat indexing to PostgreSQL?",
         "pgvector", "PostGIS", "pg_cron", "pg_stat_statements", "A", "Easy")
    ]

    # --- Unit 5: Retrieval-Augmented Generation (RAG) & Emerging Trends (12 Qs) ---
    u5 = "Unit 5: Retrieval-Augmented Generation (RAG) & Emerging Trends"
    t5_1 = "RAG Pipeline Architecture & Context Injection"
    t5_2 = "RAG Evaluation, Security & Agentic Trends"

    vdb_u5 = [
        (t5_1, "What is the primary motivation for implementing Retrieval-Augmented Generation (RAG) with Large Language Models?",
         "To ground LLM responses with authoritative up-to-date domain data, mitigate factual hallucinations, and overcome training knowledge cutoffs without costly retraining",
         "To reduce the number of tokens in the English alphabet",
         "To replace python code with assembly language",
         "To increase the parameter size of the LLM by 10x", "A", "Easy"),

        (t5_1, "In a standard naive RAG pipeline, what happens immediately after the user submits a natural language question?",
         "The query is converted into a vector embedding using the same embedding model used during document ingestion",
         "The database drops all existing vector indexes",
         "The LLM is completely fine-tuned from scratch on Wikipedia",
         "The question is translated into binary ASCII machine code", "A", "Easy"),

        (t5_1, "In the generation phase of RAG, how is the retrieved context provided to the Large Language Model?",
         "By injecting the retrieved text chunks directly into the prompt context window along with system instructions and user query",
         "By burning the retrieved context onto a physical DVD ROM",
         "By sending a fax to the server administrator",
         "By updating the LLM's frozen neural network weights on disk", "A", "Easy"),

        (t5_1, "What role does a 'Re-ranker' (e.g. Cross-Encoder) play between vector retrieval and LLM context injection in advanced RAG?",
         "It deletes the retrieved chunks",
         "It performs fine-grained joint attention over query-document pairs to accurately re-score and re-order the top retrieved chunks for optimal context quality",
         "It translates the context into French",
         "It compresses the context into a ZIP file", "B", "Medium"),

        (t5_1, "What cognitive phenomenon describes how LLMs tend to recall information placed at the extreme beginning or end of long prompt contexts better than information in the middle?",
         "Vanishing Gradient", "Lost in the Middle phenomenon", "Dying ReLU", "Catastrophic Forgetting", "B", "Medium"),

        (t5_1, "What is 'Hypothetical Document Embeddings' (HyDE) in advanced query transformation?",
         "Generating a hypothetical answer using an LLM first, embedding that hypothetical text, and using its vector to retrieve real relevant context documents",
         "Creating fake vectors that cause memory errors",
         "Deleting user queries that contain hypothetical questions",
         "Storing empty files in the vector database", "A", "Hard"),

        (t5_2, "Which evaluation framework provides automated metrics (Faithfulness, Answer Relevance, Context Precision, Context Recall) to evaluate RAG pipelines using LLMs as judges?",
         "Ragas (or TruLens)", "PyUnit", "JUnit 4", "SonarQube", "A", "Medium"),

        (t5_2, "In RAG pipeline evaluation, what does the metric 'Faithfulness' measure?",
         "Whether the generated response can be mathematically and factually inferred strictly from the retrieved context without hallucination",
         "How quickly the query executed in milliseconds",
         "The total number of words in the user's question",
         "The accuracy of the network switch routing table", "A", "Easy"),

        (t5_2, "What security vulnerability in RAG pipelines occurs when an attacker embeds malicious instructions inside an ingested document that hijacks the LLM's system prompt upon retrieval?",
         "SQL Injection", "Indirect Prompt Injection (Document Poisoning)", "Cross-Site Scripting (XSS)", "Buffer Overflow", "B", "Medium"),

        (t5_2, "What is 'GraphRAG'?",
         "An advanced RAG methodology that combines Knowledge Graphs with vector embeddings to enable multi-hop reasoning and holistic thematic synthesis across complex corpora",
         "Drawing line graphs in Microsoft Excel",
         "Displaying vector embeddings as pie charts",
         "Restricting RAG to 2D image coordinates", "A", "Hard"),

        (t5_2, "In 'Agentic RAG', how does an autonomous AI Agent interact with a vector database differently from naive RAG?",
         "The agent dynamically formulates sub-queries, decides which tools/retrievers to call, evaluates retrieved quality, and iteratively refines searches until confident",
         "The agent replaces the vector database with a single text file",
         "The agent only answers 'Yes' or 'No'",
         "The agent requires manual human intervention for every token", "A", "Hard"),

        (t5_2, "What is 'Multimodal RAG'?",
         "A RAG architecture capable of retrieving and synthesizing information across multiple modalities simultaneously (text, technical diagrams, tables, and images)",
         "A system that runs on multiple operating systems",
         "A pipeline that uses multiple microphones",
         "An algorithm with multiple while loops", "A", "Easy")
    ]

    for q in vdb_u1:
        questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in vdb_u2:
        questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in vdb_u3:
        questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in vdb_u4:
        questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in vdb_u5:
        questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))

    return questions


def get_all_sem5_questions():
    all_q = []
    all_q.extend(get_sem5_questions())
    all_q.extend(get_java_questions())
    all_q.extend(get_cloud_ai_questions())
    all_q.extend(get_data_eng_questions())
    all_q.extend(get_vector_db_questions())
    return all_q
