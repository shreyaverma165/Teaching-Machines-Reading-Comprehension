from matplotlib import pyplot as plt

def threshold_acc(predictions, y_valid):
    correct_count = 0
    threshold = 0
    for sample_ind, sample_y in enumerate(y_valid):
        for ind,op in enumerate(sample_y):
            if op==1 and predictions[sample_ind][ind]>threshold:
                correct_count+=1
    return 100*correct_count/float(len(y_valid))



def get_predicted_labels(predictions):
    predicted_labels = []
    for pred in predictions:
        ans_labels = [-1]*4
        ans_label_ind = pred.index(max(pred))
        ans_labels[ans_label_ind]=1
        predicted_labels.append(tuple(ans_labels))
    return predicted_labels


def highest_val_correct_acc(predictions, y_valid):
    correct_count = 0
    y_pred = get_predicted_labels(predictions)
    for y_t, y_p in zip(y_valid, y_pred):
        if y_t==y_p:
            correct_count+=1
    return 100*correct_count/float(len(y_valid))


