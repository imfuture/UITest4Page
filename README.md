<pre style="background-color:#2b2b2b;color:#a9b7c6;font-family:'Courier New';font-size:12.0pt;">UITest4Page项目目前具有以下功能：<br>1、对webdriver进行了第二次的简单封装，使用更加方便 public/common/pyselenium.py<br>(ps：这个是在虫师的pyse基础加了打印日志功能,参考：https://github.com/defnngj/pyse)<br>2、可以对excel表进行数据读取，完成数据驱动:public/common/datainfo.py<br>3、具有打印日志的功能，打印在控制台和文件中：public/common/log.py,日志保存在report/log/目录下<br>4、读取配置文件(.ini文件):public/common/readconfig.py<br>5、具有发邮件的功能:public/common/sendmail.py<br>6、生成测试报告：html测试报告的路径：report/testreport/目录下<br>7、使用了PageObject模式来编写测试脚本<br><br>整个项目的目录结构:<br>├─config 配置文件的目录<br>│  │  config.ini   存放配置文件<br>│  │  globalparam.py  重要的全局参数，如log、report的路径配置等<br>│  │  __init__.py<br>│  │<br>│<br>├─data   测试数据<br>│  ├─formaldata # 正式环境测试数据<br>│  └─testdata  # 测试环境的数据<br>│          searKey.xlsx<br>│<br>├─public  公共的文件库<br>│  │  __init__.py<br>│  │<br>│  ├─common  封装的公共方法<br>│  │  │  basepage.py<br>│  │  │  datainfo.py<br>│  │  │  log.py<br>│  │  │  mytest.py<br>│  │  │  publicfunction.py<br>│  │  │  pyselenium.py<br>│  │  │  pyselenium20161107.py<br>│  │  │  readconfig.py<br>│  │  │  sendmail.py<br>│  │  │  __init__.py<br>│  │  │<br>│  │<br>│  ├─pages 使用pageobject模式编写测试脚本，存放page的目录<br>│  │  │  baiduIndexPage.py<br>│  │  │  __init__.py<br>│<br>├─report 测试报告<br>│  ├─image 截图目录<br>│  ├─log 日志目录<br>│  │      2016-11-07.log<br>│  │<br>│  └─testreport  html测试报告目录<br>│          TestResult2016-11-07_16_15_51.html<br>│<br>└─testcase 存放测试用例<br>    │  test_baidu.py<br><br>使用说明:<br>安装响应的库: pip install xlrd,selenium,configparser<br>1、在config.ini中配置项目路径：project_path<br>2、测试数据放在data目录下面<br>3、使用pageobject，写page页面，在测试用例里面调用放在public/pages目录下<br>4、在testcase目录下面，编写测试用例，可以分模块编写，建相应的目录<br>5、执行run.py,就可以执行所有的测试用例<br>6、在report/log里面查看日志<br>7、在report/testreport里面查看html测试报告<br><br>关于pyselenium的使用:<br>该py文件是根据虫师的pyse改的，加了一个日志，根据自己的需要加了几个函数<br>可以参考虫师的pyse,github地址:https://github.com/defnngj/pyse<br>虫师的博客园地址：https://github.com/defnngj/pyse<br><br>导入PySlenium文件<br>import PySelenium<br>1、启动浏览器：<br>启动谷歌浏览器<br>dr = PySelenium.PySelenium('chrom')<br>启动远程浏览器比如使用grid施行分布式执行<br>dr = PySelenium.PySelenium(RChrome','127.0.0.1:8080')<br>2、在地址栏输入网址：<br>dr.open('http://www.baidu.com')<br>3、窗口最大化<br>dr.max_window()<br>4、设置浏览器的窗口的大小<br>dr.set_window(800,500)<br>5、不清除文本框的内容直接输入值(比如说：进行文件上传时，上传文件的路径，如果清除就会报错)：<br>dr.type('id-&gt;su','小石头tester')<br>6、先清除文本框的内容，然后再输入值（用得很多）：<br>dr.clear_type('name-&gt;su','虫师')<br>7、直接点击元素<br>dr.click('css-&gt;#kw')<br>8、右键点击元素：<br>dr.right_click('id-&gt;kw')<br>9、将鼠标移动到一个元素上<br>dr.move_to_element('clas-&gt;btn1.btn-green.btn-search')<br>10、双击元素<br>dr.double_click("id-&gt;kw")<br>11、将一个元素拖拽到另外一个元素上<br>dr.drag_and_drop('id-&gt;kw1','id-&gt;kw2')<br>12、根据连接的text来点击(&lt;a href="http://www.baidu.com"&gt;百度&lt;/a&gt;)<br>dr.click_text('百度')<br>13、关闭窗口，driver<br>dr.quit()<br>14、执行js脚本<br>dr.js('script')<br>15、获取元素的属性<br>dr.get_attribute("id-&gt;su","href")<br>16、获取元素的文本信息text<br>dr.get_text('id-&gt;su')<br>17、返回当前页面的title<br>dr.get_title()<br>18、返回当前页面的url<br>dr.get_url()<br>20、进入frame<br>dr.switch_to_frame('id-&gt;kw')<br>21、退出frame<br>dr.switch_to_frame_out()<br>22、判断元素是否存在<br>dr.element_exist('id-&gt;kw')<br>23、截图<br>dr.take_screenshot('file_path')<br>24、进入最新的table<br>dr.into_new_window()<br>25、输入内容并且回车<br>dr.type_and_enter('id-&gt;kw')<br>26、使用js来点击某个元素<br>dr.js_click('id-&gt;kw')<br>27、返回原生的webdriver，进行个性化需求<br>dr.origin_driver()<br></pre>
