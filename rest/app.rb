# frozen_string_literal: true

require 'socket'
require 'sinatra'

require_relative 'sparql_client'
require_relative 'soap_client'

set :port, 5000

soap_client   = SOAPClient.new(ENV['SOAP_CLIENT_URL'] || 'http://localhost:8000?wsdl')
sparql_client = SPARQLClient.new

get '/' do
  erb :landing_page
end

get '/lists' do
  @movies       = soap_client.movies_data 2
  @semester_num = 2

  soap_client.htwk_info @semester_num

  @htwk_infos     = soap_client.htwk_infos
  @semester_infos = soap_client.semester_infos

  erb :lists
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

post '/show-extra' do
  data    = JSON.parse request.body.read
  data[1] = data[1].gsub(/\t/, '')
  res     = sparql_client.show_movie(data)

  res.to_json
end
