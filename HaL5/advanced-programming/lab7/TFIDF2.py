import os
from math import log

class Doc:
    '''
    Lớp mô tả một đối tượng văn bản, lớp này có 1 thuộc tính là wordCount kiểu từ điển
    
    với key là các từ trong văn bản và value là số lần các từ đó xuất hiện trong văn bản
    
    CHÚ Ý: Để cho đơn giản, mỗi từ trong văn bản được phân cách bởi dấu cách, các từ phân biệt hoa thường...
    
    Nói chung 2 từ A và B mà A == B nhận giá trị false là khác nhau. 
    Ví dụ từ "anh" và "Anh" là khác nhau
          từ "anh." và "anh" là khác nhau
    
    '''
    def __init__(self,filename):
        self.wordCount = dict()
        self.loadWordCountFromFile(filename)
        
    def loadWordCountFromFile(self,filename):
        '''
        Hàm thực hiện đọc vào file filename và đếm tần suất xuất hiện các từ rồi đưa vào wordCount
        
        Hàm này được gọi đến trong hàm dựng, do vậy bắt buộc phải viết đúng hàm này, nếu không các hàm khác sẽ không được
        chấm điểm
        
        '''
        f = open(filename,'r')
        for line in f:
            line = line.strip().split()
            for word in line:
                self.wordCount[word] = self.wordCound.get(word, 0) + 1
        f.close()
    
class TFIDF:
    '''
        Lớp mô tả việc tính chỉ số TFIDF cho các từ trong văn bản dựa trên kho văn bản
        Lớp này có 2 thuộc tính là corpusPath và data, trong đó:
        - corpusPath là đường dẫn tới thư mục chứa các tệp văn bản
        - data là một từ điển với key là tên các file văn bản, và value là các đối tượng Doc tương ứng
        với key
        
    '''
    def __init__(self, corpusPath):
        self.corpusPath = corpusPath       
        self.data = dict()       
        self.loadCorpus(corpusPath)
            
    def loadCorpus(self,corpusPath):
        '''
        
        Hàm thực hiện đọc các file văn bản trong thư mục corpusPath, và xây dựng các đối tượng
        
        Doc tương ứng và đưa vào data
        
         Hàm này được gọi đến trong hàm dựng, do vậy bắt buộc phải viết đúng hàm này, nếu không các hàm khác sẽ không được
        chấm điểm
        
        '''
        files = os.listdir(corpusPath)
        for file in files:
            self.data[file] = Doc(file)
    
    def tf(self,w,d):
        '''
        Tính và trả về chỉ số tf của từ w trong Doc d (d là 1 đối tượng Doc)
        Công thức tính tf(w,d) như sau:
        - Gọi tfw là số lần w xuất hiện trong d (ví dụ tfw = 3)
        - Gọi tfm là số lần 1 từ bất kỳ xuất hiện nhiều nhất trong d (ví dụ tfm = 6)
        - khi đó tf(w,d) = tfw/tfm (ví dụ 3/6 = 0.5)
        
        '''
        tfw = d.wordCount.get(w,0)
        tfm = max(d.wordCount.values())
        return tfw/tfm
    
    def idf(self, w):
        '''
        Tính và trả chỉ số idf của từ w trong kho văn bản data
        Chỉ số idf của w là idf(w) được tính như sau:
        - Gọi N là số văn bản có trong kho data (ví dụ N = 10)
        - Gọi m là số văn bản trong kho data có chứa từ w (ví dụ m = 3)
        - khi đó: idf(w) = log(N/(1+m)) (ví dụ idf(w) = log(10/(1+3)) = 0.9162907318741551)
        
        CHÚ Ý DÙNG math.log để tính log
        '''
        N = len(self.data)
        m = 0
        for d in self.data.values():
            if w in d.wordCount:
                m += 1
        return log(N/(1+m))
    
    def tfidf(self, w, d):
        '''
        Hàm tính và trả lại chỉ số tfidf của từ w trong văn bản d (d là một đối tượng Doc) trên kho dữ liệu data
        Chỉ số tfidf(w,d) được tính như sau:
        tfidf(w, d) = tf(w,d) * idf(w)
        '''
        return self.tf(w, d) * self.idf(w)
    
    
    def getKTopicWordFromCopus(self, k):
        '''
        Hàm thực hiện tính và trả lại danh sách k từ khác nhau có chỉ số tfidf cao nhất trong kho văn bản data
        
        Danh sách được sắp xếp tăng dần theo thứ tự từ điển mặc định (không cần sắp xếp theo tiếng Việt)
        
        CHÚ Ý: 2 từ giống nhau trong 2 văn bản khác nhau có thể cùng có chỉ số tfidf trong top k 
        từ có chỉ số tfidf cao nhất, tuy nhiên kết quả chỉ lấy 1 từ 
        (có nghĩa là trong danh sách kết quả, k từ đôi một khác nhau)
        '''
        lst = []
        res = []
        for d in self.data.values():
            for w in d.wordCount:
                tfidf = self.tfidf(w, d)
                lst.append((w, tfidf))
        lst.sort(key=lambda x: x[1], reverse=True)
        for el in lst:
            if len(res) < k:
                if el[0] in res:
                    continue
                else:
                    res.append(el[0])
            else:
                break
        return res

if __name__ == '__main__':
    path = "D:\\Datas\\khac\\quan\\HaL\\HaL5\\advanced-programming\\lab7\\data9"
    print("yahhooo, hoooyaaa")