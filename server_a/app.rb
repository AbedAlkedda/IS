# frozen_string_literal: true

require 'sinatra'
require 'byebug'
require_relative 'soap_client'

soap_client = SOAPClient.new('http://localhost:8000?wsdl')

get '/' do
  @movies = soap_client.movies_data(10)
  erb :index
end

post '/update-list' do
  data = JSON.parse(request.body.read)
  @movies = soap_client.movies_data(data.to_i)
  @movies.to_json
end
