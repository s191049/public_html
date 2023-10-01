#!/usr/local/rvm/rubies/ruby-3.0.2/bin/ruby
# coding: utf-8

require 'erb'
require 'cgi'
#require 'ruby-mysql'
#require 'active_record'

cgi = CGI.new

# テンプレートファイルを読み込む
template = ERB.new(File.read('template.erb'))

# 次ページを用意
nextp = "./page1.erb"

# 送信データを取得
authid = cgi["authid"]
password = cgi["password"]

# データベースに接続
=begin
begin
connect = Mysql.new('localhost', 'minachan', '1967011003', 'minachan')
res = connect.query("SELECT * FROM users WHERE id="#{authid} AND password="#{password};")
rescue => e
puts "Content-Type: text/html; charset=UTF-8\n\n"
puts e
end
=end

# res = ["", ""]
=begin
if res.count == 1
  #page1
  content = ERB.new(File.read(nextp)).result(binding)
else
  #content = '<script>alert("失敗")</script>'
  content = "hoge"
end
=end

content = "hey"

#=begin
begin
require 'mysql'
content = "hoge"
rescue => e
content = e
end
#=end

# データをテンプレートに渡してHTMLを生成
output = template.result(binding)

# Content-Typeヘッダを設定し、HTMLを出力
puts "Content-Type: text/html; charset=UTF-8\n\n"
puts output
