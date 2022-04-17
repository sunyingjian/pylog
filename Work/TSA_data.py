import tensorflow as tf
import numpy as np
import pandas as pd


def data_check(training_data,train_data,blind,blind_data):
    seq_length = 100
    data_ = []
    for i in range(len(train_data)-seq_length):
        if training_data[i,-1]!=training_data[i+seq_length,-1]:
            continue
        data_.append(train_data.iloc[i:i+seq_length])
    data_ = np.array([df.values for df in data_])
    X = data_[:,:,:9]
    Y = data_[:,:,-1]-1
    Y=np.array(Y)
    Y=tf.keras.utils.to_categorical(Y)
    data_test = []
    for i in range(len(blind_data)-seq_length):
        if blind[i,-1]!=blind[i+seq_length,-1]:
            continue
        data_test.append(blind_data.iloc[i:i+seq_length])
    data_test = np.array([df.values for df in data_test])
    test_y_1 = data_test[:,:,-1]-1
    test_y_1 =np.array(test_y_1)
    test_y_1=tf.keras.utils.to_categorical(test_y_1)
    test_x = data_test[:,:,:9]
    return X,Y,test_x,test_y_1


def check1(pred):
  y_pred_1 = pred[:,50,:]
  y_pred_1_first = pred[0,:50,:]
  y_pred_1_last = pred[-1,50:,:]
  y_pred_1 = np.array([c.argmax() for c in y_pred_1])
  y_pred_1_first = np.array([c.argmax() for c in y_pred_1_first])
  y_pred_1_last = np.array([c.argmax() for c in y_pred_1_last])
  y_ture = np.append(y_pred_1_first,y_pred_1)
  y_true = np.append(y_ture,y_pred_1_last)
  return y_true

def data_pred(pred_1,pred_2):
    y_true_pred_1 = check1(pred_1)
    y_true_pred_2 = check1(pred_2)
    y_pred_true = np.append(y_true_pred_1,y_true_pred_2)
    y_pred_1 = pd.DataFrame(y_pred_true)+1
    return y_pred_1



def data_pred1(data):
    return data