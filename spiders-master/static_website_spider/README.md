# 静态页面抓取

直接使用 requests 库发出 HTTP 请求并获取响应，再利用 Beautifulsoup 来解析 html 页面。

无法抓取设计 JavaScript 动态生成的内容。

值得注意的是，不论 requests 还是 Beautifulsoup 都有其他库实现类似功能，不必局限于这两个库。