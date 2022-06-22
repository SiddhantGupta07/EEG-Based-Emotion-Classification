from sklearn import svm  # Support Vector Machine
import numpy as np  # Numpy


class EEG_Emotion_Classifier:
    def __init__(self):
        self.train_y_valence = []
        self.train_y_arousal = []
        self.train_x = np.genfromtxt('train.csv', delimiter=',')

    def output_file(self, path):
        return open(path+".dat", "r")  # opens file in read mode

    def predict_classification(self, count, train_y):
        return (float(count)/len(train_y))*100

    def emotion_classify(self):
        # Contains Supervised Valence Data
        valence_file = self.output_file("labels_1")

        for row in valence_file:
            self.train_y_valence.append(row)

        # Datayype Conversion (int to float)
        self.train_y_valence = np.array(self.train_y_valence).astype(np.float)

        self.train_y_valence = self.train_y_valence.astype(
            np.int)     # Datayype Conversion (float ot int)

        self.train_x = np.array(self.train_x)

        clf1 = svm.SVC()  # Support Vector Classifier

        # Training Support Vector Classifier with Valence Input Data
        clf1.fit(self.train_x, self.train_y_valence)

        # Contains Supervised Arousal Data
        arousal_file = self.output_file("labels_2")

        for row in arousal_file:
            self.train_y_arousal.append(row)

        # Datayype Conversion (int to float)
        self.train_y_arousal = np.array(self.train_y_arousal).astype(np.float)

        self.train_y_arousal = self.train_y_arousal.astype(
            np.int)    # Datayype Conversion (float ot int)

        clf2 = svm.SVC()    # Support Vector Classifier

        # Training Support Vector Classifier with Arousal Input Data
        clf2.fit(self.train_x, self.train_y_arousal)

        predict_valence = clf1.predict(self.train_x)
        print("valence", predict_valence)

        predict_arousal = clf2.predict(self.train_x)
        print("arousal", predict_arousal)

        valence_count = arousal_count = 0
        for i in range(len(self.train_y_valence)):
            if self.train_y_valence[i] == predict_valence[i]:
                valence_count = valence_count+1
            if self.train_y_arousal[i] == predict_arousal[i]:
                arousal_count = arousal_count+1

        print("predicted valence",
              self.predict_classification(valence_count, self.train_y_valence))
        print("predicted arousal",
              self.predict_classification(arousal_count, self.train_y_arousal))


if __name__ == "__main__":
    eegclassifier = EEG_Emotion_Classifier()
    eegclassifier.emotion_classify()
