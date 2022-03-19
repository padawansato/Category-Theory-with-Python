# 概要
- 「Pythonで始める柔らかな圏論: 読む、作る、分かる!!(永遠の相 World Structure 著)」の読書メモ
  - 挫折させない
  - ざっくりとした説明
  - 圏論を初めて学習する方のための参考書
  - 数学記号の記載はなるべく避ける
  - Pythonを利用して解説する

上記のような目標を掲げていて、かつ Kindle で 100円 だったため購入した。


---
# 対象と射 まとめ

1. 集合の要素を、圏論では対象という
2. 対象同士に関係性がある場合、対象から対象に向かって矢印を書く
3. 矢印を射という
4. 圏論は、対象と射の構造を研究する学問

---

# 合成射

`合成射.py` では 「ある対象が別の対象の一部」(対象は文字列)という関係における合成射を Python で確認した。

---

# 圏の公理

1. 対象を持つこと
2. 射を持つこと
3. 合成射を持つこと
4. 結合律を持つこと
5. 恒等射を持つこと

---

# 「圏」かどうかの検証

`1, 2, 5, 10`は圏かどうか。

圏の公理に従って、チェックする。

圏の公理

1. 対象を持つこと → OK
2. 射を持つこと
   - 例えば不等式 `1 <= 2 <= 5 <= 10` が成り立つ。
   - 不等式を射とする。
   - → OK
3. 合成射を持つこと
   - `1 →f→ 2 →g→ 5 →h→ 10`
   - 射f と 射g を合成したとして、不等式は成り立つか？成り立つ。
   - → OK
4. 結合律を持つこと
5. 恒等射を持つこと

---

# 合成射の記述方法 合成演算子

### dot(`·`) の入力方法
- Mac は unicode を記述できるため、dot(`·`)を使えるが、これは半角中黒点(`･`)と区別できない。unicode 上は、それぞれ`\u00b7`, `\uff65` であり、別の記号である。注意したい。
- Mac の場合、dot(`·`)は Shift + option + 9 キーを同時に押す。
参考資料 https://www.geoff-hart.com/resources/accents-mac.pdf
- Markdown ならば、TeX の記述方法が使える場合が多いため、`$g \cdot f$`と記述して、 $g \cdot f$ と表記できる。

---

### dot(`·`) の読み方
- dot(`·`)の読み方だが、youtube 等で英語の発話を見ると、`g·f`を`ジーアフターエフ`と読んでいる。ドット とか、サークルとか、とくに記号を読んでいるように見えなかった。意味としても" f のあとの g "ということで通りが良いため、自分も英語で `アフター` と呼ぶことにする。

```
g · f
```

$g \cdot f$

---

### 関数としての記述方法

(圏論が表現するのは関数だけにとどまらないが、)関数に置き換えると

```
h · g · f
```

は

```
h(g(f(x)))
```

と記述できる。

---
# 恒等射
- 難しいので飛ばしてもいいらしい。

### 恒等射の定義

1. 全ての対象がそれぞれ保持している
2. 対象「1」の恒等射(id_1)と 射f を合成すると 射f になる
3. 射f と対象「2」の恒等射(id_2)を合成すると 射f になる
4. $f · id_1 = f = id_2 · f$

**自分から自分へ向かう射が、無条件で恒等射と言えるわけではない** ← そうなの

4. $f · id_1 = f = id_2 · f$

つまり、対象「1」から対象「2」への射を実行するとき、 射f のあとに 恒等射を行うか、恒等射のあとに 射f を行うか、どちらでも同じことであるということ。

恒等射 id_1 の候補

対象「1」の恒等射(id_1)の候補は `1 <= 1`

この場合、不等式は成り立つため、恒等射もなりたつ。

---

# 圏と言えるかどうかの結論

圏の公理 を全て満たすことを確認した。よって、今まで見てきた集合`1, 2, 5, 10`は圏である。

1. 対象を持つこと
2. 射を持つこと
3. 合成射を持つこと
4. 結合律を持つこと
5. 恒等射を持つこと

`対象が「数字」で射が「不等号」という圏`である。

---

- python で恒等射について確認する→`恒等射.py`を参照


---

# Python の型と関数の圏

「圏論の関手」を理解するために必要となる。

「対象が Python の型で、射が Python の関数の圏」を考える。

---
# 合成関数

`関数の合成.py`

値のフロー

1. f(str 型 "Book")
2. g(int 型 5)
3. True

