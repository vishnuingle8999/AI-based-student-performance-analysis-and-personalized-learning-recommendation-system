# -*- coding: utf-8 -*-
"""
Generate 180 DBATU Questions for Semester VI (60 questions for each of the 3 subjects)
Subjects:
  1. Deep Learning (26AFAIPC601) - 60 Qs (12 per unit x 5 units)
  2. Natural Language Processing (26AFAIPC602) - 60 Qs (12 per unit x 5 units)
  3. Fundamental Edge AI (26AFAIPC603) - 60 Qs (12 per unit x 5 units)
"""

def get_deep_learning_questions():
    questions = []
    sub = "Deep Learning"
    branch = "Artificial Intelligence & Data Science"
    year = "Third Year"
    sem = "Semester VI"

    u1 = "Unit 1: Traditional Machine Learning and Artificial Neural Networks"
    t1 = "ANN Architectures & Gradient Descent"
    dl_u1 = [
        (t1, "What is the primary architectural difference between an Artificial Neuron (Perceptron) and a Biological Neuron?",
         "Artificial neurons compute a weighted sum passed through a non-linear activation function; biological neurons transmit electro-chemical action potentials via synapses and dendrites",
         "Artificial neurons have cell bodies made of plastic", "Biological neurons use floating-point numbers", "Artificial neurons cannot be trained", "A", "Easy"),
        (t1, "What mathematical problem prevented the early single-layer Perceptron from learning the XOR boolean function?",
         "The XOR function is non-linearly separable in 2D space", "The perceptron has no bias term", "Gradient descent was not yet invented", "Matrix multiplication cannot compute XOR", "A", "Easy"),
        (t1, "In training Artificial Neural Networks, what does 'Backpropagation' compute?",
         "The partial derivatives (gradients) of the loss function with respect to every trainable weight and bias using the calculus chain rule",
         "The inverse of the dataset matrix", "The optimal number of layers", "The accuracy on test data", "A", "Easy"),
        (t1, "What optimization challenge occurs when gradients become exponentially small as they backpropagate through deep layers with sigmoid activations?",
         "Vanishing Gradient Problem", "Exploding Gradient Problem", "Deadlock", "Internal Covariate Shift", "A", "Easy"),
        (t1, "What issue occurs when gradients grow exponentially large, causing catastrophic weight updates and numerical NaN overflow?",
         "Exploding Gradient Problem", "Vanishing Gradient Problem", "Dying ReLU", "Overfitting", "A", "Easy"),
        (t1, "Which activation function is defined as f(x) = max(0, x)?",
         "Rectified Linear Unit (ReLU)", "Sigmoid", "Hyperbolic Tangent (Tanh)", "Leaky ReLU", "A", "Easy"),
        (t1, "What is the 'Dying ReLU' problem in deep neural networks?",
         "When neurons output 0 for all inputs and have a gradient of 0, permanently stopping weight updates if learning rate is too high",
         "When CPU temperature exceeds limits", "When weights are initialized to 1", "When the loss reaches zero", "A", "Medium"),
        (t1, "How does 'Leaky ReLU' address the dying ReLU issue?",
         "By introducing a small non-zero slope (e.g. 0.01*x) for negative inputs: f(x) = x if x > 0 else alpha*x",
         "By converting negative numbers into positive absolute values", "By setting all negative gradients to 1", "By normalizing weights to unit norm", "A", "Medium"),
        (t1, "What is the primary role of the Softmax function in the output layer of a multi-class neural network classifier?",
         "It normalizes raw output logits into a valid probability distribution where all values are positive and sum to 1",
         "It introduces non-linear negative values", "It performs feature selection", "It prunes redundant connections", "A", "Easy"),
        (t1, "Which popular deep learning optimizer computes individual adaptive learning rates using both first moments (momentum) and second moments of the gradients?",
         "Adam (Adaptive Moment Estimation)", "Stochastic Gradient Descent (SGD)", "Adagrad", "RMSProp alone", "A", "Easy"),
        (t1, "What is 'Weight Decay' in neural network optimization?",
         "L2 regularization that adds a penalty proportional to the sum of squared weights to the loss function to prevent overfitting",
         "Physical degradation of hard drive sectors", "The loss of precision in 16-bit floats", "Decreasing the learning rate per epoch", "A", "Medium"),
        (t1, "What happens during forward propagation in a Multi-Layer Perceptron (MLP)?",
         "Inputs are multiplied by weight matrices, summed with biases, and passed through activation functions layer by layer to produce an output prediction",
         "Gradients are calculated using the chain rule", "Weights are updated using the learning rate", "Loss is differentiated", "A", "Easy")
    ]

    u2 = "Unit 2: Deep Architecture and Convolutional Neural Networks (CNN)"
    t2 = "CNNs, Convolutions & Vision Architectures"
    dl_u2 = [
        (t2, "What are the two primary computational principles that make Convolutional Neural Networks (CNNs) superior to dense networks for computer vision?",
         "Local Receptive Fields (Sparse Connectivity) and Parameter / Weight Sharing across spatial locations",
         "Full matrix connectivity and unbounded weights", "Sequential recurrent memory gates", "Elimination of non-linear activations", "A", "Medium"),
        (t2, "What operation slides a kernel filter over an input feature map and computes the element-wise dot product at each position?",
         "2D Convolution", "Max Pooling", "Batch Normalization", "Global Average Pooling", "A", "Easy"),
        (t2, "What is the primary function of a Pooling layer (such as Max Pooling) in a CNN?",
         "To downsample spatial dimensions (height and width), reducing computational parameters while introducing translation invariance",
         "To increase the number of color channels", "To calculate gradient loss", "To normalize weights to zero mean", "A", "Easy"),
        (t2, "What formula calculates the spatial output dimension O of a convolution given input dimension W, kernel size K, padding P, and stride S?",
         "O = floor((W - K + 2*P) / S) + 1", "O = (W + K) / S", "O = W * K - P", "O = (W - K) * S", "A", "Hard"),
        (t2, "What breakthrough CNN architecture developed by Alex Krizhevsky et al. won the ImageNet 2012 competition using GPUs and ReLU?",
         "AlexNet", "LeNet-5", "ResNet-50", "VGG-16", "A", "Easy"),
        (t2, "What architectural design characteristic defines the VGG network (Simonyan & Zisserman, 2014)?",
         "Using stacks of small 3x3 convolution filters throughout the entire network instead of large 7x7 or 11x11 filters",
         "Using no activation functions", "Having only 2 layers", "Eliminating pooling layers", "A", "Medium"),
        (t2, "What landmark innovation in ResNet (He et al., 2015) enabled the training of ultra-deep networks (152+ layers) without vanishing gradients?",
         "Residual / Skip Connections (Identity Shortcut Mappings: F(x) + x)", "Inception Depth Modules", "Extreme Dropout of 90%", "Binary Quantization", "A", "Easy"),
        (t2, "How does Batch Normalization accelerate neural network training and improve generalization?",
         "By normalizing layer inputs across the mini-batch to zero mean and unit variance, mitigating internal covariate shift and acting as a mild regularizer",
         "By sorting mini-batch samples alphabetically", "By eliminating backpropagation", "By doubling the learning rate every epoch", "A", "Medium"),
        (t2, "What is the role of 'Dropout' regularization during CNN training?",
         "Randomly deactivating a fraction p of neurons during each forward training step to prevent complex co-adaptations of feature detectors",
         "Dropping corrupted image files from disk", "Stopping training if validation loss rises", "Deleting output layers", "A", "Easy"),
        (t2, "What object detection framework treats detection as a single regression problem from image pixels directly to bounding box coordinates (Redmon et al.)?",
         "YOLO (You Only Look Once)", "R-CNN", "Fast R-CNN", "Sliding Window Classifier", "A", "Easy"),
        (t2, "What U-shaped CNN architecture with skip connections between encoder and decoder is widely used for biomedical image segmentation?",
         "U-Net", "AlexNet", "GoogLeNet", "DenseNet", "A", "Easy"),
        (t2, "What is 'Global Average Pooling' often used to replace dense fully-connected layers before the final classification head?",
         "A layer that computes the average of each entire feature map into a single scalar value, reducing parameters and preventing overfitting",
         "A layer that calculates global dataset variance", "A pooling layer that deletes feature maps", "An image resizing script", "A", "Medium")
    ]

    u3 = "Unit 3: Deep Sequence Models (RNN, GRU, LSTM)"
    t3 = "RNNs, LSTMs & Sequence Modeling"
    dl_u3 = [
        (t3, "What architectural feature allows Recurrent Neural Networks (RNNs) to process sequential data of variable length?",
         "Recurrent cyclic feedback connections that maintain an internal hidden state h_t summarizing past sequence history",
         "Multi-head self-attention without recurrence", "Convolutional filters with stride 10", "Static lookup tables", "A", "Easy"),
        (t3, "What algorithm is used to train standard Recurrent Neural Networks by unfolding the network across time steps?",
         "Backpropagation Through Time (BPTT)", "Standard Hebbian Learning", "K-Means Partitioning", "Forward Chaining", "A", "Easy"),
        (t3, "Why do standard simple RNNs struggle to learn long-term dependencies across long sequences?",
         "Repeated matrix multiplications across time steps cause gradients to vanish or explode exponentially during BPTT",
         "Because RNNs cannot accept text inputs", "Because simple RNNs have no activation functions", "Because time steps must be sorted", "A", "Medium"),
        (t3, "What three gating mechanisms regulate information flow inside a Long Short-Term Memory (LSTM) cell (Hochreiter & Schmidhuber, 1997)?",
         "Forget Gate, Input Gate, and Output Gate", "Read Gate, Write Gate, and Delete Gate", "Push Gate, Pop Gate, and Swap Gate", "Encoder Gate, Decoder Gate, and Latent Gate", "A", "Easy"),
        (t3, "What is the primary role of the 'Forget Gate' in an LSTM cell?",
         "Deciding what information to discard from the previous cell state C_{t-1} using a sigmoid function: f_t = sigma(W_f * [h_{t-1}, x_t] + b_f)",
         "Resetting all weights to zero", "Deleting the current word token", "Clearing GPU RAM", "A", "Medium"),
        (t3, "What component in an LSTM serves as a constant error carousel / linear highway allowing gradients to flow across hundreds of time steps with minimal decay?",
         "Cell State (C_t)", "Hidden State (h_t) alone", "Candidate Vector", "Softmax Layer", "A", "Medium"),
        (t3, "How does the Gated Recurrent Unit (GRU) simplify the LSTM architecture (Cho et al., 2014)?",
         "It merges cell state and hidden state, and combines gates into just two gates: an Update Gate and a Reset Gate",
         "It removes all gates completely", "It replaces recurrence with feedforward dense layers", "It only accepts binary inputs", "A", "Medium"),
        (t3, "What is a 'Bidirectional RNN' (BiLSTM)?",
         "A network comprising two independent recurrent layers that process the input sequence simultaneously in both forward and reverse chronological order",
         "An RNN that translates between two languages", "An RNN that predicts both inputs and outputs", "An RNN running on two computers", "A", "Easy"),
        (t3, "In a Sequence-to-Sequence (Seq2Seq) architecture for machine translation, what is the role of the 'Encoder'?",
         "To process the variable-length input sequence and compress it into a fixed-size latent context vector",
         "To generate the final target translation", "To display subtitles on screen", "To format output into JSON", "A", "Easy"),
        (t3, "What major limitation of the fixed-size context vector in basic Seq2Seq led Bahdanau et al. (2014) to introduce the Attention Mechanism?",
         "The bottleneck problem where compressing long sentences into a single vector caused severe information loss",
         "Inability to run on GPUs", "Lack of backpropagation support", "Failure on short sentences", "A", "Medium"),
        (t3, "What is 'Teacher Forcing' during RNN training?",
         "Feeding the ground truth target token from the previous time step as input to the decoder instead of the model's own predicted token",
         "A human teacher manually grading each output", "Penalizing models that generate errors", "Pre-training on Wikipedia", "A", "Hard"),
        (t3, "What deep learning model combination is traditionally used for Image Captioning?",
         "A CNN encoder to extract visual feature vectors paired with an RNN/LSTM decoder to generate descriptive sentence tokens",
         "A Decision Tree paired with Random Forest", "Two linear regression models", "A K-Means clusterer", "A", "Easy")
    ]

    u4 = "Unit 4: Deep Unsupervised Learning, GANs & Transfer Learning"
    t4 = "Autoencoders, GANs & Transfer Learning"
    dl_u4 = [
        (t4, "What is the primary objective of an Autoencoder neural network?",
         "To learn an efficient low-dimensional compressed representation (encoding) of input data by training to reconstruct the input at its output layer",
         "To classify images into 1000 categories", "To predict future stock prices", "To encrypt passwords", "A", "Easy"),
        (t4, "What are the two core structural components of an Autoencoder?",
         "Encoder (compresses input into latent bottleneck code z) and Decoder (reconstructs input from z)",
         "Generator and Discriminator", "Actor and Critic", "Policy and Value networks", "A", "Easy"),
        (t4, "What probabilistic extension of autoencoders enforces a Gaussian prior over the latent space to enable smooth generative sampling?",
         "Variational Autoencoder (VAE)", "Denoising Autoencoder", "Sparse Autoencoder", "Contractive Autoencoder", "A", "Medium"),
        (t4, "What two terms comprise the loss function optimized in a Variational Autoencoder (ELBO)?",
         "Reconstruction Loss (e.g. MSE or BCE) + Kullback-Leibler (KL) Divergence regularization term",
         "Cross-entropy + Information Gain", "Hinge loss + L1 penalty", "Accuracy + F1 score", "A", "Hard"),
        (t4, "What two adversarial neural networks compete against each other in a Generative Adversarial Network (GAN) proposed by Ian Goodfellow (2014)?",
         "Generator (generates synthetic data) and Discriminator (distinguishes real data from synthetic fakes)",
         "Encoder and Decoder", "Teacher and Student", "Forward network and Backward network", "A", "Easy"),
        (t4, "What is the objective of the Generator in a GAN minimax game?",
         "To generate realistic synthetic data that minimizes the probability of the Discriminator correctly identifying it as fake",
         "To classify input images", "To compress images into MP3 files", "To optimize database queries", "A", "Easy"),
        (t4, "What training instability in GANs occurs when the generator collapses to producing only a limited variety of identical output samples?",
         "Mode Collapse", "Vanishing Gradients", "Overfitting", "Catastrophic Forgetting", "A", "Medium"),
        (t4, "What is 'Transfer Learning' in deep learning?",
         "Reusing a model pre-trained on a massive dataset (e.g. ImageNet) as the starting point for a model on a different but related target task",
         "Transferring files over FTP", "Copying weights between CPU registers", "Translating code from C to Python", "A", "Easy"),
        (t4, "What is 'Fine-Tuning' in transfer learning workflows?",
         "Unfreezing some or all layers of a pre-trained model and training them on target domain data with a small learning rate",
         "Changing monitor brightness", "Tuning audio equalizers", "Increasing batch size by 100", "A", "Easy"),
        (t4, "Why is Data Augmentation (e.g. random cropping, horizontal flipping, rotation) routinely applied during computer vision model training?",
         "To artificially expand dataset diversity and invariance, significantly reducing overfitting",
         "To compress images to smaller file sizes", "To make images look artistic", "To convert color images to grayscale", "A", "Easy"),
        (t4, "What generative model family replaces GANs in state-of-the-art image synthesis (e.g. Stable Diffusion, Midjourney)?",
         "Denoising Diffusion Probabilistic Models (Diffusion Models)", "Decision Forests", "K-Means", "Single Perceptrons", "A", "Medium"),
        (t4, "What is a 'Wasserstein GAN' (WGAN)?",
         "A GAN variant that uses Earth Mover's (Wasserstein-1) Distance as loss to provide smooth, meaningful gradients and eliminate mode collapse",
         "A GAN that generates water textures", "A GAN trained underwater", "A GAN running on Windows only", "A", "Hard")
    ]

    u5 = "Unit 5: Responsible AI, MLOps and Industrial Applications"
    t5 = "Explainable AI, MLOps & Model Deployment"
    dl_u5 = [
        (t5, "What is the primary goal of Explainable AI (XAI)?",
         "To produce transparent methods and interpretations that allow human experts to understand, trust, and audit how complex AI models make predictions",
         "To write code comments automatically", "To translate Python into English", "To speed up model training by 2x", "A", "Easy"),
        (t5, "Which model-agnostic explainability method explains individual predictions by approximating the model locally with an interpretable surrogate model?",
         "LIME (Local Interpretable Model-agnostic Explanations)", "PCA", "K-Means", "Grid Search", "A", "Medium"),
        (t5, "What explainability framework calculates the fair marginal contribution of each input feature based on cooperative game theory?",
         "SHAP (SHapley Additive exPlanations)", "Lasso regression", "Backpropagation", "Z-Score Analysis", "A", "Medium"),
        (t5, "What is 'Algorithmic Bias' in production artificial intelligence systems?",
         "Systematic and repeatable errors in computer systems that create unfair outcomes, privileging one arbitrary group of users over another",
         "A mathematical error in floating point addition", "A bias weight in a neural neuron", "A compiler warning", "A", "Easy"),
        (t5, "What is 'Concept Drift' in deployed machine learning systems?",
         "When the statistical relationship between input features and target labels changes over time in production environments",
         "When hard drives run out of storage", "When Python libraries are updated", "When developers change jobs", "A", "Medium"),
        (t5, "What open-source platform manages the end-to-end machine learning lifecycle including experiment tracking, model registry, and deployment?",
         "MLflow (or Kubeflow)", "Apache HTTP Server", "Git alone", "VLC Media Player", "A", "Easy"),
        (t5, "What is 'Model Quantization' in deploying deep neural networks to production edge devices?",
         "Converting floating-point 32-bit weights (FP32) into reduced precision integers (such as INT8) to drastically reduce memory and latency with negligible loss in accuracy",
         "Quantifying the number of lines of Python code", "Calculating the purchase cost of GPUs", "Measuring model accuracy in percentages", "A", "Easy"),
        (t5, "Which open-source high-performance inference runtime developed by Microsoft and partner companies standardizes model representation across frameworks?",
         "ONNX Runtime (Open Neural Network Exchange)", "PostgreSQL", "React.js", "Docker CLI", "A", "Medium"),
        (t5, "What is 'Canary Deployment' in model deployment strategies?",
         "Gradually rolling out a new model version to a small subset (e.g. 5%) of live production users to verify performance before full rollout",
         "Deploying models in coal mines", "Training models on bird sounds", "Deploying models exclusively at midnight", "A", "Medium"),
        (t5, "What is 'Data Poisoning' in adversarial machine learning security?",
         "An attack where malicious data is injected into the training set to manipulate the model's behavior or create backdoors",
         "Deleting database backups", "Overheating CPU chips", "Corrupting network DNS", "A", "Medium"),
        (t5, "What is the primary role of a 'Feature Store' (e.g. Feast) in production MLOps pipelines?",
         "A centralized repository that stores, versions, and serves standardized features consistently for both offline training and low-latency online inference",
         "An app store for downloading smartphone games", "A repository of CSS icons", "A cloud billing dashboard", "A", "Medium"),
        (t5, "What is 'A/B Testing' in production model evaluation?",
         "Randomly splitting live production traffic between two candidate models (Model A vs Model B) to statistically evaluate business KPIs",
         "Testing two different monitors", "Running tests on two CPUs", "Alphabetical sorting of test cases", "A", "Easy")
    ]

    for q in dl_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in dl_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in dl_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in dl_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in dl_u5: questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_nlp_questions():
    questions = []
    sub = "Natural Language Processing"
    branch = "Artificial Intelligence & Data Science"
    year = "Third Year"
    sem = "Semester VI"

    u1 = "Unit 1: Lexical Analysis and Morphology"
    t1 = "Morphology & Language Modeling"
    nlp_u1 = [
        (t1, "What is 'Morphology' in natural language processing?",
         "The study of the internal structure of words and how words are formed from smaller meaningful units called morphemes",
         "The study of sentence syntax trees", "The study of vocal chord acoustics", "The calculation of vector distances", "A", "Easy"),
        (t1, "What is the difference between a 'Stem' and a 'Lemma' in lexical analysis?",
         "A stem is a crude heuristic chopping of affixes; a lemma is the canonical base dictionary form of a word based on vocabulary and POS",
         "A stem is always capitalized", "A lemma is an antonym", "There is no difference in modern NLP", "A", "Easy"),
        (t1, "Which computational model with states and transitions is widely used for morphological parsing and inflectional analysis?",
         "Finite State Transducer (FST)", "Decision Tree", "Support Vector Machine", "Convolutional Layer", "A", "Medium"),
        (t1, "What is a 'Part-of-Speech' (POS) Tagging task in NLP?",
         "Assigning grammatical category labels (such as Noun, Verb, Adjective, Preposition) to each token in a sentence",
         "Counting the total words in an essay", "Checking if spelling is correct", "Translating text into Hindi", "A", "Easy"),
        (t1, "In N-gram language modeling, what does a 'Bigram' model assume under the Markov assumption?",
         "The probability of the current word depends solely on the single immediately preceding word: P(w_n | w_{n-1})",
         "Words are completely independent of all context", "Sentences must have at least 10 words", "Words depend on the entire history", "A", "Easy"),
        (t1, "What is 'Perplexity' in evaluating statistical language models?",
         "A metric of how well a probability model predicts a sample; lower perplexity indicates better predictive ability (PPL = 2^H)",
         "The percentage of misspelled words", "The training time in minutes", "The number of tokens in vocabulary", "A", "Medium"),
        (t1, "Why is smoothing (e.g. Good-Turing, Kneser-Ney smoothing) required in N-gram language models?",
         "To reassign probability mass from frequent n-grams to unseen n-grams to prevent assigning zero probability to valid test sentences",
         "To convert words into embeddings", "To remove stop words", "To lowercase all characters", "A", "Medium"),
        (t1, "Which generative probabilistic model with hidden states and observed emissions is traditionally used for POS tagging and speech recognition?",
         "Hidden Markov Model (HMM)", "K-Means", "Linear Regression", "Autoencoder", "A", "Easy"),
        (t1, "What dynamic programming algorithm finds the most likely sequence of hidden states (e.g. POS tags) in an HMM?",
         "Viterbi Algorithm", "Dijkstra's Algorithm", "Forward-Backward Algorithm", "Inside-Outside Algorithm", "A", "Medium"),
        (t1, "What dynamic programming algorithm calculates the total probability of an observed sequence in an HMM?",
         "Forward Algorithm", "Viterbi Algorithm", "Bubble Sort", "A* Search", "A", "Hard"),
        (t1, "What algorithm is used to train HMM transition and emission parameters from unannotated text (unsupervised estimation)?",
         "Baum-Welch Algorithm (Expectation-Maximization for HMMs)", "Gradient Descent", "QuickSort", "Nelder-Mead", "A", "Hard"),
        (t1, "What linguistic property of many Indian languages (like Marathi, Hindi, Tamil) poses challenges for standard morphology parsers?",
         "High morphological richness, agglutination, and complex inflectional paradigms",
         "Complete lack of verbs", "Using non-alphabetical hieroglyphs", "Strict fixed word order", "A", "Medium")
    ]

    u2 = "Unit 2: Speech Processing & Acoustic Models"
    t2 = "Speech Processing & Audio Recognition"
    nlp_u2 = [
        (t2, "What are the primary vocal organs involved in human speech articulation?",
         "Vocal cords (larynx), tongue, teeth, lips, alveolar ridge, hard palate, and velum (soft palate)",
         "Ears and auditory cortex", "Eyeballs and retina", "Finger muscles", "A", "Easy"),
        (t2, "What is a 'Phoneme' in linguistics and acoustic modeling?",
         "The smallest perceptually distinct unit of sound in a specified language that distinguishes one word from another",
         "A written letter in an alphabet", "A paragraph of text", "A musical note frequency", "A", "Easy"),
        (t2, "What spectral audio representation is most widely used as input features for automated speech recognition (ASR)?",
         "Mel-Frequency Cepstral Coefficients (MFCCs) / Mel-Spectrograms", "Raw uncompressed WAV amplitude only", "MP3 bitrate headers", "MIDI tracks", "A", "Medium"),
        (t2, "Why is the 'Mel Scale' used in acoustic audio signal processing?",
         "It approximates the human auditory system's non-linear frequency perception, which is more sensitive to pitch changes at lower frequencies",
         "It converts sound into text strings", "It compresses audio to 10% size", "It removes background noise automatically", "A", "Medium"),
        (t2, "What is 'Word Boundary Detection' (Speech Segmentation) in continuous speech processing?",
         "Identifying the acoustic transition points where one word ends and the next begins in continuous conversational speech",
         "Drawing boxes around words on a page", "Counting punctuation marks", "Measuring microphone decibels", "A", "Easy"),
        (t2, "What is 'Text-to-Speech' (TTS) synthesis?",
         "Converting written digital text into synthesized human-like spoken audio waveforms",
         "Transcribing recorded speech into text", "Translating English audio to Spanish", "Filtering background noise from phone calls", "A", "Easy"),
        (t2, "What traditional TTS approach generates speech by splicing and stringing together recorded segments of real human voice recordings?",
         "Concatenative Speech Synthesis", "Formant Synthesis", "WaveNet Diffusion", "Neural Vocoding", "A", "Medium"),
        (t2, "What neural vocoder architecture developed by DeepMind generates raw audio waveforms sample-by-sample using dilated causal convolutions?",
         "WaveNet", "AlexNet", "BERT", "VGG-19", "A", "Medium"),
        (t2, "In speech recognition systems, what is the role of the 'Acoustic Model'?",
         "To model the relationship between the audio signal features (e.g. MFCCs) and phonetic acoustic units",
         "To check grammatical spelling of sentences", "To translate between languages", "To format output into HTML", "A", "Easy"),
        (t2, "In speech recognition systems, what is the role of the 'Language Model'?",
         "To compute the probability distribution over word sequences, ensuring recognized words form coherent, natural sentences",
         "To measure acoustic volume", "To power the physical speakers", "To calibrate the microphone sensitivity", "A", "Easy"),
        (t2, "What metric evaluates automated speech recognition accuracy by calculating insertions, deletions, and substitutions?",
         "Word Error Rate (WER)", "BLEU score", "ROUGE-1", "Mean Squared Error", "A", "Easy"),
        (t2, "What search algorithm is typically used in speech decoders to explore the most promising acoustic/language hypotheses efficiently?",
         "Beam Search (pruned Viterbi search)", "Breadth-First Exhaustive Search", "Random Search", "Linear Search", "A", "Medium")
    ]

    u3 = "Unit 3: Parsing Algorithms & Named Entity Recognition"
    t3 = "Syntactic Parsing & Sequence Labeling"
    nlp_u3 = [
        (t3, "What is a 'Context-Free Grammar' (CFG) characterized by?",
         "Four-tuple G = (V, Sigma, R, S) where every production rule in R rewrites a single non-terminal into a string of terminals and non-terminals",
         "Rules where terminals rewrite into non-terminals", "Grammars with no rules", "Regular expressions with no parentheses", "A", "Medium"),
        (t3, "What dynamic programming chart parsing algorithm parses sentences in O(n^3) time using grammars in Chomsky Normal Form (CNF)?",
         "CYK (Cocke-Younger-Kasami) Algorithm", "Viterbi Algorithm", "Dijkstra Algorithm", "Kruskal Algorithm", "A", "Medium"),
        (t3, "What chart parser parses arbitrary context-free grammars using dot notations and operations: Predictor, Scanner, Completer?",
         "Earley Parser", "CYK Parser", "Shift-Reduce Parser", "Recursive Descent Parser", "A", "Hard"),
        (t3, "What parsing formalism represents sentence syntax via directed binary grammatical relations (e.g. nsubj, dobj, amod) between words rather than phrase trees?",
         "Dependency Parsing", "Constituency / Phrase Structure Parsing", "Finite State Morphological Parsing", "N-gram Modeling", "A", "Easy"),
        (t3, "What is 'Syntactic Ambiguity' (such as Prepositional Phrase Attachment) in NLP?",
         "A situation where a sentence can produce multiple valid parse trees representing different interpretations (e.g. 'I saw the man with a telescope')",
         "A sentence with misspelled words", "A sentence with foreign words", "An audio file with static noise", "A", "Easy"),
        (t3, "What information extraction task identifies and classifies mentions of rigid entities (Persons, Organizations, Locations, Dates) in unstructured text?",
         "Named Entity Recognition (NER)", "Part-of-Speech Tagging", "Sentence Tokenization", "Stemming", "A", "Easy"),
        (t3, "What tagging scheme is standardly used for Named Entity Recognition to distinguish between beginning, inside, and outside of multi-word entities?",
         "BIO (or IOB / BILOU) Tagging Scheme", "ASCII encoding", "RGB color scheme", "Base64 encoding", "A", "Easy"),
        (t3, "What discriminative sequence labeling model optimizes conditional probability P(Y | X) globally over entire label sequences, avoiding the label bias problem of MEMMs?",
         "Conditional Random Fields (CRF)", "Maximum Entropy Markov Models (MEMM)", "Naive Bayes Classifier", "Single Perceptron", "A", "Hard"),
        (t3, "What is 'Shallow Parsing' (Chunking)?",
         "Identifying non-recursive constituent phrases (like Noun Phrases NP, Verb Phrases VP) without building a complete deep parse tree",
         "Parsing text without grammar rules", "Reading only the first 5 words of a paragraph", "Converting text to uppercase", "A", "Easy"),
        (t3, "In transition-based dependency parsing, what three actions does the parser execute using a stack, a buffer, and relation arcs?",
         "Shift, Left-Arc, and Right-Arc", "Push, Pop, and Peek", "Map, Reduce, and Filter", "Predict, Scan, and Complete", "A", "Hard"),
        (t3, "What probabilistic extension of CFGs assigns probability scores to each production rule such that P(A -> alpha) sums to 1 for each non-terminal A?",
         "Probabilistic Context-Free Grammar (PCFG)", "Deterministic Finite Automaton", "Hidden Markov Model", "Turing Machine", "A", "Medium"),
        (t3, "What metric evaluates Named Entity Recognition performance?",
         "Precision, Recall, and Micro/Macro F1-Score on entity spans", "Accuracy on punctuation marks", "Perplexity", "Word Error Rate", "A", "Easy")
    ]

    u4 = "Unit 4: Lexical Knowledge Networks & Word Sense Disambiguation"
    t4 = "WordNet, WSD & Coreference"
    nlp_u4 = [
        (t4, "What is 'WordNet' developed at Princeton University under George Miller?",
         "A large lexical database of English where nouns, verbs, adjectives, and adverbs are grouped into sets of cognitive synonyms called 'Synsets'",
         "A social network for linguists", "A web search engine", "A Python package for downloading web pages", "A", "Easy"),
        (t4, "What lexical semantic relation represents the 'IS-A' relationship in WordNet (e.g. 'robin' is a kind of 'bird')?",
         "Hypernymy (superordinate) and Hyponymy (subordinate)", "Meronymy and Holonymy", "Antonymy", "Synonymy", "A", "Easy"),
        (t4, "What lexical semantic relation represents the 'PART-OF' relationship in WordNet (e.g. 'wheel' is part of 'car')?",
         "Meronymy (part) and Holonymy (whole)", "Hyponymy and Hypernymy", "Polysemy", "Metaphor", "A", "Easy"),
        (t4, "What is 'Word Sense Disambiguation' (WSD)?",
         "The task of computationally determining which sense of a polysemous word is used in a specific sentence context",
         "Correcting spelling errors in words", "Translating words into Spanish", "Counting syllables in a word", "A", "Easy"),
        (t4, "What classic dictionary-based algorithm disambiguates a target word by calculating overlap between words in dictionary definitions of senses and the context sentence?",
         "Lesk Algorithm (Simplified Lesk)", "Viterbi Algorithm", "PageRank Algorithm", "CYK Algorithm", "A", "Medium"),
        (t4, "What is 'Coreference Resolution' in natural language processing?",
         "The task of identifying all referring expressions (such as pronouns, proper nouns, noun phrases) in a discourse that refer to the same real-world entity",
         "Checking grammar agreement between subject and verb", "Resolving merge conflicts in git", "Translating references in bibliographies", "A", "Easy"),
        (t4, "In the sentence 'Dr. Ambedkar drafted the Constitution, and he presented it to the assembly', what linguistic phenomenon links 'he' to 'Dr. Ambedkar'?",
         "Anaphora Resolution (Pronominal Anaphora)", "Metaphorical Extension", "Morphological Derivation", "Part-of-Speech Tagging", "A", "Easy"),
        (t4, "What are 'Semantic Roles' (Thematic Roles) such as Agent, Patient, Instrument, and Theme in semantic analysis?",
         "Abstract conceptual roles that express the semantic relationship between a predicate (event) and its participants",
         "Grammatical roles like subject and object only", "HTML roles for web accessibility", "Database user permissions", "A", "Medium"),
        (t4, "What project developed at UC Berkeley annotates sentences with semantic frames and frame elements based on Fillmore's Frame Semantics?",
         "FrameNet (and PropBank)", "ImageNet", "WordNet only", "Wikipedia", "A", "Medium"),
        (t4, "What linguistic property describes words having multiple related meanings (e.g. 'wood' meaning forest vs building material)?",
         "Polysemy", "Homonymy (unrelated identical words)", "Synonymy", "Antonymy", "A", "Easy"),
        (t4, "What is 'Cross-Lingual WordNet' (such as IndoWordNet)?",
         "A linked lexical network interconnecting WordNets of multiple languages through shared conceptual synset IDs",
         "A translation dictionary without relations", "An alphabet conversion tool", "A font package", "A", "Easy"),
        (t4, "What graph-based unsupervised algorithm applies PageRank-like propagation over lexical semantic graphs to perform Word Sense Disambiguation?",
         "Babelfy / Personalized PageRank over WordNet graphs", "Dijkstra Shortest Path", "Binary Search", "Kruskal MST", "A", "Hard")
    ]

    u5 = "Unit 5: NLP Applications & Modern Architectures"
    t5 = "Transformers, Sentiment & Machine Translation"
    nlp_u5 = [
        (t5, "What revolutionary neural architecture introduced by Vaswani et al. (2017) discarded recurrent connections and relied entirely on Self-Attention?",
         "The Transformer Architecture", "Multilayer Perceptron", "Convolutional ResNet", "Deep Boltzmann Machine", "A", "Easy"),
        (t5, "What is the mathematical formula for Scaled Dot-Product Attention given queries Q, keys K, values V, and dimension d_k?",
         "Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V", "Attention = Q * K * V", "Attention = sigmoid(Q + K) * V", "Attention = relu(Q * K^T)", "A", "Easy"),
        (t5, "What pre-trained transformer model by Devlin et al. (Google, 2018) uses bidirectional masked language modeling (MLM) for natural language understanding?",
         "BERT (Bidirectional Encoder Representations from Transformers)", "GPT-1", "Word2Vec", "ELMo", "A", "Easy"),
        (t5, "What task classifies text documents into positive, negative, or neutral sentiment polarity?",
         "Sentiment Analysis", "Named Entity Recognition", "Dependency Parsing", "Speech Synthesis", "A", "Easy"),
        (t5, "What task determines whether a hypothesis sentence is True (Entailment), False (Contradiction), or Undetermined (Neutral) given a premise?",
         "Natural Language Inference (NLI) / Textual Entailment", "Question Answering", "Machine Translation", "Topic Modeling", "A", "Easy"),
        (t5, "In modern Neural Machine Translation (NMT), what metric standardly evaluates translation quality against professional human reference translations?",
         "BLEU (Bilingual Evaluation Understudy) and METEOR / COMET", "Perplexity", "Accuracy on words", "Mean Squared Error", "A", "Easy"),
        (t5, "What is 'Cross-Lingual Information Retrieval' (CLIR)?",
         "A retrieval system where users query in one language (e.g. Marathi) to retrieve relevant documents written in another language (e.g. English)",
         "Searching across two different hard drives", "Searching on both Google and Yahoo", "Translating HTML tags", "A", "Medium"),
        (t5, "What is 'Extractive Question Answering' (such as SQuAD benchmark)?",
         "Locating and extracting the exact start and end token indices of the answer span directly from a provided passage of text",
         "Writing an original creative story", "Calling a customer support phone number", "Translating queries into SQL", "A", "Easy"),
        (t5, "What is 'Abstractive Text Summarization' compared to 'Extractive Summarization'?",
         "Abstractive summarization synthesizes and paraphrases key concepts generating novel words not present in the original text; extractive merely selects verbatim sentences",
         "Abstractive summarization deletes random paragraphs", "Extractive summarization creates new vocabulary", "Both methods are completely identical", "A", "Medium"),
        (t5, "Why is 'Positional Encoding' necessary in Transformer models?",
         "Because self-attention operates as a set-based permutation-invariant function with no innate sense of token order or sequence position",
         "Because computers cannot read negative indices", "Because GPU threads require thread IDs", "Because vocabulary sizes are bounded", "A", "Hard"),
        (t5, "What autoregressive transformer family by OpenAI generates text sequentially token-by-token using causal masked self-attention?",
         "GPT (Generative Pre-trained Transformer) Series", "BERT Series", "T5 Encoder", "RoBERTa", "A", "Easy"),
        (t5, "What is 'Multi-Head Attention' in the Transformer architecture?",
         "Projecting queries, keys, and values into multiple representation subspaces in parallel to attend to information from different representation positions simultaneously",
         "Running the model on multiple computer screens", "A model with multiple output classification heads", "A server with multiple CPUs", "A", "Medium")
    ]

    for q in nlp_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in nlp_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in nlp_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in nlp_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in nlp_u5: questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_edge_ai_questions():
    questions = []
    sub = "Fundamental Edge AI"
    branch = "Artificial Intelligence & Data Science"
    year = "Third Year"
    sem = "Semester VI"

    u1 = "Unit 1: Fundamentals of Heterogeneous Systems & SoC"
    t1 = "SoC Architecture & Inter-Processor Communication"
    eai_u1 = [
        (t1, "What defines a System-on-Chip (SoC) in modern embedded edge computing?",
         "An integrated circuit that integrates all core components of an electronic computer (CPU, GPU, memory controller, I/O, accelerators) onto a single silicon substrate",
         "A motherboard with separate plug-in cards", "A cloud server farm", "A software operating system", "A", "Easy"),
        (t1, "What is the primary architectural difference between an Application Processor (e.g. ARM Cortex-A) and a Microcontroller (e.g. ARM Cortex-M)?",
         "Application processors feature MMUs, run rich full operating systems (Linux/Android), and optimize for high throughput; microcontrollers prioritize deterministic real-time control with low power consumption",
         "Microcontrollers run 100x faster than Application Processors", "Application processors do not require power", "There is no difference", "A", "Medium"),
        (t1, "What is a 'Heterogeneous Compute System' on an Edge AI device?",
         "A system combining multiple processor architectures (e.g. CPU, GPU, DSP, NPU) on a single platform to execute different computational tasks efficiently",
         "A system with computers made by different manufacturers", "A computer with two different monitors", "A system with mixed USB ports", "A", "Easy"),
        (t1, "What is Inter-Processor Communication (IPC) on a heterogeneous multicore SoC?",
         "Hardware and software protocols (such as RPMsg, OpenAMP) that enable heterogeneous CPU cores to synchronize and exchange messages/data",
         "Browsing web pages via HTTP", "Typing commands into terminal", "Connecting to a printer via Wi-Fi", "A", "Medium"),
        (t1, "Which IPC mechanism provides the highest throughput for transferring raw camera video frames between camera ISP and AI accelerators on an SoC?",
         "Shared Physical Memory buffers with hardware cache coherency", "Serial UART lines", "Software HTTP requests", "TCP socket loopback", "A", "Medium"),
        (t1, "What is a Remote Procedure Call (RPC) in embedded multicore software?",
         "A protocol that allows a program on one processor core to cause a procedure/subroutine to execute on another core transparently",
         "A telephone call to technical support", "An operating system reboot command", "A disk formatting instruction", "A", "Easy"),
        (t1, "What open-source software framework standardizes communication and lifecycle management between Linux host processors and RTOS coprocessors on heterogeneous SoCs?",
         "OpenAMP (Open Asymmetric Multi-Processing) and RPMsg", "Apache Spark", "Node.js", "Docker Compose", "A", "Hard"),
        (t1, "Why is low latency critical for Edge AI applications compared to cloud AI processing?",
         "Edge AI makes immediate real-time decisions locally (e.g. autonomous braking, robotic control, medical defibrillators) without waiting for network round-trip delays",
         "Because edge devices have faster internet speeds than data centers", "Because edge devices have infinite memory", "Because cloud AI is illegal", "A", "Easy"),
        (t1, "What is a key security and privacy advantage of Edge AI computing?",
         "Sensitive user data (e.g. biometric camera feeds, voice recordings) is processed locally on-device without being transmitted over public internet networks",
         "Edge devices cannot be physically stolen", "Edge AI never makes classification errors", "Edge AI eliminates software bugs", "A", "Easy"),
        (t1, "What hardware constraint severely limits edge AI deployment compared to cloud data centers?",
         "Strict constraints on thermal dissipation, physical size, battery power consumption, and memory capacity",
         "Edge devices cannot execute addition operations", "Edge devices cannot connect to cameras", "Edge devices only run Windows 95", "A", "Easy"),
        (t1, "What is Asymmetric Multiprocessing (AMP) on an embedded SoC?",
         "An execution model where different processor cores run different operating systems and execute distinct dedicated tasks independently",
         "All cores running identical Linux instances under a single scheduler", "A computer with an odd number of cores", "A broken processor", "A", "Medium"),
        (t1, "What is 'Zero-Copy' data transfer in embedded computer vision pipelines?",
         "Sharing memory pointers directly between camera capture, preprocessing, and inference hardware without copying bytes across buffers",
         "Transferring zero bytes over the bus", "A file deletion command", "Compressing files to zero size", "A", "Medium")
    ]

    u2 = "Unit 2: Hardware Abstraction Layers (HAL) & Power Management"
    t2 = "HAL, MMIO & Power-Aware Scheduling"
    eai_u2 = [
        (t2, "What is a Hardware Abstraction Layer (HAL) in embedded systems programming?",
         "A layer of software drivers and APIs that provides application code with a uniform, device-independent interface to physical hardware peripherals",
         "A sheet of metal that protects circuits", "A graphics rendering engine", "A compiler optimization pass", "A", "Easy"),
        (t2, "What is Memory-Mapped I/O (MMIO)?",
         "A hardware mechanism where peripheral device registers and control registers are mapped directly into the CPU's memory address space",
         "Storing files on an external SD card", "Swapping memory to hard disk", "A cloud storage API", "A", "Medium"),
        (t2, "What is 'Pin Multiplexing' (Pin Muxing) on microcontrollers and SoCs?",
         "The capability of a physical silicon pin to be programmatically assigned to different internal hardware functions (e.g. GPIO, I2C, SPI, UART, PWM)",
         "Connecting multiple wires to one pin using solder", "Multiplying clock frequencies", "A hardware defect", "A", "Easy"),
        (t2, "What is 'Power Domain Management' on modern low-power edge processors?",
         "The ability to independently power down (gating) inactive silicon blocks and peripherals while keeping necessary subsystems powered",
         "Buying electricity from multiple power companies", "Using multiple AC adapters", "Running solar panels on servers", "A", "Medium"),
        (t2, "What is 'Dynamic Voltage and Frequency Scaling' (DVFS)?",
         "Dynamically adjusting processor clock frequency and operating voltage according to instantaneous computational workload to conserve energy",
         "Manually flipping electrical switches", "Overheating the CPU intentionally", "Alternating current to direct current conversion", "A", "Medium"),
        (t2, "What is a 'Wake-on-Interrupt' mechanism in battery-operated edge sensors?",
         "Keeping the main processor in an ultra-low-power deep sleep mode until an external hardware event (e.g. motion detection pin interrupt) triggers a wake-up",
         "Restarting the computer every hour", "An alarm clock ringtone", "A software infinite loop", "A", "Easy"),
        (t2, "What is the primary difference between a General-Purpose Compute Unit (CPU) and a Task-Specific Compute Unit (e.g. NPU)?",
         "CPUs offer programmable flexibility for diverse software; task-specific NPUs optimize hardwired data paths and arithmetic units for specific operations (e.g. matrix multiply) with extreme energy efficiency",
         "CPUs consume less power than task-specific units", "Task-specific units can run any operating system", "There is no difference", "A", "Easy"),
        (t2, "What is a 'Watchdog Timer' (WDT) in embedded edge deployments?",
         "A hardware timer that automatically resets the processor if the software hangs, enters an infinite loop, or fails to periodically 'kick/feed' the timer",
         "A timer that monitors security guards", "A clock displayed on the desktop", "A software profiling benchmark", "A", "Easy"),
        (t2, "What is 'Deep Sleep' (Standby) mode in edge microcontrollers?",
         "A power-saving state where the core CPU clock is stopped and high-speed oscillators are disabled, reducing power consumption to microamperes",
         "Turning off the room lights", "Running screensavers", "Formatting the hard drive", "A mode that causes permanent hardware shutdown", "A", "Easy"),
        (t2, "What is Direct Memory Access (DMA) controller and why is it vital for Edge AI pipelines?",
         "A specialized hardware unit that transfers data directly between peripherals (e.g. Camera/ADC) and memory without burdening the CPU with per-byte transfers",
         "A bus that allows random people to access data", "A software memory allocation function in C", "A security vulnerability", "A", "Medium"),
        (t2, "What communication bus protocol uses two bidirectional lines: Serial Data (SDA) and Serial Clock (SCL)?",
         "I2C (Inter-Integrated Circuit)", "SPI (Serial Peripheral Interface)", "CAN Bus", "RS-232", "A", "Easy"),
        (t2, "What high-speed synchronous 4-wire serial interface uses MOSI, MISO, SCK, and CS lines for fast sensor communication?",
         "SPI (Serial Peripheral Interface)", "I2C", "UART", "USB 1.0", "A", "Easy")
    ]

    u3 = "Unit 3: Basics of Neural Hardware Acceleration & Vision Processing"
    t3 = "SIMD Acceleration & MIPI-CSI Vision"
    eai_u3 = [
        (t3, "What does SIMD stand for in computer processor architecture?",
         "Single Instruction, Multiple Data", "Synchronous Interface Memory Device", "Silicon Integrated Matrix Driver", "Shared Instruction Modular Delivery", "A", "Easy"),
        (t3, "How does SIMD vectorization accelerate neural network calculations on edge CPUs (e.g. ARM NEON)?",
         "By executing a single arithmetic operation (like Multiply-Accumulate) across multiple data elements in a wide vector register simultaneously",
         "By running code on multiple cloud servers", "By skipping calculations completely", "By compiling to assembly", "A", "Easy"),
        (t3, "What camera interface specification developed by the Mobile Industry Processor Interface alliance is standard for high-bandwidth edge vision cameras?",
         "MIPI-CSI (Camera Serial Interface, e.g. CSI-2)", "VGA analog port", "Parallel SCSI port", "PS/2 keyboard port", "A", "Easy"),
        (t3, "What is the primary role of an Image Signal Processor (ISP) in an edge vision processing chain?",
         "Converting raw Bayer pattern sensor data through demosaicing, auto-white balance, auto-exposure, gamma correction, and noise filtering into viewable RGB/YUV images",
         "Compressing video into MP4 files exclusively", "Encrypting image files with RSA", "Uploading images to social media", "A", "Medium"),
        (t3, "What is the primary computational bottleneck when running raw high-resolution computer vision models on edge hardware?",
         "High-resolution frame buffers require enormous memory bandwidth and billions of convolution multiply-accumulate operations per second",
         "Camera sensors generate text files", "RGB colors require floating-point conversions", "HDMI cables overheat", "A", "Easy"),
        (t3, "What color space format separates luminance (Y) from chrominance (U/V) and is widely favored in edge video pipelines to reduce memory bandwidth?",
         "YUV / YCbCr (e.g. NV12, YUV420p)", "RGB24 exclusively", "CMYK print format", "Grayscale 1-bit", "A", "Easy"),
        (t3, "What open-source computer vision library optimized for edge devices provides real-time image processing and inference primitives?",
         "OpenCV", "Matplotlib", "Requests", "Jinja2", "A", "Easy"),
        (t3, "What is 'Frame Dropping' in edge video analytics under heavy computational load?",
         "Intentionally skipping intermediate video frames to keep the AI processing pipeline synchronized in real-time with incoming live video feeds",
         "Damaging physical glass lenses", "Corrupting memory sectors", "A network hardware fault", "A", "Medium"),
        (t3, "What hardware accelerator instruction computes (a * b) + c in a single clock cycle, forming the core primitive of neural convolutions?",
         "Fused Multiply-Accumulate (FMA / MAC)", "Bitwise XOR", "Floating Point Division", "Branch on Equal", "A", "Easy"),
        (t3, "Why is Ring-Buffer queuing commonly used between the camera capture driver and the edge AI inference model?",
         "To handle asynchronous timing jitter and decouple camera frame arrival rates from model processing times without dropping frames",
         "To encrypt video frames", "To convert video to audio", "To store historical video for 10 years", "A", "Medium"),
        (t3, "What ARM vector extension technology provides 128-bit SIMD processing for digital signal processing and machine learning on Cortex-A cores?",
         "ARM NEON", "Intel SSE", "AMD 3DNow", "MIPS ASE", "A", "Easy"),
        (t3, "What embedded Linux kernel framework provides standardized APIs for camera video capture and streaming peripherals?",
         "V4L2 (Video4Linux2)", "ALSA audio", "systemd", "glibc", "A", "Medium")
    ]

    u4 = "Unit 4: Specialized Accelerators (DSPs and NPUs)"
    t4 = "DSPs, NPUs & Edge Acceleration"
    eai_u4 = [
        (t4, "What does NPU stand for in modern AI hardware terminology?",
         "Neural Processing Unit", "Network Power Utility", "Nano Peripheral Unit", "Node Protocol Universal", "A", "Easy"),
        (t4, "What is the primary function of a Neural Processing Unit (NPU) on an edge SoC?",
         "A specialized, hardware-optimized circuit designed to accelerate neural network operations (convolutions, matrix multiplications, non-linear activations) with high TOPS/Watt",
         "To replace the system hard drive", "To render 3D video game graphics", "To route internet packets", "A", "Easy"),
        (t4, "What metric is standardly used to express the peak computational throughput of an edge AI accelerator?",
         "TOPS (Tera Operations Per Second)", "GHz CPU clock rate", "RPM disk rotational speed", "Baud rate", "A", "Easy"),
        (t4, "What metric measures the energy efficiency of an Edge AI accelerator for battery-powered edge computing?",
         "TOPS / Watt (Tera Operations per Second per Watt)", "Bytes per second", "Megapixels per dollar", "Clock latency in nanoseconds", "A", "Easy"),
        (t4, "What is a Digital Signal Processor (DSP) and how does it assist edge AI pipelines?",
         "A specialized microprocessor optimized for fast mathematical manipulation of real-world continuous signals (audio, sensor signals, image preprocessing) offloading the CPU",
         "A printer controller", "A wireless mouse driver", "A screen calibration tool", "A", "Medium"),
        (t4, "What proprietary hardware acceleration engine is embedded in Google Edge TPU devices?",
         "A custom ASIC designed by Google to run lightweight TensorFlow Lite models with high efficiency for edge applications",
         "An Intel Core i9 processor", "An NVIDIA GeForce graphics card", "A mechanical relay array", "A", "Easy"),
        (t4, "What edge AI module family by NVIDIA integrates GPU cores, ARM CPUs, and deep learning accelerators for edge robotics (e.g. Nano, Orin)?",
         "NVIDIA Jetson Series", "NVIDIA RTX 4090 Desktop", "NVIDIA Tesla V100 Server", "NVIDIA Quadro Mining Edition", "A", "Easy"),
        (t4, "What software toolchain compiles neural network computational graphs into optimized hardware-specific instructions for edge NPUs?",
         "NPU Model Compiler / Neural Graph Compiler (e.g. TensorRT, Edge TPU Compiler, TVM)",
         "Standard GNU gcc without flags", "Python interpreter runtime", "Web browser JavaScript engine", "A", "Medium"),
        (t4, "What is 'Kernel Fusion' in neural network graph optimization for edge accelerators?",
         "Combining multiple consecutive operations (e.g. Convolution + Batch Normalization + ReLU) into a single execution kernel to avoid reading/writing to external memory",
         "Fusing physical silicon chips with heat", "Merging two operating system kernels", "Concatenating two audio files", "A", "Hard"),
        (t4, "What is 'Memory Bandwidth Bottleneck' (Von Neumann Bottleneck) in edge deep learning inference?",
         "The latency and energy cost of repeatedly moving weight matrices between off-chip DRAM and processing cores exceeding the cost of the actual computation",
         "A broken RAM stick", "A slow internet Wi-Fi router", "A full hard drive", "A", "Medium"),
        (t4, "Which lightweight open-source inference engine developed by Apache/LF AI supports diverse edge hardware through automated tensor optimization?",
         "Apache TVM", "SQLite", "Apache Ant", "GNU Wget", "A", "Hard"),
        (t4, "What is the typical power budget for an ultra-low-power Edge AI microcontroller running TinyML models?",
         "Milliwatts (mW) or microwatts (uW)", "100 to 500 Watts", "10 Kilowatts", "Zero power", "A", "Easy")
    ]

    u5 = "Unit 5: Model Compression & Quantization (FP32 to INT8)"
    t5 = "Quantization, Pruning & TinyML Deployment"
    eai_u5 = [
        (t5, "What is the primary motivation for 'Model Compression' in Edge AI?",
         "To reduce model memory footprint, decrease inference latency, and minimize energy consumption so models fit on constrained edge devices",
         "To make the code readable to humans", "To increase the cost of the device", "To add more layers to the neural network", "A", "Easy"),
        (t5, "What mathematical transition occurs during INT8 Post-Training Quantization (PTQ)?",
         "Floating-point 32-bit (FP32) weights and activations are mapped to 8-bit integers (INT8) via scale and zero-point parameters: q = round(r / S) + Z",
         "Numbers are converted into hexadecimal strings", "Weights are rounded to 0 or 1 exclusively", "Matrix dimensions are reduced to 1x1", "A", "Medium"),
        (t5, "What percentage reduction in model memory size is achieved when converting a neural network from FP32 (4 bytes per parameter) to INT8 (1 byte per parameter)?",
         "Approximately 75% reduction (4x compression ratio)", "50% reduction", "99% reduction", "10% reduction", "A", "Easy"),
        (t5, "What is the difference between Symmetric Quantization and Asymmetric Quantization?",
         "Symmetric quantization maps zero to zero (Z = 0) with a symmetric range [-R, +R]; Asymmetric quantization maps arbitrary real ranges [R_min, R_max] with a non-zero zero-point Z",
         "Symmetric quantization is for text; asymmetric is for images", "Asymmetric quantization uses complex numbers", "There is no difference", "A", "Hard"),
        (t5, "What is 'Quantization-Aware Training' (QAT)?",
         "Simulating low-precision integer quantization effects (via fake quantization nodes) during model training/fine-tuning so the model learns to compensate for precision loss",
         "Training on quantum computers", "Training without data", "Deleting weights during testing", "A", "Hard"),
        (t5, "What is 'Weight Pruning' in neural network optimization?",
         "Removing redundant or near-zero connection weights from the network to create sparse models that execute faster and occupy less memory",
         "Deleting half of the training dataset", "Trimming physical wires inside the CPU", "Shortening variable names in source code", "A", "Easy"),
        (t5, "What is the difference between Structured Pruning and Unstructured Pruning?",
         "Structured pruning removes entire channels, filters, or layers preserving dense matrix structures for standard hardware; unstructured pruning zeroes out individual arbitrary weights creating sparse matrices",
         "Structured pruning only works on text models", "Unstructured pruning requires quantum computers", "There is no difference", "A", "Hard"),
        (t5, "What is 'Knowledge Distillation' in model compression?",
         "Training a compact, lightweight 'Student' network to mimic the soft probability outputs and behavior of a large, complex 'Teacher' network",
         "Reading textbooks into memory", "Copying weights verbatim between identical models", "Exporting database tables to CSV", "A", "Medium"),
        (t5, "What lightweight open-source software framework by Google is designed specifically for running deep learning models on mobile, edge, and IoT devices?",
         "TensorFlow Lite (TFLite) / TFLite Micro", "PyTorch Large Server", "Hadoop MapReduce", "Kubernetes", "A", "Easy"),
        (t5, "What emerging field of machine learning brings AI inference to ultra-low-power microcontrollers (e.g. ARM Cortex-M, Arduino UNO Q, ESP32) consuming under 1 mW?",
         "TinyML (Tiny Machine Learning)", "Cloud Big Data", "Quantum Grid Computing", "Mainframe Batch Analytics", "A", "Easy"),
        (t5, "What software tool provides an end-to-end web platform to collect edge sensor data, train TinyML models, and export optimized C++ source code for microcontrollers?",
         "Edge Impulse", "Microsoft Word", "Postman", "Wireshark", "A", "Easy"),
        (t5, "What is 'Calibration' in Post-Training Quantization?",
         "Passing a representative sample dataset through the model to determine the dynamic activation ranges (min/max) for setting optimal scaling factors S",
         "Measuring the physical temperature of the CPU", "Adjusting screen resolution", "Calibrating the battery voltage meter", "A", "Medium")
    ]

    for q in eai_u1: questions.append((branch, year, sem, sub, u1, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in eai_u2: questions.append((branch, year, sem, sub, u2, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in eai_u3: questions.append((branch, year, sem, sub, u3, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in eai_u4: questions.append((branch, year, sem, sub, u4, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    for q in eai_u5: questions.append((branch, year, sem, sub, u5, q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
    return questions


def get_all_sem6_questions():
    all_q = []
    all_q.extend(get_deep_learning_questions())
    all_q.extend(get_nlp_questions())
    all_q.extend(get_edge_ai_questions())
    return all_q
