require 'socket'

class Network
	def self.TCPServer
		server = TCPServer.new 'localhost', 3002

		# Servers run forever
		loop do
	  	client = server.accept

	  	client.puts "Welcome! You are visitor ##{rand(1..20)}"
	  	client.puts "Time: #{Time.now}"

	  	client.close
		end
	end

	def self.UDPServer
		socket = UDPSocket.new

		# nil is understood as localhost
    socket.bind nil, 3003
    while true
      packet = socket.recvfrom 1024
      puts packet
    end
	end
end

# To Run
# ruby -r "./server.rb" -e 'Network.TCPServer'
