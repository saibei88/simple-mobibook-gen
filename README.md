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
