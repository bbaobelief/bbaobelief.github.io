Title: Google Code Prettify 代码高亮显示行号
Date: 2014-09-25 12:37:19
Category: Web
Tags: html模版, CSS
Slug: google-code-prettify


以前我使用 highlight.js,现在换了kindeditor编辑器。为了更好的兼容性，代码高亮插件改为Prettify，出现无法显示行号问题，记录解决方法。

#### 1.修改code.js文件49行为

```
html = '<pre class="prettyprint linenums' + cls + '">\n' + K.escape(code) + '</pre> ';
```

#### 2.修改主题文件github.css，添加

```
/* IE indents via margin-left */
li.L0,
li.L1,
li.L2,
li.L3,
li.L4,
li.L5,
li.L6,
li.L7,
li.L8,
li.L9 {
  list-style-type: decimal !important
}

pre.prettyprint ol li {
margin-left: 10px;
padding-left: 10px;
border-left: 2px solid #BBE9BB;
}
```

#### 3.自用hemisu.css主题样式

```
/* Hemisu Light */
/* Original theme - http://noahfrederick.com/vim-color-scheme-hemisu/ */
.prettyprint {
  background: white;
  font-family: Menlo, 'Bitstream Vera Sans Mono', 'DejaVu Sans Mono', Monaco, Consolas, monospace;
  font-size: 12px;
  line-height: 1.5;
  border: 1px solid #ccc;
  padding: 10px;
}

.pln {
  color: #111111;
}

@media screen {
  .str {
    color: #739200;
  }

  .kwd {
    color: #739200;
  }

  .com {
    color: #999999;
  }

  .typ {
    color: #ff0055;
  }

  .lit {
    color: #538192;
  }

  .pun {
    color: #111111;
  }

  .opn {
    color: #111111;
  }

  .clo {
    color: #111111;
  }

  .tag {
    color: #111111;
  }

  .atn {
    color: #739200;
  }

  .atv {
    color: #ff0055;
  }

  .dec {
    color: #111111;
  }

  .var {
    color: #111111;
  }

  .fun {
    color: #538192;
  }
}
@media print, projection {
  .str {
    color: #006600;
  }

  .kwd {
    color: #006;
    font-weight: bold;
  }

  .com {
    color: #600;
    font-style: italic;
  }

  .typ {
    color: #404;
    font-weight: bold;
  }

  .lit {
    color: #004444;
  }

  .pun, .opn, .clo {
    color: #444400;
  }

  .tag {
    color: #006;
    font-weight: bold;
  }

  .atn {
    color: #440044;
  }

  .atv {
    color: #006600;
  }
}
/* Specify class=linenums on a pre to get line numbering */
ol.linenums {
  margin-top: 0;
  margin-bottom: 0;
}

/* IE indents via margin-left */
li.L0,
li.L1,
li.L2,
li.L3,
li.L4,
li.L5,
li.L6,
li.L7,
li.L8,
li.L9 {
  list-style-type: decimal !important
}

/* Alternate shading for lines */
li.L1,
li.L3,
li.L5,
li.L7,
li.L9 {
  /* */
}

pre.prettyprint ol li {
margin-left: 10px;
padding-left: 10px;
border-left: 2px solid #BBE9BB;
}
```