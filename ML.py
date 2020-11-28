from string import punctuation
from pymystem3 import Mystem
from nltk.corpus import stopwords
import nltk
from scipy.sparse import *
from scipy import *
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

nltk.download("stopwords")

# Create lemmatizer and stopwords list
mystem = Mystem()
russian_stopwords = stopwords.words("russian")

text_1 = 'Предложение экономии на затратах уборки помещений'
text_2 = 'Экономия на уборке помещений'
text_3 = 'Я люблю котов'
text_4 = 'Вы любите розы?'

# Обучаем векторайзер
vectorizer = CountVectorizer()


# Функция обработки
def normalization_of_supply(text_list):
    # Принимает на вход лист, и отдает лист
    normal_text_list = []
    for text in text_list:
        tokens = mystem.lemmatize(text.lower())
        tokens = tuple(
            token
            for token in tokens
            if token not in russian_stopwords and token != " " and token.strip() not in punctuation
        )

        text = " ".join(tokens)
        normal_text_list.append(text)

    return normal_text_list


# Для преобрзования вычислений в единый результат точности
def cosine_sim_vectors(vector_1, vector_2):
    vector_1 = vector_1.reshape(1, -1)
    vector_2 = vector_2.reshape(1, -1)

    return cosine_similarity(vector_1, vector_2)[0][0]


def model(text_list):
    # На вход принимает два текста в виде массива
    # Если они похожи, возвращает True
    # Если нет, False

    # Создание векторайзера
    normal_text = normalization_of_supply(text_list)
    vector = vectorizer.fit_transform(normal_text)  # Трансформ
    vector = csr_matrix(vector, dtype=int8).todense()  # Оптимизация

    similar = cosine_similarity(vector)
    if cosine_sim_vectors(vector[0], vector[1]) > 0.45:
        return True
    else:
        return False


print(model([text_3, text_4]))
