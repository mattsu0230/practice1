qs= [
        {"q":"apple","a":"りんご"},
        {"q":"banana","a":"バナナ"},
        {"q":"orange","a":"オレンジ"}
    ]
score=0

print('''<h1>hello</h1>
<p>世界の皆さん,
<b>こんにちは</b></p>''')

for index in range (len(qs)):
    
    q=qs[index]['q']
    
    print("Q{0} {1}".format((index+1),q))

    userinput=input("回答を入力:")
 
    print("回答:{0}".format(userinput))
     
    if userinput.upper()==qs[index]['a']:
        print("正解")
        score+=1
    else:
        print("不正解")
        
print("{0}問中 {1}問正解".format(len(qs),score))


