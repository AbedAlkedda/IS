require 'socket'
require 'byebug'


class Client
	def tcp_client
		socket = TCPSocket.new 'localhost', 3002

		while line = socket.gets
		  puts line
		end

		socket.close
	end

	def udp_client
		counter = 0
		socket  = UDPSocket.open
    socket.connect 'localhost', 3003
    while true
      socket.send "counter => #{counter}", 0, 'localhost', 3003
      sleep 1
      return if counter > 10
    	counter += 1
    end
	end
end

client = Client.new

# TCP
# client.tcp_client

# UDP
client.udp_client
