## RSA 算法的实现

脚本使用方法：

### 生成密钥

```sh
python test.py make-keys rsakey
```
公钥保存在 rsakey.pub 中， 私钥保存在 rsakey.priv 中


### 对文件内容加密 

假如有文件 明文.txt：

```sh
python test.py encrypt 明文.txt from rsakey to 密文.txt
```

将生成 密文.txt

### 对文件内容解密 

假如有文件 密文.txt：

```sh
python test.py decrypt 密文.txt as rsakey to 解密后.txt
```

将生成 解密后.txt


推荐关注公众号 「Python七号」，学习 Python 实战技能。
