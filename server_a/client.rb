require 'awesome_print'
require 'byebug'
require 'savon'

client = Savon.client(wsdl: 'http://localhost:5000?wsdl')

# response = client.call(:add_numbers, message: { a: 3, b: 3 })

# puts response.body[:add_numbers_response][:add_numbers_result]

response = client.call(:titles, message: { elements: 10 })

result = response.body[:titles_response][:titles_result][:string]

puts result
