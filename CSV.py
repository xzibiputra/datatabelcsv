import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://academy.dqlab.id/dataset/penduduk_gender_head.csv")
#dataset diambil dari website dqlab.id
table.head()
x_label = table ['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation = 90)
plt.xlabel('Kelurahan di jakarta pusat')
plt.ylabel('Jumlah laki laki')
plt.title('Pesebaran Jumlah Penduduk Laki Laki di Jakarta Pusat')
plt.show()
