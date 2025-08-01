qa_ai_ml_stats = [
    # --- AI Basics ---
    ("What is Artificial Intelligence?",
     "Artificial Intelligence (AI) is the simulation of human cognitive functions by machines. "
     "It includes reasoning, learning, decision-making, natural language understanding, and perception. AI systems can be rule‑based or learn from data to perform tasks typically requiring human intelligence."),

    ("What are the types of AI?",
     "AI is broadly categorized into: "
     "- Narrow AI (specialized tasks like image recognition), "
     "- General AI (hypothetical systems with human-level reasoning across domains), "
     "and Super AI (speculative, surpassing human intelligence overall)." ),

    ("What is the Turing Test?",
     "Proposed by Alan Turing, this test checks if a machine’s responses are indistinguishable from a human’s in natural conversation. "
     "If an evaluator cannot reliably tell machine from human, the machine is considered to ‘pass’."),

    ("What is the difference between AI and ML?",
     "AI is a broad field concerned with making machines intelligent. "
     "Machine Learning (ML) is a subset where algorithms learn patterns from labeled or unlabeled data to make predictions or decisions without explicit programming."),

    ("What is Deep Learning?",
     "Deep Learning is a subfield of ML that uses neural networks with multiple hidden layers (deep architectures) to automatically learn high‑level features from raw data, excelling in image, speech, and text tasks."),

    # --- ML Concepts ---
    ("What is supervised learning?",
     "In supervised learning, models are trained on labeled data (inputs with known outputs). "
     "The goal is to learn the mapping so the model can predict outputs on new inputs accurately."),

    ("What is unsupervised learning?",
     "Unsupervised learning deals with unlabeled data, discovering hidden structures or clusters. "
     "Techniques include clustering (e.g. K‑means), association rules, and anomaly detection."),

    ("What is reinforcement learning?",
     "Reinforcement learning involves an agent that learns optimal behavior by interacting with an environment, "
     "receiving rewards or penalties as feedback to improve its decision-making policy over time."),

    ("What is overfitting in ML?",
     "Overfitting occurs when a model performs extremely well on training data by memorizing it, but fails to generalize to new data. "
     "It often stems from overly complex models and limited data."),

    ("What is underfitting?",
     "Underfitting happens when a model is too simplistic to capture underlying patterns in data, resulting in poor performance on both training and validation sets."),

    # --- Model Evaluation ---
    ("What is accuracy in ML?",
     "Accuracy is the proportion of true results (both true positives and true negatives) among total cases examined. "
     "Best for balanced datasets."),

    ("What is precision?",
     "Precision measures the proportion of correctly predicted positive observations out of all predicted positives. "
     "Useful when the cost of false positives is high."),

    ("What is recall?",
     "Recall (sensitivity) is the proportion of actual positives correctly identified. "
     "Critical when missing a positive outcome is costly."),

    ("What is the F1 Score?",
     "F1 Score is the harmonic mean of precision and recall. "
     "It provides a single metric to balance false positives and false negatives, especially with imbalanced classes."),

    ("What is a confusion matrix?",
     "A confusion matrix is a table showing counts of true positives, true negatives, false positives, and false negatives. "
     "It's essential for evaluating classifier performance beyond accuracy."),

    # --- Algorithms ---
    ("What is linear regression?",
     "Linear regression predicts a continuous outcomes using a linear combination of input features. "
     "It estimates relationships, e.g. predicting price based on area and age."),

    ("What is logistic regression?",
     "Logistic regression is used for binary classification. It models the probability of a certain class using the logistic (sigmoid) function."),

    ("What is a decision tree?",
     "A decision tree is a flowchart-like structure where nodes represent feature tests, branches represent outcomes, and leaves represent decisions. "
     "It's interpretable and non-parametric."),

    ("What is a random forest?",
     "Random Forest is an ensemble learning technique that builds multiple decision trees on random subsets of data/features and aggregates their predictions to improve accuracy and reduce overfitting."),

    ("What is a support vector machine (SVM)?",
     "SVM finds the optimal hyperplane that separates classes in feature space by maximizing the margin between classes. "
     "It works well in high-dimensional spaces."),

    # --- Statistics & Maths ---
    ("What is a probability distribution?",
     "A probability distribution defines how probabilities are assigned over possible outcomes. "
     "Discrete distributions use PMFs; continuous ones use PDFs."),

    ("What is Bayes' Theorem?",
     "Bayes’ Theorem provides a mathematical rule to update the probability of a hypothesis based on new evidence. "
     "P(H|E) = [P(E|H)*P(H)] / P(E)." ),

    ("What is standard deviation?",
     "Standard deviation is a measure of how spread out numerical data is from its mean. "
     "A low standard deviation indicates data is close to the mean."),

    ("What is the central limit theorem?",
     "This theorem states that the distribution of sample means approaches a normal distribution as sample size increases, regardless of the original distribution."),

    ("What is a p-value?",
     "A p‑value quantifies the probability of observing data at least as extreme as the current dataset under the null hypothesis. "
     "Lower p-values (<0.05) suggest statistical significance."),

    # --- Feature Engineering ---
    ("What is feature scaling?",
     "Feature scaling transforms input features into a similar scale (e.g., normalization or standardization) to ensure faster convergence and better model performance."),

    ("What is one‑hot encoding?",
     "One‑hot encoding converts categorical variables into binary vectors, where each category becomes a separate column."),

    ("What is dimensionality reduction?",
     "Dimensionality reduction techniques (e.g. PCA) reduce the number of input variables while retaining most information, improving model efficiency."),

    ("What is PCA (Principal Component Analysis)?",
     "PCA transforms correlated features into a smaller number of uncorrelated principal components, ordered by variance explained."),

    ("What is multicollinearity?",
     "Multicollinearity happens when independent variables are highly correlated, making coefficient estimates unstable in regression models."),

    # --- Neural Networks ---
    ("What is a neuron in a neural network?",
     "A neuron takes weighted inputs, adds a bias, passes the sum through an activation function, and outputs a signal. "
     "It’s the basic unit of a neural network."),

    ("What is an activation function?",
     "Activation functions (e.g. ReLU, Sigmoid, Tanh) introduce non-linearity, enabling the network to learn complex patterns."),

    ("What is backpropagation?",
     "Backpropagation is the algorithm that calculates gradients of the loss function and updates neural network weights via gradient descent."),

    ("What is an epoch?",
     "An epoch is one full pass through the entire training dataset during model training."),

    ("What is a learning rate?",
     "The learning rate is a hyperparameter that controls the step size when updating weights during training. "
     "A small rate may slow training; a large rate may overshoot minima."),

    # --- Advanced Topics ---
    ("What is gradient descent?",
     "Gradient descent is an optimization algorithm that minimizes a loss function by iteratively adjusting parameters in the opposite direction of the gradient."),

    ("What is stochastic gradient descent (SGD)?",
     "SGD updates model parameters based on one training example at a time, enabling faster updates but with more variance in convergence."),

    ("What is regularization?",
     "Regularization (L1 or L2) adds a penalty to the loss function to discourage overly large weights, helping to prevent overfitting."),

    ("What is dropout in deep learning?",
     "Dropout randomly disables neurons during training, reducing overfitting and improving generalization."),

    ("What is a convolutional neural network (CNN)?",
     "A CNN uses convolutional layers and pooling to automatically learn spatial hierarchies in image and text data."),

    # --- Practical ML ---
    ("What is cross-validation?",
     "Cross-validation splits data into multiple train/test folds to assess how models generalize to unseen data."),

    ("What is hyperparameter tuning?",
     "Hyperparameter tuning involves selecting the best model parameters (like tree depth or learning rate) via grid search, random search, or Bayesian optimization."),

    ("What is ensemble learning?",
     "Ensemble learning combines multiple models, such as bagging or boosting, to improve performance and robustness."),

    ("What is XGBoost?",
     "XGBoost is a high-performance, scalable implementation of gradient boosting used widely in structured data competitions."),

    ("What is model drift?",
     "Model drift occurs when the statistical properties of input data change over time, causing performance degradation."),

    # --- Ethics and AI ---
    ("What is model interpretability?",
     "Model interpretability refers to how easily humans can understand a model’s decisions, crucial for trust and accountability."),

    ("What are biases in AI?",
     "Biases are systematic errors in AI systems from flawed data or algorithms that can reinforce unfair or discriminatory outcomes."),

    ("What is explainable AI (XAI)?",
     "XAI involves designing AI models that are understandable and transparent to humans, enabling validation and trust."),

    ("What is fairness in machine learning?",
     "Fairness ensures models make equitable predictions across different groups, minimizing discrimination."),

    ("What is the difference between AI ethics and AI safety?",
     "AI ethics focuses on responsible design/use of AI, while AI safety aims to prevent unintended harm from AI systems in operation.")
]
