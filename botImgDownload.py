import pickle
from re import I
import requests
from time import sleep

f=open('botimg.pkl','rb')
botImgs=pickle.load(f)
f.close()


# botImgs=list(set(botImgs))
# i=0
# for imgs in botImgs:
#     if(imgs.find('50x50')!=-1 or imgs.find('.gif')!=-1):
#         botImgs.remove(imgs)
#         i=i+1
#         print("去重复",i,'个')
print('totol：',len(botImgs))
i=0
for src in botImgs:
    i+=1
    img_resp = requests.get(src)
    sleep(1)
    img_name = src.split("/")[-1]  # 拿到url中的最后一个/以后的内容
    with open("./imgbon/"+img_name, mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件
    print('num ',i,' finish!')



f=open('botimg.pkl','wb')
pickle.dump(botImgs,f,True)
f.close()

print('over!')