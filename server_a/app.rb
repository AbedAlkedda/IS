# frozen_string_literal: true

require 'sinatra'
require 'byebug'
require_relative 'soap_client'

get '/' do
  @movies = SOAPClient.new('http://localhost:8000?wsdl').movies_data(20)
  @others = SOAPClient.new('http://localhost:8000?wsdl').movies_data(20)

  erb :index
end
