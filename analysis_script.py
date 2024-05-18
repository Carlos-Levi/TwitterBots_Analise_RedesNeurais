# analysis_script.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
from keras.models import Sequential
from keras.layers import Dense
from sklearn.cluster import KMeans

# Função para carregar os dados
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Função para preprocessar os dados
def preprocess_data(df):
    # Identificar colunas categóricas
    categorical_columns = df.select_dtypes(include=['object']).columns

    # Converter colunas categóricas em variáveis dummy
    df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

    # Normalizar as features
    X = df.drop('is_a_bot', axis=1)
    y = df['is_a_bot']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

# Função para treinar a rede neural
def train_supervised_model(X_train, y_train):
    model = Sequential()
    model.add(Dense(12, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=0)

    return model

# Função para treinar o modelo KMeans
def train_unsupervised_model(X, n_clusters=2):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(X)
    return kmeans

# Função para avaliar o modelo
def evaluate_model(model, X_test, y_test):
    y_pred = (model.predict(X_test) > 0.5).astype("int32")
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    return accuracy, precision, recall, cm

# Exemplo de execução do script
if __name__ == "__main__":
    df = load_data('twitter_bots.xlsx')
    X, y = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    supervised_model = train_supervised_model(X_train, y_train)
    accuracy, precision, recall, cm = evaluate_model(supervised_model, X_test, y_test)

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"Confusion Matrix:\n{cm}")
