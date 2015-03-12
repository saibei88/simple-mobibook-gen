A single mobi ebook generator with python.<br />

Following files are templates for .opf and .ncx files. DO NOT MODIFY THEM.<br />
lxb.opf   <br />
toc.ncx  <br />

Following files are simple examples. <br />
cover.jpg    #Choose a image for your book as cover, rename it to cover.jpg <br />
#The script would check the text in  &lt;h4&gt;&lt;/h4&gt; tag as the title of the .ncx file. <br />
preface.html  <br />
chap1.html  <br />

USAGE: <br />
Choose a cover.jpg for the cover of your book. <br />
Create a preface.html file as the preface of your book. <br />
Put all chapters of your book in order as chap1.html chap2.html .etc. <br />
Run the main.py with "python main.py". <br />
Compile the out.opf with kindlegen using "kindlegen out.opf". <br />
Then you will get the "out.mobi" file. <br />
<br />
kindlegen for linux: <br />
http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz <br />

一个简单的mobi电子书生成脚本 <br />

这2个文件是opf和ncx模板，最好不要改动 <br />
lxb.opf   <br />
toc.ncx <br />

这3个文件是举个栗子 <br />
cover.jpg #封面，选一个你要的封面图片，命名成这样就行了 <br />
脚本里会去查下面几个html文件的&lt;h4&gt;&lt;/h4&gt;标签作为ncx文件的标题 <br />
preface.html  <br />
chap1.html <br />


使用方法，把preface.html 和不同章节按顺序命名 chap1.html chap2.html chap3.html ... 放到这个目录下面 <br />
然后运行  <br />
python main.py  <br />
再用kindlegen out.opf 就可以得到 out.mobi #默认情况下的名称 <br />
kindlegen linux 版下载地址  <br />
http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz  <br />
