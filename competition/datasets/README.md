## version01.csv
- all objects to **numerical type**
- identical product code  
<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>마더코드</th>
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군</th>
    <th>판매단가</th>
    <th>노출</th>
    <th>month</th>
    <th>취급액</th>
  </tr>
</table>

![image](https://user-images.githubusercontent.com/52376448/91631930-643c2780-ea18-11ea-87f7-70b40df53504.png)



<br><br><br>
## version02.csv
- **brand** info
<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>마더코드</th>
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군</th>
    <th>브랜드</th>
    <th>노출</th>
    <th>month</th>
    <th>판매단가</th>
    <th>취급액</th>
  </tr>
</table>

![image](https://user-images.githubusercontent.com/52376448/91631952-8d5cb800-ea18-11ea-8873-54959da6bbf4.png)



<br><br><br>
## version03.csv
- matching **brand code** and **brand name**
- some brands share same brand codes(ex.product code '200602' and '202449')

<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>마더코드</th>
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군</th>
    <th>브랜드</th>
    <th>노출(분)</th>
    <th>month</th>
    <th>판매단가</th>
    <th>취급액</th>
  </tr>
</table>

![image](https://user-images.githubusercontent.com/52376448/92242566-efc32600-eefa-11ea-9a87-d329590bf804.png)



<br><br><br>
## version04.csv
- splited into **minutes**
- not changed the time it broadcasted
- cannot upload on github because of the memory size -> shared on KakaoTalk
<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>노출</th>
    <th>마더코드</th>
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군</th>
    <th>판매단가</th>
    <th>브랜드</th>
    <th>취급액</th>
  </tr>
</table>

![image](https://user-images.githubusercontent.com/52376448/92242872-70822200-eefb-11ea-85fc-1d282de4182e.png)



<br><br><br>
## version05.csv
- included **external data**(floating population)
- not splited into minutes -> will be uploaded on GitHub or shared on KakaoTalk soon
<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>노출(분)</th>
    <th>마더코드</th>
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군</th>
    <th>브랜드</th>
    <th>판매단가</th>
    <th>유동인구</th>
    <th>취급액</th>
  </tr>
</table>

![image](https://user-images.githubusercontent.com/52376448/92242630-09fd0400-eefb-11ea-8500-1e994839965a.png)



<br><br><br>
## version06.csv
- included **external data**(floating population)
- splited into **minutes** -> shared on KakaoTalk because of the massive file size
<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>노출</th>
    <th>마더코드</th>
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군</th>
    <th>브랜드</th>
    <th>판매단가</th>
    <th>유동인구</th>
    <th>취급액</th>
  </tr>
</table>

![image](https://user-images.githubusercontent.com/52376448/92242957-94456800-eefb-11ea-8601-9336d5d549a0.png)



<br><br><br>
## version07.csv
- deleted some brand names which are **not real brand**
- does not contain floating floating population
- is not splitted into minutes.
<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>마더코드</th>    
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군</th>
    <th>브랜드</th>
    <th>노출</th>
    <th>month</th>
    <th>판매단가</th>
    <th>취급액</th>
  </tr>
</table>

![image](https://user-images.githubusercontent.com/52376448/92242675-1e410100-eefb-11ea-8977-31c5306ca820.png)

<br><br><br>
## version08.csv
- deleted some brand names which are **not real brand**
- deleted month column
- does not contain floating floating population
- is not splitted into minutes.
<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>마더코드</th>    
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군</th>
    <th>브랜드</th>
    <th>노출</th>
    <th>판매단가</th>
    <th>취급액</th>
  </tr>
</table>

<br><br><br>
## version13.csv
- deleted some brand names which are **not real brand**
- deleted month column
- contain floating floating population
- contain fine dust
- is splitted into minutes.

<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>노출(분)</th>
    <th>마더코드</th>    
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군</th>
    <th>브랜드</th>
    <th>판매단가</th>
    <th>유동인구</th>
    <th>PM10</th>
    <th>PM25</th>
    <th>취급액</th>
  </tr>
</table>

<br><br><br>
## version14.csv
- deleted some brand names which are **not real brand**
- deleted month column
- deleted '무형상품군'
- contain floating floating population
- contain fine dust
- is splitted into minutes.

<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>노출(분)</th>
    <th>마더코드</th>    
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군</th>
    <th>브랜드</th>
    <th>판매단가</th>
    <th>유동인구</th>
    <th>PM10</th>
    <th>PM25</th>
    <th>취급액</th>
  </tr>
</table>

<br><br><br>
## version15.csv
- onehotencoding : 상품군
- deleted some brand names which are **not real brand**
- deleted month column
- deleted '무형상품군'
- contain floating floating population
- contain fine dust
- is splitted into minutes.

<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>노출(분)</th>
    <th>마더코드</th>    
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군0</th>
    <th>상품군1</th>
    <th>상품군2</th>
    <th>상품군3</th>
    <th>상품군4</th>
    <th>상품군5</th>
    <th>상품군6</th>
    <th>상품군7</th>
    <th>상품군8</th>
    <th>상품군9</th>
    <th>상품군10</th>
    <th>상품군11</th>
    <th>브랜드</th>
    <th>판매단가</th>
    <th>유동인구</th>
    <th>PM10</th>
    <th>PM25</th>
    <th>취급액</th>
  </tr>
</table>

<br><br><br>
## version16.csv
- onehotencoding : 상품군,노출(분)
- deleted some brand names which are **not real brand**
- deleted month column
- deleted '무형상품군'
- contain floating floating population
- contain fine dust
- is splitted into minutes.

<table>
  <tr>
    <th>순서</th>
    <th>방송일시</th>
    <th>노출분 2</th>
    <th>노출분 3</th>
    <th>노출분 ..40 까지 </th>
    <th>노출(분)</th>
    <th>마더코드</th>    
    <th>상품코드</th>
    <th>상품명</th>
    <th>상품군0</th>
    <th>상품군1</th>
    <th>상품군2</th>
    <th>상품군3</th>
    <th>상품군4</th>
    <th>상품군5</th>
    <th>상품군6</th>
    <th>상품군7</th>
    <th>상품군8</th>
    <th>상품군9</th>
    <th>상품군10</th>
    <th>상품군11</th>
    <th>브랜드</th>
    <th>판매단가</th>
    <th>유동인구</th>
    <th>PM10</th>
    <th>PM25</th>
    <th>취급액</th>
  </tr>
</table>


## version18.csv
![image](https://user-images.githubusercontent.com/52376448/93671110-3c058d00-fadb-11ea-900c-294bb176ffb1.png)
