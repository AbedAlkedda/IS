# frozen_string_literal: true

# SPARQL Client
class SPARQLClient
  attr_reader :actors, :abstract

  def show_movie(movie)
    @client = SPARQL::Client.new('http://dbpedia.org/sparql')

    query   = _query_header
    query  += "\n ?film dbp:name\"#{movie}\"@en .\n"
    query  += _query_footer
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

  def _query_footer
    <<~SPARQL
        FILTER (lang(?abstract) = "ar")
        BIND(?film AS ?title)
      }
    SPARQL
  end
end
