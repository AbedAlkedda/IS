# frozen_string_literal: true

require 'sinatra'
require 'byebug'
require_relative 'soap_client'

set :port, 5000

soap_client = SOAPClient.new(ENV['SOAP_CLIENT_URL'] || 'http://localhost:8000?wsdl')

get '/' do
  @movies = soap_client.movies_data 2

  soap_client.htwk_info 2
  @htwk_infos    = soap_client.htwk_infos
  @semeter_infos = soap_client.semeter_infos

  erb :index
end

post '/update-list' do
  data    = JSON.parse request.body.read
  @movies = soap_client.movies_data data.to_i

  @movies.to_json
end
