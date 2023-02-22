# frozen_string_literal: true

require 'savon'
require 'byebug'

# SOAP Client
class SOAPClient
  attr_reader :htwk_infos

  def initialize(wsdl_url)
    @client = Savon.client(wsdl: wsdl_url)
  end

  def movies_data(count)
    response = @client.call :movies_data, message: { elements: count }

    response.body[:movies_data_response][:movies_data_result][:movie_data]
  end

  def htwk_info
    response = @client.call :htwk_info

    @htwk_infos = response.body[:htwk_info_response][:htwk_info_result].to_a

    response.body[:htwk_info_response][:htwk_info_result].to_a
  end
end
