# frozen_string_literal: true

require 'savon'
require 'byebug'
# SOAP Client
class SOAPClient
  def initialize(wsdl_url)
    @client = Savon.client(wsdl: wsdl_url)
  end

  def titles_top(count)
    response = @client.call(:titles, message: { elements: count })
    response.body[:titles_response][:titles_result][:string]
  end

  def movies_data(count)
    response = @client.call(:movies_data, message: { elements: count })
    response.body[:movies_data_response][:movies_data_result][:movie_data]
  end
end

# client = SOAPClient.new('http://localhost:8000?wsdl')
# titles = client.movies_data(20)

# puts titles
