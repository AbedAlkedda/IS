# frozen_string_literal: true

require 'savon'
require 'byebug'

# SOAP Client
class SOAPClient
  attr_reader :htwk_infos, :semester_infos

  def initialize(wsdl_url)
    @client = Savon.client(wsdl: wsdl_url)
  end

  def movies_data(elements)
    response = @client.call :movies_data, message: { elements: elements }

    response.body[:movies_data_response][:movies_data_result][:movie_data]
  end

  def htwk_info(ele)
    response       = @client.call :semester_infos, message: { ele: ele }
    @semester_infos = response.body[:semester_infos_response][:semester_infos_result]

    response    = @client.call :htwk_info, message: { ele: ele }
    @htwk_infos = response.body[:htwk_info_response][:htwk_info_result].to_a

    response.body[:htwk_info_response][:htwk_info_result].to_a
  end
end
