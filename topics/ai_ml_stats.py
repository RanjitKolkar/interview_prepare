"""
AI, Statistics, Machine Learning & Mathematics Interview Preparation Questions & Answers
Format: (Question, Crisp Answer with Key Characteristics and Example)
"""

qa_ai_ml_stats = [
    (
        "What is Artificial Intelligence (AI) and what are its primary categories?",
        "**Direct Answer:** Artificial Intelligence is the engineering of computational systems capable of performing tasks typically requiring human intelligence, categorized into Narrow AI (task-specific), General AI (AGI - human-level across domains), and Super AI (ASI - surpassing all human capability).\n\n"
        "**Key Characteristics:**\n"
        "• Narrow AI (ANI): Operates strictly within predefined domain constraints; dominant current form.\n"
        "• General AI (AGI): Hypothetical cross-domain reasoning, transfer learning, and autonomous context synthesis.\n"
        "• Super AI (ASI): Speculative threshold where self-improving recursive AI exceeds aggregate human cognition.\n\n"
        "**Example:** AlphaFold predicting 3D protein structures is Narrow AI; a self-directed system writing novel physics proofs while managing a corporation would be AGI."
    ),
    (
        "What is the difference between AI, Machine Learning, and Deep Learning?",
        "**Direct Answer:** AI is the overarching umbrella discipline of intelligent machines; Machine Learning is the subset focused on learning statistical patterns from data without explicit rules; and Deep Learning is the subfield of ML utilizing multi-layered artificial neural networks to automatically extract hierarchical features.\n\n"
        "**Key Characteristics:**\n"
        "• AI encompasses rule-based expert systems, heuristic search (A*), logic programming, and statistical models.\n"
        "• Traditional ML relies heavily on manual feature engineering (e.g. TF-IDF, edge detection filters).\n"
        "• Deep Learning performs representation learning directly on raw data (pixels, raw text, audio waveforms) using deep architectures.\n\n"
        "**Example:** An expert system using if-else rules is AI; a Random Forest classifying spam via hand-crafted word-frequency features is ML; a ResNet classifying tumor biopsy images is Deep Learning."
    ),
    (
        "What is Supervised Learning vs. Unsupervised Learning vs. Reinforcement Learning?",
        "**Direct Answer:** Supervised Learning trains models on input-output pairs ($X, y$) to learn a predictive mapping; Unsupervised Learning discovers latent structures and clusters from unlabeled data ($X$); and Reinforcement Learning trains an agent to take sequential actions in an environment to maximize cumulative reward.\n\n"
        "**Key Characteristics:**\n"
        "• Supervised: Classification (discrete labels) and Regression (continuous outputs); requires expensive labeled training sets.\n"
        "• Unsupervised: Clustering (K-Means), Dimensionality Reduction (PCA), and Association Rules; no ground-truth target.\n"
        "• Reinforcement Learning: Formulated as a Markov Decision Process (MDP) using exploration vs. exploitation (Q-Learning, PPO).\n\n"
        "**Example:** Predicting house prices from square footage is Supervised; grouping customer purchasing behaviors into personas is Unsupervised; training an agent to master chess or fly a drone is Reinforcement Learning."
    ),
    (
        "What is the Turing Test and what are its modern limitations?",
        "**Direct Answer:** Proposed by Alan Turing in 1950 (the Imitation Game), the test evaluates whether a computer's natural language dialogue can be distinguished from that of a human by an evaluator; modern critiques note it tests behavioral deception rather than genuine understanding or consciousness.\n\n"
        "**Key Characteristics:**\n"
        "• Blinds the human judge to whether responses originate from a machine or human terminal.\n"
        "• Susceptible to the 'Chinese Room' argument (John Searle): syntactic symbol manipulation does not imply semantic comprehension.\n"
        "• Modern LLMs readily pass conversational Turing tests, yet still hallucinate and fail basic causal reasoning.\n\n"
        "**Example:** An LLM mimicking conversational human hesitations can deceive an evaluator into believing it is a human, despite having zero subjective awareness."
    ),
    (
        "What is Overfitting and Underfitting, and how do you diagnose them?",
        "**Direct Answer:** Overfitting occurs when a model memorizes noise and sample-specific idiosyncrasies in the training data, leading to poor test generalization (low train loss, high test loss); Underfitting occurs when a model is too simplistic to capture the underlying pattern (high train loss, high test loss).\n\n"
        "**Key Characteristics:**\n"
        "• Overfitting (High Variance): Model complexity is too high; mitigated by regularization, dropout, pruning, and more data.\n"
        "• Underfitting (High Bias): Model complexity is too low; mitigated by adding features, decreasing regularization, and using non-linear models.\n"
        "• Diagnosed via Learning Curves plotting train loss vs. validation loss across epochs.\n\n"
        "**Example:** An unconstrained 100-depth Decision Tree achieves 99.8% train accuracy but drops to 64% validation accuracy (Overfitting); a simple linear line fitted to an S-curve achieves 55% on both (Underfitting)."
    ),
    (
        "What is the Confusion Matrix and what metrics are derived from it?",
        "**Direct Answer:** A Confusion Matrix is a $2 \\times 2$ (or $N \\times N$) contingency table summarizing the counts of True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN) produced by a classification model against ground-truth labels.\n\n"
        "**Key Characteristics:**\n"
        "• Accuracy = $\\frac{TP+TN}{TP+TN+FP+FN}$; misleading for imbalanced classes.\n"
        "• Precision = $\\frac{TP}{TP+FP}$ (minimizes False Alarms).\n"
        "• Recall (Sensitivity) = $\\frac{TP}{TP+FN}$ (minimizes Missed Detections).\n"
        "• F1-Score = $2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}}$ (harmonic mean).\n\n"
        "**Example:** In cancer diagnosis, a False Negative (sending a sick patient home) is catastrophic; medical diagnostic models tune their decision threshold to maximize Recall above 99%."
    ),
    (
        "How does Gradient Descent work and what is the difference between Batch, Mini-Batch, and Stochastic (SGD)?",
        "**Direct Answer:** Gradient Descent is an iterative first-order optimization algorithm that minimizes an objective loss function by updating parameter weights in the opposite direction of the loss gradient, proportional to the learning rate $\\alpha$ ($w \\leftarrow w - \\alpha \\nabla L(w)$).\n\n"
        "**Key Characteristics:**\n"
        "• Batch GD: Computes gradients over the entire dataset; smooth convergence but computationally prohibitive on large data.\n"
        "• Stochastic GD (SGD): Updates weights after evaluating a single random sample; noisy path helps escape shallow local minima.\n"
        "• Mini-Batch GD: Evaluates mini-batches (e.g. 32, 64, 256 samples); balances GPU vectorization speed with gradient stability.\n\n"
        "**Example:** Training a neural network on 1,000,000 images using mini-batches of 128 images allows parallel tensor operations while updating weights 7,812 times per epoch."
    ),
    (
        "What is Backpropagation in Deep Learning?",
        "**Direct Answer:** Backpropagation is an efficient algorithm that calculates the partial derivative of the scalar loss function with respect to every weight in a multi-layer neural network by applying the calculus Chain Rule from the output layer backward to the input layer.\n\n"
        "**Key Characteristics:**\n"
        "• Forward Pass computes activations and loss; Backward Pass computes gradients via dynamic programming to avoid redundant matrix multiplications.\n"
        "• Prone to Vanishing Gradient problem (gradients shrink toward zero in deep networks using Sigmoid) and Exploding Gradients.\n"
        "• Mitigated by ReLU activations, Batch Normalization, and Residual Connections (ResNet skips).\n\n"
        "**Example:** In a 5-layer network predicting credit default, Backpropagation computes $\\frac{\\partial L}{\\partial w_{ij}}$ for layer 2 by chaining gradients through layers 5, 4, and 3."
    ),
    (
        "What is Bayes' Theorem and how is it applied in Machine Learning?",
        "**Direct Answer:** Bayes' Theorem calculates the posterior probability of a hypothesis $H$ given observed evidence $E$ using prior probability and likelihood: $P(H|E) = \\frac{P(E|H) \\cdot P(H)}{P(E)}$.\n\n"
        "**Key Characteristics:**\n"
        "• Prior $P(H)$: initial belief before observing new evidence.\n"
        "• Likelihood $P(E|H)$: probability of observing evidence $E$ assuming $H$ is true.\n"
        "• Posterior $P(H|E)$: updated belief incorporating the new evidence.\n"
        "• Foundation of Naive Bayes classifiers, Bayesian optimization, and Bayesian neural networks.\n\n"
        "**Example:** A rare malware affects 0.1% of systems ($P(M)=0.001$). A scan is 99% accurate. If a machine tests positive, Bayes' Theorem reveals the true probability of infection is only ~9% due to the low base rate."
    ),
    (
        "What is the difference between Parametric and Non-Parametric models?",
        "**Direct Answer:** Parametric models assume a fixed functional form with a predetermined number of parameters that do not grow with the size of the training dataset, whereas Non-Parametric models make no strict distributional assumptions and their effective parameter count grows with more training data.\n\n"
        "**Key Characteristics:**\n"
        "• Parametric: Linear Regression, Logistic Regression, Naive Bayes; fast to train, highly interpretable, higher bias.\n"
        "• Non-Parametric: K-Nearest Neighbors, Decision Trees, SVM with RBF kernel; flexible, captures complex non-linear boundaries, higher variance.\n"
        "• Non-parametric does not mean 'zero parameters', but rather flexible, data-driven parameter structures.\n\n"
        "**Example:** Linear Regression fits a fixed equation $y = w_1 x_1 + w_0$ regardless of whether you have 100 or 10,000,000 data rows; KNN stores all data points, increasing memory requirements as data grows."
    ),
    (
        "What are Activation Functions and why are Non-Linearities essential in Neural Networks?",
        "**Direct Answer:** Activation functions determine whether and to what degree a neuron should fire by transforming its weighted input sum ($w^T x + b$); non-linear activations are essential because without them, any multi-layered network collapses mathematically into a single linear regression ($W_2 W_1 x = W_{combined} x$).\n\n"
        "**Key Characteristics:**\n"
        "• Sigmoid: Maps to $(0, 1)$; causes vanishing gradients for large $|z|$; non-zero centered.\n"
        "• Tanh: Maps to $(-1, +1)$; zero-centered; still suffers from vanishing gradients at extremes.\n"
        "• ReLU (Rectified Linear Unit): $f(z) = \\max(0, z)$; computationally fast, avoids vanishing gradients for positive inputs; prone to 'Dying ReLU' (fixed by Leaky ReLU/GELU).\n\n"
        "**Example:** Modern Large Language Models (GPT, LLaMA) use GELU (Gaussian Error Linear Unit) or SwiGLU activation functions to allow smooth gradient flow during deep transformer pretraining."
    ),
    (
        "What is the Transformer Architecture and why did it replace RNNs and LSTMs?",
        "**Direct Answer:** The Transformer is a deep learning architecture based entirely on the Self-Attention mechanism, processing entire sequences in parallel rather than sequentially, which eliminates recurrent bottlenecks and allows scaling to billions of parameters across massive datasets.\n\n"
        "**Key Characteristics:**\n"
        "• Self-Attention computes Query ($Q$), Key ($K$), and Value ($V$) dot-products: $\\text{Attention}(Q,K,V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right) V$.\n"
        "• RNNs/LSTMs process tokens step-by-step ($O(T)$ sequential steps), preventing GPU parallelization and suffering from catastrophic forgetting over long context windows.\n"
        "• Multi-Head Attention enables the model to simultaneously attend to syntax, semantic references, and factual connections.\n\n"
        "**Example:** In the sentence *'The server refused the connection because it was overloaded'*, self-attention allows the token *'it'* to attend strongly to *'server'* rather than *'connection'* regardless of distance."
    ),
    (
        "What is Retrieval-Augmented Generation (RAG) and how does it prevent Hallucinations?",
        "**Direct Answer:** RAG is an AI architectural pattern that enhances Large Language Models by retrieving relevant factual passages from an external knowledge base (vector database) and injecting them into the LLM's prompt context at query time, anchoring responses in verifiable enterprise data.\n\n"
        "**Key Characteristics:**\n"
        "• Decouples external factual memory from fixed model parameter weights.\n"
        "• Chunks documents, embeds them using embedding models, and indexes them via approximate nearest neighbor search (HNSW, FAISS).\n"
        "• Prevents hallucinations, enables source citation, and permits updating knowledge instantly without expensive model retraining.\n\n"
        "**Example:** An internal SOC assistant queries a vector database for the organization's firewall policy before answering *'What ports are allowed for SSH egress?'*, quoting the exact internal security SOP."
    )
]
