import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier

# data_file
train_path = os.path.join("data", "train")
test_path = os.path.join("data", "test")
result_path = os.path.join("data", "result")


def test_data():
    test_x = []
    try:
        file = open(test_path, 'r')
    except OSError:
        print("Could not open/read file:", test_path)
    with file:
        for line in file.readlines():
            line = line.strip()
            tmp = line.split('\t')
            while len(tmp) != 14:
                tmp.append("0:1")
            for i, fn in enumerate(tmp):
                tmp[i] = int(tmp[i].split(':')[0])
            test_x.append(tmp)
    return np.array(test_x)


def main():
    data_x = []
    data_y = []

    try:
        file = open(train_path, 'r')
    except OSError:
        print("Could not open/read file:", train_path)

    with file:
        for line in file.readlines():
            tmp = line.strip()
            tmp = tmp.split(' ')
            while len(tmp) != 15:
                tmp.append("0:1")
            # class
            if tmp.pop(0) == "+1":
                data_y.append([1])
            else:
                data_y.append([-1])
            # feature_no
            for i, fn in enumerate(tmp):
                tmp[i] = int(tmp[i].split(':')[0])
            data_x.append(tmp)

    x = np.array(data_x)
    y = np.array(data_y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y)

    model = SGDClassifier(loss="hinge")
    model.fit(x_train, y_train.ravel())

    y_pred = model.predict(x_test)
    print(model.score(x_test, y_test.ravel()))

    x_res = test_data()
    y_res = model.predict(x_res)

    try:
        result_file = open(result_path, 'w')
    except OSError:
        print("Could not open/read file:", result_path)
    with result_file:
        for y in y_res:
            if y == 1:
                result_file.write("+1")
            else:
                result_file.write("-1")
            result_file.write('\n')


if __name__ == "__main__":
    main()