図: 関数の合成

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="321px" viewBox="-0.5 -0.5 321 261" content="&lt;mxfile host=&quot;Electron&quot; modified=&quot;2022-03-19T08:11:03.958Z&quot; agent=&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/16.5.1 Chrome/96.0.4664.110 Electron/16.0.7 Safari/537.36&quot; etag=&quot;vcAdAfeRkg-mtbto0tLu&quot; version=&quot;16.5.1&quot; type=&quot;device&quot;&gt;&lt;diagram id=&quot;v92y-lTXs8RKk6qdmRQe&quot; name=&quot;ページ1&quot;&gt;1Vddb5swFP01SNtDKz4Cgcfmo91DV03rpG6PTnDAlbGRcRrSX79rbAIuSdaqrcQeQuzji43PufdgnGBe1DcClfl3nmLq+G5aO8HC8f1kEsFVAXsNRFNfA5kgqYa8Drgnz9iArkG3JMWVFSg5p5KUNrjmjOG1tDAkBN/ZYRtO7VVLlOEBcL9GdIg+kFTmGo1Dt8O/YZLl7cqea0YK1AYboMpRync9KFg6wVxwLnWrqOeYKu5aXvR91ydGDw8mMJOvueHhF3683t7dLaKHm5+Pz4wR7/Ziomd5QnRrNmweVu5bBnAKhJguFzLnGWeILjt0JviWpVgt40Kvi7nlvATQA/ARS7k36qKt5ADlsqBmdLgVs7uKb8Uan3n+NiWQyLA8ExfoOLWX3gKGqBvMCyzFHgIEpkiSJ1t8ZHIoO8R1NEPDMP0G1j1/SPsydGauE09Ukjp+RGE3s5WAVqZaNcBOcAVXihlcv8BPYV+PynWLVlCFFsWIkoxBew0UYwHAExaSQJ5fmYGCpKlWE1fkGa2a+ZSeJSdMNgyEMydcHJXrbG7BQrg+VqxmEaseLDXMXRfupev5ob53b830ar3M5D/UZnohfLOpIHFeCnp4hndoPJC4kkKpCEInSyeeDZWjFFxNSbDLicT3JWpSfwe++kLLqtRWtyG1KrvT9TPg/iTHQexa/AatAe96rmegvGd4LfbxNeL+25rebTyYrhpLbovhXV4UvNKLknF5UXDWi7JzXtS0/AgVKkGbsWYCNxyxKx3y6kNsaToNrLLxx25LQ7X1yiO1pcgfmy15Q4J6ByTG2YeciI4YE66J/K1mvJzCu1D3/zT9JI5Nf1GbJZvOvtf5gQUBBlSRNdjnH7lGZnNHTroq5cHmYmcZqWvi9ozvpellqkbmvjOb6gPaeP3tVI292d/Uqes/O3QlA5FX8LF4eEWxVaX+Rup1oWt73ST5NK+Dbvfhqcnvvt6D5V8=&lt;/diagram&gt;&lt;/mxfile&gt;" onclick="(function(svg){var src=window.event.target||window.event.srcElement;while (src!=null&amp;&amp;src.nodeName.toLowerCase()!='a'){src=src.parentNode;}if(src==null){if(svg.wnd!=null&amp;&amp;!svg.wnd.closed){svg.wnd.focus();}else{var r=function(evt){if(evt.data=='ready'&amp;&amp;evt.source==svg.wnd){svg.wnd.postMessage(decodeURIComponent(svg.getAttribute('content')),'*');window.removeEventListener('message',r);}};window.addEventListener('message',r);svg.wnd=window.open('https://viewer.diagrams.net/?client=1&amp;page=0&amp;edit=_blank');}}})(this);" style="cursor:pointer;max-width:100%;max-height:261px;"><defs/><g><path d="M 80 40 L 233.63 40" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 238.88 40 L 231.88 43.5 L 233.63 40 L 231.88 36.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 40px; margin-left: 160px;"><div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">射 f<br />x : len ( x )</div></div></div></foreignObject><text x="160" y="43" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="11px" text-anchor="middle">射 f...</text></switch></g><ellipse cx="40" cy="40" rx="40" ry="40" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 40px; margin-left: 1px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">str 型</div></div></div></foreignObject><text x="40" y="44" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">str 型</text></switch></g><path d="M 257.86 73.32 L 185.72 181.42" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 182.81 185.79 L 183.78 178.02 L 185.72 181.42 L 189.61 181.91 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 127px; margin-left: 225px;"><div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">射 g<br />x : x &gt;= 5</div></div></div></foreignObject><text x="225" y="131" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="11px" text-anchor="middle">射 g...</text></switch></g><ellipse cx="280" cy="40" rx="40" ry="40" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 40px; margin-left: 241px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">int 型</div></div></div></foreignObject><text x="280" y="44" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">int 型</text></switch></g><path d="M 58 79.04 L 132.72 182.51" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 135.79 186.76 L 128.86 183.14 L 132.72 182.51 L 134.53 179.04 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 134px; margin-left: 99px;"><div data-drawio-colors="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 11px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; background-color: rgb(255, 255, 255); white-space: nowrap;">合成射<br />g · f</div></div></div></foreignObject><text x="99" y="137" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="11px" text-anchor="middle">合成射&#xa;g · f</text></switch></g><ellipse cx="160" cy="220" rx="40" ry="40" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 220px; margin-left: 121px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">bool 型</div></div></div></foreignObject><text x="160" y="224" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">bool 型</text></switch></g></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.diagrams.net/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Text is not SVG - cannot display</text></a></switch></svg>

**Python では Lambda 式を使って簡単に引数に関数を受け取って、関数を組み合わせて関数を返す関数を実装できる。**

```python
def compose(fn1, fn2):
    return lambda x: fn2(fn1(x))
```


---





# 参考資料
- category theory for programmers https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/
  - 有志による翻訳版：プログラマのための圏論 https://zenn.dev/taketo1024/books/850b20937af93b
- category theory for python: yomutukuruwakaru (Japanese Edition). Kindle Edition.
