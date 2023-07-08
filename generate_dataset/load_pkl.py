import pickle

# with open("../trans-SVNet/train_val_paths_labels1.pkl", "rb") as f:
with open("./train_val_paths_labels_7classes.pkl", "rb") as f:
    data = pickle.load(f)

print(data[0][0])
print(data[1][0])
print(data[2][0])
print(data[3][0])
print(data[4][0])
print(data[5][0])
print(data[6][0])
print(data[7][0])
print(data[8][0])

tr_data = data[2]
tr_num = [0] * 7
for i, tr in enumerate(tr_data):
    tr_num[tr[0]] += 1
print(tr_num)
std = tr_num[2]
for num in tr_num:
    print(std / num)

vl_data = data[3]
vl_num = [0] * 7
for i, vl in enumerate(vl_data):
    vl_num[vl[0]] += 1
print(vl_num)

ts_data = data[7]
ts_num = [0] * 7
for i, ts in enumerate(ts_data):
    ts_num[ts[0]] += 1
print(ts_num)
exit()

video1_paths = data[0][:data[4][0]]
video1_labels = data[2][:data[4][0]]

video2_paths = data[0][data[4][0]:data[4][0] + data[4][1]]
video2_labels = data[2][data[4][0]:data[4][0] + data[4][1]]

video3_paths = data[0][data[4][0] + data[4][1]:data[4][0] + data[4][1] + data[4][2]]
video3_labels = data[2][data[4][0] + data[4][1]:data[4][0] + data[4][1] + data[4][2]]

new_data = list()
new_data.append(video1_paths)
new_data.append(video2_paths)
new_data.append(video1_labels)
new_data.append(video2_labels)
new_data.append([data[4][0]])
new_data.append([data[4][1]])
new_data.append(video3_paths)
new_data.append(video3_labels)
new_data.append([data[4][2]])

with open("./Trans-SVNet/toriaezu_data.pkl", "wb") as g:
    pickle.dump(new_data, g)

with open("./Trans-SVNet/toriaezu_data.pkl", "rb") as f:
    data = pickle.load(f)
print(data[0][0])
print(data[1][0])
print(data[2][0])
print(data[3][0])
print(data[4])
print(data[5])
print(data[6][0])
print(data[7][0])
print(data[8])
