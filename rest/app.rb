# frozen_string_literal: true

require 'sinatra'
require 'byebug'
require_relative 'soap_client'

set :port, 5000

soap_client = SOAPClient.new(ENV['SOAP_CLIENT_URL'] || 'http://localhost:8000?wsdl')

get '/' do
  @movies       = soap_client.movies_data 2
  @semester_num = 2

  soap_client.htwk_info @semester_num

  @htwk_infos     = soap_client.htwk_infos
  @semester_infos = soap_client.semester_infos

  erb :index
end

post '/update-list' do
  data    = JSON.parse request.body.read
  @movies = soap_client.movies_data data.to_i

  @movies.to_json
end

post '/update-htwk-info' do
  data          = JSON.parse request.body.read
  @semester_num = data.to_i

  soap_client.htwk_info @semester_num
  @htwk_infos     = soap_client.htwk_infos
  @semester_infos = soap_client.semester_infos

  [@htwk_infos, @semester_infos].to_json
end
