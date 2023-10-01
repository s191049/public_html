#!/usr/local/rvm/rubies/ruby-3.0.2/bin/ruby
require 'erb'
erb = ERB.new(File.read("hoge.erb"))
print erb.result(binding)
#print "hoge"
