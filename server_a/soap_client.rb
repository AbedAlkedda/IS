# frozen_string_literal: true

require 'savon'
require 'byebug'
# SOAP Client
class SOAPClient
  def initialize(wsdl_url)
    @client = Savon.client(wsdl: wsdl_url)
  end

  def movies_data(count)
    response = @client.call(:movies_data, message: { elements: count })
    response.body[:movies_data_response][:movies_data_result][:movie_data]
  end
end
