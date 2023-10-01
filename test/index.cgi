#!/usr/local/rvm/rubies/ruby-3.0.2/bin/ruby
require 'erb'

# テンプレートファイルを読み込む
template = ERB.new(File.read('template.erb'))

# データを用意
# data = "hoge"
data = "./login.erb"

begin
#page1
content = ERB.new(File.read(data)).result(binding)

# データをテンプレートに渡してHTMLを生成
output = template.result(binding)
rescue => e
output = e
end

# Content-Typeヘッダを設定し、HTMLを出力
puts "Content-Type: text/html; charset=UTF-8\n\n"
puts output
