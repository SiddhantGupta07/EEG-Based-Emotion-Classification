import pickle
import os
from multiprocessing import Pool


# Channels as defined in the raw data
channel = ['Fp1', 'AF3', 'F3', 'F7', 'FC5', 'FC1', 'C3', 'T7', 'CP5', 'CP1', 'P3', 'P7', 'PO3', 'O1', 'Oz',
           'Pz', 'Fp2', 'AF4', 'Fz', 'F4', 'F8', 'FC6', 'FC2', 'Cz', 'C4', 'T8', 'CP6', 'CP2', 'P4', 'P8', 'PO4', 'O2']

# defining number of each category
nLabel, nTrial, nUser, nChannel, nTime = 4, 40, 32, 32, 8064

# generating label files from input raw data
fout_labels0 = open("labels_0.dat", 'w')
fout_labels1 = open("labels_1.dat", 'w')
fout_labels2 = open("labels_2.dat", 'w')
fout_labels3 = open("labels_3.dat", 'w')

for i in range(nUser):  # nUser #4, 40, 32, 40, 8064 4 labels, 40 sample for each user, 32 such user, 40 electrode, 8064*40 features
    if i < 10:
        fileName = '%0*d' % (2, i+1)
    else:
        fileName = i+1
    fname = "/data_preprocessed_python/data_preprocessed_python/s" + \
        str(fileName)+".dat"
    x = pickle.load(open(fname, 'rb'))
    # print fname
    for tr in range(nTrial):
        fout_data = open("features_raw.csv", 'w')
        for ch in channel:
            fout_data.write(ch+",")
        fout_data.write("\n")
        for dat in range(nTime):
            for ch in range(nChannel):
                if ch < 32:
                    if ch == 31:
                        fout_data.write(str(x['data'][tr][ch][dat]))
                    else:
                        fout_data.write(str(x['data'][tr][ch][dat])+",")
            fout_data.write("\n")
        fout_labels0.write(str(x['labels'][tr][0]) + "\n")
        fout_labels1.write(str(x['labels'][tr][1]) + "\n")
        fout_labels2.write(str(x['labels'][tr][2]) + "\n")
        fout_labels3.write(str(x['labels'][tr][3]) + "\n")
        fout_data.close()
        os.system('python creating_vector.py')
        # print "user " + str(i) + " trail" + str(tr)
fout_labels0.close()
fout_labels1.close()
fout_labels2.close()
fout_labels3.close()
# print "\n"+"Print Successful"
