import matplotlib.pyplot as plt
import numpy as np
import torch

# cp = torch.load("./best_model/emd_lr5e-4/loss.pth")
cp = torch.load("./best_model/train_emd_loss.pth")
# cp = torch.load("./best_model/tecno_loss.pth")
# cp = torch.load("./best_model/trans_SV_loss.pth")
train_loss_list = cp["train_loss"]
valid_loss_list = cp["valid_loss"]

y_axis = list(range(0, len(train_loss_list)))

y_axis = np.array(y_axis)
train = np.array(train_loss_list)
valid = np.array(valid_loss_list)

plt.plot(y_axis, train / 5, color="red")
plt.plot(y_axis, valid, color="blue")
# plt.savefig("./best_model/train_emd_6ch_1tensor.png")
# plt.savefig("./best_model/tecno_6ch_1tensor.png")
# plt.savefig("./best_model/transSV_6ch_1tensor.png")
plt.show()
