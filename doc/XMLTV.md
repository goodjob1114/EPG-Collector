# XMLTV

> The XMLTV Project is a set of (mostly Perl) utilities to manage your TV viewing. They work with TV listings stored in the XMLTVFormat, which is based on XML. The idea is to separate out the back-end (getting the listings) from the front-end (displaying them for the user), and to implement useful operations like picking out your favorite programmes as filters that read and write XML documents.

XMLTV 有好幾層意思。
它指一種用以表示 TV 節目單的 XML 格式；
又指一個可以產生此種 XML 檔案的 perl 模組；
也是一套可以搜尋、下載 XMLTV 檔案的軟體的集合，後文記述的工具包即指這套。

- http://wiki.xmltv.org/index.php/Main_Page/
- http://wiki.xmltv.org/index.php/XMLTVFormat
- http://wiki.xmltv.org/index.php/XMLTVProject
- https://code.google.com/p/python-xmltv/  使用 Python 開發，幫助解析 XMLTV 檔案。

### XMLTV 下載器

- http://sourceforge.net/projects/xmltv/  使用 Perl 開發，自行編譯安裝，主要的工具包。
- http://sourceforge.net/projects/autoepg/  需要在 Windows 環境執行。
- http://www.artificialworlds.net/freeguide/  使用 Java 開發，可以輸出 XMLTV 清單。
- http://tvguide.sourceforge.net  需要註冊 Schedules Direct。
- http://epgdownloader.sourceforge.net  使用 Perl 開發。

### XMLTV 工具包

除了自行編譯安裝，如果是 Ubunt 環境，其實可以透過以下指令安裝：
```
sudo apt-get install xmltv xmltv-gui xmltv-util python-xmltv libxmltv-perl freeguide ontv
```

XMLTV 的工具執行時，大多會根據各自的設定檔（*.conf）來運作。
設定檔一般會放在 `~/.xmltv/` 目錄下。
如果某個工具首次執行還沒有設定檔，可以加 `--configure` 參數執行，進行設定檔初始化。

* `tv_find_grabbers` 搜尋並列出系統中所有的 grabber 程式。
```
tv_find_grabbers
```

* `tv_grab_*` 真正的 XMLTV 抓取器。
通常一個國家或地區由一個 grabber 負責，每個 grabber 會抓很多個頻道的訊息。
例如 tv_grab_ar 就是抓取 Argentina 電視節目的 grabber。
一個 grabber 會搭配一個自己的 conf 檔，可以設定要抓取哪些電信業者、哪些頻道。
初次執行 grabber 沒有 conf 檔時，可以加上 `--configure` 參數。
但有些 grabber 會是例外，可能需要某些認證的參數，
這跟 grabber 的資料來源有關，如果資料來源需要註冊，則需要註冊資訊。
```
tv_grab_ar --configure
tv_grab_ar --output result.xml
tv_grab_ar --output reslult.xml --days 5
tv_grab_ar --output reslult.xml --days 1 --offset 1
tv_grab_ar --output reslult.xml --days 1 --offset 2
tv_grab_ar --output reslult.xml --days 1 --offset 3
tv_grab_ar --output reslult.xml --days 1 --offset 4
tv_grab_ar --output reslult.xml --days 1 --offset 5
```

* `tv_validate_grabber` 檢驗 grabber 是否正常運作。
```
tv_validate_grabber  tv_grab_*
```

* `tv_grab_combiner` 將多個 grabbers 合併成一個抓取任務來執行。
```
tv_grab_combiner --configure
tv_grab_combiner
```

* `tv_grep` 從 XMLTV 檔中過濾節目或頻道。
```
man tv_grep
```

* `tv_sort` 根據日期排序 XMLTV 檔內容。
```
tv_sort  origin.xml --output result.xml
```

* `tv_split` 根據日期或頻道將 XMLTV 檔切割。
```
tv_split --output %channel-%Y%m%d.xml  origin.xml
```

* `tv_cat` 將多個 XMLTV 檔案串接起來。
```
tv_cat  --output all.xml a.xml b.xml c.xml
```

* `tv_check` 比對手上的節目單與播放單是否有差異或有即將演出的節目。
```
tv_check --configure （直接叫出 GUI 畫面）
tv_check --scan --shows=shows.xml --guide=guide.xml
```
