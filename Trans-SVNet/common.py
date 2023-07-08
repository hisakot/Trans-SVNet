import copy
import numpy as np
import torch
import time

# all
PKL_DATA = "./train_val_paths_labels.pkl"
# PKL_DATA = "./train_val_paths_labels1.pkl"

# generate_LFB.py
EMBED = "./best_model/emd_lr10e-5/resnetfc_ce_epoch_11_6ch_tp.pth"

# generate_LFB.py tecno.py trans_SV.py
LFB_TRAIN = "./LFB/6ch_1tensor_6class/g_LFB50_train.pkl"
LFB_VAL = "./LFB/6ch_1tensor_6class/g_LFB50_val.pkl"
LFB_TEST = "./LFB/6ch_1tensor_6class/g_LFB50_test.pkl"

# trans_SV.py
TECNO_MODEL = "TeCNO50_epoch_8_6ch_1tensor_6class_re"
SAVE_RESULT_CSV = "./result_6ch_re_tp.csv"

# tecno.py trans_SV.py
# weights_train = np.asarray([7.8549160671462825,
# 1.2566660272395933,
# 1.0,
# 1.8242829295460874,
# 4.011635027556644,
# 1.5556874851579197,
# 1.0069166922840456])
weights_train = np.asarray([12.55195530726257,
    1.9412476239847936,
    1.0,
    6.346892655367232,
    3.2309462180040263,
    2.089657738095238])

tp = np.asarray([
    [1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1]])

def transition_probability(preds):
    osa = 0
    phase = list()
    softmax = torch.nn.Softmax(dim=0)
    for i, pred in enumerate(preds):
        sort, indices = torch.sort(pred)
        new_pred = copy.copy(pred)
        new_pred = softmax(new_pred)

        high_p = 5
        while high_p >= 0:
            if tp[osa][indices[high_p].item()] == 1:
                if indices[high_p].item() == 5:
                    phase.append(5)
                else:
                    if new_pred.data[indices[high_p].item()] > 0.50:
                        phase.append(indices[high_p].item())
                        osa = indices[high_p].item()
                        before_pred = new_pred
                    else:
                        try:
                            new_pred = before_pred
                        except UnboundLocalError:
                            before_pred = new_pred
                break
            else:
                new_pred.data[indices[high_p]] = 0
                new_pred = softmax(new_pred)
                high_p -= 1
                # try:
                #     new_pred = before_pred
                # except UnboundLocalError:
                #     before_pred = new_pred
                # break
        try:
            new_pred = new_pred.unsqueeze(dim=0)
            after_preds = torch.cat((after_preds, new_pred), dim=0)
        except NameError:
            after_preds = new_pred

    return after_preds
