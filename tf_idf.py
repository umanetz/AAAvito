from operator import itemgetter
from math import log


class CountVectorizer:
    def __init__(self) -> None:
        self.vocabulary = None


    def count_vocab_(self, raw_documents: list) -> list:
        """Create counter of tokens for each document"""
        self.vocabulary = dict()
        self.inverse_vocabulary = dict()
        vocabulary_count = 0
        documents_counter = []

        for doc in raw_documents:
                feature_counter = {}

                for feature in self.check_split_doc(doc):
                        if feature not in self.vocabulary:
                            self.vocabulary[feature] = vocabulary_count
                            self.inverse_vocabulary[vocabulary_count] = feature
                            vocabulary_count += 1
                        
                        feature_idx = self.vocabulary[feature]
                        if feature_idx not in feature_counter:
                            feature_counter[feature_idx] = 1
                        else:
                            feature_counter[feature_idx] += 1

                documents_counter.append(feature_counter)

        return documents_counter
                    

    def build_matrix(self, documents_counter: dict) -> list:
        """Create matrix of token count"""
        whidth = len(self.vocabulary)
        matrix = []

        for counter in documents_counter:
            tokens_position = [0] * whidth

            for feature_idx, num in counter.items():
                tokens_position[feature_idx] = num
            matrix.append(tokens_position)

        return matrix
        

    def check_split_doc(self, doc: str) -> list:
        """Check that doc is str"""
        if not isinstance(doc, str):
            raise ValueError(f"{doc} not str")

        return doc.lower().split()


    def check_vocabulary_(self) -> None:
        """Check if vocabulary is empty or not fitted"""
        if self.vocabulary is None:
            raise ValueError("Vocabulary  not fitted")

        elif len(self.vocabulary) == 0:
            raise ValueError("Vocabulary is empty")


    def check_corpus(self, corpus: list) -> None:
        """Check that corpus is list"""
        if not isinstance(corpus, list):
            raise TypeError(f"Corpus is not list")


    def fit_transform(self, raw_documents: list) -> list:
            """Fit and transform raw_documents
            raw_documents : list
            """
            self.check_corpus(raw_documents)
            documents_counter = self.count_vocab_(raw_documents)
            X = self.build_matrix(documents_counter)
            return X


    def get_feature_names(self) -> list:
        """Extract features"""
        self.check_vocabulary_()
        return [t for t, _ in sorted(self.vocabulary.items(), key = itemgetter(1))]


class TfidfTransformer():
    def __init__(self) -> None:
        pass
    def tf_transform(self, count_matrix):
        tf_matrix = []
        for v in  (count_matrix):
            n = sum(v)
            tf_matrix.append([freq / n for freq in v])
        return tf_matrix


    def idf_transform(self, count_matrix):
        n_doc = len(count_matrix)
        max_words = len(count_matrix[0])
        idf_matrix = []
        for word_i in range(max_words):
            n_doc_with_word = 0

            for v in count_matrix:
                if v[word_i] != 0:
                    n_doc_with_word += 1
            idf_matrix.append(log((n_doc + 1) / (n_doc_with_word + 1)) + 1)
        return idf_matrix


    def fit_transform(self, count_matrix):
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        n_words = len(tf[0])
        tf_idf_matrix = []

        for tf_vector in tf:
            tf_idf_v = []
            for i in range(n_words):
                tf_idf_v.append(tf_vector[i] * idf[i])

            tf_idf_matrix.append(tf_idf_v)
        return tf_idf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, raw_documents: list) -> list:
        count_matrix = super().fit_transform(raw_documents)
        return self.transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    tfidf_transformer = TfidfVectorizer()
    X = tfidf_transformer.fit_transform([
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',
        ])
    print(X)
