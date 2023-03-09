import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b=(np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp**2) - np.mean(zp) ** 2)
a=np.mean(ks)-b*np.mean(zp)
ks=ks.reshape((-1,1))
zp=zp.reshape((-1,1))
zp=np.hstack([np.ones((len(zp),1)),zp])
result_1=np.dot(np.linalg.inv(np.dot(zp.T,zp)),np.dot(zp.T,ks))
print(result_1)

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
ks=ks.reshape((-1,1))
zp=zp.reshape((-1,1))
result_2=np.dot(np.linalg.inv(np.dot(zp.T,zp)),np.dot(zp.T,ks))
print(result_2)