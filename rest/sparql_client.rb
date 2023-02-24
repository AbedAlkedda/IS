# frozen_string_literal: true

require 'sparql/client'

# SPARQL Client
class SPARQLClient
  attr_reader :actors, :abstract

  def show_movie(movie)
    @client = SPARQL::Client.new('http://dbpedia.org/sparql')

    query   = _query_header
    query  += "\n ?film dbp:name\"#{movie[0]}\"@en .\n"
    query  += _query_footer movie[1]
    result  = @client.query query
    @actros = []

    return ['', ''] if result.empty?

    result.each_with_index { |_, i| @actros << result[i][:starring].to_s.split('/').last.gsub('_', ' ') }

    @abstract = result.first[:abstract].to_s

    [@actros, @abstract]
  end

  private

  def _query_header
    <<~SPARQL
      PREFIX dbp: <http://dbpedia.org/property/>
      PREFIX dbo: <http://dbpedia.org/ontology/>

      SELECT ?starring ?abstract
      WHERE {
        ?film dbo:starring ?starring .
        ?film dbo:abstract ?abstract .
    SPARQL
  end

  def _query_footer(lang)
    <<~SPARQL
        FILTER (lang(?abstract) = "#{lang}")
        BIND(?film AS ?title)
      }
    SPARQL
  end
end
