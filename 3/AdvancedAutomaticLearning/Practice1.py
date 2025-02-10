import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (accuracy_score, precision_score, 
                             recall_score, f1_score, confusion_matrix, classification_report, roc_auc_score, roc_curve)
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

# Ensure SHAP is installed
try:
    import shap
except ModuleNotFoundError:
    print("SHAP module not found. Please install it using 'pip install shap'.")
    shap = None

# Set random seed for reproducibility
np.random.seed(42)

def plot_roc_curve(y_test, y_prob, model_name):
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.plot(fpr, tpr, label=f'{model_name} (AUC = {roc_auc_score(y_test, y_prob):.2f})')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()

def evaluate_models(X_train, X_test, y_train, y_test, models):
    results = []
    plt.figure(figsize=(8, 6))
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else np.zeros_like(y_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        auc = roc_auc_score(y_test, y_prob) if len(np.unique(y_test)) == 2 else np.nan
        results.append({
            'Model': name,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1': f1,
            'AUC': auc
        })
        print(f"\nModel: {name}")
        print(classification_report(y_test, y_pred))
        sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
        plt.title(f'Confusion Matrix - {name}')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.show()
        if len(np.unique(y_test)) == 2:
            plot_roc_curve(y_test, y_prob, name)
    return pd.DataFrame(results)

# Load and analyze the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]

sns.pairplot(iris_df, hue='species', palette='viridis')
plt.suptitle('Iris Dataset Pair Plot', y=1.02)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    'SVM': SVC(probability=True, random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Logistic Regression': LogisticRegression(random_state=42),
    'MLP (100,)': MLPClassifier(hidden_layer_sizes=(100,), random_state=42, max_iter=1000),
    'MLP (50,50)': MLPClassifier(hidden_layer_sizes=(50,50), random_state=42, max_iter=1000)
}

iris_results = evaluate_models(X_train_scaled, X_test_scaled, y_train, y_test, models)
print("Iris Dataset Results:")
print(iris_results)

cancer = load_breast_cancer()
cancer_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
cancer_df['diagnosis'] = cancer.target

plt.figure(figsize=(12, 10))
sns.heatmap(cancer_df.corr(), cmap='coolwarm', annot=False)
plt.title('Correlation Matrix of Breast Cancer Features')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42, stratify=cancer.target)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

cancer_results = evaluate_models(X_train_scaled, X_test_scaled, y_train, y_test, models)
print("\nBreast Cancer Dataset Results:")
print(cancer_results)

# Feature importance analysis
for name, model in models.items():
    if hasattr(model, 'feature_importances_'):
        plt.figure(figsize=(8, 6))
        sns.barplot(x=model.feature_importances_, y=cancer.feature_names)
        plt.title(f'Feature Importance - {name}')
        plt.show()

# SHAP analysis
if shap:
    explainer = shap.Explainer(models['Decision Tree'], X_train_scaled)
    shap_values = explainer(X_test_scaled)
    shap.summary_plot(shap_values, X_test_scaled)
