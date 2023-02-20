require 'savon'
require 'byebug'
require 'awesome_print'

client = Savon.client(wsdl: 'http://localhost:5000?wsdl')

response = client.call(:add_numbers, message: { a: 3, b: 3 })

puts response.body[:add_numbers_response][:add_numbers_result]
