from gensim.models import word2vec,doc2vec
from LtpUtil import LtpUtil

word2vec1='./model/wiki.zh.model'
word2vec2='./model/wiki.zh.model.syn0.npy'
word2vec3='./model/wiki.zh.model.syn1neg.npy'
word2vec4='./model/wiki.zh.vector'

model = word2vec.Word2Vec.load(word2vec1)
candidates = ['我想听周杰伦的歌','我要听周杰伦的歌'
              ,'我喜欢张杰的歌'
              ,'有没有适合睡觉听的歌'
              ,'播放一些舒缓的歌曲'
              ,'我想听纯音乐']
tests = ['我喜欢周杰伦的歌'
         ,'我想听舒缓类型的音乐'
         ]
text = '我喜欢周杰伦的歌'
print(text)
ltpUtil = LtpUtil()
text_list = list(ltpUtil.Segmentor(text))
candidates_list = []
scores = []

for candidate in candidates:
    candidates_list.append(list(ltpUtil.Segmentor(candidate)))
    scores.append(model.n_similarity(text_list,candidate))

for num in range(len(candidates)):
    print(candidates[num],'\t',scores[num])




