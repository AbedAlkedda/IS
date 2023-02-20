# frozen_string_literal: true

require 'savon'

# SOAP Client
class SOAPClient
  def initialize(wsdl_url)
    @client = Savon.client(wsdl: wsdl_url)
  end

  def get_titles(count)
    response = @client.call(:titles, message: { elements: count })
    response.body[:titles_response][:titles_result][:string]
  end
end

client = SOAPClient.new('http://localhost:8000?wsdl')
titles = client.get_titles(10)

puts titles
