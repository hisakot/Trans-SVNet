import csv
import datetime
import glob
import os

WORKFLOW = ["unknown", "Marking", "Bosmin_Infusion", "Flap_head", "Flap_tail",
            "Flap_outer", "Flap_inner", "Sentinel_Lymph_Node_Biopsy",
            "Mammary_Gland_Pealing_from_Pectoralis_Major_Muscle",
            "Mammary_Gland_Pealing_from_Surrounding_Tissue", "Cleaning",
            "Drain_Insertion", "Skin_Suture", "Other_moving", "Other_preparation"]

EVENT = ["", "Surgical_Incision", "Homeostasis_Cauterization_with_Electrocautery",
         "Homeostasis_Energizing_with_Settler", "Homeostasis_Suture_with_Forceps",
         "Getting_Surgical_Instrument"]

DOC = ["20170707main", "20200214_1_main", "20200214_2_main",
       "20220405assistant", "20220422DrHayashida",
       "20220628mainDrIshikawa", "20220715mainDrSeki"]

idx = 7

file_path = "E:\/" + DOC[idx - 1] + "/"
wf_csv = file_path + "workflow_annotation.csv"
org_imgs = "../../Dataset/surgery/org_imgs/" + str(idx) + "/*.png"
# wf_csv = "E:\/20220628mainDrIshikawa/workflow_annotation.csv"
# org_imgs = "E:\/20220628mainDrIshikawa/org_imgs/*.png"

def make_dataset():
    dataset_dicts = list()

    # load workflow annotation csv file
    fieldname = ["kind", "fi", "start", "end", "diff", "name"]
    with open(wf_csv, "r") as f:
       reader = csv.DictReader(f, fieldnames=fieldname)
       wf_dicts = [row for row in reader]

    # load images
    img_paths = glob.glob(org_imgs)
    img_paths.sort()

    for i, img_path in enumerate(img_paths):
        img_num = int(os.path.splitext(os.path.basename(img_path))[0])
        now_sec = i * (1 / 25)
        now_sec = datetime.timedelta(seconds=now_sec) # type : timedelta

        # load start and end time as timedelta
        std = datetime.datetime(2022, 1, 1)
        for wf_dict in wf_dicts:
            start = datetime.datetime.strptime("2022-01-01 " + wf_dict["start"], "%Y-%m-%d %X.%f")
            # start = datetime.datetime.strptime("2022-01-01 " + wf_dict["start"], "%Y-%m-%d %M:%S.%f")
            start -= std
            end = datetime.datetime.strptime("2022-01-01 " + wf_dict["end"], "%Y-%m-%d %X.%f")
            # end = datetime.datetime.strptime("2022-01-01 " + wf_dict["end"], "%Y-%m-%d %M:%S.%f")
            end -= std
            if now_sec >= start and now_sec <= end:
                if wf_dict["kind"] == "workflow":
                    workflow = wf_dict["name"]
                    # merge workflow
                    if "Flap" in workflow:
                        wf = "Flap"
                    elif "Drain" in workflow:
                        wf = "Cleaning"
                    elif "Cleaning" in workflow:
                        wf = "Cleaning"
                    elif "Mammary" in workflow:
                        wf = "Mammary_Gland_Pealing"
                    elif "Bosmin" in workflow:
                        wf = "Before_Incision"
                    elif "Marking" in workflow:
                        wf = "Before_Incision"
                    elif "Lymph" in workflow:
                        # wf = "Lymph_Node"
                        wf = "Mammary_Gland_Pealing"
                    elif "Skin_Incision" in workflow:
                        wf = "Flap"
                    elif "Other" in workflow:
                        wf = "Other"
                    else:
                        wf = workflow
                elif wf_dict["kind"] == "event":
                    continue
                continue

        dataset_dicts.append({"Frame" : img_num, "Phase" : wf})

    return dataset_dicts

dataset = make_dataset()
with open("../../Dataset/surgery/phase_annotations/" + str(idx) + "_phase.txt", "w") as f:
    for item in dataset:
        f.write(str(item["Frame"]) + "\t" + item["Phase"] + "\n")
