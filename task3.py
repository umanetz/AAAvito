from operator import itemgetter
from collections.abc import Iterable


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


vectorizer = CountVectorizer()
X = vectorizer.fit_transform([
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste',
    ])

for row in X:
    print(*row)
print(vectorizer.get_feature_names())
