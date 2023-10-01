#!/usr/local/rvm/rubies/ruby-3.0.2/bin/ruby
require "cgi"
qs = CGI.new

print "Content-Type: text/html\n"
print "\n"
hoge="asdf"
lines = []
File.open("hoge.html", "r") do |f|
  f.each_line do |l|
    lines.push(l)
    print l
  end
end
#p lines
