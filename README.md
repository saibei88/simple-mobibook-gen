A single mobi ebook generator with python.

Following files are templates for .opf and .ncx files. DO NOT MODIFY THEM.
lxb.opf   
toc.ncx

Following files are  simple examples .
cover.jpg    #Choose a image for your book as cover, rename it to cover.jpg
#The script would check the text in  <h4></h4> tag as the title of the .ncx file.
preface.html 
chap1.html

USAGE:
Choose a cover.jpg for the cover of your book.
Create a preface.html file as the preface of your book.
Put all chapters of your book in order as chap1.html chap2.html .etc.
Run the main.py with "python main.py".
Compile the out.opf with kindlegen using "kindlegen out.opf".
Then you will get the "out.mobi" file.

kindlegen for linux:
http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz

一个简单的mobi电子书生成脚本

这2个文件是opf和ncx模板，最好不要改动
lxb.opf   
toc.ncx

这3个文件是举个栗子
cover.jpg #封面，选一个你要的封面图片，命名成这样就行了
脚本里会去查下面几个html文件的<h4></h4>标签作为ncx文件的标题
preface.html 
chap1.html


使用方法，把preface.html 和不同章节按顺序命名 chap1.html chap2.html chap3.html ... 放到这个目录下面
然后运行
python main.py
再用kindlegen out.opf 就可以得到 out.mobi #默认情况下的名称
kindlegen linux 版下载地址
http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz
