import pickle
import requests
from time import sleep

f=open('topimg.pkl','rb')
topImgs=pickle.load(f)
f.close()


# topImgs=list(set(topImgs))
# i=0
# for imgs in topImgs:
#     if(imgs.find('50x50')!=-1 or imgs.find('.gif')!=-1):
#         topImgs.remove(imgs)
#         i=i+1
#         print("去重复",i,'个')
for src in topImgs:
        img_resp = requests.get(src)
        sleep(1)
        img_name = src.split("/")[-1]  # 拿到url中的最后一个/以后的内容
        with open("./imgtop/"+img_name, mode="wb") as f:
            f.write(img_resp.content)  # 图片内容写入文件



f=open('topimg.pkl','wb')
pickle.dump(topImgs,f,True)
f.close()

print('over!')
    