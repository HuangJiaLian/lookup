# 查词帮
一个更方便的查词工具

## 依赖
```
## 1. Translate Shell 
https://github.com/soimort/translate-shell
## 2. pyperclip
https://pyperclip.readthedocs.io/en/latest/introduction.html
## 3. notify-send
sudo apt install libnotify-bin
## 4. festival
sudo apt install festival festvox-kallpc16k
## 5. xsel
sudo apt install xsel
```



## 使用

``` bash
python lookup.py
```

1. 将单词复制到剪贴板，程序便会自动查询，朗读单词。
2. 查词后默认会将翻译结果存在Primary缓冲区中，使用鼠标中键即可粘贴到对应位置。

